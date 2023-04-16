import os
import openai
from flask import Flask
from flask_cors import CORS
from flask import request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route("/", methods = ['POST'])
def hello_world():
    try:       
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt=request.json['prompt'],
        temperature=0.7,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
      )
      return {"message": response}
    except:
      print('error')
      return {"message": "error"}
    
if __name__ == "__main__":
    from waitress import serve
    print('server started')
    serve(app, host="0.0.0.0", port=8080)