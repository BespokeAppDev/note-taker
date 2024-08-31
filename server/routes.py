from flask import request, jsonify
from utils import save_audio, process_audio

def init_routes(app):

    @app.route('/record', methods=['POST'])
    def record_audio():
        audio_data = request.files['audio']
        file_path = save_audio(audio_data)
        return jsonify({"message": "Audio saved successfully", "file_path": file_path})

    @app.route('/transcribe', methods=['POST'])
    def transcribe_audio():
        file_path = request.json.get('file_path')
        transcript = process_audio(file_path)
        return jsonify({"transcript": transcript})

    @app.route('/summarize', methods=['POST'])
    def summarize_text():
        text = request.json.get('text')
        summary = summarize_text(text)
        return jsonify({"summary": summary})

