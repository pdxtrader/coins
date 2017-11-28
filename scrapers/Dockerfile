FROM python:3
WORKDIR /usr/code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "/usr/code/run.py" ]