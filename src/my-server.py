from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return ' you called \n'

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo

@app.route("/echo", methods=['POST'])
def echo():
    return "You said: " + request.form.get('text', '') 

##
# AI generated - provided with lab instructions
# Trial division algorithm to find prime factors of a number
#

// ...existing code...

@app.route('/trial_division/<int:n>')
def trial_division(n):
   factors = []
   d = 2
   while n > 1:
      while n % d == 0:
         factors.append(d)
         n //= d
      d += 1
   return json.dumps({"factors": factors})
// ...existing code...


# Remove the print(trial_division(360)) line, as Flask endpoints should not be called directly like this.

if __name__ == "__main__":
   app.run(host='0.0.0.0')