import gradio as gr

# custom modules
from bio_summarize import bio_summarize
from explainer import explainer

def func_composition(image_file):
    summarized_report = bio_summarize(image_path) # accepts an image as an input
    explained_report = explainer(summarized_report)

    return explained_report

gr_demo = gr.Interface(
    fn = func_composition,
    inputs = gr.inputs.Image(type = "pil"),
    outputs = "text",
    title = "Medicalese -> English"
    description="Upload your report here"
)

gr_demo.launch()