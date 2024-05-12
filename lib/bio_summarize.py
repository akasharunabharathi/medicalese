"""
This module is responsible for handling user input and explaining their reports to them.
"""
import os
import requests
from decouple import config
from langchain.prompts import PromptTemplate

import ocr

os.environ["HUGGINGFACEHUB_API_TOKEN"] = config("HUGGINGFACEHUB_API_TOKEN")
headers = {"Authorization": f"Bearer {os.environ['HUGGINGFACEHUB_API_TOKEN']}"}
parameters = {"temperature": 0, "max_length": 1024}

API_URL = "https://api-inference.huggingface.co/models/Falconsai/medical_summarization"


def query_summarizer(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def bio_summarize(file_name: str):
    """
    Accepts a pdf file or an image as an input. Input is, additionally, a medical report. 
    This function reads the report, summairzes it for the user, and returns the summary.
    """
    is_pdf_file = ".pdf" in file_name
    image_types = [".jpeg", ".jpg", ".heic", ".png"]
    is_image_file = any(image_type in file_name for image_type in image_types)
    report = None

    template_message = """You are a nurse at a hospital, and are now dealing with patients 
    that don't know biolgy, and consequently, don't fully understand their reports. Your job 
    is to explain their reports to them, in a simpler manner, without the biological terms, i.e. in layman terms. 
    Help them understand what is happening with their bodies.
    Here is their report:\n\n{report_string}"""

    prompt_template = PromptTemplate.from_template(
        template = template_message
    )

    if is_pdf_file:
        # TODO: PDF File Handling
        pass
    elif is_image_file:
        report = ocr.image_report(file_name)
        prompt = prompt_template.format(report_string = report)
        report_summary = query_summarizer({"inputs":prompt, "parameters":parameters})
        print(report_summary)
        generated_text = ""
        generated_text = report_summary[0]["summary_text"]
        return clean_formatter(generated_text)
    else:
        raise TypeError("Not an accepted file type")

    return None

def clean_formatter(report_summary):
  sentences = report_summary.split(".")
  clean_report = ""
  sentence_count = 0
  for sentence in sentences:
    sentence = sentence.strip()
    if sentence != "":
      new_sentence = sentence[0].upper() + sentence[1:] + ". "
      if sentence_count == 0:
        clean_report += new_sentence
      else:
        clean_report += " " + new_sentence

  return clean_report