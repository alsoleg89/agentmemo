"""Language registry and shared morphological tokenizer.

The ``tokenize()`` function is the single implementation used by both the
retriever (TF-IDF search) and the extractor (cosine deduplication).
Using the same tokenizer in both places ensures that morphological
normalization is consistent: if "маркетингового" and "маркетинга" are
treated as the same stem during retrieval, they will also be deduplicated
correctly.

Usage::

    from ai_knot.languages import DEFAULT_LANGUAGES, tokenize, get_languages

    tokens = tokenize("маркетингового контент Python", DEFAULT_LANGUAGES)
    # → ["маркетинг", "контент", "python"]

    # Restrict to a single language
    ru_only = get_languages(["ru"])
    tokens = tokenize("маркетингового контент", ru_only)

    # Register a custom language
    from ai_knot.languages import register
    from ai_knot.languages._lang import LanguageDef
    register(LanguageDef(code="kk", script_pattern=r"[\u0400-\u04FF]", suffixes=("дың",), min_stem=4))
    langs = get_languages(["kk", "ru"])

Built-in codes: en, ru, de, fr, es, it, pt, uk, pl, tr, ar, el, fi, zh, ja
"""

from __future__ import annotations

import re
import unicodedata
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
        ValueError: If any code is not registered.
    """
    missing = [c for c in codes if c not in _REGISTRY]
    if missing:
        available = sorted(_REGISTRY)
        raise ValueError(f"Unknown language codes: {missing!r}. Available: {available}")
    return tuple(_REGISTRY[c] for c in codes)


# ── Shared tokenizer ───────────────────────────────────────────────────────────

def tokenize(text: str, langs: tuple[LanguageDef, ...] = ()) -> list[str]:
    """Morphological tokenizer shared by retrieval and deduplication.

    For each token the function checks every configured :class:`LanguageDef`
    in order.  The first language whose ``script_pattern`` matches the token
    wins.  Its suffix table is applied (longest-first) keeping a stem of at
    least ``min_stem`` characters; then prefix stripping is attempted on the
    resulting stem.  Tokens that match no language pass through unchanged
    (e.g. numbers, punctuation fragments).

    Additional pre-processing:
    - Unicode NFC normalization — ``é`` (decomposed) becomes ``é`` (composed)
      so diacritic handling is consistent across platforms.
    - CamelCase splitting — ``FastAPI`` → ``fast api`` before tokenization.
    - All tokens are lowercased.

    Args:
        text: Input string (any language / script mix).
        langs: Language definitions to apply.  Pass :data:`DEFAULT_LANGUAGES`
            for the default set or an empty tuple to disable stemming entirely.

    Returns:
        List of lowercase, morphologically normalized tokens.
    """
    # Normalize Unicode to composed form (NFC) before any other processing.
    text = unicodedata.normalize("NFC", text)
    # Split camelCase: "FastAPI" → "Fast API"
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    # Extract tokens: Unicode letters and digits, excluding underscores.
    raw_tokens = re.findall(r"[^\W_]+", text.lower())

    result: list[str] = []
    for t in raw_tokens:
        matched = False
        for lang in langs:
            if re.search(lang.script_pattern, t):
                # Suffix stripping
                stem = t
                for suffix in lang.suffixes:
                    if t.endswith(suffix) and len(t) - len(suffix) >= lang.min_stem:
                        stem = t[: -len(suffix)]
                        break
                # Prefix stripping on the resulting stem
                for prefix in lang.prefixes:
                    if stem.startswith(prefix) and len(stem) - len(prefix) >= lang.min_stem:
                        stem = stem[len(prefix):]
                        break
                result.append(stem)
                matched = True
                break
        if not matched:
            result.append(t)
    return result


# ── Auto-register built-ins ───────────────────────────────────────────────────
# Imported after registry helpers are defined to avoid NameError.

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

# Default: all 15 built-in languages.
# Script detection is per-token so including extra languages adds no cost
# for tokens that do not match their script patterns.
DEFAULT_LANGUAGES: tuple[LanguageDef, ...] = (
    _EN, _RU, _DE, _FR, _ES, _IT, _PT, _UK, _PL, _TR, _AR, _EL, _FI, _ZH, _JA
)

__all__ = [
    "DEFAULT_LANGUAGES",
    "LanguageDef",
    "get_languages",
    "register",
    "tokenize",
]
