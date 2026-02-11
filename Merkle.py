import hashlib
ZERO_HASH='0'*64

def double_sha256(data):
    if isinstance(data, str):
        data = bytes.fromhex(data)
    first_pass=hashlib.sha256(data).digest()
    second_pass=hashlib.sha256(first_pass).digest()
    return second_pass

def computeMerkle_parent(left, right):
    left_bytes=bytes.fromhex(left)
    right_bytes=bytes.fromhex(right)
    return double_sha256(left_bytes + right_bytes).hex()


def compute_merkle_root(tx_hashes):

    if not tx_hashes:
        return ZERO_HASH  #

    current_level = list(tx_hashes)

    while len(current_level) > 1:
        next_level = []
        if len(current_level) % 2 != 0:
            current_level.append(ZERO_HASH)

        for i in range(0, len(current_level), 2):
            left_node = current_level[i]
            right_node = current_level[i + 1]
            parent = computeMerkle_parent(left_node, right_node)
            next_level.append(parent)

        current_level = next_level

    return current_level[0]