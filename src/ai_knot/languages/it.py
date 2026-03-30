"""Italian language definition (Latin + diacritics, medium inflection)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="it",
    script_pattern=r"[a-zA-ZàèéìíîòóùúÀÈÉÌÍÎÒÓÙÚ]",
    suffixes=(
        # 7-char+
        "amento",
        "amenti",
        "azione",
        "azioni",
        # 5-char
        "mente",
        "ismo",
        "ista",
        "isti",
        "iste",
        # 4-char
        "ando",
        "endo",
        "ato",
        "ata",
        "ati",
        "ate",
        "oso",
        "osa",
        "osi",
        "ose",
        "ità",
        # 3-char
        "ore",
        "ori",
        "are",
        "ere",
        "ire",
        "ivo",
        "iva",
        # 2-char
        "io",
        "ia",
        "ie",
        "si",
        # 1-char
        "o",
        "a",
        "i",
        "e",
    ),
    min_stem=4,
)
