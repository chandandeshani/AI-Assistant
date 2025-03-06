import subprocess
import os
import shutil

# Define folder name
VOICE_FOLDER = "/home/veronica/Desktop/dume_speech/voice"

# Create the voice folder temporarily
os.makedirs(VOICE_FOLDER, exist_ok=True)

# Define script paths
script1 = "/home/veronica/Desktop/dume_speech/dume.py"
script2 = "/home/veronica/Desktop/dume_speech/dume_voice.py"

try:
    # Run both scripts concurrently
    process1 = subprocess.Popen(["python3", script1])
    process2 = subprocess.Popen(["python3", script2])

    # Wait for both scripts to finish
    process1.wait()
    process2.wait()
finally:
    # Remove the voice folder after both scripts have finished
    shutil.rmtree(VOICE_FOLDER, ignore_errors=True)
    print("Temporary 'voice' folder deleted.")

