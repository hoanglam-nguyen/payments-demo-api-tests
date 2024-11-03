# payments-demo-api-tests

Example project that performs API tests for [payments-demo-quarkus-app](https://github.com/alexandrchumakin/payments-demo-quarkus-app.git) using [pytest](https://github.com/pytest-dev/pytest).

## Prerequisites
This project was tested on Python 3.11.8.

Make sure `payments-demo-quarkus-app` is running in the minikube cluster with port-forwarding configured to **localhost:8080** ([detailed instructions](https://github.com/alexandrchumakin/payments-demo-quarkus-app?tab=readme-ov-file#run-minikube-cluster)), e.g.:
```shell
./scripts/start-minikube.sh
kubectl port-forward ${container-name} 8080:8081
```
Note that the remote port might be different from the original instructions. In my case, it was **8081**, which I found out by inspecting the logs via `kubectl logs deployments/payments-demo-quarkus-app`.

## Setup
In a separate terminal session, create a virtual environment and install dependencies:
```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the tests	
Run `test_create_payment` test:
```shell
pytest tests/test_payment_requests.py::test_create_payment
```

Run `create_multiple_payments` test:
```shell
pytest tests/test_payment_requests.py::test_create_multiple_payments
```

Or run both tests:
```shell
pytest tests
```
