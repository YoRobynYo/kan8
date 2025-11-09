import subprocess
import os
import sys

OLLAMA_PORT = 11434

def find_and_kill_process():
    """Finds the process using the Ollama port and kills it."""
    print(f"Checking for process on port {OLLAMA_PORT}...")
    
    # Use lsof to find the process ID (PID)
    try:
        # -t: only display PID
        # -i: filter by internet address (port)
        lsof_output = subprocess.run(
            ['lsof', '-ti', f':{OLLAMA_PORT}'],
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError:
        # lsof returns non-zero if no process is found, which is fine
        return False

    pids = lsof_output.stdout.strip().split()
    
    if not pids:
        print("No process found using the port.")
        return False

    for pid in pids:
        print(f"Found process with PID {pid} using port {OLLAMA_PORT}. Killing it...")
        try:
            # Kill the process
            subprocess.run(['kill', '-9', pid], check=True)
            print(f"Successfully killed process {pid}.")
        except subprocess.CalledProcessError as e:
            print(f"Error killing process {pid}: {e}", file=sys.stderr)
            
    return True

def start_ollama():
    """Starts the Ollama server."""
    print("\nStarting Ollama server...")
    # Use os.execvp to replace the current Python process with the ollama serve command
    # This keeps the terminal session active for the server output
    try:
        # The 'serve' command will run in the foreground
        os.execvp('ollama', ['ollama', 'serve'])
    except FileNotFoundError:
        print("Error: 'ollama' command not found. Make sure it's in your PATH.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # 1. Find and kill any existing process
    find_and_kill_process()
    
    # 2. Start the Ollama server
    start_ollama()