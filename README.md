# Voice Assistant with Google Search

This Python project is a simple voice assistant that can take user queries via text or speech input, perform a Google search, and read out the search results. The assistant offers an interactive way to ask questions, listen to responses, and even open search results in a web browser if requested.

## Features

- **Text-to-Speech (TTS)**: Converts text to speech using the `pyttsx3` library.
- **Speech Recognition**: Uses `speech_recognition` to capture and interpret user commands via microphone.
- **Web Scraping**: Scrapes Google search results using `requests` and `BeautifulSoup`.
- **Browser Integration**: Allows the option to open search results directly in the browser.

## Requirements

The following Python libraries are required for this project:

- `requests`: For sending HTTP requests to retrieve search results.
- `beautifulsoup4`: For parsing HTML data.
- `pyttsx3`: For text-to-speech functionality.
- `speech_recognition`: For speech-to-text processing.
- `webbrowser`: For opening links in the default web browser.

To install the required libraries, you can run:

```bash
pip install requests beautifulsoup4 pyttsx3 SpeechRecognition
```

## Usage

1. **Run the script**:
    ```bash
    python voice_assistant.py
    ```
2. **Provide Input**: You can either type or speak your query.
    - If you choose to enable speech recognition, the assistant will listen for your question.
    - If speech recognition is not enabled, you can type your question.
3. **Hear Results**: The assistant will speak out a summary of the search results.
4. **Open in Browser**: When prompted, you can choose to open the Google search results in your browser.

## How It Works

1. **Initialization**: The assistant initializes `pyttsx3` for TTS and sets up microphone access.
2. **Query Handling**: The user chooses to enable speech recognition or input a query manually.
3. **Search**: The assistant performs a Google search and scrapes the top results.
4. **Results Display**: The assistant displays and reads out the top results.
5. **Browser Option**: The user can choose to open the search results in their web browser.

## Example

```plaintext
HELLO
HOW CAN I HELP YOU
Do you want speech recognition? (yes/no): yes
Speak now: [User speaks a question]
Assistant: "Here are some results about [query]"
Assistant reads results aloud...
Do you want to open it in Google? (yes/no): yes
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
