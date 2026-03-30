"""English language definition."""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="en",
    script_pattern=r"[a-zA-Z]",
    suffixes=("s",),
    min_stem=3,
)
