"""Arabic language definition (Arabic script, suffix-only stripping)."""

from ai_knot.languages._lang import LanguageDef

# Arabic has root-and-pattern morphology which cannot be handled by simple
# suffix stripping.  This definition strips common case/number suffixes and
# definite article clitics, giving a partial normalisation without any
# new dependencies.
LANGUAGE = LanguageDef(
    code="ar",
    script_pattern=r"[\u0600-\u06FF]",
    suffixes=(
        # Feminine dual / plural
        "تان",
        "تين",
        "ات",
        # Masculine sound plural
        "ون",
        "ين",
        # Dual
        "ان",
        # Possessive/object suffixes
        "ها",
        "هم",
        "هن",
        "كم",
        "كن",
        "نا",
        # Nisba adjective
        "ية",
        "ي",
    ),
    min_stem=3,
)
