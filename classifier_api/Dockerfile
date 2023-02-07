FROM python:3.8

RUN pip install --no-cache-dir "fastapi[all]"
RUN pip install --no-cache-dir tensorflow
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir Pillow

WORKDIR /api
ADD ./api .

EXPOSE 8001

ENV REMBG_API="http://127.0.0.1:8000"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
