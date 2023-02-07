from rembg import remove
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
import uuid
import os

app = FastAPI()

resultsDir = "results"
if not os.path.exists(resultsDir):
    os.mkdir(resultsDir)

app.mount(os.path.join("/", resultsDir), StaticFiles(directory=resultsDir), name="static")

@app.post("/rembg")
async def removebackground(file: UploadFile = File(...)):
    try:
        imgBytes = file.file.read() # TODO: Verify img.
        rembgImg = remove(imgBytes)
        randomName = uuid.uuid4().hex
        tmpImgPath = os.path.join(resultsDir, randomName)
        with open(tmpImgPath, "wb") as imgfile:
            imgfile.write(rembgImg)

    except Exception as e:
        return {"message": str(e)}
    
    finally:
        file.file.close()
    
    return {"imgpath": tmpImgPath}
