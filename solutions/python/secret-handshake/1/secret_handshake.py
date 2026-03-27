def commands(binary_str):
    positions = {
        0: "wink",
        1: "double blink",
        2: "close your eyes",
        3: "jump",
        4: lambda lst: lst.reverse()
    }
    secret_handshake = []

    for index, char in enumerate(binary_str[::-1]):
        if char == "1":
            action = positions[index]
            if callable(action):
                action(secret_handshake)
            else:
                secret_handshake.append(action)


    return secret_handshake