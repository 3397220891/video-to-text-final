from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import whisper

app = FastAPI()

# ✅ 使用 tiny 模型更快
model = whisper.load_model("tiny")

# ✅ 允许前端跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    contents = await file.read()
    with open("temp.mp4", "wb") as f:
        f.write(contents)

    result = model.transcribe("temp.mp4")
    english_text = result["text"]

    return {
        "text": english_text
    }
