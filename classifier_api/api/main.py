from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input
from fastapi import FastAPI, File, UploadFile
import requests as r
import numpy as np
import os
from PIL import Image
import io

classes = {
            0: 'Blazer',
            1: 'Blouse',
            2: 'Body',
            3: 'Dress',
            4: 'Hat',
            5: 'Hoodie',
            6: 'Longsleeve',
            7: 'Outwear',
            8: 'Pants',
            9: 'Polo',
            10: 'Shirt',
            11: 'Shoes',
            12: 'Shorts',
            13: 'Skirt',
            14: 'T-Shirt',
            15: 'Top',
            16: 'Undershirt'
}

model = keras.models.load_model('./models/model.m5')

model.compile(optimizer="adam",
              metrics=['accuracy'],
              loss="categorical_crossentropy")

def predict(imgbytes):
    
    img = Image.open(io.BytesIO(imgbytes))
    img = img.convert('RGB')
    img = img.resize((150, 150), Image.NEAREST)
    x = image.img_to_array(img)
    
    x = preprocess_input(x)
    x = np.expand_dims(x, axis=0)

    predictions = model.predict(x)

    return predictions

def rembg(imgbytes):
    resp = r.post(f"http://rembgapi/rembg", files={"file":imgbytes})
    resp = resp.json()
    imgpath = resp["imgpath"]
    remimgbytes = r.get(f"http://rembgapi/{imgpath}").content
    return remimgbytes

app = FastAPI()

@app.post("/img-classify")
async def classify(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        img = rembg(contents)

        predictions = predict(img)[0].tolist()
        predictions = list(map(lambda pred: float(pred) * 100, predictions))
        predictions = zip(classes.values(), predictions)
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        file.file.close()
    
    return {"predictions":predictions}