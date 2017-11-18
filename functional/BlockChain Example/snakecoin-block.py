import hashlib
import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data.encode) +
                   str(self.previous_hash))

        return sha.hexdigest()


def create_genesis_block():
    # Manually create a block with
    # index zero and arbitary previous hash
    return Block(0, datetime.datetime.now(), "Genesis Block", b"0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "Hey! I'm block %d" %this_index
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)



# Create the blockchain and add the genesis node
blockchain = [create_genesis_block(),]
previous_block = blockchain[0]

# Number of blocks to add
num_of_block = 20


# Add blocks to the chain
for i in range(num_of_block):
    to_add = next_block(previous_block)
    blockchain.append(to_add)
    previous_block = to_add

    # Tell about it
    print("Block %d added" %to_add.index)
    print("Hash: ", to_add.hash)

