# Text-to-Image using sdxl-turbo - README

## Overview

**Text-to-Image using sdxl-turbo** is a project that transforms textual descriptions into visually compelling images. This implementation utilizes the **SDXL-Turbo** model from StabilityAI via Hugging Face's Diffusers library. The application is built using **Gradio** for an interactive web interface, allowing users to generate high-quality images by simply entering prompts.

The project is hosted on Hugging Face Spaces and can be accessed at:  
[Text-to-Image on Hugging Face](https://huggingface.co/spaces/ajaysoni197/Text-to-image)

---

## Features

- **Text-to-Image Conversion**: Generate images from simple textual prompts.
- **Negative Prompts**: Exclude unwanted elements from the generated image using negative prompts.
- **Customizable Parameters**:  
  - *Seed*: Control image randomness or randomize it for unique outputs.
  - *Resolution*: Adjust width and height for tailored image sizes.
  - *Guidance Scale*: Fine-tune the model’s adherence to the prompt.
  - *Inference Steps*: Specify the number of steps for the generation process.
- **Predefined Examples**: Quickly test the tool with sample prompts.
- **Advanced Settings**: Accessible controls for fine-grained customization.

---

## Prerequisites

Ensure the following dependencies are installed:

- `transformers`
- `accelerate`
- `huggingface_hub`
- `gradio`
- `diffusers`
- `torch`
- `numpy`

Install all required libraries using:

```bash
pip install transformers accelerate huggingface_hub gradio diffusers torch numpy
```

---

## How It Works

1. **Input Prompt**: Enter a textual description of the desired image in the "Prompt" field.
2. **Optional Settings**:  
   - Add a *negative prompt* to avoid specific elements.
   - Adjust parameters such as seed, width, height, guidance scale, and inference steps in the "Advanced Settings" section.
3. **Image Generation**: Click the **Run** button to generate the image.
4. **Output**: The generated image and the seed used are displayed for review.

---

## Code Explanation

### Key Components

1. **Model Initialization**:  
   The Stable Diffusion XL Turbo model is loaded using the Hugging Face Diffusers library.

   ```python
   model_sdxl_turbo_id = "stabilityai/sdxl-turbo"
   model_sdxl = DiffusionPipeline.from_pretrained(model_sdxl_turbo_id, torch_dtype=torch_dtype)
   model_sdxl = model_sdxl.to(device)
   ```

2. **Image Generation Function**:  
   The `infer` function takes user inputs and generates an image using the model.

   ```python
   def infer(prompt, negative_prompt, seed, randomize_seed, width, height, guidance_scale, num_inference_steps, ...):
       if randomize_seed:
           seed = random.randint(0, MAX_SEED)
       generator = torch.Generator().manual_seed(seed)
       image = model_sdxl(...).images[0]
       return image, seed
   ```

3. **Gradio Interface**:  
   Gradio's `Blocks` layout organizes the user interface with input fields, sliders, buttons, and an output area.

   ```python
   with gr.Blocks(css=css) as demo:
       ...
       gr.on(
           triggers=[run_button.click, prompt.submit],
           fn=infer,
           inputs=[prompt, negative_prompt, seed, ...],
           outputs=[result, seed],
       )
   ```

4. **Predefined Examples**:  
   Sample prompts are included for quick testing.

   ```python
   examples = [
       "Astronaut in a jungle, sitting near a lion",
       "An influencer, blond hair, blue eyes, riding a green horse",
       "A delicious cheesecake slice",
   ]
   ```

---

## Running the Application

1. Save the code in a `.py` file or use it in a notebook.
2. Run the script. The Gradio app will launch and provide a URL to access the interface.
3. Enter a prompt and generate images by clicking **Run**.

---

## Hosting on Hugging Face Spaces

This project is also hosted on Hugging Face Spaces for easy access. Visit the following link to explore:  
[Text-to-Image on Hugging Face](https://huggingface.co/spaces/ajaysoni197/Text-to-image)

---

## Future Enhancements

- **Multimodal Features**: Combine image and text for hybrid generation.
- **Real-Time Adjustments**: Modify parameters dynamically during generation.
- **Additional Models**: Support for other diffusion models like DALL·E or Imagen.

---

## Credits

- **Model**: [StabilityAI/SDXL-Turbo](https://huggingface.co/stabilityai/sdxl-turbo)
- **Interface**: Built with [Gradio](https://gradio.app/)
- **Hosting**: [Hugging Face Spaces](https://huggingface.co/spaces)

For feedback or contributions, feel free to reach out.