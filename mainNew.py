"""
Author: Mayank Sharma
Description: Harvey, a chatbot script using Tkinter, answers questions from a knowledge base and Wolfram Alpha. Conversation logs are saved for user interactions.
"""

import wolframalpha
import json
from difflib import get_close_matches
import pyttsx3
import os
import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button

KNOWLEDGE_BASE_FILE = 'knowledge_base.json'
engine = pyttsx3.init()
logs_directory = "conversation_logs"


def create_conversation_log_file():
    if not os.path.exists(logs_directory):
        os.mkdir(logs_directory)

    return os.path.join(
        logs_directory, f"conversation_{len(os.listdir(logs_directory)) + 1}.txt")


def save_conversation_to_file(log_filename, user_input, bot_response):
    with open(log_filename, 'a') as log_file:
        log_file.write(f"You: {user_input}\nHarvey: {bot_response}\n\n")


def load_or_create_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(
            f"Knowledge base file '{file_path}' not found. Creating a new one.")
        return {"qa_pairs": []}
    except json.JSONDecodeError:
        print(
            f"Error decoding JSON in '{file_path}'. Creating a new knowledge base.")
        return {"qa_pairs": []}


def find_and_get_answer(user_input: str, knowledge_base: dict) -> str or None:
    user_input_lower = user_input.lower()
    questions_lower = [qa["question"].lower()
                       for qa in knowledge_base["qa_pairs"]]
    best_match = get_close_matches(
        user_input_lower, questions_lower, n=1, cutoff=0.6)

    if best_match:
        return knowledge_base["qa_pairs"][questions_lower.index(best_match[0])]["answer"]
    else:
        wolfram_app_id = 'L98HQH-R6YE48VKHH'
        wolfram_client = wolframalpha.Client(wolfram_app_id)

        try:
            wolfram_res = wolfram_client.query(user_input)
            wolfram_answer = next(wolfram_res.results).text

            return wolfram_answer

        except StopIteration:
            return "I don't know..."


class ChatBotApp:
    def __init__(self, master):
        self.master = master
        master.title("Harvey")

        self.chat_display = Text(master, wrap="word", state=tk.DISABLED,
                                 bg="#1E1E1E", fg="white", font=("Helvetica", 12))
        self.scrollbar = Scrollbar(master, command=self.chat_display.yview)
        self.chat_display['yscrollcommand'] = self.scrollbar.set

        self.message_entry = Entry(
            master, width=50, bg="#333333", fg="white", font=("Helvetica", 12))
        self.send_button = Button(master, text="Send", command=self.send_message, bg="#4CAF50", fg="white",
                                  font=("Helvetica", 12, "bold"))

        # Bind Enter key to send_message
        self.message_entry.bind("<Return>", lambda event: self.send_message())
        # Bind Ctrl+Q to stop speaking
        self.master.bind("<Control-q>", lambda event: self.stop_speaking())

        # Arrange widgets using grid layout
        self.chat_display.grid(row=0, column=0, columnspan=2,
                               padx=10, pady=10, sticky="nsew")
        self.scrollbar.grid(row=0, column=2, sticky='ns')
        self.message_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.send_button.grid(row=1, column=1, pady=10, sticky="ew")

        # Configure grid weights to make the chat display expandable
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

    def send_message(self):
        try:
            message = self.message_entry.get()
            response = find_and_get_answer(message, knowledge_base)
            save_conversation_to_file(log_filename, message, response)
            self.display_message("You: " + message)
            self.display_message("Harvey: " + response)
            # Update the chat display and then speak the answer using the TTS engine
            self.master.update()
            engine.say(response)
            engine.runAndWait()
            self.message_entry.delete(0, tk.END)

        except Exception as e:
            print(f"Error: {e}")
            # Handle other exceptions if needed

    def display_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def stop_speaking(self):
        # Stop speaking instantly
        engine.stop()


def main():
    global knowledge_base
    knowledge_base = load_or_create_knowledge_base(KNOWLEDGE_BASE_FILE)
    global log_filename
    log_filename = create_conversation_log_file()

    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
