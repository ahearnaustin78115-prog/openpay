"""Provider-neutral checkout orchestration for Visa and Cash App Pay."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import re
from typing import Protocol


class PaymentMethod(str, Enum):
    VISA_CARD = "visa_card"
    CASH_APP_PAY = "cash_app_pay"


@dataclass(frozen=True)
class CheckoutRequest:
    order_id: str
    amount_minor: int
    currency: str
    payment_method: PaymentMethod
    idempotency_key: str


@dataclass(frozen=True)
class CheckoutSession:
    session_id: str
    redirect_url: str
    expires_at: datetime


class PaymentGateway(Protocol):
    def create_checkout_session(
        self, request: CheckoutRequest
    ) -> CheckoutSession:
        """Create a hosted checkout session using the selected payment method."""
        ...


def create_checkout(
    request: CheckoutRequest, gateway: PaymentGateway
) -> CheckoutSession:
    """Validate a trusted order request and delegate checkout to an adapter."""
    if not isinstance(request.order_id, str) or not request.order_id.strip():
        raise ValueError("order_id must not be empty")
    if type(request.amount_minor) is not int or request.amount_minor <= 0:
        raise ValueError("amount_minor must be a positive integer")
    if not isinstance(request.currency, str) or not re.fullmatch(
        r"[A-Z]{3}", request.currency
    ):
        raise ValueError("currency must be a three-letter uppercase code")
    if not isinstance(request.payment_method, PaymentMethod):
        raise ValueError("unsupported payment method")
    if (
        not isinstance(request.idempotency_key, str)
        or not request.idempotency_key.strip()
    ):
        raise ValueError("idempotency_key must not be empty")

    return gateway.create_checkout_session(request)
