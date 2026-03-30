"""Polish language definition (Latin + diacritics, heavy inflection)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="pl",
    script_pattern=r"[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]",
    suffixes=(
        # 7-char+
        "owania",
        "owanie",
        "ościach",
        # 5-char
        "ności",
        "owego",
        "owych",
        "ować",
        # 4-char
        "ości",
        "owej",
        "owym",
        "owie",
        "ować",
        # 3-char
        "ach",
        "ami",
        "owi",
        "iem",
        "owy",
        "owa",
        "owe",
        # 2-char
        "ów",
        "om",
        "ie",
        "ią",
        "ię",
    ),
    min_stem=4,
)
