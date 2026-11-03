# Provider-neutral payment example

The sample in [`examples/provider_agnostic_payments.py`](../examples/provider_agnostic_payments.py)
defines a small adapter contract for starting hosted checkout with Visa or Cash
App Pay. [`examples/checkout_request.json`](../examples/checkout_request.json)
shows the request shape, and [`payment-flow.mmd`](payment-flow.mmd) shows the
high-level flow.

The application supplies a `PaymentGateway` implementation for its chosen
payment processor. The adapter maps `visa_card` and `cash_app_pay` to that
processor's supported hosted checkout methods and returns the session URL. This
example intentionally does not implement a processor or handle payment
credentials.

## Trust and security boundaries

- Treat the JSON as an internal service request, not trusted browser input.
  Authenticate the customer, load the order from server-side storage, and
  calculate the amount there.
- `amount_minor` is an integer in the currency's minor unit (for example, 2599
  means USD 25.99). Do not use floating-point amounts.
- Collect card details only on the payment processor's hosted page; never send
  a PAN, CVV, Cash App credentials, or other payment credentials through this
  application.
- Generate and persist the idempotency key on the server. Reuse it for retries
  of the same checkout attempt.
- The adapter must verify webhook signatures and deduplicate provider events.
  Fulfill orders only after a verified payment event; a browser redirect alone
  is not proof of payment.
- Before redirecting, accept only checkout URLs returned by the configured
  adapter and validate them against that adapter's allowed HTTPS origins.

This is an integration example, not a production-ready payment service. A real
adapter must implement its processor's session creation, webhook verification,
event normalization, and error handling.
