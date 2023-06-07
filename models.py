from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from .exception import PaymentKeyNotFound
from .oTreePayoutRefModule.payout_url_generator import PayoutURLGenerator

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'payment'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        # Check for payment keys
        payment_keys = ['expId', 'sessId', 'expShortName']
        for k in payment_keys:
            if k not in self.session.config.keys(
            ) or self.session.config[k] is None:
                raise PaymentKeyNotFound(k)

    def vars_for_admin_report(self):
        participants = self.session.get_participants()
        # The base url added directly in template:
        # This is super hacky, but it seems that I cannot access the View for the Admin Page
        # from oTree. Note that this part differs for otree>5 due to the swtich from django
        # to starlette.
        urls_with_id = [
            p._start_url() + "/?participant_label=[TEILNEHMER-ID_EINFÜGEN]"
            for p in participants
        ]

        return {
            'urls_with_id': urls_with_id,
            'participants': participants,
        }


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Required if the Hroot ID is not passed via the
    # participant label.
    hroot_id = models.StringField(
        label="Bitte geben Sie Ihre Teilnehmer-ID ein:")

    def create_paymentURL(self):
        """

        Small helper function to create a payment URL.
        """
        expShortName = self.session.config['expShortName']
        expId = self.session.config['expId']
        sessId = self.session.config['sessId']
        pid = self.participant.label
        final_payoff = float(self.participant.payoff_plus_participation_fee())
        paymentURL = PayoutURLGenerator(expShortName,
                                        expId,
                                        sessId,
                                        pid,
                                        final_payoff).getPayoutURL()
        return paymentURL
