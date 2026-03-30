"""Japanese language definition (Hiragana/Katakana/Kanji, light suffix list).

Japanese is primarily analytic/agglutinative.  Common verb/adjective endings
(hiragana) can be stripped for a basic normalisation.  Full morphological
analysis requires a dedicated library such as MeCab or Fugashi.
"""

from ai_knot.languages._lang import LanguageDef

LANGUAGE = LanguageDef(
    code="ja",
    script_pattern=r"[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]",
    suffixes=(
        # 5-char (hiragana — each kana = 1 char but longer match first)
        "している",
        # 4-char
        "られる",
        "させる",
        "された",
        # 3-char
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
