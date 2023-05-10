from __future__ import annotations
from hashlib import _Hash, sha256
from typing import Any


class Block:
    def __init__(self, data: Any, prev_hash: _Hash) -> None:
        self.hash: _Hash | None = None
        self.prev_hash: _Hash = prev_hash
        self.nonce = 0
        self.data = data

    def mine(self, difficulty) -> None:
        difficulty_constraint = 2 ** (256 - difficulty)
        self.hash = sha256(str(self).encode("utf-8"))
        while int(self.hash.hexdigest(), 16) > difficulty_constraint:
            self.nonce += 1
            self.hash = sha256(str(self).encode("utf-8"))

    def __str__(self) -> str:
        return f"{self.prev_hash.hexdigest()}{self.nonce}{self.data}"
