from nova.assistant import chat_with_nova

def main():
    print("NOVA: Neural Operator for Virtual Assistance")
    print("Type your mission-critical question below. Type 'exit' to quit.\n")

    while True:
        user_input = input(">> ")

        # Handle exit before calling the model
        if user_input.strip().lower() in ["exit", "quit"]:
            print("Shutting down NOVA. Stay safe out there.")
            break

        print("Query received. Stand by...\n")

        try:
            response = chat_with_nova(user_input)
            print(f"NOVA: {response}\n")
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}\n")

if __name__ == "__main__":
    main()
