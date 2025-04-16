def encodeDecode():
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + steps

        if new_position > 26:
            new_position = new_position % 26

        print(alphabet[new_position], end="")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

text = input("Enter a text: ").lower()
direction = input("Enter direction (encode or decode):")
steps = int(input("Enter steps: "))

if direction == 'encode':
    encodeDecode()
else:
    steps = steps * -1
    encodeDecode()
