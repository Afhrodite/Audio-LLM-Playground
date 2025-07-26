from transformers import pipeline

def transcribe_audio_file(audio_path="downloaded_audio.mp3"):
    # Load Whisper ASR model
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )

    # Transcribe the audio file
    transcription = pipe(audio_path, batch_size=8)["text"]
    return transcription

if __name__ == "__main__":
    result = transcribe_audio_file()
    print(result)