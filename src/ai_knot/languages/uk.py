"""Ukrainian language definition (Cyrillic script, inflectional morphology)."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="uk",
    script_pattern=r"[\u0400-\u04FF]",
    suffixes=(
        # 7-char+
        "ального",
        "альному",
        "альними",
        # 6-char
        "ського",
        "ському",
        "альний",
        "альної",
        # 5-char
        "ської",
        "ських",
        "ністю",
        "овими",
        "ового",
        "овому",
        # 4-char
        "ного",
        "ному",
        "ному",
        "ній",
        "ній",
        "ові",
        # 3-char
        "ого",
        "ому",
        "ним",
        "них",
        "ами",
        "ями",
        # 2-char
        "ий",
        "ій",
        "ої",
        "ах",
        "ях",
        "ам",
        "ям",
        "ом",
        "ем",
    ),
    min_stem=4,
)
