from __future__ import annotations
import hashlib
from typing import List, Any
from .block import Block


class Chain:
    def __init__(self, difficulty: int) -> None:
        self.difficulty: int = difficulty
        self.blocks: List[hashlib._Hash] = []
        self.pool: List[hashlib._Hash] = []
        self.create_origin_block()

    def create_origin_block(self) -> None:
        origin = Block(data="Origin", prev_hash=hashlib.sha256(str("0" * 16).encode("utf-8")))
        origin.mine(self.difficulty)
        self.blocks.append(origin)

    def proof_of_work(self, block: Block):
        hash = hashlib.sha256(str(block).encode("utf-8"))
        return (
            block.hash.hexdigest() == hash.hexdigest()
            and int(hash.hexdigest(), 16) < 2 ** (256 - self.difficulty)
            and block.prev_hash == self.blocks[-1].hash
        )

    def add_to_chain(self, block: Block):
        if self.proof_of_work(block):
            self.blocks.append(block)

    def add_to_pool(self, data: Any):
        self.pool.append(data)

    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop(0)
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.difficulty)
            self.add_to_chain(block)
