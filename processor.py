import os
import groq
from typing import List

client = groq.Groq(api_key=os.environ.get("GROQ_API_KEY"))

def process_symptoms(symptoms: List[str]) -> List[int]:
    all_symptoms = ["fever", "cough", "fatigue", "headache", "nausea", "shortness of breath", "sore throat", "body aches", "loss of taste or smell", "diarrhea"]
    
    prompt = f"""Given the following list of symptoms: {', '.join(symptoms)}
    Please return a one-hot encoded vector for these symptoms based on the following list of all possible symptoms: {', '.join(all_symptoms)}
    Return only the vector as a comma-separated list of 0s and 1s, without any additional text."""

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that processes medical symptoms and returns one-hot encoded vectors."},
            {"role": "user", "content": prompt}
        ],
        model="mixtral-8x7b-32768",
        temperature=0,
        max_tokens=100
    )

    one_hot_vector = [int(bit) for bit in response.choices[0].message.content.strip().split(',')]
    
    return one_hot_vector

symptoms = ["fever", "cough", "fatigue"]
result = process_symptoms(symptoms)
print(f"One-hot encoded vector: {result}")