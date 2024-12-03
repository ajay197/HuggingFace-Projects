# -*- coding: utf-8 -*-
"""Image Captioning HuggingFace

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FYjUmqM33RHpfd_855qQqGtMasztVYKF

### Image Semantics (Captioning)
"""

!pip install transformers accelerate huggingface_hub gradio

import gradio as gr
from PIL import Image
import torch
from transformers import pipeline

pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

# Generate semantics
def generate_semantics(image):
    caption = pipe(image)[0]['generated_text']
    print("caption-----", caption)
    return caption

# Function to clear the input and output fields
def clear_fields_caption():
    return None, ""

# Gradio interface
with gr.Blocks(css="""
    .orange-btn {background-color: orange; color: white;}
    .output-box {width: 100%; height: 300px; overflow: auto; object-fit: contain; margin-left: 0;}
    """) as iface:
    iface.title = "Geniphy.ai"
    iface.description = "Generate images based on your prompt using a diffusion model"

    with gr.Tabs():
        # Image semantics tab
        with gr.Tab("Image Semantics"):
            with gr.Row():
                # Left Column: Uploaded image
                with gr.Column():
                    uploaded_image = gr.Image(label="Upload an Image", type="pil")  # Input image

                # Right Column: Caption output
                with gr.Column():
                    generated_caption = gr.Textbox(label="Generated Semantics", lines=2)  # Caption output

            # Row for buttons
            with gr.Row():
                clear_button = gr.Button("Clear")  # Clear button on the left
                generate_button = gr.Button("Generate Semantics", elem_classes="orange-btn")  # Orange button on the right

            # Button click actions
            generate_button.click(
                fn=generate_semantics,
                inputs=uploaded_image,
                outputs=generated_caption
            )

            clear_button.click(
                fn=clear_fields_caption,
                inputs=None,
                outputs=[uploaded_image, generated_caption]
            )

iface.launch()

