"""French language definition (Latin + diacritics, light inflection)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="fr",
    script_pattern=r"[a-zA-ZàâäéèêëîïôùûüÿçÀÂÄÉÈÊËÎÏÔÙÛÜŸÇ]",
    suffixes=(
        # 8-char+
        "issement",
        "issements",
        # 6-char
        "ements",
        "ations",
        "ateurs",
        "atrice",
        "iences",
        "issant",
        # 5-char
        "ement",
        "ation",
        "ateur",
        "ience",
        "ances",
        "ences",
        "ibles",
        "ables",
        "isant",
        # 4-char
        "ance",
        "ence",
        "able",
        "ible",
        "ment",
        "tion",
        "sion",
        "isme",
        "iste",
        # 3-char
        "aux",
        "eux",
        "ant",
        "ent",
        "ait",
        # 2-char
        "es",
        "er",
        "ez",
        # 1-char
        "s",
        "e",
    ),
    min_stem=4,
)
