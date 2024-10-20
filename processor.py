import os
import groq
from typing import List
from joblib import load
import numpy as np


os.environ["GROQ_API_KEY"] = "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"
client = groq.Groq(api_key=os.environ["GROQ_API_KEY"])

all_symptoms=['abdominal_pain','acidity','altered_sensorium','anxiety','back_pain','blackheads','bladder_discomfort','blister','bloody_stool','blurred_and_distorted_vision','breathlessness','bruising','burning_micturition','chest_pain','chills','cold_hands_and_feets','constipation','continuous_feel_of_urine','continuous_sneezing','cough','cramps','dark_urine','dehydration','diarrhoea','dischromic_patches','dizziness','extra_marital_contacts','fatigue','foul_smell_ofurine','headache','high_fever','hip_joint_pain','indigestion','joint_pain','knee_pain','lethargy','loss_of_appetite','loss_of_balance','mood_swings','movement_stiffness','muscle_wasting','muscle_weakness','nausea','neck_pain','nodal_skin_eruptions','obesity','pain_during_bowel_movements','pain_in_anal_region','patches_in_throat','pus_filled_pimples','red_sore_around_nose','restlessness','scurring','shivering','silver_like_dusting','skin_peeling','skin_rash','spinning_movements','stiff_neck','stomach_pain','sunken_eyes','sweating','swelling_joints','swelling_of_stomach','ulcers_on_tongue','vomiting','watering_from_eyes','weakness_in_limbs','weakness_of_one_body_side','weight_gain','weight_loss','yellowish_skin','itching']


def process_symptoms(symptoms) -> List[int]:

    prompt = f"""Given the following description of symptoms: {symptoms}
    Please return the top three distinct symptoms corresponding to the following symptoms list: 
    {all_symptoms}. If the symptom is not in the list, ignore it. Output the selected symptoms exactly as they appear in the list as a Python list. """

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that processes medical symptoms and returns exactly the top 3 distinct symptoms from the list of {all_symptoms} exactly as it appears. ."},
            {"role": "user", "content": prompt}
        ],
        model="llama3-groq-70b-8192-tool-use-preview",
        temperature=0,
        max_tokens=300
    )

    content = response.choices[0].message.content.strip().strip('[]').replace("'", "").split(', ')
    print(f"Raw API response: {content}")

    if not content:
        raise ValueError("Received empty response from API")

    # Split the content and convert to integers, ignoring non-numeric values
    one_hot_vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    # content[1] = content[1].replace("1", "2")
    # content[2] = content[2].replace("1", "3")
    print(content)
    for i in range(len(content)):
        try:
            idx = all_symptoms.index(content[i])
            one_hot_vector[idx] = 1
        except:
            continue
    # for bit in content.split(','):
    #     bit = bit.strip()
    #     if bit in ('0', '1'):
    #         one_hot_vector.append(int(bit))

    # Handle the case where the vector length doesn't match
    # if len(one_hot_vector) != len(all_symptoms):
    #     print(f"Warning: Vector length mismatch. Expected {len(all_symptoms)}, but got {len(one_hot_vector)}")
    #     if len(one_hot_vector) > len(all_symptoms):
    #         print("Truncating the vector to match the expected length.")
    #         one_hot_vector = one_hot_vector[:len(all_symptoms)]
    #     else:
    #         print("Padding the vector with zeros to match the expected length.")
    #         one_hot_vector += [0] * (len(all_symptoms) - len(one_hot_vector))
    one_hot_vector = np.array(one_hot_vector)
    print(one_hot_vector.shape)
    return one_hot_vector

def inference(one_hot_vector):
    model = load("20241020-DiseasePredictionModelDump.joblib")
    print(model.n_features_in_)
    mapper = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}
    pred = model.predict(one_hot_vector.reshape(1,-1))
    return mapper[pred[0]]

symptoms = "I am experiencing a slight fever with a runny nose and sharp pain on the top of my head."
try:
    result = process_symptoms(symptoms)
    print(f"One-hot encoded vector: {result}")
    
    # Print symptoms that are present (1 in the vector)
    present_symptoms = [symptom for symptom, value in zip(all_symptoms, result) if value == 1]
    print("Present symptoms:")
    for symptom in present_symptoms:
        print(f"- {symptom}")
except Exception as e:
    print(f"An error occurred: {str(e)}")