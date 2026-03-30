"""Portuguese language definition (Latin + diacritics, medium inflection)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="pt",
    script_pattern=r"[a-zA-ZàáâãçéêíóôõúüÀÁÂÃÇÉÊÍÓÔÕÚÜ]",
    suffixes=(
        # 7-char
        "amento",
        "amentos",
        # 6-char
        "amente",
        "imento",
        "idades",
        # 5-char
        "mente",
        "ções",
        "ismo",
        "ista",
        # 4-char
        "ção",
        "cao",
        "ados",
        "adas",
        "osos",
        "osas",
        "ando",
        "endo",
        # 3-char
        "ado",
        "ada",
        "oso",
        "osa",
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
