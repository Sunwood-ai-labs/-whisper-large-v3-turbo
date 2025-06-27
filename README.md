---
title: Whisper Turbo
emoji: 🤯
colorFrom: indigo
colorTo: red
sdk: gradio
sdk_version: 5.0.0
app_file: app.py
pinned: false
tags:
- whisper-event
---

# Whisper Large V3 Turbo Audio Transcription

This is a Gradio-based web application that provides audio transcription and translation using OpenAI's Whisper Large V3 Turbo model. The application offers multiple interfaces for different audio input sources and supports SRT subtitle generation.

## Features

### 🎤 **Microphone Recording**
- Real-time audio recording from your microphone
- Instant transcription or translation
- Support for arbitrary length recordings

### 📁 **File Upload**
- Upload audio files for transcription
- Supports common audio formats
- Batch processing capability

### 🎬 **YouTube Integration**
- Direct transcription from YouTube URLs
- Automatic audio extraction
- Support for videos up to 1 hour in length

### 📝 **Output Options**
- **Text Output**: Plain text transcription
- **SRT Subtitles**: Downloadable subtitle files with timestamps
- **Translation**: Convert speech to English text
- **Transcription**: Convert speech to text in original language

## Technical Specifications

- **Model**: [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)
- **Framework**: 🤗 Transformers
- **Interface**: Gradio with Ocean theme
- **GPU Acceleration**: Enabled with Hugging Face Spaces GPU
- **Chunk Processing**: 30-second chunks for optimal performance
- **Batch Size**: 8 for efficient processing

## Usage

### Getting Started
1. Choose your preferred input method from the three tabs:
   - **Microphone**: Record audio directly
   - **Audio file**: Upload pre-recorded files
   - **YouTube**: Paste a YouTube video URL

2. Select your task:
   - **Transcribe**: Convert speech to text in the original language
   - **Translate**: Convert speech to English text

3. Choose output format:
   - Uncheck "SRTで出力" for plain text
   - Check "SRTで出力" to download SRT subtitle file

4. Click submit and wait for processing

### File Limitations
- Audio file size limit: 1GB
- YouTube video length limit: 1 hour (3600 seconds)
- Supported audio formats: WAV, MP3, FLAC, M4A, and more

## Installation & Setup

This application is designed to run on Hugging Face Spaces with GPU acceleration. For local development:

```bash
# Install dependencies
pip install -r requirements.txt

# Install system packages (Ubuntu/Debian)
sudo apt-get install ffmpeg

# Run the application
python app.py
```

## Dependencies

- `transformers` - Hugging Face Transformers library
- `yt-dlp` - YouTube audio extraction
- `gradio` - Web interface framework
- `torch` - PyTorch for model inference
- `ffmpeg` - Audio processing (system package)

## Architecture

The application consists of:
- `app.py` - Main application with core transcription logic
- `tab/mf_transcribe.py` - Microphone interface
- `tab/file_transcribe.py` - File upload interface  
- `tab/yt_transcribe.py` - YouTube URL interface
- `whisper_notebook.ipynb` - Example usage and demos

---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference