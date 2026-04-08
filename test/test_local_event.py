# test_local_event.py
import gradio as gr

my_event = gr.LocalEvent("my_event")


def emitter(text, request: gr.Request):
    print(f"session hash: {request.session_hash}")
    gr.emit("my_event", data={"msg": text})
    return "emitted"


def receiver(evt: gr.LocalEventData):
    # Backend-only side effect — no UI output
    print(f"received: {evt.data}")


with gr.Blocks() as demo:
    inp = gr.Textbox()
    out_a = gr.Textbox()

    btn = gr.Button("Go")
    btn.click(fn=emitter, inputs=[inp], outputs=out_a)

    gr.on([my_event], receiver, inputs=None, outputs=None)

demo.launch()
