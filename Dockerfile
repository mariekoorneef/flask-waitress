FROM python:3.7.1

WORKDIR usr/src/app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY app/app.py ./

CMD ["python", "./app.py"]