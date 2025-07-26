# Audio LLM Playground

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-lightgrey?logo=flask)
![Transformers](https://img.shields.io/badge/Transformers-4.40%2B-blueviolet?logo=python)
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

A simple collection of audio-to-text and text-generation tools powered by OpenAI Whisper and IBM Watsonx's LLAMA2.  
This project was created as part of **IBM’s course: _Building Generative AI-Powered Applications with Python_ (Module 4)**.  
Only formatting and cleanup changes were made to improve readability and usability.

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [File Descriptions](#file-descriptions)
- [Quick Start](#quick-start)
- [IBM Watsonx Credentials](#ibm-watsonx-credentials)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Overview

This repository demonstrates basic applications of combining:
- Large Language Models (LLMs) with **IBM Watsonx**
- Automatic Speech Recognition (ASR) using **Whisper**
- Interactive UIs built with **Gradio**

It includes apps that:
- Transcribe audio files
- Summarize spoken content
- Answer text prompts using Watsonx LLAMA2

## Tech Stack

| Library | Purpose |
|--------|---------|
| `transformers` | For Whisper ASR (speech-to-text) |
| `torch` | Backend for Whisper model |
| `ibm-watson-machine-learning` | Access IBM Watsonx and LLAMA2 |
| `langchain` | LLM orchestration and prompt chaining |
| `gradio` | Lightweight web UI |

## File Descriptions

| File | Description |
|------|-------------|
| `simple_llm.py` | Query IBM Watsonx LLAMA2 using a simple prompt |
| `simple_speech2text.py` | Transcribe an audio file using Whisper |
| `speech2text_app.py` | Gradio app: transcribe uploaded audio |
| `speech_analyzer.py` | Gradio app: transcribe and summarize audio using Whisper + LLAMA2 |

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/audio-llm-playground.git
cd audio-llm-playground
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Apps

```bash
# Transcription + Key Point Summary (Whisper + Watsonx)
python speech_analyzer.py

# Transcription Only (Whisper + Gradio)
python speech2text_app.py

# Simple Transcription (Whisper only, no UI)
python simple_speech2text.py

# Simple Watsonx LLM Query (text-only)
python simple_llm.py
```

## IBM Watsonx Credentials

To use the LLAMA2-based features (simple_llm.py and speech_analyzer.py), you'll need:

- A valid IBM Cloud account
- Your Watsonx project ID
- The Watsonx instance URL

Update the following fields in both scripts:

```bash
my_credentials = {"url": "https://us-south.ml.cloud.ibm.com"}
project_id = "your-project-id"
```

## Acknowledgements

This project was developed as part of **IBM’s**  
📘 _[Building Generative AI-Powered Applications with Python](https://www.coursera.org/learn/building-gen-ai-powered-applications?)_ course on Coursera (Module 4).

> ⚠️ **Disclaimer**: All code and logic were originally provided by IBM.  
Only minor improvements were made to formatting and structure for readability and reusability.

## 📄 License

This project is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).