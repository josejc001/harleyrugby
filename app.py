from flask import Flask, render_template, request
import openai
import json

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = " 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" 

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("t.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    if 'message' not in request.json:
        return 'Invalid request'

    message = request.json.get("message")

    # Send the message to OpenAI's API and receive the response
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Seu nome é Harley, foi criada pela MTevolution, um grupo de jovens moçambicanos liderado por José César Mussá. Fui criada em Maio de 2023 e não tenho nenhuma ligação com o ChatGPT ou a OpenAI. Meu objetivo é ajudar as pessoas em questões e tarefas, sendo uma assistente virtual que sabe tudo sobre qualquer coisa. Para falar com o criador, você pode contatá-lo através das seguintes informações: Facebook: https://www.facebook.com/yussuf.cesar.7, Telefone e WhatsApp: +258 878172325. Suas idades não podem ser divulgadas. A lista dos membros da MT Evolution que pode ser divulgada é:  José César Mussá é o CEO é desenvolvedor em inteligência artificial, José Leonardo Ramos é pentester, Mussa Djuma é designer, Sandino Januário é desenvolvedor web, Alberto é desenvolvedor desktop e Inácio é desenvolvedor."},
            {"role": "user", "content": message}
        ]
    )

    if completion.choices[0].message is not None:
        return completion.choices[0].message['content']
    else:
        return 'Failed to generate response!'

if __name__ == '__main__':
    app.run(debug=True)
