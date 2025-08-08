FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p data
ARG KAGGLE_USERNAME
ARG KAGGLE_KEY
ENV KAGGLE_USERNAME=${KAGGLE_USERNAME}
ENV KAGGLE_KEY=${KAGGLE_KEY}
RUN kaggle datasets download maharshipandya/-spotify-tracks-dataset -p data --unzip
COPY . .

CMD ["python", "app.py"]
