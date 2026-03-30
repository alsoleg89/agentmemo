"""LanguageDef — morphological descriptor for a single natural language."""

from __future__ import annotations

import warnings
from dataclasses import dataclass, field


@dataclass(frozen=True)
class LanguageDef:
    """Morphological descriptor for one natural language.

    Fields:
        code: ISO 639-1 language code (e.g. ``"en"``, ``"ru"``).
        script_pattern: Regex that matches at least one character of this
            language's script.  Used per-token to decide which language's
            suffix/prefix tables to apply.
        suffixes: Inflectional suffixes to strip, ordered **longest-first**.
            Longest-first ordering prevents partial stripping (e.g.
            ``"ований"`` must be tried before ``"ий"``).
        prefixes: Inflectional or derivational prefixes to strip after suffix
            stripping, ordered **longest-first**.  Mainly useful for Arabic
            (definite article ال and preposition clitics و، ب، ل، ف).
        min_stem: Minimum stem length after stripping.  Prevents
            over-stemming short words.  Default 4.
    """

    code: str
    script_pattern: str
    suffixes: tuple[str, ...] = field(default_factory=tuple)
    prefixes: tuple[str, ...] = field(default_factory=tuple)
    min_stem: int = 4

    def __post_init__(self) -> None:
        # Warn (not raise) when suffixes are not longest-first.
        # This is a data quality check — wrong ordering silently degrades quality.
        for i in range(len(self.suffixes) - 1):
            if len(self.suffixes[i]) < len(self.suffixes[i + 1]):
                warnings.warn(
                    f"LanguageDef({self.code!r}): suffix {self.suffixes[i]!r} "
                    f"is shorter than {self.suffixes[i + 1]!r}. "
                    "Suffixes must be longest-first for correct stripping.",
                    stacklevel=2,
                )
                break
        for i in range(len(self.prefixes) - 1):
            if len(self.prefixes[i]) < len(self.prefixes[i + 1]):
                warnings.warn(
                    f"LanguageDef({self.code!r}): prefix {self.prefixes[i]!r} "
                    f"is shorter than {self.prefixes[i + 1]!r}. "
                    "Prefixes must be longest-first for correct stripping.",
                    stacklevel=2,
                )
                break
