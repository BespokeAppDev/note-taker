from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("AI_API_KEY")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file to the data directory
    filepath = os.path.join("../data/", file.filename)
    file.save(filepath)

    # Transcribe the file using Whisper API
    with open(filepath, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    # Summarize the transcript
    summary = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following transcript:\n{transcript['text']}",
        max_tokens=150
    )

    return jsonify({'transcript': transcript['text'], 'summary': summary.choices[0].text})

if __name__ == "__main__":
    app.run(debug=True)

