text = input("请输入要加密的文本: ")
shift = int(input("请输入加密偏移量 (整数): "))
encrypted_text = ""
for char in text:
    if char.isalpha():
        is_upper = char.isupper()
        char = char.lower()
        shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        if is_upper:
            shifted_char = shifted_char.upper()
        encrypted_text += shifted_char
    else:
        encrypted_text += char
print("加密后的文本:", encrypted_text)