FROM python:2.7.9
COPY requirements.txt /src/
WORKDIR /src
RUN pip install ipython && pip install -r requirements.txt
CMD ["python", "main.py"]
