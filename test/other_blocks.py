
import gradio as gr

with gr.Blocks() as demo:

    # my_event = gr.LocalEvent("my_event")

    # def emitter(text, request: gr.Request):
    #     print(f"session hash: {request.session_hash}")
    #     gr.emit("my_event", data={"msg": text})
    #     return "emitted"

    # def receiver(evt: gr.LocalEventData):
    #     print(f"receiving: {evt.data}")
    #     return evt.data["msg"]

    inp = gr.Textbox()
    out_a = gr.Textbox()

    # out_b = gr.Textbox()

    btn = gr.Button("Go")

    # btn.click(emitter, inputs=[inp], outputs=out_a)
    btn.click(lambda x: gr.emit("my_event", data={"msg": x}), inputs=[inp], outputs=out_a)



demo.launch()
