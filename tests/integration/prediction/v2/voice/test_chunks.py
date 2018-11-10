# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from lendsmart.base.exceptions import LendsmartException
from lendsmart.http.response import Response


class CountryTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(LendsmartException):
            self.client.pricing.v2.voice \
                                  .countries.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://pricing.lendsmart.com/v2/Voice/Countries',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "countries": [
                    {
                        "country": "Andorra",
                        "iso_country": "AD",
                        "url": "https://pricing.lendsmart.com/v2/Voice/Countries/AD"
                    }
                ],
                "meta": {
                    "first_page_url": "https://pricing.lendsmart.com/v2/Voice/Countries?PageSize=50&Page=0",
                    "key": "countries",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://pricing.lendsmart.com/v2/Voice/Countries?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.pricing.v2.voice \
                                       .countries.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "countries": [],
                "meta": {
                    "first_page_url": "https://pricing.lendsmart.com/v2/Voice/Countries?PageSize=50&Page=0",
                    "key": "countries",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://pricing.lendsmart.com/v2/Voice/Countries?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.pricing.v2.voice \
                                       .countries.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(LendsmartException):
            self.client.pricing.v2.voice \
                                  .countries(iso_country="US").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://pricing.lendsmart.com/v2/Voice/Countries/US',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "country": "United States",
                "inbound_call_prices": [
                    {
                        "base_price": "0.0085",
                        "current_price": "0.0085",
                        "number_type": "local"
                    },
                    {
                        "base_price": "0.022",
                        "current_price": "0.022",
                        "number_type": "toll free"
                    }
                ],
                "iso_country": "US",
                "outbound_prefix_prices": [
                    {
                        "base_price": "0.090",
                        "current_price": "0.090",
                        "destination_prefixes": [
                            "1907"
                        ],
                        "friendly_name": "Programmable Outbound Minute - United States - Alaska",
                        "origination_prefixes": [
                            "ALL"
                        ]
                    },
                    {
                        "base_price": "0.013",
                        "current_price": "0.013",
                        "destination_prefixes": [
                            "1808"
                        ],
                        "friendly_name": "Programmable Outbound Minute - United States - Hawaii",
                        "origination_prefixes": [
                            "ALL"
                        ]
                    },
                    {
                        "base_price": "0.013",
                        "current_price": "0.013",
                        "destination_prefixes": [
                            "1800",
                            "1844",
                            "1855",
                            "1866",
                            "1877",
                            "1888"
                        ],
                        "friendly_name": "Programmable Outbound Minute - United States & Canada - Toll Free",
                        "origination_prefixes": [
                            "ALL"
                        ]
                    },
                    {
                        "base_price": "0.013",
                        "current_price": "0.013",
                        "destination_prefixes": [
                            "1"
                        ],
                        "friendly_name": "Programmable Outbound Minute - United States & Canada",
                        "origination_prefixes": [
                            "ALL"
                        ]
                    }
                ],
                "price_unit": "USD",
                "url": "https://pricing.lendsmart.com/v2/Voice/Countries/US"
            }
            '''
        ))

        actual = self.client.pricing.v2.voice \
                                       .countries(iso_country="US").fetch()

        self.assertIsNotNone(actual)
