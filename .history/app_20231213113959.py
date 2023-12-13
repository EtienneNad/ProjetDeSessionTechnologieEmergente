from flask import Flask, render_template, request
import openai

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de la clé API d'OpenAI
openai.api_key = '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'

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour l'API de traitement des messages
@app.route('/api', methods=['POST'])
def api():
    # Récupération du message depuis la requête POST
    message = request.json.get("message")

    # Appel à l'API OpenAI pour la génération de la réponse
    reponse = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': message}]
    )

    # Vérification si la génération de la réponse a réussi
    if reponse.choices[0].message != None:
        return reponse.choices[0].message
    else:
        return 'La génération de la réponse a échoué !'

# Exécution de l'application Flask
if __name__ == '__main__':
    app.run()
