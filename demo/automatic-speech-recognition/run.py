import gradio as gr
import os

# save your HF API token from https:/hf.co/settings/tokens as an env variable to avoid rate limiting
hf_token = os.getenv("hf_token")

# automatically load the interface from a HF model
# you can remove the hf_token parameter if you don't care about rate limiting.
demo = gr.load(
    "huggingface/facebook/wav2vec2-base-960h",
    title="Speech-to-text",
    inputs="mic",
    description="Let me try to guess what you're saying!",
    hf_token=hf_token
)

demo.launch()
