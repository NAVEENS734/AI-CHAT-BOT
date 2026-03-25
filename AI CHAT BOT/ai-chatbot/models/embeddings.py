"""Optional embeddings helper placeholder."""

from __future__ import annotations

from typing import List


def embed_text(text: str) -> List[float]:
    """Return a tiny deterministic placeholder embedding."""
    base = sum(ord(char) for char in text)
    return [float((base + offset) % 1000) / 1000.0 for offset in range(8)]

