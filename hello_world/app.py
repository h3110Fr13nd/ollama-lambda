import json
import ollama
import subprocess


command = "ollama serve & sleep 1 && ollama run stablelm2:1.6b-q2_K"
subprocess.run(command, shell=True, check=True, text=True)
def lambda_handler(event, context):
    message = json.loads(event['body'])['message']
    response = ollama.generate(model="stablelm2:1.6b-zephyr-q2_K",prompt=message)
    print(response)
    return response["response"]
