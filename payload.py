import subprocess

# Open a new GNOME Terminal window and list directory contents
subprocess.run(["gnome-terminal", "--", "bash", "-c", "ls; exec bash"])
