"""
This module is responsible for handling user input and explaining their reports to them.
"""
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
import ocr

llm = HuggingFacePipeline.from_model_id(
    model_id="google/pegasus-xsum",
    task="summarization",
    model_kwargs={"temperature": 0, "max_length": 256},
)

def bio_summarize(file_name: str):
    """
    Accepts a pdf file or an image as an input. Input is, additionally, a medical report. 
    This function reads the report, summairzes it for the user, and returns the summary.
    """
    is_pdf_file = file_name.contains(".pdf")
    is_image_file = file_name.contains(".jpeg") or file_name.contains(".jpg") or file_name.contains(".heic") or file_name.contains(".png")
    report = None
    
    template_message = """You are a nurse at a hospital, and are now dealing with patients 
    that don't know biolgy, and consequently, don't fully understand their reports. Your job 
    is to explain their reports to them, in a simple, reassuring way. Here is their report:\n\n{report_string}"""
    
    prompt_template = PromptTemplate.from_template(
        input_variables = ["report_string"],
        template = template_message
    )

    if is_pdf_file:
        pass
    elif is_image_file:
        report = ocr.image_report(file_name)
        print(report)
        prompt_template.format(report_string = report)
    else:
        pass

    return llm(prompt_template)
