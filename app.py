from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_contact():
    email = request.form.get('email')
    return f"Merci pour votre message ! Email reçu : {email}"

if __name__ == '__main__':
    app.run(debug=True)
