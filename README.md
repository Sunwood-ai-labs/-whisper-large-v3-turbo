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

# Whisper Large V3 Turbo - Audio Transcription & Translation

🎵 **A powerful speech-to-text web application powered by OpenAI's Whisper Large V3 Turbo model** 🎵

[日本語版](#日本語版) | [English](#english-version)

## English Version

### 🌟 Features

- **🎤 Multiple Input Methods**: Support for microphone recording, audio file upload, and YouTube video transcription
- **🌍 Multilingual Support**: Transcribe and translate audio in multiple languages
- **📄 SRT Subtitle Generation**: Export transcriptions as SRT subtitle files
- **⚡ GPU Acceleration**: Optimized for fast processing with CUDA support
- **🎯 High Accuracy**: Powered by OpenAI's state-of-the-art Whisper Large V3 Turbo model
- **🔄 Real-time Processing**: Fast transcription with batch processing optimization

### 🚀 Quick Start

#### Option 1: Use Online (Recommended)
Visit the [Hugging Face Space](https://huggingface.co/spaces/Sunwood-ai-labs/whisper-large-v3-turbo) to use the application directly in your browser.

#### Option 2: Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/Sunwood-ai-labs/whisper-large-v3-turbo.git
cd whisper-large-v3-turbo
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
# Install PyTorch (visit https://pytorch.org for specific instructions)
pip install torch
```

3. **Install system dependencies**
```bash
# On Ubuntu/Debian
sudo apt-get install ffmpeg

# On macOS with Homebrew
brew install ffmpeg

# On Windows, download FFmpeg from https://ffmpeg.org
```

4. **Run the application**
```bash
python app.py
```

5. **Open your browser** and navigate to the local URL displayed in the terminal (typically `http://localhost:7860`)

### 📖 Usage Guide

The application provides three different ways to transcribe audio:

#### 🎤 Microphone Tab
1. Click on the "Microphone" tab
2. Click the record button and speak into your microphone
3. Stop recording when finished
4. Select "transcribe" or "translate" task
5. Optionally enable "SRTで出力" for subtitle file output
6. Click "Submit" to process

#### 📁 Audio File Tab
1. Click on the "Audio file" tab
2. Upload an audio file (supports various formats: mp3, wav, m4a, etc.)
3. Select "transcribe" or "translate" task
4. Optionally enable "SRTで出力" for subtitle file output
5. Click "Submit" to process

#### 🎬 YouTube Tab
1. Click on the "YouTube" tab
2. Paste a YouTube video URL
3. Select "transcribe" or "translate" task
4. Optionally enable "SRTで出力" for subtitle file output
5. Click "Submit" to process

### 🔧 Technical Details

- **Model**: OpenAI Whisper Large V3 Turbo
- **Framework**: Gradio for web interface
- **Backend**: Hugging Face Transformers
- **Audio Processing**: FFmpeg
- **GPU Support**: CUDA-enabled for faster processing
- **Batch Size**: Optimized with batch size of 8
- **File Limits**: Up to 1GB for audio files, 1 hour for YouTube videos

### 🛠️ Development

#### Project Structure
```
whisper-large-v3-turbo/
├── app.py                 # Main application file
├── tab/                   # Tab-specific modules
│   ├── mf_transcribe.py   # Microphone interface
│   ├── file_transcribe.py # File upload interface
│   └── yt_transcribe.py   # YouTube interface
├── requirements.txt       # Python dependencies
├── packages.txt          # System dependencies
└── whisper_notebook.ipynb # Example notebook
```

#### Key Functions
- `transcribe()`: Main transcription function with SRT support
- `create_srt_content()`: Converts transcription to SRT format
- `format_timestamp()`: Formats time for SRT files
- `download_yt_audio()`: Downloads YouTube audio

### 📋 Requirements

- Python 3.8+
- PyTorch
- Transformers
- Gradio
- FFmpeg
- yt-dlp

### 🔗 Links

- [OpenAI Whisper](https://openai.com/research/whisper)
- [Hugging Face Model](https://huggingface.co/openai/whisper-large-v3-turbo)
- [Gradio Documentation](https://gradio.app)

---

## 日本語版

### 🌟 機能

- **🎤 複数の入力方法**: マイク録音、音声ファイルアップロード、YouTube動画の文字起こしに対応
- **🌍 多言語サポート**: 複数言語での音声認識と翻訳
- **📄 SRT字幕生成**: 文字起こし結果をSRT字幕ファイルとしてエクスポート
- **⚡ GPU高速化**: CUDA対応による高速処理
- **🎯 高精度**: OpenAIの最先端Whisper Large V3 Turboモデル搭載
- **🔄 リアルタイム処理**: バッチ処理最適化による高速文字起こし

### 🚀 クイックスタート

#### オプション1: オンライン使用（推奨）
[Hugging Face Space](https://huggingface.co/spaces/Sunwood-ai-labs/whisper-large-v3-turbo)にアクセスして、ブラウザで直接アプリケーションを使用できます。

#### オプション2: ローカルインストール

1. **リポジトリのクローン**
```bash
git clone https://github.com/Sunwood-ai-labs/whisper-large-v3-turbo.git
cd whisper-large-v3-turbo
```

2. **依存関係のインストール**
```bash
pip install -r requirements.txt
# PyTorchのインストール（https://pytorch.org で詳細な手順を確認）
pip install torch
```

3. **システム依存関係のインストール**
```bash
# Ubuntu/Debianの場合
sudo apt-get install ffmpeg

# macOS（Homebrew使用）の場合
brew install ffmpeg

# Windows の場合、https://ffmpeg.org からFFmpegをダウンロード
```

4. **アプリケーションの実行**
```bash
python app.py
```

5. **ブラウザを開いて**、ターミナルに表示されるローカルURL（通常 `http://localhost:7860`）にアクセス

### 📖 使用方法

アプリケーションは3つの異なる方法で音声を文字起こしできます：

#### 🎤 マイクタブ
1. 「Microphone」タブをクリック
2. 録音ボタンをクリックしてマイクに向かって話す
3. 録音完了後、停止ボタンをクリック
4. 「transcribe」または「translate」タスクを選択
5. 字幕ファイル出力が必要な場合は「SRTで出力」をチェック
6. 「Submit」をクリックして処理開始

#### 📁 音声ファイルタブ
1. 「Audio file」タブをクリック
2. 音声ファイルをアップロード（mp3、wav、m4aなど各種形式に対応）
3. 「transcribe」または「translate」タスクを選択
4. 字幕ファイル出力が必要な場合は「SRTで出力」をチェック
5. 「Submit」をクリックして処理開始

#### 🎬 YouTubeタブ
1. 「YouTube」タブをクリック
2. YouTube動画のURLを貼り付け
3. 「transcribe」または「translate」タスクを選択
4. 字幕ファイル出力が必要な場合は「SRTで出力」をチェック
5. 「Submit」をクリックして処理開始

### 🔧 技術詳細

- **モデル**: OpenAI Whisper Large V3 Turbo
- **フレームワーク**: Gradio（Webインターフェース）
- **バックエンド**: Hugging Face Transformers
- **音声処理**: FFmpeg
- **GPU対応**: 高速処理のためのCUDA対応
- **バッチサイズ**: 8で最適化
- **ファイル制限**: 音声ファイル最大1GB、YouTube動画最大1時間

### 🛠️ 開発

#### プロジェクト構造
```
whisper-large-v3-turbo/
├── app.py                 # メインアプリケーションファイル
├── tab/                   # タブ固有のモジュール
│   ├── mf_transcribe.py   # マイクインターフェース
│   ├── file_transcribe.py # ファイルアップロードインターフェース
│   └── yt_transcribe.py   # YouTubeインターフェース
├── requirements.txt       # Python依存関係
├── packages.txt          # システム依存関係
└── whisper_notebook.ipynb # サンプルノートブック
```

#### 主要機能
- `transcribe()`: SRT対応メイン文字起こし機能
- `create_srt_content()`: 文字起こし結果をSRT形式に変換
- `format_timestamp()`: SRTファイル用の時間フォーマット
- `download_yt_audio()`: YouTube音声ダウンロード

### 📋 要件

- Python 3.8以上
- PyTorch
- Transformers
- Gradio
- FFmpeg
- yt-dlp

### 🔗 リンク

- [OpenAI Whisper](https://openai.com/research/whisper)
- [Hugging Face モデル](https://huggingface.co/openai/whisper-large-v3-turbo)
- [Gradio ドキュメント](https://gradio.app)

---

## 📄 License

This project is open source. Please check the repository for license details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference