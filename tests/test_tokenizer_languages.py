"""Tests for language-aware tokenisation in TFIDFRetriever._tokenize."""

from __future__ import annotations

import pytest

from ai_knot.languages import DEFAULT_LANGUAGES, LanguageDef, get_languages
from ai_knot.languages.en import LANGUAGE as EN
from ai_knot.languages.ru import LANGUAGE as RU
from ai_knot.retriever import TFIDFRetriever, _tokenize


class TestTokenizeBasic:
    def test_english_plural_stripped(self) -> None:
        tokens = _tokenize("marketing campaigns", (EN,))
        assert "campaign" in tokens

    def test_english_plural_not_stripped_short_word(self) -> None:
        tokens = _tokenize("the bus", (EN,))
        # "bus" has 3 chars — stem would be 2, below min_stem=3 → not stripped
        assert "bus" in tokens

    def test_russian_suffix_stripped(self) -> None:
        # маркетингового (genitive) → strip "ового" → "маркетинг"
        tokens = _tokenize("маркетингового контент", (RU,))
        assert "маркетинг" in tokens

    def test_russian_suffix_not_stripped_below_min_stem(self) -> None:
        # "рот" (3 chars) → stem after stripping would be < 4 → unchanged
        tokens = _tokenize("рот", (RU,))
        assert "рот" in tokens

    def test_camel_case_split(self) -> None:
        tokens = _tokenize("FastAPI endpoint", DEFAULT_LANGUAGES)
        assert "fast" in tokens
        assert "api" in tokens


class TestTokenizeLanguageScope:
    def test_ru_only_english_not_stemmed(self) -> None:
        # With only Russian active, English "campaigns" should NOT be stemmed
        tokens = _tokenize("campaigns", (RU,))
        # "campaigns" contains no Cyrillic → falls through to unmatched → unchanged
        assert "campaigns" in tokens

    def test_en_only_russian_not_stemmed(self) -> None:
        # With only English active, Russian inflected form passes through unchanged
        tokens = _tokenize("маркетинговый", (EN,))
        # No Latin chars → not matched by English → appended as-is
        assert "маркетинговый" in tokens

    def test_empty_langs_no_stemming(self) -> None:
        tokens = _tokenize("campaigns маркетинговый", ())
        assert "campaigns" in tokens
        assert "маркетинговый" in tokens

    def test_both_langs_each_stemmed(self) -> None:
        tokens = _tokenize("campaigns маркетингового", DEFAULT_LANGUAGES)
        assert "campaign" in tokens
        assert "маркетинг" in tokens


class TestKnowledgeBaseLanguagesParam:
    def test_default_includes_all_builtins(self) -> None:
        retriever = TFIDFRetriever()
        # Default is all built-ins — Russian suffix stripping works
        tokens = _tokenize("маркетингового", retriever._langs)
        assert "маркетинг" in tokens

    def test_custom_languages_ru_only(self) -> None:
        retriever = TFIDFRetriever(languages=get_languages(["ru"]))
        # English plural not stripped
        tokens = _tokenize("campaigns", retriever._langs)
        assert "campaigns" in tokens

    def test_custom_languages_empty(self) -> None:
        retriever = TFIDFRetriever(languages=())
        tokens = _tokenize("campaigns маркетинговый", retriever._langs)
        assert "campaigns" in tokens
        assert "маркетинговый" in tokens

    def test_custom_language_register_and_use(self) -> None:
        from ai_knot.languages import register

        de_test = LanguageDef(
            code="_de_test",
            script_pattern=r"[a-zA-ZäöüÄÖÜß]",
            suffixes=("ungen", "ung", "en", "er"),
            min_stem=4,
        )
        register(de_test)
        langs = get_languages(["_de_test"])
        tokens = _tokenize("Einstellungen", langs)
        # "Einstellungen" → strip "ungen" → "Einstell"
        assert "einstell" in tokens


@pytest.mark.parametrize(
    ("code", "word", "expected_stem"),
    [
        ("de", "Einstellungen", "einstell"),       # strip "ungen"
        ("fr", "gouvernements", "gouvern"),         # strip "ements"
        ("es", "configuraciones", "configur"),      # strip "aciones"
        ("it", "configurazione", "configur"),          # strip "azione"
        ("pl", "zakupami", "zakup"),                # strip "ami"
        ("tr", "ayarlardan", "ayar"),               # strip "lardan"
    ],
)
def test_builtin_language_suffix_stripping(code: str, word: str, expected_stem: str) -> None:
    langs = get_languages([code])
    tokens = _tokenize(word, langs)
    assert expected_stem in tokens, (
        f"Expected stem {expected_stem!r} in {tokens} for {word!r} ({code})"
    )
