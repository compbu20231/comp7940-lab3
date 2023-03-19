FROM python:3.7

WORKDIR /app

COPY *.py .
COPY *.txt .


RUN pip install pip update
RUN pip install -r requirements.txt

ENV ACCESS_TOKEN 5778452675:AAFYX2aD0nvv489JI6v5bTpC5dbsvPsMA1U
ENV HOST "redis-10929.c56.east-us.azure.cloud.redislabs.com"
ENV PASSWORD "0MN7YM92mFtzMsjyMKdSZF2u2sGQIzht"
ENV REDISPORT 10929
ENV OPENAI_API_KEY "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"

CMD ["python", "chatbot.py"]