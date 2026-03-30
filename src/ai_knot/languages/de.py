"""German language definition (Latin + umlauts, inflectional morphology)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="de",
    script_pattern=r"[a-zA-ZäöüÄÖÜß]",
    suffixes=(
        # 8-char+
        "ierungen",
        "isierung",
        "schaften",
        # 6-char
        "ierung",
        "lichen",
        "licher",
        "liches",
        "ischen",
        "ischer",
        "isiert",
        # 5-char
        "schaft",
        "heiten",
        "keiten",
        "ungen",
        "isten",
        "ismus",
        # 4-char
        "heit",
        "keit",
        "lich",
        "isch",
        "sten",
        "erns",
        "ern",
        "ung",
        # 3-char
        "est",
        "ste",
        "ers",
        "ens",
        # 2-char
        "en",
        "er",
        "em",
        "es",
        "st",
        # 1-char
        "e",
        "s",
    ),
    min_stem=4,
)
