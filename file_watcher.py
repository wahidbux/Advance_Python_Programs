# filename: file_watcher.py
# Run: python file_watcher.py <path_to_file>

import sys, time, os

def watch_file(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist.")
        return
    
    print(f"Watching {filepath} for changes (Press Ctrl+C to stop)...")
    last_modified = os.path.getmtime(filepath)

    try:
        while True:
            time.sleep(1)
            new_modified = os.path.getmtime(filepath)
            if new_modified != last_modified:
                print(f"{filepath} modified at {time.ctime(new_modified)}")
                last_modified = new_modified
    except KeyboardInterrupt:
        print("\nStopped watching.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_watcher.py <path_to_file>")
        sys.exit(1)
    watch_file(sys.argv[1])
