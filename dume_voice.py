import os
import time
import sounddevice as sd
import soundfile as sf

VOICE_FOLDER = "voice"

def get_sorted_audio_files():
    """Fetch and sort the audio files in order (1.mp3, 2.mp3, ...)"""
    files = [f for f in os.listdir(VOICE_FOLDER) if f.endswith(".mp3")]
    return sorted(files, key=lambda x: int(os.path.splitext(x)[0]))  # Sort by number

def wait_for_file(file_path, timeout=5):
    """Wait for the file to be completely written before opening it."""
    start_time = time.time()
    while not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        if time.time() - start_time > timeout:  # Prevent infinite waiting
            print(f"Error: Timed out waiting for {file_path}")
            return False
        time.sleep(0.5)  # Wait 500ms before checking again
    return True

def play_audio(file_path):
    """Play an audio file."""
    if not wait_for_file(file_path):
        return  # Skip if the file is not ready

    try:
        data, samplerate = sf.read(file_path)
        sd.play(data, samplerate)
        sd.wait()
    except Exception as e:
        print(f"Error playing {file_path}: {e}")

def main():
    """Continuously check for new audio files and play them in order."""
    played_files = set()  # Keep track of played files

    # Wait until at least one audio file is available
    while not get_sorted_audio_files():
#        print("Waiting for audio files to be created...")
        time.sleep(1)  # Check every second

    while True:
        files = get_sorted_audio_files()
        for file in files:
            file_path = os.path.join(VOICE_FOLDER, file)
            if file not in played_files:
                print(f"Playing: {file}")
                play_audio(file_path)
                played_files.add(file)

        print("Waiting for new audio files...")
        time.sleep(1)  # Wait for 1 second before checking again

if __name__ == "__main__":
    os.makedirs(VOICE_FOLDER, exist_ok=True)  # Ensure folder exists
    main()

