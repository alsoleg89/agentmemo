"""Built-in language definitions and registry for morphological tokenisation.

Usage::

    from ai_knot.languages import get_languages, register
    from ai_knot.languages import LanguageDef

    # Use a subset of built-ins
    langs = get_languages(["en", "ru"])

    # Register a custom language
    DE = LanguageDef(code="de", script_pattern=r"[a-zA-ZäöüÄÖÜß]", suffixes=("ung",), min_stem=4)
    register(DE)
    langs = get_languages(["en", "ru", "de"])

Built-in codes: en, ru, de, fr, es, it, pt, uk, pl, tr, ar, el, fi, zh, ja
"""

from __future__ import annotations

from collections.abc import Sequence

from ai_knot.languages._lang import LanguageDef

# ── Registry ──────────────────────────────────────────────────────────────────

_REGISTRY: dict[str, LanguageDef] = {}


def register(lang: LanguageDef) -> None:
    """Register a language definition under its ISO code.

    Overwrites any existing definition with the same code.
    """
    _REGISTRY[lang.code] = lang


def get_languages(codes: Sequence[str]) -> tuple[LanguageDef, ...]:
    """Resolve a list of ISO 639-1 codes to LanguageDef objects.

    Args:
        codes: Language codes to look up (e.g. ``["en", "ru"]``).

    Returns:
        Tuple of :class:`LanguageDef` objects in the same order as *codes*.

    Raises:
        ValueError: If any code is not in the registry.
    """
    missing = [c for c in codes if c not in _REGISTRY]
    if missing:
        available = sorted(_REGISTRY)
        raise ValueError(f"Unknown language codes: {missing!r}. Available: {available}")
    return tuple(_REGISTRY[c] for c in codes)


# ── Auto-register built-ins ───────────────────────────────────────────────────
# Imported after the registry helpers are defined to avoid NameError.

from ai_knot.languages.ar import LANGUAGE as _AR  # noqa: E402
from ai_knot.languages.de import LANGUAGE as _DE  # noqa: E402
from ai_knot.languages.el import LANGUAGE as _EL  # noqa: E402
from ai_knot.languages.en import LANGUAGE as _EN  # noqa: E402
from ai_knot.languages.es import LANGUAGE as _ES  # noqa: E402
from ai_knot.languages.fi import LANGUAGE as _FI  # noqa: E402
from ai_knot.languages.fr import LANGUAGE as _FR  # noqa: E402
from ai_knot.languages.it import LANGUAGE as _IT  # noqa: E402
from ai_knot.languages.ja import LANGUAGE as _JA  # noqa: E402
from ai_knot.languages.pl import LANGUAGE as _PL  # noqa: E402
from ai_knot.languages.pt import LANGUAGE as _PT  # noqa: E402
from ai_knot.languages.ru import LANGUAGE as _RU  # noqa: E402
from ai_knot.languages.tr import LANGUAGE as _TR  # noqa: E402
from ai_knot.languages.uk import LANGUAGE as _UK  # noqa: E402
from ai_knot.languages.zh import LANGUAGE as _ZH  # noqa: E402

for _lang in (_EN, _RU, _DE, _FR, _ES, _IT, _PT, _UK, _PL, _TR, _AR, _EL, _FI, _ZH, _JA):
    register(_lang)

# Default: all built-in languages.
# When no languages are specified, the tokeniser covers every language
# whose definition ships with ai-knot.  Script detection is per-token, so
# including extra languages has no negative effect on tokens that do not
# match their script patterns.
DEFAULT_LANGUAGES: tuple[LanguageDef, ...] = (
    _EN,
    _RU,
    _DE,
    _FR,
    _ES,
    _IT,
    _PT,
    _UK,
    _PL,
    _TR,
    _AR,
    _EL,
    _FI,
    _ZH,
    _JA,
)

__all__ = [
    "DEFAULT_LANGUAGES",
    "LanguageDef",
    "get_languages",
    "register",
]
