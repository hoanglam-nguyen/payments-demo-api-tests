import requests

def create_new_payment(amount: float, currency: str, name: str, base_url: str) -> tuple[dict, int]:
    """Creates a new payment entry.

    Args:
        amount (float): The amount for the payment.
        currency (str, optional): The currency for the payment.
        name (str, optional): The name associated with the payment.
        base_url (str): The base URL of the server hosting the payment API.

    Returns:
        tuple[dict, int]: A tuple containing the payment as a dict and the status code
        indicating if the creation was successful (201).
    """
    url = f"{base_url}/payments"

    headers = {
        "Authorization": "Basic am9objpqb2hu",
        "Content-Type": "application/json"
    }
    data = {
        "amount": amount,
        "currency": currency,
        "name": name
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json(), response.status_code

def get_payment(payment_id: int, base_url: str) -> tuple[dict, int]:
    """Fetches a payment entry by ID.

    Args:
        payment_id (int): The ID of the payment to retrieve.
        base_url (str): The base URL of the server hosting the payment API.

    Returns:
        tuple[dict, int]: A tuple containing the payment as a dict and the status code.
    """
    url = f"{base_url}/payments/{payment_id}"
    headers = {
        "Authorization": "Basic am9objpqb2hu"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json(), response.status_code
    else:
        return {}, response.status_code

def get_all_payments(base_url: str) -> tuple[list, int]:
    """Fetches all payment entries.

    Args:
        base_url (str): The base URL of the server hosting the payment API.

    Returns:
        tuple[list, int]: A tuple containing a list of all payments and the status code.
    """
    url = f"{base_url}/payments"
    headers = {
        "Authorization": "Basic am9objpqb2hu"
    }

    response = requests.get(url, headers=headers)
    return response.json(), response.status_code

def delete_payment(payment_id: int, base_url: str) -> int:
    """Deletes a payment entry by ID.

    Args:
        payment_id (int): The ID of the payment to delete.
        base_url (str): The base URL of the server hosting the payment API.

    Returns:
        int: The HTTP status code indicating the result of the delete operation.
    """
    url = f"{base_url}/payments/{payment_id}"
    headers = {
        "Authorization": "Basic am9objpqb2hu"
    }

    response = requests.delete(url, headers=headers)
    return response.status_code

def delete_all_payments(base_url: str) -> None:
    """Deletes all payment entries.

    Retrieves all payments using `get_all_payments` and iteratively deletes each payment
    by calling `delete_payment` with the payment's ID.

    Args:
        base_url (str): The base URL of the server hosting the payment API.

    Returns:
        None
    """
    payments, _ = get_all_payments(base_url)
    for p in payments:
        delete_payment(p["id"], base_url)

if __name__ == '__main__':
    app_base_url = "http://localhost:8080"
    delete_all_payments(app_base_url)
    payment, _ = create_new_payment(amount=11.13, currency="USD", name="Test consumer", base_url=app_base_url)
    print(payment)
    print(get_payment(payment["id"], app_base_url))
    delete_payment(payment["id"], app_base_url)
