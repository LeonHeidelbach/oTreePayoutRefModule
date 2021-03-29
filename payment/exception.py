class PaymentKeyNotFound(Exception):

    def __init__(self, missing_key):
        self.missing_key = missing_key
        self.message = (f"The key '{self.missing_key}' is required to contruct " 
                        "the payment link but was not defined in the session config.")
        super().__init__(self.message)
