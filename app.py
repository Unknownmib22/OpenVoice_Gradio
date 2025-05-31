import gradio as gr
import os
from openvoice.openvoice_app import inference

def generate_voice(reference_audio, text, emotion, language):
    output_path = "output.wav"
    if reference_audio is not None:
        reference_path = "reference_temp.wav"
        reference_audio.save(reference_path)

        inference(
            reference_audio_path=reference_path,
            text=text,
            output_path=output_path,
            emotion=emotion,
            language=language
        )

        return output_path
    return None

gr.Interface(
    fn=generate_voice,
    inputs=[
        gr.Audio(label="Upload Your Voice (WAV)", type="file"),
        gr.Textbox(label="Text to Speak", placeholder="Type here...", lines=2),
        gr.Dropdown(label="Emotion", choices=["neutral", "happy", "sad", "angry"], value="neutral"),
        gr.Dropdown(label="Language", choices=["en", "hi", "zh", "es", "fr", "de", "ja"], value="en")
    ],
    outputs=gr.Audio(label="Generated Voice"),
    title="OpenVoice Voice Cloner",
    description="Upload your voice and generate audio in your style."
).launch()
