import gradio as gr
from app import transcribe, MODEL_NAME
import tempfile

def file_transcribe_fn(audio, task, as_srt):
    if as_srt:
        srt_str = transcribe(audio, task, as_srt=True)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".srt", mode="w", encoding="utf-8") as f:
            f.write(srt_str)
            return f.name
    else:
        return transcribe(audio, task, as_srt=False)

file_transcribe = gr.Interface(
    fn=file_transcribe_fn,
    inputs=[
        gr.Audio(sources="upload", type="filepath", label="Audio file"),
        gr.Radio(["transcribe", "translate"], label="Task", value="transcribe"),
        gr.Checkbox(label="SRTで出力", value=False)
    ],
    outputs=gr.outputs.File(label="SRTファイル") if True else "text",
    title="Whisper Large V3: Transcribe Audio",
    description=(
        "Transcribe long-form microphone or audio inputs with the click of a button! Demo uses the"
        f" checkpoint [{MODEL_NAME}](https://huggingface.co/{MODEL_NAME}) and 🤗 Transformers to transcribe audio files"
        " of arbitrary length."
    ),
    allow_flagging="never",
)