def encode(numbers):
    output = []

    for number in numbers:
        if number == 0:
            output.append(0)
            continue

        chunks = []
        while number > 0:
            chunk = number & 0x7F
            number >>= 7 
            chunks.append(chunk)

        chunks.reverse()
        
        for i in range(len(chunks)):
            if i < len(chunks) - 1:
                chunks[i] |= 0x80

        output.extend(chunks)

    return output


def decode(bytes_):
    values = []
    current_value = 0
    sequence_pending = False 

    for byte in bytes_:
        data = byte & 0x7F

        current_value = (current_value << 7) | data

        if (byte & 0x80) == 0:
            values.append(current_value)
            current_value = 0
            sequence_pending = False
        else:
            sequence_pending = True

    if sequence_pending:
        raise ValueError("incomplete sequence")

    return values