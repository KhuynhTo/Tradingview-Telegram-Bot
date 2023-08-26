from flask import Flask, request
from threading import Thread
import telegrambot
import json
app = Flask('')
@app.route('/webhook', methods=['POST', 'GET'])
def post_message():
  try:
    jsonRequest=request.args.get("jsonRequest")
    if request.method == 'POST':
      payload = request.data
      if jsonRequest == "true":
        payload = json.dumps(request.json, indent=4)
      print("[I] Payload: \n", payload)
      #telegrambot.sendMessage(payload)
      telegrambot.sendMessage(payload.decode('utf-8'))
      return 'success', 200
    else:
      print("Get request")
      return 'success', 200
  except Exception as e:
    print("[X] Exception Occured : ", e)
    return 'failure', 500

@app.route('/')
def main():
  return 'Your bot is alive!'

def run():
  app.run(host='0.0.0.0', port=5000)


def start_server_async():
  server = Thread(target=run)
  server.start()

def start_server():
  app.run(host='0.0.0.0', port=5000)