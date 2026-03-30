"""Russian language definition (Cyrillic script, heavy inflection).

Suffixes are ordered longest-first and deduplicated.
"""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="ru",
    script_pattern=r"[\u0400-\u04FF]",
    suffixes=(
        # 8-char
        "овского",
        "овскому",
        "овским",
        "ального",
        "альному",
        "альным",
        "ованием",
        "ованию",
        "овании",
        # 7-char
        "ировать",
        "ируется",
        # 6-char
        "ующего",
        "ующему",
        "ующим",
        "ование",
        "ировал",
        "ировала",
        # 5-char
        "ского",
        "скому",
        "ским",
        "ового",
        "овому",
        "овым",
        "ность",
        "ности",
        "ально",
        "альной",
        # 4-char
        "овать",
        "ующий",
        "ующая",
        "ующее",
        "ующих",
        # 3-char
        "ого",
        "его",
        "ому",
        "ему",
        "ами",
        "ями",
        "ков",
        "ием",
        # 2-char
        "ый",
        "ий",
        "ой",
        "ых",
        "их",
        "ов",
        "ев",
        "ах",
        "ях",
        "ам",
        "ем",
        "им",
        "ом",
    ),
    min_stem=4,
)
