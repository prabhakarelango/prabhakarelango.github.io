from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Define the chatbot's responses
responses = {
    "hi": "Hello! Nice to meet you.",
    "how are you": "I'm fine, thank you. How are you?",
    "i am fine": "That's good :)",
    "what's your name": "I am nobody",
    "bye": "Goodbye!",
    "default": "I'm sorry. Something went wrong. <a href='/help'>Click here</a> to know more."
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_response")
def get_response():
    user_input = request.args.get("user_input")
    bot_response = responses.get(user_input.lower(), responses["default"])
    return bot_response


@app.route("/help")
def default():
    return render_template("help.html")


if __name__ == "__main__":
    app.run(debug=True)
