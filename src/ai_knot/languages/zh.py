"""Chinese language definition (CJK script, analytic — no inflection).

Mandarin Chinese has no inflectional morphology.  Each CJK character is
already a morpheme, so the suffix table is empty.  Script detection is
still useful to route tokens through the correct code path.
"""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="zh",
    script_pattern=r"[\u4E00-\u9FFF\u3400-\u4DBF\uF900-\uFAFF]",
    suffixes=(),
    min_stem=1,
)
