from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

def run_llm_query():
    # Set IBM Watsonx credentials and generation parameters
    my_credentials = {"url": "https://us-south.ml.cloud.ibm.com"}
    params = {
        GenParams.MAX_NEW_TOKENS: 700,
        GenParams.TEMPERATURE: 0.1,
    }

    # Initialize the model
    llama_model = Model(
        model_id="meta-llama/llama-3-2-11b-vision-instruct",
        credentials=my_credentials,
        params=params,
        project_id="skills-network",
    )

    # Wrap the model with LangChain WatsonxLLM
    llm = WatsonxLLM(llama_model)

    # Define your prompt
    prompt = "How to read a book effectively?"
    
    # Get and return the response
    return llm(prompt)

if __name__ == "__main__":
    result = run_llm_query()
    print(result)