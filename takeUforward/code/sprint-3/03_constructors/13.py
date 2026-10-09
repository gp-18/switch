# Abstract Base Class (ABC) with Constructor Invariants
# Abstract classes cannot be instantiated, but their constructors define common invariant state.
#
# 1. PaymentProcessor(ABC):
#    - __init__(self, api_key: str, currency: str = "USD"):
#      validate that api_key is non-empty; raise ValueError("API key cannot be empty") if invalid.
#      store self.api_key and self.currency.
#    - @abstractmethod def process_payment(self, amount: float) -> str: pass
#
# 2. StripeProcessor(PaymentProcessor):
#    - __init__(self, api_key: str, currency: str = "USD", webhook_secret: str = ""):
#      call super().__init__(api_key, currency).
#      store self.webhook_secret = webhook_secret.
#    - Implement process_payment(self, amount): returns f"Processed ${amount} via Stripe"
#
# 3. PayPalProcessor(PaymentProcessor):
#    - __init__(self, api_key: str, currency: str = "USD", client_id: str = ""):
#      call super().__init__(api_key, currency).
#      store self.client_id = client_id.
#    - Implement process_payment(self, amount): returns f"Processed ${amount} via PayPal"
#
# Example 1:
# Input:  s = StripeProcessor("sk_test_123", "USD", "whsec_abc")
# Output: s.api_key == "sk_test_123", s.currency == "USD", s.webhook_secret == "whsec_abc"
#
# Example 2:
# Input:  PaymentProcessor("key")
# Output: TypeError: Can't instantiate abstract class PaymentProcessor
#

# Write your solution below:


from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def __init__(self, api_key: str, currency: str = "USD"):
        if not api_key:
            raise ValueError("API key cannot be empty")

        self.api_key = api_key
        self.currency = currency

    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass


class StripeProcessor(PaymentProcessor):
    def __init__(
        self,
        api_key: str,
        currency: str = "USD",
        webhook_secret: str = ""
    ):
        super().__init__(api_key, currency)
        self.webhook_secret = webhook_secret

    def process_payment(self, amount: float) -> str:
        return f"Processed ${amount} via Stripe"


class PayPalProcessor(PaymentProcessor):
    def __init__(
        self,
        api_key: str,
        currency: str = "USD",
        client_id: str = ""
    ):
        super().__init__(api_key, currency)
        self.client_id = client_id

    def process_payment(self, amount: float) -> str:
        return f"Processed ${amount} via PayPal"


# Example 1: Stripe
s = StripeProcessor("sk_test_123", "USD", "whsec_abc")

print(s.api_key)
print(s.currency)
print(s.webhook_secret)
print(s.process_payment(100.0))

# Example 2: PayPal
p = PayPalProcessor("paypal_key_123", client_id="client_abc")

print(p.process_payment(50.0))