"""Spanish language definition (Latin + diacritics, medium inflection)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="es",
    script_pattern=r"[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]",
    suffixes=(
        # 7-char+
        "amiento",
        "imientos",
        "aciones",
        "idades",
        # 6-char
        "amente",
        "imiento",
        # 5-char
        "ación",
        "iones",
        "mente",
        "istas",
        "iendo",
        "acion",
        # 4-char
        "ando",
        "ados",
        "adas",
        "osos",
        "osas",
        "ismo",
        "ista",
        "idad",
        "ción",
        "cion",
        # 3-char
        "ado",
        "ada",
        "oso",
        "osa",
        "ero",
        "era",
        "ión",
        "ion",
        "mos",
        "ron",
        "ban",
        # 2-char
        "ar",
        "er",
        "ir",
        "as",
        "os",
        "es",
    ),
    min_stem=4,
)
