import os
from werkzeug.utils import secure_filename
from transcribe import transcribe_audio
from summarize import summarize_text

UPLOAD_FOLDER = './data'

def save_audio(audio_data):
    filename = secure_filename(audio_data.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    audio_data.save(file_path)
    return file_path

def process_audio(file_path):
    transcript = transcribe_audio(file_path)
    summary = summarize_text(transcript)
    return summary
