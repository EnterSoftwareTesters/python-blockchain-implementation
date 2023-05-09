import hashlib

class Block():
    def __init__(self, data, prev_hash = "0000000000000000") -> None:
        self.hash = None
        self.prev_hash = prev_hash
        self.nonce = 0
        self.data = data

    def mine(self, difficulty) -> None:
        difficulty_constraint = 2**(256-difficulty)
        self.hash = hashlib.sha256(str(self).encode("utf-8"))
        while int(self.hash.hexdigest(), 16) > difficulty_constraint:
            self.nonce += 1
            self.hash = hashlib.sha256(str(self).encode("utf-8"))

    def __str__(self) -> str:
        return f"{self.prev_hash}{self.nonce}{self.data}"