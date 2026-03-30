"""ai-knot — Agent Knowledge Layer. Extract. Store. Retrieve. Any backend."""

from __future__ import annotations

from ai_knot.knowledge import KnowledgeBase
from ai_knot.languages import LanguageDef
from ai_knot.types import ConversationTurn, Fact, MemoryType, SnapshotDiff

__version__ = "0.6.0"

__all__ = [
    "ConversationTurn",
    "Fact",
    "KnowledgeBase",
    "LanguageDef",
    "MemoryType",
    "SnapshotDiff",
    "__version__",
]
