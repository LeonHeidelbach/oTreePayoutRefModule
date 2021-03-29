# Payment module for the DICE payment platform

This module can be used in any oTree experiment project to generate individual payment URLs for the DICE-Lab payment platform.

* The following information can/must be included in the generated URL:
    * Experiment short name **(optional)**
    * Experiment ID (can be found either on the experiment page within ORSEE or the payment platform)
    * Participant ID (encrypted participant ID as supplied with the "participant_label" variable) **(optional)**
    * Payout amount (the amount earned by the participant) **(optional)**

# How to implement the module

The `"PayoutURLGenerator"` class creates all parts of the payment URL separately and combines them into a URL-String.

There are two options to create a payment URL: 
1. Instantiate a `"PayoutURLGenerator"` object and pass the necessary variable details directly to the constructor method.
2. Instantiate a `"PayoutURLGenerator"` object and set the necessary variable details through usage of the setter methods. 

Both options can be used in conjunction when creating a list of multiple payout URLs for the same experiment and only the participant id and the payout amount are subject to change.

Calling the `getPayoutURL` method on the instantiated object returns the constructed URL string using the current instance parameters.

```python
##  0 -> Placeholder for any integer
## "X" -> Placeholder for any string

# Method 1.
paymentURLGenerator = PayoutURLGenerator()
paymentURLGenerator.setExpShortName("TestExp")
paymentURLGenerator.setExpId(0000000000)
paymentURLGenerator.setPid("XXXXXXXXXXXXXXX")
paymentURLGenerator.setPayout(10.10)
paymentURL = paymentURLGenerator.getPayoutURL()

# Method 2.
paymentURL = PayoutURLGenerator("TestExp",0000000000,000000000000000,10.10).getPayoutURL()

# Method 3.
paymentURL = PayoutURLGenerator("TestExp","0000000000","XXXXXXXXXXXXXXX",10.10).getPayoutURL()
```