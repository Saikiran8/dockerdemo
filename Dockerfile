FROM python:3.8.0-buster
WORKDIR /Docker_dev
COPY requirements.txt .

ADD main.py .
RUN pip install -r requirements.txt
#COPY /Docker_Dev .
CMD ["python","./main.py"]