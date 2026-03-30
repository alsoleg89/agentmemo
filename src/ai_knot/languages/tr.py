"""Turkish language definition (Latin + special chars, agglutinative morphology)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="tr",
    script_pattern=r"[a-zA-ZçğıöşüÇĞIÖŞÜ]",
    suffixes=(
        # 6-char
        "lardan",
        "lerden",
        "laştır",
        "leştir",
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
        "ışın",
        # 3-char
        "lar",
        "ler",
        "lik",
        "lık",
        "lük",
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
