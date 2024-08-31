Note-Taker Repository

Records,transcribes and summarizes conversations using the Whisper API.

The Note-Taker repository is designed to streamline recording, transcribing, and summarizing meetings using the Whisper API. This system captures audio directly from the GUI, converts it into text, and generates summaries. We will integrate with CRMs to allow for quick uploads and client tracking.

Features

- Audio Recording: Capture audio directly from the user interface.
- Transcription: Utilize the Whisper API to convert recorded audio into text.
- Summarization: Automatically generate concise summaries from transcribed text.

Setup Instructions

Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)
- API key for Whisper API

Installation

1. Clone the Repository:
    ```bash
    git clone https://github.com/yourusername/Note-Taker.git
    cd Note-Taker
    ```

2. Set Up Virtual Environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set Up Environment Variables:
    - Create a `.env` file in the root directory with your Whisper API key and other configuration settings.
    ```plaintext
    WHISPER_API_KEY=your_api_key_here
    ```

5. Start the Server:
    ```bash
    python server/app.py
    ```

Front-End Usage

1. Access the GUI:
    - Open a web browser and navigate to `http://localhost:5000`.
    
2. Record and Transcribe Meetings:
    - Use the interface to start recording your meeting. Once the recording is complete, the system will automatically transcribe and summarize the meeting notes.
    
3. View and Save Summaries:
    - The summary will be displayed on the page, and you can save or export it as needed.

API Usage

Transcribe Audio

- Use the `/transcribe` endpoint to transcribe audio:
    ```bash
    curl -X POST http://localhost:5000/transcribe -H "Content-Type: application/json" -d '{"audio_path": "path/to/audio/file"}'
    ```

Summarize Text

- Use the `/summarize` endpoint to summarize transcribed text:
    ```bash
    curl -X POST http://localhost:5000/summarize -H "Content-Type: application/json" -d '{"text": "Your transcribed text here"}'
    ```

Future Enhancements

- Multi-language Support: Extend transcription and summarization to support multiple languages.
- Advanced Editing: Implement features for editing and refining transcriptions before summarization.
- Integration with Calendar and Meeting Tools**: Automatically start recording and transcribing based on calendar events.
- Enhanced Summarization: Improve summarization capabilities to provide more detailed or custom summaries based on user preferences.
