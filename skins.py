import re

from const import regex_skin_id, weapon_names, doppler_phases
from schemas import Data, Skin


def get_weapon_and_pattern(icon_path: str) -> [str, str]:
    skin_id = regex_skin_id.match(icon_path).group(1)

    for weapon in weapon_names:
        if skin_id.startswith(weapon):
            pattern = skin_id[(len(weapon) + 1) :].lower()
            return weapon, pattern


def is_knife(weapon: str) -> bool:
    return weapon.startswith("weapon_knife") or weapon.startswith(
        "weapon_bayonet"
    )


def is_not_weapon(weapon: str) -> bool:
    """Возвращает True если перчатки или нож, False если оружие"""
    return not weapon.startswith("weapon_") or is_knife(weapon)


def get_skin(key: str, icon_path: str, data: Data):
    weapon, pattern = get_weapon_and_pattern(icon_path)
    item = data.items[weapon]
    _is_not_weapon = is_not_weapon(weapon)
    name = item.item_name if _is_not_weapon else item.item_name_prefab
    description = (
        item.item_description
        if _is_not_weapon
        else item.item_description_prefab
    )

    _is_knife = is_knife(weapon)

    stat_trak = _is_knife or bool(
        data.stat_trak_skins.get(f"[{pattern}]{weapon}")
    )

    doppler_phase = doppler_phases.get(
        data.paint_kits[pattern]["paint_index"]
    )  # TODO: create load_paint_kits

    rarity = (  # TODO: create load_rarities
        f"rarity_{data.rarities[f'[{pattern}]{weapon}'].rarity}_weapon"
        if not _is_not_weapon
        else "rarity_ancient_weapon" if _is_knife else "rarity_ancient"
    )

    team = (
        "both"
        if not item.used_by_classes or len(item.used_by_classes) == 2
        else item.used_by_classes[0]
    )

    return Skin(
        id=key,
        name=name,
        description=description,
        weapon=weapon,
        stat_trak=stat_trak,
        pattern=pattern,
        rarity=rarity,
        team=team,
    )


def get_skins(data: Data, items_game: dict) -> list[Skin]:
    skins = []

    for key, value in items_game["alternate_icons2"]["weapon_icons"].items():
        icon_path: str = value["icon_path"]

        if icon_path.endswith("_light"):
            skins.append(get_skin(key, icon_path, data))

    return skins
