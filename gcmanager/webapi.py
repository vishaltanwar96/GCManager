import json

import falcon

from gcmanager.domain import SuccessfulResponse
from gcmanager.serializers import GiftCardAssetSummarySerializer
from gcmanager.serializers import GiftCardCreateRequestSerializer
from gcmanager.serializers import GiftCardSerializer
from gcmanager.usecases import AddGiftCardUseCase
from gcmanager.usecases import FetchUnusedGiftCardsUseCase
from gcmanager.usecases import GiftCardAssetInformationUseCase


class GiftCardAssetInformationResource:
    def __init__(self, use_case: GiftCardAssetInformationUseCase) -> None:
        self._use_case = use_case
        self._serializer = GiftCardAssetSummarySerializer()

    def on_get(self, request: falcon.Request, response: falcon.Response) -> None:
        assets = self._use_case.summarize()
        serialized_data = self._serializer.dump(assets)
        response.text = SuccessfulResponse(data=serialized_data).serialize()
        response.status = falcon.HTTP_200


class GiftCardResource:
    def __init__(
        self,
        create_use_case: AddGiftCardUseCase,
        get_unused_use_case: FetchUnusedGiftCardsUseCase,
    ) -> None:
        self._create_use_case = create_use_case
        self._get_unused_use_case = get_unused_use_case
        self._dump_serializer = GiftCardSerializer()
        self._load_serializer = GiftCardCreateRequestSerializer()

    def on_get(self, request: falcon.Request, response: falcon.Response) -> None:
        gift_cards = self._get_unused_use_case.fetch()
        serialized_data = self._dump_serializer.dump(gift_cards, many=True)
        response.text = SuccessfulResponse(data=serialized_data).serialize()
        response.status = falcon.HTTP_200

    def on_post(self, request: falcon.Request, response: falcon.Response) -> None:
        payload = json.loads(request.bounded_stream.read())
        gift_card_create_request = self._load_serializer.load(payload)
        self._create_use_case.create(gift_card_create_request)
        response.status = falcon.HTTP_201
