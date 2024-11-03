import requests

def create_new_payment(amount: float, currency: str, name: str) -> tuple[dict, int]:
    """Creates a new payment entry.

    Args:
        amount (float): The amount for the payment.
        currency (str, optional): The currency for the payment.
        name (str, optional): The name associated with the payment.

    Returns:
        tuple[dict, int]: A tuple containing the payment as a dict and the status code
        indicating if the creation was successful (201).
    """
    url = "http://localhost:8080/payments"
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

def get_all_payments() -> tuple[list, int]:
    """Fetches all payment entries.

    Returns:
        tuple[list, int]: A tuple containing a list of all payments and the status code.
    """
    url = "http://localhost:8080/payments"
    headers = {
        "Authorization": "Basic am9objpqb2hu"
    }

    response = requests.get(url, headers=headers)
    return response.json(), response.status_code

def delete_payment(payment_id: int) -> int:
    """Deletes a payment entry by ID.

    Args:
        payment_id (int): The ID of the payment to delete.

    Returns:
        int: The HTTP status code indicating the result of the delete operation.
    """
    url = f"http://localhost:8080/payments/{payment_id}"
    headers = {
        "Authorization": "Basic am9objpqb2hu"
    }

    response = requests.delete(url, headers=headers)
    return response.status_code

def delete_all_payments() -> None:
    """Deletes all payment entries.

    Retrieves all payments using `get_all_payments` and iteratively deletes each payment
    by calling `delete_payment` with the payment's ID.

    Returns:
        None
    """
    payments, _ = get_all_payments()
    for p in payments:
        delete_payment(p["id"])

if __name__ == '__main__':
    payment, _ = create_new_payment(amount=11.13, currency="USD", name="Test consumer")
    print(payment)
    print(get_all_payments())
    delete_payment(payment["id"])

