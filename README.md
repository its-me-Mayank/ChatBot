# Harvey Chatbot

Harvey is a versatile chatbot script designed for interactive conversations. It intelligently answers user questions using a combination of pre-existing knowledge and the Wolfram Alpha computational engine. The script features a user-friendly chat interface built with Tkinter, and it saves detailed conversation logs for future reference.

## Features

### 1. Question Answering

Harvey can provide insightful answers to user queries based on its internal knowledge base. Additionally, it leverages Wolfram Alpha to gather more detailed information when needed.

### 2. Chat Interface

The script boasts a simple yet effective chat interface created using Tkinter. Users can input questions, receive responses, and engage in seamless conversations.

### 3. Conversation Logging

Every interaction with Harvey is logged meticulously. This ensures that users can review past conversations and facilitates improvements to the chatbot's capabilities.

## Usage

1. **Run the Script:**
    ```bash
    python harvey_chatbot.py
    ```

2. **Ask Questions:**
   - Enter questions in the chat interface.
   - Press 'Send' or simply hit Enter.

3. **Receive Responses:**
   - Harvey responds based on its knowledge base and additional information from Wolfram Alpha.

4. **Conversation Logs:**
   - All interactions are logged in the `conversation_logs` directory, providing a detailed record of the conversation history.

## Dependencies

Ensure you have the following Python libraries installed:
- **wolframalpha:** Install using `pip install wolframalpha`
- **pyttsx3:** Install using `pip install pyttsx3`
- **Tkinter:** Included with most Python installations.

## Configuration

- **Wolfram Alpha App ID:**
  - Update the Wolfram Alpha app ID in the script: `wolfram_app_id = 'L98HQH-R6YE48VKHH'`.

- **Knowledge Base:**
  - Customize the knowledge base by editing the `knowledge_base.json` file.

## Author

Mayank Sharma

Feel free to explore, modify, and enhance Harvey to suit your specific requirements. Happy chatting!
