import google.generativeai as genai
genai.configure(api_key="AIzaSyCObCOnOc6bdcm2vYVW8NFTQekW2CO53zA")
model = genai.GenerativeModel("gemini-1.5-flash")
system_prompt = ("Summarize paragraph into keypoints")
def chat_with_bot(user_input):
    prompt = system_prompt + user_input
    response = model.generate_content(prompt)
    return response.text
if __name__ == "__main__":
    print("Welcome to the chatbot. Ask me anything!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Byeeeeeeeee!")
            break
        response = chat_with_bot(user_input)
        print(f"Bot: {response}")
