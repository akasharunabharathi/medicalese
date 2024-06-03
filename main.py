import ocr
import os
import bio_summarize as bio_summarize
from fastapi import FastAPI, File, UploadFile

import warnings
warnings.filterwarnings("ignore")

app = FastAPI()

app.get("/")
async def home_page():
    return {"info":"absolutely nothing to see here"}

@app.post("/process_image")
async def process_image(image_file: UploadFile):
    image_file_obj = image_file.file # This is the SpooledTempFile I can pass to functions that expect a file-like objetc
    report_json = bio_summarize(image_file_obj) # dictionary with the og report text and the summary
    # ommitted explainer.py calling since I don;t know how much space Fargate will allot to the host machines 
    # running my containers, I would like to stay within the Free Tier... and Llama-3 is well, large -_-
    
    return report_json

if __name__ == "__main__":
    os.system('export PYTHONPATH="/workspaces/medicalese/lib:$PYTHONPATH"')
    # os.system("fastapi run lib/main.py")
    os.system("uvicorn main:app --host 0.0.0.0 --port 80")