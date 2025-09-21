# Intent Recognition With Virtual Assistance 🤖

A **voice-enabled virtual assistant** that can recognize user intents and perform tasks such as opening applications, checking system status, browsing the web, managing schedules, and interacting with social media. Built using **Python**, **TensorFlow**, and **Natural Language Processing (NLP)**.

---

## Features

- **Voice Interaction**: Listen and respond to user commands using speech recognition.
- **Intent Recognition**: Understand and classify user queries with a trained deep learning model.
- **Application Control**: Open and close system apps like Calculator, Notepad, and Paint.
- **Web Browsing**: Open websites like Google, Facebook, WhatsApp, Instagram, and Discord.
- **System Monitoring**: Check CPU usage and battery status.
- **Volume Control**: Adjust system volume using voice commands.
- **Schedule Management**: Speak your university or personal timetable.
- **Dynamic Responses**: Personalized responses based on recognized intents.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Intent-Recognition-With-Virtual-Assistance.git
   cd Intent-Recognition-With-Virtual-Assistance


Install dependencies:

pip install -r requirements.txt


Required libraries:

pyttsx3

speech_recognition

tensorflow

numpy

pyautogui

psutil

Ensure you have the model and required files:

chat_model.h5 – trained intent recognition model

tokenizer.pkl – tokenizer for text preprocessing

label_encoder.pkl – label encoder for intent labels

intends.json – JSON file containing intents and responses
