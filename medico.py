import openai

# Paste your API key here
client = openai.OpenAI(api_key="secret_key")

def simplify_medical_report(report):
    prompt = f"Simplify this medical report for a layperson:\n\n{report}"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=300
    )

    return response.choices[0].message.content

# Example usage
original_report = """
Patient Name: thejaswini
Age: 45
Diagnosis: Hypertension and Type 2 Diabetes
Medications:
- Amlodipine 5mg once daily
- Metformin 500mg twice daily
Lab Results:
- Blood Pressure: 150/95 mmHg
- Fasting Blood Sugar: 130 mg/dL
- HbA1c: 7.4%
Recommendations:
- Low-sodium, low-sugar diet
- 30 minutes exercise daily
- Monthly follow-up with physician
"""

simplified_text = simplify_medical_report(original_report)
print("Simplified Report:\n", simplified_text)
