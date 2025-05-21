# ennchan_interface_cmd/app.py
import time
import os
import sys
from ennchan_rag.ask import ask

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the application header."""
    print("=" * 80)
    print("EnnchanRAG Command Line Interface".center(80))
    print("Type 'exit', 'quit', 'close', or 'q' to exit".center(80))
    print("=" * 80)
    print()

def main():
    clear_screen()
    print_header()
    
    run = True
    while run:
        try:
            prompt = input("\033[1mUser:\033[0m ")
            if prompt.lower() in ["exit", "quit", "close", "q"]:
                print("\nThank you for using EnnchanRAG. Goodbye!")
                run = False
            elif prompt.strip() == "":
                continue
            else:
                start_time = time.time()
                print("\033[90mThinking...\033[0m")
                
                reply = ask(prompt, "..\\config.json")
                
                end_time = time.time()
                runtime = end_time - start_time
                
                # Clear the "Thinking..." line
                sys.stdout.write("\033[F\033[K")
                
                print(f"\033[1;34mAssistant:\033[0m {reply}")
                print(f"\033[90m(Response time: {runtime:.2f} seconds)\033[0m\n")
        
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Exiting...")
            run = False
        except Exception as e:
            print(f"\n\033[31mError: {e}\033[0m")
            print("Please try again or type 'exit' to quit.")

if __name__ == "__main__":
    main()
