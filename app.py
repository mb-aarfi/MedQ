from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import joblib

app = Flask(__name__, static_url_path='/static')

# Initialize appointments list
appointments = []

categories = [
    {"name": "Covid"},
    {"name": "Skin and Hair", "image": "images/allergy.png"},
    {"name": "Women Health", "image": "images/woman.png"},
    {"name": "General Physician", "image": "images/stethoscope.png"},
    {"name": "Dental Care", "image": "images/floss.png"},
    {"name": "Bones and Joints", "image": "images/pain-in-joints.png"},
    {"name": "Mental Wellness", "image": "images/mental-health.png"},
    {"name": "Ear, Nose & Throat", "image": "images/sore-throat.png"},
    {"name": "Sexual Health", "image": "images/std.png"},
    {"name": "Child Specialist", "image": "images/specialist.png"},
    {"name": "Homeopathy", "image": "images/homeopathy.png"},
    {"name": "Digestive Issues", "image": "images/heart-problem.png"},
    {"name": "Eye Specialist", "image": "images/ophtalmology.png"},
    {"name": "Heart", "image": "images/heart-attack.png"},
    {"name": "Physiotherapy", "image": "images/physical-therapy.png"},
    {"name": "Brain & Nerves", "image": "images/brain.png"},
    {"name": "Lungs & Breathing", "image": "images/lungs.png"},
    {"name": "Kidney Issues", "image": "images/kidney.png"},
    {"name": "General Surgery", "image": "images/plastic-surgery.png"},
    {"name": "Diabetes Management", "image": "images/sugar-blood-level.png"},
    {"name": "Ayurveda", "image": "images/ayurveda.png"},
    {"name": "Cancer", "image": "images/breast-cancer.png"},
    {"name": "Urinary Issues", "image": "images/bladder.png"},
    {"name": "Veterinary", "image": "images/veterinary.png"},
    {"name": "Diet & Nutrition", "image": "images/diet.png"}
]

category_priority = {
    "Covid": 5,
    "Skin and Hair": 1,
    "Women Health": 3,
    "General Physician": 2,
    "Dental Care": 2,
    "Bones and Joints": 3,
    "Mental Wellness": 4,
    "Ear, Nose & Throat": 2,
    "Sexual Health": 4,
    "Child Specialist": 4,
    "Homeopathy": 1,
    "Digestive Issues": 3,
    "Eye Specialist": 2,
    "Heart": 5,
    "Physiotherapy": 2,
    "Brain & Nerves": 5,
    "Lungs & Breathing": 4,
    "Kidney Issues": 4,
    "General Surgery": 5,
    "Diabetes Management": 3,
    "Ayurveda": 1,
    "Cancer": 5,
    "Urinary Issues": 3,
    "Veterinary": 2,
    "Diet & Nutrition": 2
}

model = joblib.load('priority_model.pkl')

def load_symptoms():
    with open('symptoms.json') as f:
        return json.load(f)

symptoms_data = load_symptoms()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/form')
def form():
    return render_template('form.html', categories=categories)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html', appointments=appointments)

@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    name = request.form.get('name')
    age = request.form.get('age')
    category = request.form.get('category')
    symptoms = request.form.get('symptoms')
    mobile_number = request.form.get('mobile_number')
    slot_number = request.form.get('slot_number')

    try:
        age = int(age)
    except ValueError:
        return jsonify({"error": "Invalid age value"}), 400

    priority = category_priority.get(category, 1)

    appointment = {
        "name": name,
        "age": age,
        "concern": category,
        "symptoms": symptoms,
        "mobile_number": mobile_number,
        "slot_number": slot_number,
        "priority": priority
    }

    appointments.append(appointment)
    appointments.sort(key=lambda x: x['priority'], reverse=True)

    return jsonify({"message": "Appointment added successfully!"}), 200

@app.route('/clear_appointments', methods=['POST'])
def clear_appointments():
    global appointments
    appointments = []
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
