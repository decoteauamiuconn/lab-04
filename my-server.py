from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
   return " you called \n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST']) #route = url, method = POST
#assuming POST was imported with Flask
def echo():
   return "You said: " + request.form['text']

#@app.route("/")

##
# AI generated - provided with lab instructions
# Trial division algorithm to find prime factors of a number
#
def trial_division(n):
   factors = []
   # Handle 2 separately
   while n % 2 == 0:
      factors.append(2)
      n //= 2

   # Check odd numbers up to sqrt(n)
   p = 3
   while p * p <= n:
      while n % p == 0:
         factors.append(p)
         n //= p
      p += 2

   if n > 1:
      factors.append(n)
   return factors

print(trial_division(360)) # [2, 2, 2, 3, 3, 5]

if __name__ == "__main__":
   app.run(host='0.0.0.0')