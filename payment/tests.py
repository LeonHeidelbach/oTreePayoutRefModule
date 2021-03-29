from otree.api import Currency as c, currency_range, expect, Submission
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.participant.label is None:
            yield pages.OrseeID, dict(orsee_id="test-id")
        expect(str(self.participant.payoff_plus_participation_fee()), "in", self.html)
        yield Submission(pages.Payoff, check_html=False)
