import openai

# Set your OpenAI API key
openai.api_key = "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"  # Or use your environment variable

def get_viola_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or use "gpt-4" if you have access
        messages=[{"role": "system", "content": "You are Viola, a sarcastic, chaotic, and funny girl who loves teasing people."},
                  {"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content'].strip()

# Example chat function
def chat_with_viola():
    print("Viola: Hey, it's me! Let's chat!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Viola: Bye! Don't miss me too much!")
            break
        
        viola_reply = get_viola_response(user_input)
        print(f"Viola: {viola_reply}")

if __name__ == "__main__":
    chat_with_viola()
