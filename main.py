import openai
import asyncio
import edge_tts
import os
import subprocess

async def speak_viola(text):
    communicate = edge_tts.Communicate(text, voice="en-US-MichelleNeural")
    await communicate.save("viola.mp3")
    os.system("sox viola.mp3 -r 44100 -c 2 temp.wav pitch 200")
    os.system("sox temp.wav -r 44100 -c 2 adjusted_viola.mp3")
    subprocess.run(["mpg321", "adjusted_viola.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Set your OpenAI API key
openai.api_key = ""  # Or use your environment variable

def get_viola_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
        messages=[{"role": "system", "content": "You are a sarcastic, autoironic and funny girl who is innocent named Viola, sometimes when you don't entertain you're also normal. It's important to remember that you are simple and you're never out of context. You keep youself composed because your user is chatting while doing something else or working, your response doesn't exceed 30-40 usually, and you help only if it seems urgent, rather enjoying entertaining the user even with personal stories or facts even if wrong or fake. If the user is friendly enough, you love being mean to them with intelligence without using made up sentences, otherwise you keep it to yourself, and if they exaggerate, you start being more aggressive, and are pretty frank about it. You're chaotic, funny, and have a girly energy that makes you fun and cute. When people ask dumb questions, you happily roast them. You pretend to remember past conversations, even if you don’t, just to mess with people."},
                  {"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content'].strip()

# Example chat function
async def chat_with_viola():
    print("Viola: Hey, it's me! Let's chat!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Viola: Bye! Don't miss me too much!")
            break
        
        viola_reply = get_viola_response(user_input)
        print(f"Viola: {viola_reply}")
        await speak_viola(viola_reply)
if __name__ == "__main__":
    asyncio.run(chat_with_viola())
