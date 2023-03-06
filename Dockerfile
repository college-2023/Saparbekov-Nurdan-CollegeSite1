
FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /home/ubuntu/Nurdan/actions-runner/_work/ Saparbekov-Nurdan-CollegeSite1/Saparbekov-Nurdan-CollegeSite1

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt
