from fastapi import FastAPI, File, UploadFile
from colorthief import ColorThief
from math import sqrt
from PIL import Image
import io

app = FastAPI()

mainColors = ["FFFFFF", "000000", "C4C4C4", "FF0000", "FF9A02", "FFF504", "6AF001", "00DEC3", "8C4D02", "FF037C", "B603E3", "0B8500" ,"1100D2"]

def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  return tuple(rgb)

def getClosestMainColor(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in map(hex_to_rgb, mainColors):
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

@app.post("/color-ext")
async def extractcolors(file: UploadFile = File(...)):
    try:
        imgBytes = file.file.read() # TODO: Verify img.
        img = Image.open(io.BytesIO(imgBytes))
        img = img.convert('RGB')
        img = img.resize((150, 150), Image.NEAREST)

        ct = ColorThief(img)
        dom = ct.get_color(quality=1)
        closestMainColor = getClosestMainColor(dom)
        hexformat = '#%02x%02x%02x' % dom
        closestColorHex = '#%02x%02x%02x' % closestMainColor

        palette = ct.get_palette()

    except Exception as e:
        return {"error": str(e)}
    
    finally:
        file.file.close()
    
    return {"dominant_color":hexformat, "closest_color":closestColorHex, "color_palette":palette}
