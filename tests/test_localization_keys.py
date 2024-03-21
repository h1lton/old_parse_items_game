import vdf

from load_data import load_data, load_translation
from schemas import Languages

data = load_data()

translation = load_translation()


def is_valid_key(key: str | None) -> bool:
    if key is None:
        return True
    if key.startswith("#"):
        return False
    if not key.islower():
        return False

    return True


def test_keys():
    for _id, item in data.items.items():
        keys = [
            item.description,
            item.item_description_prefab,
            item.item_name,
            item.item_name_prefab,
        ]

        if item.tag:
            keys += [item.tag.group_text, item.tag.text]

        for key in keys:
            assert is_valid_key(key), f"key {key} not valid in items.{_id}"
