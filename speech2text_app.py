from transformers import pipeline
import gradio as gr

def transcribe_audio(audio_file):
    # Initialize Whisper pipeline
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )
    return pipe(audio_file, batch_size=8)["text"]

def main():
    iface = gr.Interface(
        fn=transcribe_audio,
        inputs=gr.Audio(sources="upload", type="filepath"),
        outputs=gr.Textbox(),
        title="Audio Transcription App",
        description="Upload an audio file to get the transcribed text.",
    )
    iface.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()