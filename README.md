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

## Installation 🛠️

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Intent-Recognition-With-Virtual-Assistance.git
   cd Intent-Recognition-With-Virtual-Assistance
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Required libraries:**
   - pyttsx3
   - speech_recognition
   - tensorflow
   - numpy
   - pyautogui
   - psutil

3. Ensure you have the model and required files:
   - `chat_model.h5` – trained intent recognition model  
   - `tokenizer.pkl` – tokenizer for text preprocessing  
   - `label_encoder.pkl` – label encoder for intent labels  
   - `intends.json` – JSON file containing intents and responses  

---

## Usage ▶️

Run the assistant:

```bash
python main.py
```

- The assistant will greet you based on the time of day.  
- Speak your commands clearly. Examples:
  - "Open calculator"
  - "What is the CPU usage?"
  - "Open Facebook"
  - "University timetable"
  - "Mute the sound"
- To exit, say: `"exit"`

---

## Project Structure 📂

```
├── Intent-Recognition-With-Virtual-Assitance/
├── intends.json        # Intent-response mappings
├── chat_model.h5           # Trained Keras model
├── tokenizer.pkl           # Tokenizer for text preprocessing
├── label_encoder.pkl       # Label encoder for intents
├── main.py                 # Main assistant script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## How It Works ⚙️

- **Speech Recognition**: Converts your voice to text using `speech_recognition`.  
- **Intent Classification**: Uses the trained model to classify user intent.  
- **Response Generation**: Chooses a response from `intents.json` or performs system/web actions.  
- **Text-to-Speech**: Speaks the response using `pyttsx3`.  

---

## Future Improvements 🚀

- Add more intents for advanced tasks.  
- Integrate with calendar APIs for dynamic schedule management.  
- Add a GUI interface for easier interaction.  
- Include context-aware conversations for better understanding.  

---

## License 📄

This project is licensed under the MIT License.  
