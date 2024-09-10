import time
import sys

def main():
    print("Starting the program...")
    for i in range(5):
        print(f"Wait for it... {i}")
        time.sleep(1)
    
    print("About to crash!")
    sys.exit(1)  # This will cause the script to exit with an error code

if __name__ == "__main__":
    main()
