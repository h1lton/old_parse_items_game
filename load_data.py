import os.path

import vdf

from download_data import download_translation
from schemas import Data, Item, Prefab, Languages


def load_items_game() -> dict:
    with open("items_game.txt") as f:
        data = vdf.load(f)
    return data["items_game"]


def load_translation(language: Languages | str = Languages.english) -> dict:
    if isinstance(language, str):
        language = Languages(language)

    file_name = f"{language}.translation"

    if not os.path.exists(file_name):
        download_translation(language)

    with open(file_name, encoding="utf-8") as vdf_file:
        translation: dict[str, any] = vdf.load(vdf_file)["lang"]["Tokens"]

    for key in list(translation.keys()):
        translation[key.lower()] = translation.pop(key)

    return translation


def load_prefabs(data: Data, items_game: dict):
    for key, prefab in items_game["prefabs"].items():
        inner_prefab: dict = items_game["prefabs"].get(prefab.get("prefab"))

        def get_value(_key: str):
            if inner_prefab:
                return prefab.get(_key) or inner_prefab.get(_key)
            return prefab.get(_key)

        data.prefabs[key] = Prefab(
            item_name=get_value("item_name"),
            item_description=get_value("item_description"),
            first_sale_date=get_value("first_sale_date"),
            prefab=prefab.get("prefab"),
            used_by_classes=prefab.get("used_by_classes"),
        )


def load_items(data: Data, items_game: dict):
    for key, item in items_game["items"].items():
        prefab = data.prefabs.get(item.get("prefab"))

        tags: dict = item.get("tags")
        tag = next(tags.values().__iter__()) if tags else None

        data.items[item["name"]] = Item(
            object_id=key,
            item_name=item.get("item_name"),
            description=item.get("item_description"),
            tag=tag,
            item_name_prefab=prefab.item_name if prefab else None,
            item_description_prefab=(
                prefab.item_description if prefab else None
            ),
            used_by_classes=(
                item.get("used_by_classes") or prefab.used_by_classes
                if prefab
                else item.get("used_by_classes")
            ),
        )


def load_item_sets(data: Data, items_game: dict):
    data.item_sets = items_game["item_sets"]


def load_stat_trak_skins(data: Data):
    crates = {}

    for item in data.items.values():
        if item.prefab == "weapon_case":
            if item.tag:
                name = item.tag.value
                crates[name] = True

    data.stat_trak_skins = {
        "[cu_m4a1_howling]weapon_m4a1": True,
    }

    for item in data.item_sets:
        if item["is_collection"] and item["name"] != "#CSGO_set_dust_2_2021":
            for key in item["items"].keys():
                if crates.get(item["name"].replace("#CSGO_", "")):
                    data.stat_trak_skins[key.lower()] = True


def load_data():
    items_game = load_items_game()
    data = Data()

    load_prefabs(data, items_game)
    load_items(data, items_game)

    return data
