import requests

def get_diagnosis_from_llm(context: str) -> str:
    response = requests.post(
        "http://localhost:1234/v1/chat/completions",
        json={
            "model": "llama-3.1-3B",
            "messages": [
                {"role": "system", "content": "You are a helpful medical assistant. Analyze the conversation and provide relevant medical advice."},
                {"role": "user", "content": context}
            ],
            "temperature": 0.3,
            "max_tokens": 200
        }
    )

    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error processing LLM response: {str(e)}")
        return "I apologize, but I'm having trouble processing your request. Could you please rephrase your symptoms?"
