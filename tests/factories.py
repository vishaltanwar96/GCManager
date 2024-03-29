import string
import uuid
from datetime import date
from datetime import datetime

import factory
from factory import DictFactory
from factory import Factory
from factory import LazyFunction
from factory.fuzzy import FuzzyChoice
from factory.fuzzy import FuzzyDate
from factory.fuzzy import FuzzyInteger
from factory.fuzzy import FuzzyNaiveDateTime
from factory.fuzzy import FuzzyText

from gcmanager.domain import GiftCard
from gcmanager.domain import GiftCardAssetSummary
from gcmanager.domain import GiftCardCreateRequest
from gcmanager.domain import GiftCardUpdateRequest


class GiftCardAssetSummaryFactory(Factory):
    class Meta:
        model = GiftCardAssetSummary

    total = FuzzyInteger(8_000, 15_000)
    used = FuzzyInteger(400, 7_000)


class GiftCardFactory(Factory):
    class Meta:
        model = GiftCard

    id = LazyFunction(uuid.uuid4)
    redeem_code = FuzzyText(length=14, chars=string.ascii_uppercase + string.digits)
    date_of_issue = FuzzyDate(start_date=date.today())
    pin = FuzzyInteger(low=1_000_000_000_000_000, high=9_999_999_999_999_999)
    timestamp = FuzzyNaiveDateTime(start_dt=datetime.now())
    is_used = False
    source = FuzzyChoice(["AMAZON", "WOOHOO", "MAGICPIN", "HDFC SMARTBUY"])
    denomination = FuzzyChoice([50, 100, 200, 500, 1_000, 2_000, 10_000])


class GiftCardUpdateRequestFactory(Factory):
    class Meta:
        model = GiftCardUpdateRequest

    id = LazyFunction(uuid.uuid4)
    redeem_code = FuzzyText(length=14, chars=string.ascii_uppercase + string.digits)
    date_of_issue = FuzzyDate(start_date=date.today())
    pin = FuzzyInteger(low=1_000_000_000_000_000, high=9_999_999_999_999_999)
    source = FuzzyChoice(["AMAZON", "WOOHOO", "MAGICPIN", "HDFC SMARTBUY"])
    denomination = FuzzyChoice([50, 100, 200, 500, 1_000, 2_000, 10_000])


class GiftCardPayloadFactory(DictFactory):
    class Params:
        redeem_code_length_greater = factory.Trait(
            redeem_code=FuzzyText(
                length=15,
                chars=string.ascii_uppercase + string.digits,
            ),
        )
        redeem_code_length_lesser = factory.Trait(
            redeem_code=FuzzyText(
                length=13,
                chars=string.ascii_uppercase + string.digits,
            ),
        )
        redeem_code_not_alphanumeric = factory.Trait(
            redeem_code=FuzzyText(length=14, chars=string.punctuation),
        )
        date_of_issue_one_year_past = factory.Trait(
            date_of_issue=LazyFunction(
                lambda: date.today().replace(year=date.today().year - 1),
            ),
        )
        pin_length_greater = factory.Trait(pin=10_000_000_000_000_000)
        pin_length_lesser = factory.Trait(pin=999_999_999_999_999)

    redeem_code = FuzzyText(length=14, chars=string.ascii_uppercase + string.digits)
    date_of_issue = FuzzyDate(start_date=date.today())
    pin = FuzzyInteger(low=1_000_000_000_000_000, high=9_999_999_999_999_999)
    source = FuzzyChoice(["AMAZON", "WOOHOO", "MAGICPIN", "HDFC SMARTBUY"])
    denomination = FuzzyInteger(low=1000, high=10000, step=1000)


class GiftCardCreateRequestFactory(Factory):
    class Meta:
        model = GiftCardCreateRequest

    redeem_code = FuzzyText(length=14, chars=string.ascii_uppercase + string.digits)
    date_of_issue = FuzzyDate(start_date=date.today())
    pin = FuzzyInteger(low=1_000_000_000_000_000, high=9_999_999_999_999_999)
    source = FuzzyChoice(["AMAZON", "WOOHOO", "MAGICPIN", "HDFC SMARTBUY"])
    denomination = FuzzyInteger(low=1000, high=10000, step=1000)
