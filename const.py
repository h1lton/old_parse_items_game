import re

BASE_URL = "https://raw.githubusercontent.com/SteamDatabase/GameTracking-CS2/master/game/csgo/pak01_dir"


regex_skin_id = re.compile(
    r"econ/default_generated/(.*?)_light", re.IGNORECASE
)

weapon_names = [
    "weapon_taser",
    "weapon_deagle",
    "weapon_elite",
    "weapon_fiveseven",
    "weapon_glock",
    "weapon_ak47",
    "weapon_aug",
    "weapon_awp",
    "weapon_famas",
    "weapon_g3sg1",
    "weapon_galilar",
    "weapon_m249",
    "weapon_mac10",
    "weapon_p90",
    "weapon_mp5sd",
    "weapon_ump45",
    "weapon_xm1014",
    "weapon_bizon",
    "weapon_mag7",
    "weapon_negev",
    "weapon_sawedoff",
    "weapon_tec9",
    "weapon_hkp2000",
    "weapon_mp7",
    "weapon_mp9",
    "weapon_nova",
    "weapon_p250",
    "weapon_scar20",
    "weapon_sg556",
    "weapon_ssg08",
    "weapon_m4a1_silencer",
    "weapon_m4a1",
    "weapon_usp_silencer",
    "weapon_cz75a",
    "weapon_revolver",
    "weapon_bayonet",
    "weapon_knife_css",
    "weapon_knife_flip",
    "weapon_knife_gut",
    "weapon_knife_karambit",
    "weapon_knife_m9_bayonet",
    "weapon_knife_tactical",
    "weapon_knife_falchion",
    "weapon_knife_survival_bowie",
    "weapon_knife_butterfly",
    "weapon_knife_push",
    "weapon_knife_cord",
    "weapon_knife_canis",
    "weapon_knife_ursus",
    "weapon_knife_gypsy_jackknife",
    "weapon_knife_outdoor",
    "weapon_knife_stiletto",
    "weapon_knife_widowmaker",
    "weapon_knife_skeleton",
    "weapon_knife_kukri",
    "studded_bloodhound_gloves",
    "studded_brokenfang_gloves",
    "sporty_gloves",
    "slick_gloves",
    "leather_handwraps",
    "motorcycle_gloves",
    "specialist_gloves",
    "studded_hydra_gloves",
]

doppler_phases = {
    # Doppler
    415: "Ruby",
    416: "Sapphire",
    417: "Black Pearl",
    418: "Phase 1",
    419: "Phase 2",
    420: "Phase 3",
    421: "Phase 4",
    # Gamma Doppler
    568: "Emerald",
    569: "Phase 1",
    570: "Phase 2",
    571: "Phase 3",
    572: "Phase 4",
    # Doppler (Butterfly Knife, Shadow Daggers)
    617: "Black Pearl",
    618: "Phase 2",
    619: "Sapphire",
    # Doppler (Talon Knife)
    852: "Phase 1",
    853: "Phase 2",
    854: "Phase 3",
    855: "Phase 4",
    # Gamma Doppler (Glock-18)
    1119: "Emerald",
    1120: "Phase 1",
    1121: "Phase 2",
    1122: "Phase 3",
    1123: "Phase 4",
}