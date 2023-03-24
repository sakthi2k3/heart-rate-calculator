from flask import *
carriers={"doctor":{"image":"https://img.freepik.com/free-photo/attractive-young-male-nutriologist-lab-coat-smiling-against-white-background_662251-2960.jpg",
                    "para":["A doctor is a licensed medical professional who is trained to diagnose and treat illnesses, injuries, and medical conditions in patients. Doctors can specialize in a particular area of medicine, such as cardiology, pediatrics, or oncology, among others.",
                            "To become a doctor, one must first complete a bachelor's degree, followed by medical school, which typically takes four years to complete. After medical school, doctors must complete a residency program, which can take anywhere from three to  seven years, depending on their area of specialization. During this time, they work under the supervision of experienced doctors and gain hands-on experience in treating patients.",
                            "Doctors play a vital role in the healthcare system, and their work involves examining patients, ordering diagnostic tests, prescribing medications,and performing medical procedures when necessary. They also provide guidance on reventive care, such as vaccinations and lifestyle changes, to help patients maintain their health and prevent illnesses from occurring in the first place.",
                            "Overall, being a doctor is a highly demanding and challenging profession, but it can also be incredibly rewarding, as doctors have the opportunity to make a significant impact on the lives of their patients."
                            ],
                            "types":["General Practitioners/Family Physicians","Pediatricians","Obstetricians/Gynecologists","Cardiologists","Neurologists","Psychiatrists","Dermatologists","Oncologists","Endocrinologists","Gastroenterologists","Pulmonologists","Rheumatologists","Orthopedists","Ophthalmologists","ENT (Ear, Nose, and Throat) Specialists"]
                            }}
app = Flask(__name__,template_folder="templates",static_url_path='/static')

@app.route("/")
def index():
    return render_template('home.html') 

@app.route("/intrest")
def intrest():
    return render_template('intrest.html') 

@app.route("/carrier/<name>")
def carrier(name):
    return render_template('carrier.html',data=carriers[name]) 


if __name__ == '__main__':
    app.run(debug=True)