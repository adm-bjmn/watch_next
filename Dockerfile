FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python -m spacy download en_core_web_md
RUN python -m spacy download en_core_web_sm
RUN pip3 install -r requirements.txt
COPY . /app
CMD python watch_next.py

