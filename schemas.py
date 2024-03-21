from enum import StrEnum, auto
from typing import Annotated

from pydantic import BaseModel, Field, model_serializer, AfterValidator, AliasPath


def key_serializer(key: str):
    if key and key.startswith("#"):
        return key[1:]
    return key


class Languages(StrEnum):
    brazilian = auto()
    bulgarian = auto()
    czech = auto()
    danish = auto()
    dutch = auto()
    english = auto()
    finnish = auto()
    french = auto()
    german = auto()
    greek = auto()
    hungarian = auto()
    italian = auto()
    japanese = auto()
    koreana = auto()
    latam = auto()
    norwegian = auto()
    polish = auto()
    portuguese = auto()
    romanian = auto()
    russian = auto()
    schinese = auto()
    schinese_pw = auto()
    spanish = auto()
    swedish = auto()
    tchinese = auto()
    thai = auto()
    turkish = auto()
    ukrainian = auto()
    vietnamese = auto()


class Prefab(BaseModel):
    item_name: str | None
    item_description: str | None
    first_sale_date: str | None
    prefab: str | None
    used_by_classes: dict | None


def translation_key_validator(key: str):
    if key.startswith("#"):
        key = key[1:]

    return key.lower()


translation_key = Annotated[str, AfterValidator(translation_key_validator)]


class Tag(BaseModel):
    group: str = Field(validation_alias="tag_group")
    value: str = Field(validation_alias="tag_value")
    group_text: translation_key = Field(validation_alias="tag_group_text")
    text: translation_key = Field(validation_alias="tag_text")


class Item(BaseModel):
    object_id: str
    item_name: translation_key | None
    description: translation_key | None
    tag: Tag | None
    item_name_prefab: translation_key | None
    item_description_prefab: translation_key | None
    used_by_classes: dict | None


class Property(BaseModel):
    id: str
    name: str


class Rarity(Property):
    color: str


class Collection(Property):
    image: str


class Skin(BaseModel):
    id: int
    name: str
    description: str
    weapon: str
    category: str
    pattern: str
    min_float: float
    max_float: float
    rarity: Rarity
    stat_trak: bool
    souvenir: bool
    paint_index: str
    wears: list[Property]
    collections: list[Collection]
    crates: list[Collection]
    team: Property


class Data(BaseModel):
    prefabs: dict[str, Prefab] = {}
    items: dict[str, Item] = {}
    item_sets: list[dict[str, any]] = []
    stat_trak_skins: dict[str, bool] = {}
