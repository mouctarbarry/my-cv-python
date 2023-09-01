from flask import Flask, render_template, request, jsonify
from contact import submit_form

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form_route():
    data = request.form

    errors = {}

    if not data.get('firstname'):
        errors['firstname'] = "J'aimerais connaître votre prénom."
    if not data.get('name'):
        errors['name'] = "Même le nom svp :)"
    if not data.get('email'):
        errors['email'] = "Un e-mail pour vous répondre."
    if not data.get('message'):
        errors['message'] = "Un petit message pour moi ?"

    if errors:
        response = {
            'success': False,
            'message': errors
        }
    else:
        response = submit_form(data)

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
