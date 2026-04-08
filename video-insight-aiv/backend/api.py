from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import whisper
import tempfile

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Whisper model
model = whisper.load_model("base")

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.post("/process")
async def process_video(file: UploadFile):
    try:
        print("Received file")

        import tempfile
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(file.file.read())
            tmp_path = tmp.name

        print("File saved:", tmp_path)

        result = model.transcribe(tmp_path)
        text = result["text"]

        print("Transcription done")

        summary = text[:200]

        return {
            "summary": summary,
            "topics": ["AI Generated"],
            "timestamps": [
                {"time": "00:00", "text": summary[:50]}
            ]
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}