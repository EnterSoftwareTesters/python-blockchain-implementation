from __future__ import annotations
import hashlib
from typing import Any
from datetime import datetime


class Block:
    def __init__(self, data: Any, prev_hash: hashlib._Hash) -> None:
        self.hash: hashlib._Hash | None = None
        self.prev_hash: hashlib._Hash = prev_hash
        self.nonce = 0
        self.data = data
        self.created_at = datetime.now()

    def mine(self, difficulty: int) -> None:
        difficulty_constraint = 2 ** (256 - difficulty)
        self.hash = hashlib.sha256(str(self).encode("utf-8"))
        while int(self.hash.hexdigest(), 16) > difficulty_constraint:
            self.nonce += 1
            self.hash = hashlib.sha256(str(self).encode("utf-8"))

    def __str__(self) -> str:
        return f"{self.prev_hash.hexdigest()}{self.nonce}{self.data}{self.created_at}"
