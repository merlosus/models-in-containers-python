# Machine Learning Deployment Strategy

This repository is intended to demonstrate the benefits of using a container based environment such as Openshift to deploy and maintain models created within the organisation. The selection of the Openshift itself is purely  based on this technology already being deployed and understood.

## Implementation Notes

This example uses the well known Titanic dataset. A classifier is trained and then dumped into a file which is then applied to unseen data. The model itself and its effectiveness are not important for this demonstration. The requirements which need to be satisfied for this to work are:

* An operational Openshift environment configured with an active webhook to this repository.
* A method for making an API call to the ``/predict`` route such as postman.
* This application should be deployed with a minimum of Python 3
* ``Scikit-Learn``,``Pandas``,``Joblib`` and  ``NumPy`` must be specified in ``requirements.txt`` file for ``pip``.

## Deployment Steps

To deploy this sample Python web application from the OpenShift web console, you should select ``python:2.7``, ``python:3.3``, ``python:3.4`` or ``python:latest``, when using _Add to project_. Use of ``python:latest`` is the same as having selected the most up to date Python version available, which at this time is ``python:3.4``.

The HTTPS URL of this code repository which should be supplied to the _Git Repository URL_ field when using _Add to project_ is:

* https://github.com/merlosus/models-in-containers-python.git

If using the ``oc`` command line tool instead of the OpenShift web console, to deploy this sample Python web application, you can run:

```
oc new-app https://github.com/merlosus/models-in-containers-python.git
```

In this case, because no language type was specified, OpenShift will determine the language by inspecting the code repository. Because the code repository contains a ``requirements.txt``, it will subsequently be interpreted as including a Python application. When such automatic detection is used, ``python:latest`` will be used.

If needing to select a specific Python version when using ``oc new-app``, you should instead use the form:

```
oc new-app python:2.7~https://github.com/merlosus/models-in-containers-python.git
```
