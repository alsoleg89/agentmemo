"""Chinese language definition (CJK script, analytic — no inflection)."""

from ai_knot.languages._lang import LanguageDef

# Mandarin Chinese is an analytic language with no inflectional morphology.
# The language definition provides script detection only; each CJK character
# is already a morpheme, so no suffix stripping is needed.
LANGUAGE = LanguageDef(
    code="zh",
    script_pattern=r"[\u4E00-\u9FFF\u3400-\u4DBF\uF900-\uFAFF]",
    suffixes=(),
    min_stem=1,
)
