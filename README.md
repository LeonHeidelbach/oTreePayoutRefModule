# oTree payment app for the DICE payment platform

This app offers a simple way to connect the experiments to the DICE payment platform. 

# Getting started

* Place the app in your oTree folder and add it to the app_sequence of your session in settings.py
  ```python
    app_sequence = ['some_app_1', 'some_app_2', 'payment']
  ```
* Add the *expId* and *expShortName* to your session settings
  * *expId*: Experiment short name from the payment platform
  * *expShortName*: Experiment ID (can be found either on the experiment page within ORSEE or the payment platform)
* Your SESSION_CONFIG should look something like this
   ```python
    SESSION_CONFIGS = [
    dict(
       name='example_session',
       display_name="example_session",
       num_demo_participants=3,
       expShortName="TestExp", # Replace with your values
       expId=0000000000, # Replace with your values
       app_sequence = ['some_app_1', 'some_app_2', 'payment']
    )]  
    ```

# Usage

* Upon creation of a session on the server, move to the *Report* Tab of the payment app and copy the URLs for the payment platform.
![admin-report](docs/images/admin_report.PNG)
* The correct participant label paramater will be automatically added to each URL by the payment platform after you assigned the URLs. 
* If participants use those links passed via the payment platform to join the session, the participant label within oTree will correspond to their ORSEE-ID.
* The participant label and the information added to the SESSION_CONFIG will be used to create a participant specific link to the payment platform 
    * Note: Always use the player and participant payoff-field of oTree to store any payments participants receive within your experiment.
* On the last page of the experiment participant will then see their final payoff in the specified real world currency and a button that links to receive their payoff  
![admin-report](docs/images/page.PNG)

# Requirements
* otree>5
  * Note that we provide a version for otree<5 in another branch