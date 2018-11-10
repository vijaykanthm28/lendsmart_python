# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from lendsmart.base.domain import Domain
from lendsmart.rest.prediction.v2 import V2


class Prediction(Domain):

    def __init__(self, lendsmart):
        """
        Initialize the Prediction Domain

        :returns: Domain for Prediction
        :rtype: lendsmart.rest.pricing.Prediction
        """
        super(Prediction, self).__init__(lendsmart)

        self.base_url = 'https://api.lendsmart.ai'

        # Versions
        self._v2 = None

    @property
    def v2(self):
        """
        :returns: Version v2 of pricing
        :rtype: lendsmart.rest.pricing.v2.V2
        """
        if self._v2 is None:
            self._v2 = V2(self)
        return self._v2

    @property
    def messaging(self):
        """
        :rtype: lendsmart.rest.pricing.v1.messaging.MessagingList
        """
        return self.v1.messaging

    @property
    def phone_numbers(self):
        """
        :rtype: lendsmart.rest.pricing.v1.phone_number.PhoneNumberList
        """
        return self.v1.phone_numbers

    @property
    def voice(self):
        """
        :rtype: lendsmart.rest.pricing.v2.voice.VoiceList
        """
        return self.v2.voice

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<lendsmart.Prediction>'

