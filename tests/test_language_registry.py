"""Tests for the language registry and LanguageDef."""

from __future__ import annotations

import pytest

from ai_knot.languages import DEFAULT_LANGUAGES, LanguageDef, get_languages, register
from ai_knot.languages.en import LANGUAGE as EN
from ai_knot.languages.ru import LANGUAGE as RU


class TestLanguageDef:
    def test_frozen(self) -> None:
        lang = LanguageDef(code="xx", script_pattern=r"[a-z]", suffixes=("s",), min_stem=3)
        with pytest.raises((AttributeError, TypeError)):
            lang.code = "yy"  # type: ignore[misc]

    def test_hashable(self) -> None:
        lang = LanguageDef(code="xx", script_pattern=r"[a-z]", suffixes=("s",), min_stem=3)
        assert hash(lang) is not None
        assert {lang, lang} == {lang}

    def test_default_min_stem(self) -> None:
        lang = LanguageDef(code="xx", script_pattern=r"[a-z]", suffixes=())
        assert lang.min_stem == 4

    def test_default_suffixes_empty(self) -> None:
        lang = LanguageDef(code="xx", script_pattern=r"[a-z]")
        assert lang.suffixes == ()


class TestRegistry:
    def test_builtin_codes_present(self) -> None:
        for code in (
            "en",
            "ru",
            "de",
            "fr",
            "es",
            "it",
            "pt",
            "uk",
            "pl",
            "tr",
            "ar",
            "el",
            "fi",
            "zh",
            "ja",
        ):
            langs = get_languages([code])
            assert len(langs) == 1
            assert langs[0].code == code

    def test_get_languages_order_preserved(self) -> None:
        langs = get_languages(["ru", "en"])
        assert langs[0].code == "ru"
        assert langs[1].code == "en"

    def test_unknown_code_raises_valueerror(self) -> None:
        with pytest.raises(ValueError, match="xx"):
            get_languages(["xx"])

    def test_error_message_lists_available(self) -> None:
        with pytest.raises(ValueError, match="en"):
            get_languages(["unknown"])

    def test_empty_list_returns_empty_tuple(self) -> None:
        assert get_languages([]) == ()

    def test_register_custom_language(self) -> None:
        custom = LanguageDef(
            code="test_lang_xyz",
            script_pattern=r"[a-z]",
            suffixes=("ing",),
            min_stem=4,
        )
        register(custom)
        langs = get_languages(["test_lang_xyz"])
        assert langs[0] is custom

    def test_default_languages_includes_all_builtins(self) -> None:
        codes = [lang.code for lang in DEFAULT_LANGUAGES]
        for code in (
            "en",
            "ru",
            "de",
            "fr",
            "es",
            "it",
            "pt",
            "uk",
            "pl",
            "tr",
            "ar",
            "el",
            "fi",
            "zh",
            "ja",
        ):
            assert code in codes

    def test_builtin_en_has_suffix_s(self) -> None:
        assert "s" in EN.suffixes

    def test_builtin_ru_has_suffixes(self) -> None:
        assert len(RU.suffixes) > 10
        assert "ого" in RU.suffixes
