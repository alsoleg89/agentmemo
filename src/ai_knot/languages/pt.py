"""Portuguese language definition (Latin + diacritics, medium inflection)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="pt",
    script_pattern=r"[a-zA-ZàáâãçéêíóôõúüÀÁÂÃÇÉÊÍÓÔÕÚÜ]",
    suffixes=(
        # 7-char+
        "amento",
        "amentos",
        "idades",
        # 6-char
        "amente",
        "imento",
        # 5-char
        "mente",
        "ando",
        "endo",
        "ismo",
        "ista",
        "ções",
        # 4-char
        "ção",
        "ados",
        "adas",
        "osos",
        "osas",
        "cao",
        # 3-char
        "ado",
        "ada",
        "oso",
        "osa",
        "ção",
        "mos",
        "ram",
        "iam",
        # 2-char
        "ar",
        "er",
        "ir",
        "as",
        "os",
        "em",
    ),
    min_stem=4,
)
