import requests

def get_diagnosis_from_llm(symptoms: str) -> str:
    prompt = f"""You are a medical assistant.
The patient describes the following symptoms: {symptoms}.
Based on this, suggest a possible diagnosis or advice. Be short and medically correct."""

    response = requests.post(
        "http://localhost:1234/v1/chat/completions",
        json={
            "model": "llama-3.1-3B",
            "messages": [
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 200
        }
    )

    return response.json()["choices"][0]["message"]["content"]
