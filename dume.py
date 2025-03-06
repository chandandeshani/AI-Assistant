import os
from langchain_ollama import OllamaLLM
from config import SYSTEM_PROMPT  # Import SYSTEM_PROMPT from config.py
import asyncio
import edge_tts
import sounddevice as sd
import soundfile as sf
import tempfile
import os

async def text_to_speech(text, voice="en-US-JennyNeural", rate="+5%"):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as temp_audio:
        temp_audio_path = temp_audio.name  # Get the path before closing

        # Generate speech and save it to a file
        tts = edge_tts.Communicate(text, voice=voice, rate=rate)
        await tts.save(temp_audio_path)

        # Read the audio file and play it
        data, samplerate = sf.read(temp_audio_path)
        sd.play(data, samplerate)
        sd.wait()


# Set model to Llama3
llm = OllamaLLM(model="llama3")

# Chat history file
CHAT_FILE = "chat.txt"

# Function to read chat history
def load_chat_history():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r", encoding="utf-8") as file:
            return file.read().strip()
    return ""

# Function to save chat history
def save_chat_history(history):
    with open(CHAT_FILE, "w", encoding="utf-8") as file:
        file.write(history)

print("dume is running! Type 'exit' to stop.")

# Load previous chat history
chat_history = load_chat_history()

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        break

    if user_input.lower() == "clear":
        chat_history = ""
        save_chat_history(chat_history)
        print("dume: Conversation history cleared.")
        continue

    # Construct prompt with chat history
    prompt = f"{SYSTEM_PROMPT}\n\nPrevious Chat:\n{chat_history}\n\nUser: {user_input}\ndume:"

    # Get response from Llama3
    response = llm.invoke(prompt).strip()
    
    asyncio.run(text_to_speech(response))
    print(f"dume: {response}")

    # Update chat history
    chat_history += f"\nUser: {user_input}\ndume: {response}"

    # Save updated chat history
    save_chat_history(chat_history)

