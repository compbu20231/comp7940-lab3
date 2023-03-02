import openai
import configparser
import os

def checkOpenAI2(message):
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # openai.api_key = config['OPENAI']['OPENAI_API_KEY']
    openai.api_key = os.environ['OPENAI_API_KEY']
    # openai.api_key = "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"
    # telegram token = 5778452675:AAFYX2aD0nvv489JI6v5bTpC5dbsvPsMA1U
    response = openai.Completion.create(
        model = "gpt-3.5-turbo",
        # model = "text-davinci-003",
        prompt=f"The following is a conversion with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenaAI. How can I help you today?\n\nHuman:{message}\nAI:",
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    print(response)
    AIResponse = response.choices[0].text.replace("\n","")
    return AIResponse


def checkOpenAI(message):
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # openai.api_key = config['OPENAI']['OPENAI_API_KEY']
    openai.api_key = os.environ['OPENAI_API_KEY']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return response['choices'][0]['message']['content']