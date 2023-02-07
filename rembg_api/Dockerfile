FROM python:3.8

RUN pip install --no-cache-dir "fastapi[all]"

RUN pip install --no-cache-dir rembg
WORKDIR /root/.u2net/
RUN wget "https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx"

WORKDIR /api
ADD ./api .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
