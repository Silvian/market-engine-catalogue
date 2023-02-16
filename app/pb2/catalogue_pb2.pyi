from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemDetails(_message.Message):
    __slots__ = ["description", "id", "image", "name", "rating", "reviews"]
    class Review(_message.Message):
        __slots__ = ["comment", "id", "item_id", "rating"]
        COMMENT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        comment: str
        id: str
        item_id: str
        rating: float
        def __init__(self, id: _Optional[str] = ..., item_id: _Optional[str] = ..., rating: _Optional[float] = ..., comment: _Optional[str] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    REVIEWS_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    image: str
    name: str
    rating: float
    reviews: _containers.RepeatedCompositeFieldContainer[ItemDetails.Review]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., rating: _Optional[float] = ..., description: _Optional[str] = ..., reviews: _Optional[_Iterable[_Union[ItemDetails.Review, _Mapping]]] = ...) -> None: ...

class ItemDetailsRequest(_message.Message):
    __slots__ = ["itemId", "reviewsLimit"]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    REVIEWSLIMIT_FIELD_NUMBER: _ClassVar[int]
    itemId: str
    reviewsLimit: int
    def __init__(self, itemId: _Optional[str] = ..., reviewsLimit: _Optional[int] = ...) -> None: ...

class Items(_message.Message):
    __slots__ = ["items"]
    class Item(_message.Message):
        __slots__ = ["id", "image", "name", "rating"]
        ID_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        id: str
        image: str
        name: str
        rating: float
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., rating: _Optional[float] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Items.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[Items.Item, _Mapping]]] = ...) -> None: ...

class ItemsRequest(_message.Message):
    __slots__ = ["itemsLimit"]
    ITEMSLIMIT_FIELD_NUMBER: _ClassVar[int]
    itemsLimit: int
    def __init__(self, itemsLimit: _Optional[int] = ...) -> None: ...
