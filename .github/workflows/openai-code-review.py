import openai
import os

# Configuration de la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_and_correct_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    # Appel à l'API OpenAI pour analyser et corriger le code
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
            {"role": "system", "content": "You are an AI code reviewer. Analyze and suggest corrections for JavaScript code."},
            {"role": "user", "content": f"Please analyze and correct the following JavaScript code:\n\n{code}"}
        ]
    )

    corrected_code = response['choices'][0]['message']['content']

    # Sauvegarder le code corrigé dans le fichier
    with open(file_path, 'w') as file:
        file.write(corrected_code)

# Parcours de tous les fichiers JavaScript pour les analyser et les corriger
for root, dirs, files in os.walk("."):
    for file_name in files:
        if file_name.endswith(".js"):
            analyze_and_correct_code(os.path.join(root, file_name))