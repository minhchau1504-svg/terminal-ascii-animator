import os
import time
import sys

# Enable ANSI escape code support on Windows
if os.name == 'nt':
    os.system('')
    import msvcrt

def clear_screen():
    print("\033[H\033[2J", end="", flush=True)

def start_alternate_screen():
    """Switches to a clean alternate screen buffer (no scrollback clutter)."""
    print("\033[?1049h", end="", flush=True)

def stop_alternate_screen():
    """Restores the original terminal screen buffer."""
    print("\033[?1049l", end="", flush=True)

def check_for_stop(delay):
    """Waits for 'delay' seconds while checking if 'q' or ESC is pressed."""
    start_time = time.time()
    while time.time() - start_time < delay:
        if os.name == 'nt':
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key in (b'\x00', b'\xe0'):
                    msvcrt.getch()
                elif key.lower() == b'q' or key == b'\x1b':
                    return True
        time.sleep(0.02)
    return False

def main():
    frames = []
    print("=== Terminal ASCII Animation Maker ===")
    print("Instructions:")
    print("- Type your art line by line, then 'END' to save a frame.")
    print("- Type 'UNDO' to erase your last typed line.")
    print("- Type 'LIST' to view all saved frames.")
    print("- Type 'DELETE' to remove the last frame, or 'DELETE <num>' for a specific frame.")
    print("- Type 'EDIT <num>' to modify a specific frame.")
    print("- Type 'PLAY' to preview (Press 'q' or ESC to stop).")
    print("- Type 'QUIT' to exit.\n")

    current_frame = []
    
    while True:
        try:
            line = input(f"Frame {len(frames) + 1} (Line) > ")
        except (KeyboardInterrupt, EOFError):
            break
            
        cmd_upper = line.strip().upper()
        parts = line.strip().split()
        cmd_action = parts[0].upper() if parts else ""
        
        if cmd_upper == 'QUIT':
            break
        elif cmd_upper == 'UNDO':
            if current_frame:
                removed = current_frame.pop()
                print(f"-> Removed line: '{removed}'\n")
            else:
                print("-> Nothing to undo in the current frame.\n")
        elif cmd_upper == 'LIST':
            if not frames:
                print("-> No saved frames yet!\n")
            else:
                print("\n--- Saved Frames ---")
                for idx, f in enumerate(frames, 1):
                    print(f"[Frame {idx}]")
                    print(f)
                    print("-" * 15)
                print()
        elif cmd_action == 'DELETE':
            if len(parts) > 1:
                try:
                    target_idx = int(parts[1]) - 1
                    if 0 <= target_idx < len(frames):
                        removed = frames.pop(target_idx)
                        print(f"-> Successfully deleted Frame {target_idx + 1}!\n")
                    else:
                        print(f"-> Invalid frame number! Choose between 1 and {len(frames)}.\n")
                except ValueError:
                    print("-> Please provide a valid number (e.g., DELETE 2).\n")
            else:
                if frames:
                    removed_frame = frames.pop()
                    print(f"-> Deleted last saved frame (Total frames now: {len(frames)})\n")
                else:
                    print("-> No saved frames to delete!\n")
        elif cmd_action == 'EDIT' and len(parts) > 1:
            try:
                target_idx = int(parts[1]) - 1
                if 0 <= target_idx < len(frames):
                    print(f"\n--- Editing Frame {target_idx + 1} ---")
                    print("Current content:")
                    print(frames[target_idx])
                    print("Enter new lines for this frame. Type 'ENDEDIT' when done:")
                    
                    new_frame_lines = []
                    while True:
                        edit_line = input(f"Edit Frame {target_idx + 1} > ")
                        if edit_line.strip().upper() == 'ENDEDIT':
                            break
                        new_frame_lines.append(edit_line)
                    
                    if new_frame_lines:
                        frames[target_idx] = "\n".join(new_frame_lines)
                        print(f"-> Frame {target_idx + 1} updated successfully!\n")
                    else:
                        print("-> Frame update cancelled (empty input).\n")
                else:
                    print(f"-> Invalid frame number! Choose between 1 and {len(frames)}.\n")
            except ValueError:
                print("-> Please provide a valid number (e.g., EDIT 2).\n")
        elif cmd_upper == 'PLAY':
            if current_frame:
                frames.append("\n".join(current_frame))
                current_frame = []
            
            if not frames:
                print("No frames created yet! Type some art first.\n")
                continue
            
            try:
                fps_input = input("Enter playback speed (frames per second, e.g., 2, 5, 10): ")
                fps = float(fps_input)
                delay = 1.0 / max(fps, 0.1)
            except ValueError:
                delay = 0.5
            
            # Switch to alternate screen buffer for clean playback
            start_alternate_screen()
            clear_screen()
            
            try:
                stopped = False
                while not stopped:
                    for frame in frames:
                        print("\033[H\033[2J" + frame, end="", flush=True)
                        if check_for_stop(delay):
                            stopped = True
                            break
            except KeyboardInterrupt:
                pass
            
            # Restore original screen buffer immediately
            stop_alternate_screen()
            print("Stopped playback. Back in editor mode.\n")
                
        elif cmd_upper == 'END':
            if current_frame:
                frames.append("\n".join(current_frame))
                print(f"-> Frame {len(frames)} saved successfully!\n")
                current_frame = []
            else:
                print("-> Current frame is empty. Type some lines first.\n")
        else:
            current_frame.append(line)

    print("\nGoodbye!")

if __name__ == "__main__":
    main()