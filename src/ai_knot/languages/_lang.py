"""LanguageDef — data descriptor for a single natural language."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class LanguageDef:
    """Morphological descriptor for one natural language.

    Fields:
        code: ISO 639-1 language code (e.g. ``"en"``, ``"ru"``).
        script_pattern: Regex that matches at least one character of this
            language's script.  Used per-token to decide which language's
            suffix table to apply.
        suffixes: Inflectional suffixes to strip, ordered **longest-first**.
            Longest-first ordering prevents partial stripping (e.g.
            ``"ований"`` must be tried before ``"ий"``).
        min_stem: Minimum stem length after stripping.  Prevents
            over-stemming short words.  Default 4.
    """

    code: str
    script_pattern: str
    suffixes: tuple[str, ...] = field(default_factory=tuple)
    min_stem: int = 4
