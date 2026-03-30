"""Japanese language definition (Hiragana/Katakana/Kanji, light suffix list)."""

from ai_knot.languages._lang import LanguageDef

# Japanese is primarily analytic/agglutinative but common verb/adjective
# conjugation endings (hiragana) can be stripped for a basic normalisation.
# Full morphological analysis would require a dedicated library (e.g. MeCab).
LANGUAGE = LanguageDef(
    code="ja",
    script_pattern=r"[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]",
    suffixes=(
        # 4-char
        "られる",
        "させる",
        "された",
        # 3-char
        "している",
        "される",
        "する",
        "した",
        "して",
        # 2-char
        "ます",
        "ません",
        "ました",
        "です",
        "でした",
        "たい",
        "ない",
    ),
    min_stem=2,
)
