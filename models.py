"""
This module is responsible for handling user input and explaining their reports to them.
"""
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from decouple import config
import os
import ocr

os.environ = config("HUGGINGFACE_HUB_API")

def bio_summarize(file_name: str):
    """
    Accepts a pdf file or an image as an input. Input is, additionally, a medical report. 
    This function reads the report, summairzes it for the user, and returns the summary.
    """
    llm = HuggingFaceHub(
    repo_id ="google/pegasus-xsum",
    task = "summarization",
    model_kwargs = {"temperature": 0, "max_length": 256},
    )

    template_message = """You are a nurse at a hospital, and are now dealing with patients 
    that don't know biolgy, and consequently, don't fully understand their reports. Your job 
    is to explain their reports to them, in a simple, reassuring way. Here is their report:\n\n{report_string}"""

    prompt_template = PromptTemplate.from_template(
        input_variables = ["report_string"],
        template = template_message
    )

    llm_chain = LLMChain(prompt = prompt_template, llm = llm)
    
    is_pdf_file = file_name.contains(".pdf")
    is_image_file = file_name.contains(".jpeg") or file_name.contains(".jpg") or file_name.contains(".heic") or file_name.contains(".png")
    report = None

    if is_pdf_file:
        pass
    elif is_image_file:
        report = ocr.image_report(file_name)
        print(report)
        print("\n\n")
        return llm_chain.run(report)
    else:
        pass

    return llm(prompt_template)
