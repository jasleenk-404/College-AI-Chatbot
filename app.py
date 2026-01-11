from flask import Flask,render_template, request , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    if  "college time" in user_message or "college timing" in user_message:
        reply = "College timings are from 9:00 AM to 4:00 PM."

    elif "library" in user_message or "library timing" in user_message:
        reply = "The library is open from 9:00 AM to 6:00 PM."

    elif "hod" in user_message:
        reply = "The HOD information can be collected from the department office."

    elif "principal" in user_message or "director" in user_message:
        reply = "The principal of the college is Dr. XYZ ABC."

    elif "exam" in user_message or "exam schedule" in user_message:
        reply = "Exams are conducted as per the academic calendar. You can check it on the college website."

    elif "admission" in user_message:
        reply = "For admission details, visit the admission office or check the official website."

    elif "faculty" in user_message:
        reply = "You can contact faculty via email or through the department office."

    elif "hostel" in user_message or "hostels" in user_message:
        reply = "Hostel facilities are available for boys and girls with mess and Wi-Fi."

    elif "canteen" in user_message or "cafeteria" in user_message or "canteen timing" in user_message:
        reply = "The college canteen serves food from 8:00 AM to 5:00 PM."

    elif "computer lab" in user_message:
        reply = "The computer lab is open from 9:00 AM to 6:00 PM for students."

    elif "sports" in user_message:
        reply = "The college has sports facilities for cricket, football, basketball, and indoor games."

    elif "transport" in user_message or "bus" in user_message:
        reply = "College provides bus facility for nearby locations. Check the transport office for routes."

    elif "hello" in user_message or "hi" in user_message:
        reply = "Hello! How can I help you with college information?"

    elif "thank" in user_message:
        reply = "You’re welcome! 😊"

    elif "clubs" in user_message:
        reply = "We have cultural, coding, debate, sports, dance, music, arts, and many other clubs.Students can join any club they like by giving autitions."

    elif "fest" in user_message:
        reply="The annual fest is 3 day event with competitions, performances, and guest lectures."

    elif "placement" in user_message:
        reply="The placement cell helps students get internship and job placements with top companies."

    elif "courses" in user_message:
        reply="we offer undergraduate, postgraduate, and diploma courses in multiple streams."

    else:
        reply = "Sorry, I don't have information on that yet. You can ask about timings, library, exams, hostel, etc."

    return jsonify({"reply": reply})


if __name__== "__main__":
    app.run(debug=True)


