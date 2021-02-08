from flask import Flask , render_template ,request ,jsonify
from flask_cors import CORS
from flask import Flask, render_template, request
import pickle
import numpy as np


# Load the Random Forest Classifier Model
filename = 'Engineering.pkl'
classifier = pickle.load(open(filename,'rb'))


app = Flask(_name_)


CORS(app)
cors=CORS(app, resources={
    r"/*": {
        "origins":"*"
    }
})


@app.route("/", methods=['POST'])
def hello():
    Natural_curiosity=int(request.form['v1'])
    Logical_thinking=int(request.form['v2'])
    Communication_skills =int(request.form['v3'])
    Attention_to_detail = int(request.form['v4'])
    Creativity=int(request.form['v5'])
    Team_work=int(request.form['v6'])
    Mathematical_skill=int(request.form['v7'])
    Problem_solving = int(request.form['v8'])
    Technical_skills = int(request.form['v9'])
    Constant_learner = int(request.form['v10'])
    Analytical_thinking = int(request.form['v11'])
    Leadership_quality = int(request.form['v12'])
    Knowledge_utilisation = int(request.form['v13'])

    data1 = np.array([[Natural_curiosity,Logical_thinking,Communication_skills,Attention_to_detail,Creativity,Team_work,Mathematical_skill,Problem_solving,Technical_skills,Constant_learner,Analytical_thinking,Leadership_quality,Knowledge_utilisation]]).tolist()
    data = int(classifier.predict(data1))
    print("//////")
    print(data)
    #data=int(123)
    return jsonify({'name': data})



app.run()