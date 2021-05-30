from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [
    {
        'id': 1, 
        'Contact': '9999999999',
        'Name': 'Jeeva Norman'
        'About': 'I am a frontend developer, and I love dogs.',
        'done': False
    },
    {
        'id': 2,
        'Contact': '8888888888',
        'Name': 'Shreenidhi Sharma'
        'About': 'I work as a VFX Artist in Mumbai, and you can find my personal work at ShreenidhiSharma.com',
        'done': False
    },
    {
        'id': 3,
        'Contact': '7777777777'
        'Name': 'Venky Maghullo'
        'About': 'Venky Maghullo is a ski instructor at Jessie's Extreme Sport Park and he used to be a tourist guide for the Grand Canyon',
        'done': False
    },
    {
        'id' = 4,
        'Contact': '6666666666'
        'Name': 'Cardi Mucklide'
        'About': 'Cardi Mucklide is a worldwide speaker and background score artist - she has recently released an album called The Veins Of Earth. She was born on September 3rd 1958, and she grew up in Melbourne.'
]

@app.route("/add-data", methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data."
        })

task = {
    'id': tasks[-1]['id']+1,
    'title': request.json['title'],
    'description': request.json.get['description'],
    'done': False
}

def add_task():
    if tasks.append(task):
        return jsonify({
            "status": "success",
            "message": "Your task was added successfully."
        })

@app.route("/add-data", methods = ['GET'])
def get_task():
    return jsonify({
        'data': task
    })
