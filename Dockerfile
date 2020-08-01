FROM python:3.7-alpine
COPY . ./
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE
CMD ["python","app.py"]