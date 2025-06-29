import requests
import os
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("apiKey_groq")

# Choose the model: "mixtral-8x7b-32768", "llama3-70b-8192",
MODEL = "llama3-70b-8192"

def enhance_text(text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "system", "content":  "You are a helpful assistant that rewrites someone's background into a professional resume format. Use bullet points, improve grammar, clarity, and tone. Structure it like a resume (Summary, Skills, Education, etc.."},
            {"role": "user", "content": f"Enhance this text:\n\n{text}"}
        ],
        "temperature": 0.7
    }

    try:
     response = requests.post(url, headers=headers, json=payload)
     response.raise_for_status()
     result = response.json()
     return result['choices'][0]['message']['content']
    except Exception as e:
       return f"Error: {e}"
    

# Example usage
#user_input = input("Input text to enhance : ") #"this is an example of bad writting which needs improvement."
#enhanced = enhance_text(user_input)
#print("Enhanced Text:\n", enhanced)

demo = gr.Interface( fn=enhance_text,
                     inputs=gr.Textbox(label="Enter Raw Resume Info", lines=8, placeholder="Paste your background info here..."),
                     outputs=gr.Textbox(label="Enhanced Resume Format"),
                     title="Custom chatbot")
demo.launch()
