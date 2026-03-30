"""Arabic language definition (Arabic script).

Arabic uses root-and-pattern morphology which cannot be fully handled by
simple suffix stripping.  This definition strips common case/number suffixes
and definite article + preposition clitics (prefixes), giving a practical
partial normalisation without additional dependencies.
"""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="ar",
    script_pattern=r"[\u0600-\u06FF]",
    suffixes=(
        # Feminine dual / plural — longest first
        "تان",
        "تين",
        # Masculine sound plural
        "ون",
        "ين",
        # Dual
        "ان",
        # Possessive / object suffixes
        "ها",
        "هم",
        "هن",
        "كم",
        "كن",
        "نا",
        # Nisba adjective
        "ية",
        # Feminine marker
        "ة",
        # Common case endings
        "ي",
    ),
    prefixes=(
        # Definite article + preposition combinations (longest first)
        "وال",
        "بال",
        "كال",
        "فال",
        # Definite article alone
        "ال",
        # Preposition clitics
        "و",
        "ب",
        "ل",
        "ف",
    ),
    min_stem=3,
)
