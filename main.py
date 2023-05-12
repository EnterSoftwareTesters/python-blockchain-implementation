from src.chain import Chain

chain = Chain(20)

while True:
    data = input("Add something to the chain: ")
    chain.add_to_pool(data)
    chain.mine()
    print("Updated Blockchain:")
    for block in chain.blocks:
        print("*" * 50)
        print(f"Hash:\t\t{block.hash.hexdigest()}")
        print(f"Previous Hash:\t{block.prev_hash.hexdigest()}")
        print(f"Nonce:\t\t{block.nonce}")
        print(f"Data:\t\t{block.data}")
        print(f"Created at:\t\t{block.created_at}")
        print("*" * 50)
