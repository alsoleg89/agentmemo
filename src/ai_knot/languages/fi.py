"""Finnish language definition (Latin + umlauts, agglutinative morphology)."""

from ai_knot.languages._lang import LanguageDef

# Finnish is highly agglutinative — suffixes can chain.  Longest-first ordering
# ensures the most specific (longest) suffix is matched first, giving a
# reasonable approximation without a full morphological analyser.
LANGUAGE = LanguageDef(
    code="fi",
    script_pattern=r"[a-zA-ZäöÄÖ]",
    suffixes=(
        # 8-char+
        "llisiin",
        "llisten",
        "lliseksi",
        # 6-char
        "llinen",
        "llisia",
        "lliset",
        # 5-char
        "linen",
        "isten",
        "isten",
        "iksi",
        # 4-char
        "inen",
        "ista",
        "istä",
        "issa",
        "issä",
        "ille",
        "ilta",
        "iltä",
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
