import sys
from nova.assistant import chat_with_nova

def main():
    print("\n NOVA: Neural Operator for Virtual Assistance")
    print("\n Type your mission-critical question below. Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input(">> ")

            if user_input.strip().lower() in ["exit", "quit"]:
                print("\nShutting down NOVA. Stay safe out there.")
                break

            print("Query received. Stand by...\n")
            sys.stdout.flush()

            response = chat_with_nova(user_input)
            print()
            print(f"NOVA: {response}\n")

        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()