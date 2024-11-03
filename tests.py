import pytest

from payment_requests import create_new_payment, get_all_payments, delete_all_payments


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    delete_all_payments()
    yield
    delete_all_payments()


def test_create_payment():
    """Test the creation of a single payment.

    Creates a payment with specific parameters and verifies that:
        1. The payment is created successfully with a 201 status code.
        2. The created payment can be retrieved from the list of all payments.
    """
    payment, status_code = create_new_payment(amount=100, currency="USD", name="Test Consumer")

    # Payment was successful and can be found in all payments
    assert status_code == 201, f"Expected status code 201, but got {status_code}"
    assert payment["id"] in map(lambda x: x["id"], get_all_payments()[0]), "Payment not found in all payments"


def test_create_multiple_payments():
    """Test the creation of multiple payments with varied parameters.

    Iterates over a list of different payment data, creates each payment, and verifies that:
        1. Each payment is created successfully with a 201 status code.
        2. Each created payment is retrievable from the list of all payments.

    The test covers different currencies and amounts to ensure varied cases are handled correctly.
    """
    payment_data = [
        {"amount": 100, "currency": "USD", "name": "Test Consumer"},
        {"amount": 150, "currency": "EUR", "name": "Test Consumer"},
        {"amount": 5000, "currency": "JPY", "name": "Test Consumer"},
        {"amount": 300, "currency": "ETH", "name": "Test Consumer"},
    ]

    payment_ids = []
    for p in payment_data:
        payment, status_code = create_new_payment(
            amount=p["amount"],
            currency=p["currency"],
            name=p["name"]
        )
        assert status_code == 201, f"Failed to create payment with data: {p}"
        payment_ids.append(payment["id"])

    # Get all payment IDs
    all_payment_ids = {p["id"] for p in get_all_payments()[0]}

    # Verify each created payment ID is in the list of all payments
    for payment_id in payment_ids:
        assert payment_id in all_payment_ids, f"Payment ID {payment_id} not found in all payments."
