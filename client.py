# client.py (OLLAMA version)
import ollama

def ask_openai(prompt):
    response = ollama.chat(
        model='mistral',
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    return response['message']['content']
