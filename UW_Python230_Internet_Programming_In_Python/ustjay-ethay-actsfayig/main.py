import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

pig_latin_post_url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
pig_latin_base_url = "https://hidden-journey-62459.herokuapp.com"
# my_heroku_app_url = "https://peaceful-journey-72644.herokuapp.com"

def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()


def get_pig_latin_url(text):
    response_text = get_pig_latin_response_text(text)
    end_of_url = extract_end_of_url(response_text)
    return pig_latin_base_url + end_of_url


def get_pig_latin_response_text(text):
    request = requests.post(pig_latin_post_url,
                            data = {'input_text':text},
                            allow_redirects=False)
    return request.text


def extract_end_of_url(response_text):
    soup = BeautifulSoup(response_text, "html.parser")
    end_of_url = soup.find('a', href=True)
    return end_of_url.getText().strip()


@app.route('/')
def home():
    fact = get_fact()
    url = get_pig_latin_url(fact)
    return url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

