from fastapi import FastAPI, UploadFile, File
from utils.ocr import extract_text_from_file
from utils.simplify import simplify_text

app = FastAPI()

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_file(contents, file.filename)
    simplified = simplify_text(text)
    return {
        "original": text,
        "simplified": simplified
    }
