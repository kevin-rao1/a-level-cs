def lz(binary_stream):
    dictionary = {}
    subsequences = []
    position = 1
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    current_subsequence = ""
    for bit in binary_stream:
        current_subsequence += bit
        if current_subsequence not in dictionary:
            dictionary[current_subsequence] = position
            subsequences.append(current_subsequence)
            position += 1
            current_subsequence = ""
            
    encoded_output = []
    for seq in subsequences:
        if len(seq) == 1:
            encoded_output.append(seq)
        else:
            new_symbol = seq[-1]
            prefix = seq[:-1]
            prefix_position = dictionary[prefix]
            prefix_binary = alphabet[prefix_position]
            
            encoded_block = prefix_binary + new_symbol
            encoded_output.append(encoded_block)
            
    return "".join(encoded_output)

input_sequence = "0000000000000000000000000101010101010"

if __name__ == "__main__":
  print(lz(input_sequence))