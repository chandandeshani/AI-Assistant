# Dume AI Assistant

This repository contains **Dume**, a voice-interactive AI assistant powered by **LangChain, Llama3, and Edge TTS**. It responds in real-time using text-to-speech and maintains conversation history.

## Features
- **Conversational AI** powered by **Llama3**
- **Text-to-Speech (TTS)** with **Edge TTS**
- **Voice playback system** for sequential audio responses
- **Persistent chat history**
- **Customizable personality** via `config.py`

## Files
- `config.py` - Defines Dume's personality, behavior, and response style.
- `dume.py` - Core chatbot that processes text input and generates responses.
- `dume_voice.py` - Handles sequential voice playback for audio responses.
- `dummy.py` - Main entry point that runs `dume.py` and `dume_voice.py` simultaneously.

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```
2. Install dependencies:
   ```bash
   pip install langchain_ollama edge-tts sounddevice soundfile
   ```

## Usage
Run `dummy.py` to start the assistant:
```bash
python dummy.py
```
This script launches both `dume.py` (AI chat) and `dume_voice.py` (voice playback).

### Commands
- **Type messages** to chat with Dume.
- **Type 'exit'** to stop the assistant.
- **Type 'clear'** to reset conversation history.

## Notes
- Dume's responses are spoken out loud using **Edge TTS**.
- The `voice` folder is created temporarily and deleted after execution.


