# Dependencies
from flask import Flask, request, jsonify
from joblib import Parallel, delayed
import traceback
import pandas as pd
import joblib
import numpy as np

# API definition
application = Flask(__name__)


@application.route("/")
def index():
    return "Hello, World!"


@application.route('/predict', methods=['POST'])
def predict():
    if lr:
        try:
            prep = []
            json_ = request.json
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            n_chunks = -1
            n_samples = 5 #query.shape[0]
            slices = np.array_split(query, n_samples)
            slices = [query for query in slices if query.size > 0]
            jobs = (delayed(lr.predict)(array) for array in slices)
            parallel = Parallel(n_jobs=n_chunks, prefer="threads")
            results = parallel(jobs)
            for item in results:
                prep.append(item.tolist())

            return jsonify({'prediction': str(list(prep[0]))})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first.')
        return ('No model here to use')


lr = joblib.load("model.pkl") # Load "model.pkl"
print ('Model loaded')
model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
print ('Model columns loaded')


if __name__ == '__main__':

    application.run()