import gradio as gr
from app import yt_transcribe as yt_transcribe_fn, MODEL_NAME
import tempfile

def yt_transcribe_wrap(yt_url, task, as_srt):
    html, text = yt_transcribe_fn(yt_url, task, as_srt=as_srt)
    if as_srt:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".srt", mode="w", encoding="utf-8") as f:
            f.write(text)
            return html, f.name
    else:
        return html, text

yt_transcribe = gr.Interface(
    fn=yt_transcribe_wrap,
    inputs=[
        gr.Textbox(lines=1, placeholder="Paste the URL to a YouTube video here", label="YouTube URL"),
        gr.Radio(["transcribe", "translate"], label="Task", value="transcribe"),
        gr.Checkbox(label="SRTで出力", value=False)
    ],
    outputs=[gr.outputs.HTML(label="YouTube"), gr.outputs.File(label="SRTファイル")],
    title="Whisper Large V3: Transcribe YouTube",
    description=(
        "Transcribe long-form YouTube videos with the click of a button! Demo uses the checkpoint"
        f" [{MODEL_NAME}](https://huggingface.co/{MODEL_NAME}) and 🤗 Transformers to transcribe video files of"
        " arbitrary length."
    ),
    allow_flagging="never",
)