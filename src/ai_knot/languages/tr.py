"""Turkish language definition (Latin + special chars, agglutinative morphology)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="tr",
    script_pattern=r"[a-zA-ZçğıöşüÇĞIÖŞÜ]",
    suffixes=(
        # 8-char+
        "leştirilmekte",
        "leştirilmiş",
        # 6-char
        "laştır",
        "leştir",
        "lardan",
        "lerden",
        # 5-char
        "larla",
        "lerle",
        "larda",
        "lerde",
        "ların",
        "lerin",
        # 4-char
        "ları",
        "leri",
        "lara",
        "lere",
        "ları",
        "leri",
        "ışın",
        # 3-char
        "lar",
        "ler",
        "lik",
        "lık",
        "lük",
        "lug",
        "dan",
        "den",
        "tan",
        "ten",
        # 2-char
        "da",
        "de",
        "ta",
        "te",
        "ya",
        "ye",
        "in",
        "ın",
        "ün",
        "un",
    ),
    min_stem=4,
)
