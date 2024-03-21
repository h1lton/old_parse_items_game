from load_data import load_data, load_translation
from skins import get_skins
from schemas import Languages

# keys_in_tags = {"tag_group", "tag_value", "tag_text", "tag_group_text"}


if __name__ == "__main__":
    data = load_data()
    translation = load_translation(Languages.russian)
