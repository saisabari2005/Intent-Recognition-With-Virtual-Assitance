from elevenlabs import generate, play
from elevenlabs import set_api_key
from api_key import api_key_data
set_api_key(api_key_data)

def engine_talk(query):
    audio = generate(
        text=query, 
        voice='Grace',
        model="eleven_monolingual_v1"
    )
    play(audio)