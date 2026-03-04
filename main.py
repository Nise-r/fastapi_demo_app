from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from detector import detect_objects

app = FastAPI(title="YOLO Object Detection API")

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    image_bytes = await file.read()
    
    output_image = detect_objects(image_bytes)

    return Response(content=output_image, media_type="image/jpeg")