import torch
import gradio as gr

# Use a pipeline as a high-level helper
from transformers import pipeline

text_summarizer = pipeline(
    "summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype=torch.bfloat16
)


def generate_summary(input):
    output = text_summarizer(input)
    return output[0]["summary_text"]


gr.close_all()
demo = gr.Interface(
    fn=generate_summary,
    inputs=[gr.Textbox(label="Input Text to Summarize", lines="10")],
    outputs=[gr.Textbox(label="Summarized Text!", lines="4")],
    title="Text Summarizer",
    description="This application summarizes given text",
)

demo.launch()
