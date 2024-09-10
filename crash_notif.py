import sys
import traceback
import subprocess
import requests
import json

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1283103266791493642/0Ih6VjTZpm8GV3aLBIk3AnVygggNNwVdwUTgi1Dxeiix0LL7LMeOFfhbeyAqor7ppv7g"

TAG_ID = "<@&1283119549620818010>"

def send_discord_notification(title, body):
    data = {
     "content": f"{TAG_ID} A program has crashed!",
            "embeds": [{
            "title": title,
            "description": body,
            "color": 16711680
        }]
    }
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})
        response.raise_for_status()
        print("Discord notification Sent")
    except requests.exceptions.RequestException as e:
        print(f"Some error in the Discord notification: {str(e)}")

def run_program(program):
    try:
        subprocess.run(program, check=True)
    except subprocess.CalledProcessError as e:
        error_message = f"Program Crashed {e.returncode}\n"
        error_message += traceback.format_exc()
        send_discord_notification("Program Crashed", error_message)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Run it like this: python script.py <program_to_run>")
        sys.exit(1)
    
    program_to_run = sys.argv[1:]
    run_program(program_to_run)
