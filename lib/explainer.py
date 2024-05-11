import os
import requests
from decouple import config
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain.prompts import PromptTemplate

os.environ["HUGGINGFACEHUB_API_TOKEN"] = config("HUGGINGFACEHUB_API_TOKEN")
login(token = os.environ["HUGGINGFACEHUB_API_TOKEN"])
# headers = {"Authorization": f"Bearer {os.environ['HUGGINGFACEHUB_API_TOKEN']}"}
parameters = {"num_return_sequences":1, "temperature":0.7}

model_name = "meta-llama/Meta-Llama-3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, token=os.environ["HUGGINGFACEHUB_API_TOKEN"])

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B"

# def query_explainer(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()

def explainer(text):
    template_message = """You are a nurse at a hospital, and are now dealing with patients 
    that don't know biolgy, and consequently, don't fully understand their reports. Your job 
    is to explain their reports to them, in a simpler manner, without the biological terms, i.e. in layman terms. 
    Help them understand what is happening with their bodies.
    Here is the medical summary of their condition:\n\n{summary}"""

    prompt_template = PromptTemplate.from_template(
        template = template_message
    )

    prompt = prompt_template.format(summary = text)
    inputs = tokenizer(prompt)
    output_explanation = tokenizer.decode(
        model.generate(inputs, **parameters)[0],
        skip_special_tokens = True
    )
    print(output_explanation)
    return output_explanation