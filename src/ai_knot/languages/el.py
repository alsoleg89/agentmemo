"""Greek language definition (Greek script, medium inflection)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="el",
    script_pattern=r"[\u0370-\u03FF\u1F00-\u1FFF]",
    suffixes=(
        # 5-char
        "ωντας",
        "οντας",
        "ήσεις",
        "ήσεων",
        "ότητα",
        # 4-char
        "ματα",
        "σεων",
        "τητα",
        "ικός",
        "ικές",
        "ικών",
        "ικού",
        # 3-char
        "ους",
        "ών",
        "εις",
        "ική",
        "ικό",
        "ησε",
        # 2-char
        "ος",
        "ης",
        "ες",
        "ας",
        "ων",
        "ει",
        "ου",
        "οι",
    ),
    min_stem=4,
)
