from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# ---- Folders ----
AUDIO_PATH = "audio"
os.makedirs(AUDIO_PATH, exist_ok=True)

# ---- Serve static files ----
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root page -> index.html
@app.get("/")
def serve_index():
    return FileResponse("static/index.html")


# ---- Receive audio from phone ----
@app.post("/audio")
async def receive_audio(file: UploadFile = File(...)):
    file_location = os.path.join(AUDIO_PATH, "network_audio.webm")

    with open(file_location, "wb") as f:
        f.write(await file.read())

    print("Received audio:", file_location)

    return {"status": "received"}