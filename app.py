from flask import Flask,render_template,url_for,request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.externals import joblib
# from joblib import load

app=Flask(__name__)
Swagger(app)

mnb = pickle.load(open(r'mnb.pkl','rb'))
countVect = pickle.load(open('tfidf.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        Reviews = request.form['Reviews']
        data = [Reviews]
        vect = countVect.transform(data).toarray()
        my_prediction = mnb.predict(vect)
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
    app.run(debug=True)
    