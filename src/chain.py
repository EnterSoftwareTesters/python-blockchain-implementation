from hashlib import _Hash, sha256
from typing import List
from block import Block


class Chain:
    def __init__(self, difficulty: int) -> None:
        self.difficulty: int = difficulty
        self.blocks: List[_Hash] = []
        self.pool: List[_Hash] = []

    def create_origin_block(self) -> None:
        origin = Block(data="", prev_hash=sha256(str("0000000000000000").encode("utf-8")))
        origin.mine(self.difficulty)
        self.blocks.append(origin)
