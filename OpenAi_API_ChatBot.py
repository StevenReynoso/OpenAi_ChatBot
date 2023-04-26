import openai
import gradio

def CustomChatGPT(user_input, api_key):
    messages.append({"role": "user", "content": user_input})
    openai.api_key = api_key
    response = openai.Completion.create(
        engine = "davinci",
        prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages]),
        temperature = 0.5,
        max_tokens = 1024,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    ChatGPT_reply = response.choices[0].text
    messages.append({"role": "system", "content": ChatGPT_reply.strip()})
    return ChatGPT_reply.strip()


api_key_input = gradio.inputs.Textbox(lines=1, label="Enter your OpenAI API key", type="password")
chat_input = gradio.inputs.Textbox(lines=7, label="Enter your message", placeholder="Type your message here...")
chat_output = gradio.outputs.Textbox(label="Chatbot response")

messages = [{"role": "system", "content": "You are a psychologist"}]

gradio.Interface(
    CustomChatGPT,
    inputs=[chat_input, api_key_input],
    outputs=chat_output,
    title="Chatbot",
    description="Talk with the Chatbot using the GPT-3 model"
).launch()
