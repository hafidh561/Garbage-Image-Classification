from fastapi import FastAPI, File, UploadFile
from starlette.responses import Response
from torchvision import transforms
import vortex.runtime as vrt
from PIL import Image
import numpy as np
import io

# Load Model and Create Variable
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
model_path = "./saved_model.onnx"
runtime_device = "cpu"
model = vrt.create_runtime_model(model_path=model_path, runtime=runtime_device)
class_names = model.class_names

# Define function to predict img
def predict_img(img):
    img = Image.open(io.BytesIO(img))
    transform_img = transforms.Compose(
        [
            transforms.Resize(size=(256, 256)),
            transforms.ToTensor(),
            transforms.Normalize(mean, std),
        ]
    )
    new_img = transform_img(img)
    new_img = np.array(new_img)
    new_img = np.expand_dims(new_img, 0)
    result = model(new_img)
    result_class = class_names[int(result[0]["class_label"].squeeze())]
    result_confidence = result[0]["class_confidence"].squeeze()
    return result_class, result_confidence


# Create Fast API
app = FastAPI()


@app.get("/")
async def index():
    return {"messages": "Open the documentations /docs or /redoc"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image = await file.read()
        predicted_class, predicted_confidence = predict_img(image)
        return {
            "filename": str(file.filename),
            "contentype": str(file.content_type),
            "class": str(predicted_class),
            "confidence": str(predicted_confidence),
        }
    except:
        return Response("Internal server error", status_code=500)
