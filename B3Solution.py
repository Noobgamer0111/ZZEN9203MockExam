import hashlib

def generate_valid_block(block_number, prediction, previous_hash):
    serial = 1
    while True:
        block_string = f"{block_number}+{prediction}+{previous_hash}+{serial}"
        # Compute SHA256 hash
        sha = hashlib.sha256()
        sha.update(block_string.encode())
        hex_digest = sha.hexdigest()
        # Check if hash starts with '0' followed by a digit (0-9)
        if len(hex_digest) < 2:
            continue  # Insufficient length for the first two characters
        if hex_digest[0] == '0' and '0' <= hex_digest[1] <= '9':
            return block_string, hex_digest, serial
        serial += 1

# Example usage: Generate Block 1 with Serial Number 25
block_1 = "Service NSW"
block_1_hash = generate_valid_block(1, block_1, "")  # Previous hash is empty for the first block
# Output will be similar to:
# '1+Service NSW+0f603b5f322a16568bf7b0acff51008466408cdccbfeff675118bbde8ca49b50+25'

print("Block 1:", block_1_hash[0])
print("Hash:", block_1_hash[1])
