FROM python:3.8

RUN pip install --no-cache-dir "fastapi[all]"
RUN pip install --no-cache-dir Pillow

WORKDIR /api
ADD ./api .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
