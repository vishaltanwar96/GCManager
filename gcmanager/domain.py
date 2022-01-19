from dataclasses import dataclass
from dataclasses import field
from datetime import date
from datetime import datetime
from typing import NewType

Denomination = NewType("Denomination", int)
RedeemCode = NewType("RedeemCode", str)
GiftCardID = NewType("GiftCardID", str)
Money = NewType("Money", int)


@dataclass(frozen=True)
class GiftCard:
    id: GiftCardID
    redeem_code: RedeemCode
    date_of_issue: date
    pin: int
    is_used: bool
    source: str
    denomination: Denomination
    timestamp: datetime = field(default_factory=datetime.now)

    @property
    def date_of_expiry(self) -> date:
        return self.date_of_issue.replace(year=self.date_of_issue.year + 1)


@dataclass(frozen=True)
class GiftCardAssetSummary:
    total: Money
    used: Money

    @property
    def unused(self) -> Money:
        return Money(self.total - self.used)


@dataclass(frozen=True)
class GiftCardUpdateRequest:
    id: GiftCardID
    redeem_code: RedeemCode
    date_of_issue: date
    pin: int
    source: str
    denomination: Denomination
