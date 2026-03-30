"""Finnish language definition (Latin + umlauts, agglutinative morphology).

Suffixes are ordered longest-first.  Finnish is highly agglutinative so
longer case suffixes must be tried before shorter ones.
"""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="fi",
    script_pattern=r"[a-zA-ZäöÄÖ]",
    suffixes=(
        # 8-char
        "lliseksi",
        # 7-char
        "llisiin",
        "llisten",
        # 6-char
        "llinen",
        "llisia",
        "lliset",
        # 5-char
        "linen",
        "isten",
        # 4-char
        "inen",
        "ista",
        "istä",
        "issa",
        "issä",
        "ille",
        "ilta",
        "iltä",
        "iksi",
        # 3-char
        "lla",
        "llä",
        "lta",
        "ltä",
        "lle",
        "ssa",
        "ssä",
        "sta",
        "stä",
        "ksi",
        # 2-char
        "na",
        "nä",
        "ta",
        "tä",
        "en",
        "in",
    ),
    min_stem=4,
)
