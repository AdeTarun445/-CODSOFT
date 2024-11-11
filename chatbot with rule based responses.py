import re

# Function to clean user input
def clean_input(user_input):
    return user_input.strip().lower()

# Predefined responses based on certain keywords
def chatbot_response(user_input):
    user_input = clean_input(user_input)

    # Greetings
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I assist you today?"
    
    # Asking for help
    elif re.search(r'\b(help|assist|support)\b', user_input):
        return "Sure! How can I help you? You can ask me about weather, time, or general information."

    # Asking for time
    elif re.search(r'\b(date|time|clock|now)\b', user_input):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    # Asking for weather (simulated)
    elif re.search(r'\b(weather|forecast)\b', user_input):
        return f"the current weather is {current_weather} ."

    # Asking for the user's name
    elif re.search(r'\b(name|who are you)\b', user_input):
        return "I'm a simple chatbot designed to help you with your queries."

    # Farewells
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a great day."

    # Unknown inputs
    else:
        return "Sorry, I didn't understand that. Can you try asking something else?"

# Main chatbot loop
def start_chat():
    print("Chatbot: Hi! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if re.search(r'\b(bye|goodbye|exit)\b', user_input.lower()):
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
start_chat()