FROM python:3.8
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
EXPOSE 3000
EXPOSE 5678
COPY . /code/
CMD ["uvicorn", "src.infra.server:app", "--reload", "--host", "0.0.0.0", "--port", "3000", "--root-path", "/api/v1"]