# Machine Learning Deployment Strategy

This repository is intended to demonstrate the benefits of using a container based environment such as Openshift to deploy and maintain models created within the organisation. The selection of the Openshift itself is purely  based on this technology already being deployed and understood.

## Implementation Notes

This example uses the well known Titanic dataset. A classifier is trained and then dumped into a file which is then applied to unseen data. The model itself and its effectiveness are not important for this demonstration. The requirements which need to be satisfied for this to work are:

* An operational Openshift environment configured with an active webhook to this repository.
* A method for making an API call to the ``/predict`` route such as postman.
* This application should be deployed with a minimum of Python 3
* ``Scikit-Learn``,``Pandas``,``Joblib`` and  ``NumPy`` must be specified in ``requirements.txt`` file for ``pip``.

## Deployment Steps

To deploy this sample Python web API from the OpenShift web console, you should select ``python:latest``, when using _Add to project_. Use of ``python:latest`` is the same as having selected the most up to date Python version available.

The HTTPS URL of this code repository which should be supplied to the _Git Repository URL_ field when using _Add to project_ is:

* https://github.com/merlosus/models-in-containers-python.git

If using the ``oc`` command line tool instead of the OpenShift web console, to deploy this sample Python web application, you can run:

```
oc new-app https://github.com/merlosus/models-in-containers-python.git
```
## Using the API

Send a POST request to

* http://your_openshift_applicaton_url/predict

The request should contain one or more JSON objects formatted as below:

Single
```
[
	{"Age": 50 , "Sex": "male", "Embarked": "S"}
]
```
Multiple
```
[
	{"Age": 50 , "Sex": "male", "Embarked": "S"},
	{"Age": 24 , "Sex": "female", "Embarked": "C"}
]
```
* Age refers to a discrete numeric value
* Sex refers to the gender represented by a string value "male" or "female"
* Embarked refers to the port in which a passenger has embarked. C - Cherbourg, S - Southampton, Q = Queenstown

# Credits

The Flask and GUniconrn program structure owes credit to Graham Dumpleton. His demonstration of Flask applications in an Openshift environment gave helpful insights.
The machine learning model was taken from a datacamp tutorial to keep the concepts simple. It was then modified to run within the GUnicorn context on the Openshift environment.
 
* https://www.datacamp.com/community/tutorials/machine-learning-models-api-python
* https://github.com/GrahamDumpleton
