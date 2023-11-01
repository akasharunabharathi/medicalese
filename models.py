"""
This module is responsible for handling user input and explaining their reports to them.
"""
from langchain import HuggingFaceHub
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from decouple import config
import os
import ocr

def bio_summarize(file_name: str):
    """
    Accepts a pdf file or an image as an input. Input is, additionally, a medical report. 
    This function reads the report, summairzes it for the user, and returns the summary.
    """
    llm = HuggingFaceHub(
    repo_id ="google/pegasus-xsum",
    task = "summarization",
    model_kwargs = {"temperature": 0, "max_length": 1024},
    )

    is_pdf_file = ".pdf" in file_name
    image_types = [".jpeg", ".jpg", ".heic", ".png"]
    is_image_file = any(image_type in file_name for image_type in image_types)
    # is_image_file = file_name.contains(".jpeg") or file_name.contains(".jpg") or file_name.contains(".heic") or file_name.contains(".png")
    report = None

    template_message = """You are a nurse at a hospital, and are now dealing with patients 
    that don't know biolgy, and consequently, don't fully understand their reports. Your job 
    is to explain their reports to them, in a simpler manner, without the biological terms, i.e. in layman terms. 
    Help them understand what is happening with their bodies.
    Here is their report:\n\n{report_string}"""

    prompt_template = PromptTemplate.from_template(
        template = template_message
    )

    llm_chain = LLMChain(prompt = prompt_template, llm = llm)

    if is_pdf_file:
        pass
    elif is_image_file:
        report = ocr.image_report(file_name)
        prompt_template.format(report_string = report)
        return llm_chain.run(report)
    else:
        pass

    return None
