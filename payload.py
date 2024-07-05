import subprocess

subprocess.run(["xfce4-terminal", "--", "bash", "-c", "ls; exec bash"])
