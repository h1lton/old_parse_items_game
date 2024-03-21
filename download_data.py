import sys
from enum import StrEnum, auto

import requests

from const import BASE_URL
from schemas import Languages


def download_items_game():
    with open("items_game.txt", "wb") as f:
        r = requests.get(f"{BASE_URL}/scripts/items/items_game.txt")
        f.write(r.content)


def download_translation(language: Languages | str):
    if isinstance(language, str):
        language = Languages(language)

    with open(f"{language}.translation", "wb") as f:
        r = requests.get(f"{BASE_URL}/resource/csgo_{language}.txt")
        f.write(r.content)


if __name__ == "__main__":
    err = (
        "Нужно указать флаг -i если хотите загрузить items_game.txt\n"
        "или -l <LANGUAGE> если хотите загрузить локализацию."
    )
    try:
        mode = sys.argv[1]
        match mode:
            case "-i":
                print("downloading items_game.txt...")
                download_items_game()

            case "-l":
                try:
                    language = Languages(sys.argv[2])
                    print(f"downloading {language}.translation...")
                    download_translation(language)

                except IndexError:
                    print("Нужно указать язык -l <LANGUAGE>")

            case default:
                print(err)

    except IndexError:
        print(err)

    print("success")
