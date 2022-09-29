import MainTrainer
import requests
import json


def main(link):
    udata = str(link)
    response = requests.get(udata)
    with open("captcha.png", "wb") as file_img:
        file_img.write(response.content)
    url = "captcha.png"
    try:
        code = str(MainTrainer.resolve(url))
        return code
    except Exception as e:
        return e
