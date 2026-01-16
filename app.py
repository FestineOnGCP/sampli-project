from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def get_ip():
    # Get the client's IP address
    # Check for forwarded IP (in case of proxies/load balancers)
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    else:
        ip = request.remote_addr
    
    return f"<h1>Your IP is: {ip}</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
