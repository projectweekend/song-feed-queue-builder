FROM python:2.7.9
COPY requirements.txt /src/
RUN cd /src && pip install ipython && pip install -r requirements.txt
COPY main.py /src/
WORKDIR /src
CMD ["python", "main.py"]
