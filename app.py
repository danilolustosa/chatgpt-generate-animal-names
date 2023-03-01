import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        print(response)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Sugira três nomes para um animal doméstico.

            Animal: Gato
            Nomes: Tom, Chico, Frajola
            Animal: Cachorro
            Names: Tob, Bob, Fred
            Animal: {}
            Nomes:""".format(
                    animal.capitalize()
                )
