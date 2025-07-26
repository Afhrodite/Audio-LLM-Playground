from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
import gradio as gr

def get_llm_chain():
    # IBM Watsonx credentials and config
    my_credentials = {"url": "https://us-south.ml.cloud.ibm.com"}
    params = {
        GenParams.MAX_NEW_TOKENS: 800,
        GenParams.TEMPERATURE: 0.1,
    }

    # Load LLAMA2 model
    llama_model = Model(
        model_id="meta-llama/llama-3-2-11b-vision-instruct",
        credentials=my_credentials,
        params=params,
        project_id="skills-network",
    )

    # Wrap the model
    llm = WatsonxLLM(llama_model)

    # Create prompt template
    prompt_template = """
<s><<SYS>>
List the key points with details from the context: 
[INST] The context: {context} [/INST] 
<</SYS>>
"""
    prompt = PromptTemplate(input_variables=["context"], template=prompt_template)

    # Return the chain
    return LLMChain(llm=llm, prompt=prompt)

def analyze_audio(audio_file):
    # Transcribe the audio
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )
    transcript = pipe(audio_file, batch_size=8)["text"]

    # Analyze the text
    chain = get_llm_chain()
    return chain.run(transcript)

def main():
    iface = gr.Interface(
        fn=analyze_audio,
        inputs=gr.Audio(sources="upload", type="filepath"),
        outputs=gr.Textbox(),
        title="Audio Summary Generator",
        description="Upload an audio file to get summarized key points.",
    )
    iface.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()
