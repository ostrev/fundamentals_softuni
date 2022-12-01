number_of_pieces = int(input())
pieces_dictionary = {}

for _ in range(number_of_pieces):
    data = input(). split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]

    if piece not in pieces_dictionary:
        pieces_dictionary[piece] = []
    pieces_dictionary[piece] = [composer, key]

command = input()

while command != "Stop":
    data = command.split("|")
    if data[0] == 'Add':
        piece = data[1]
        composer = data[2]
        key = data[3]
        if piece in pieces_dictionary:
            print(f"{piece} is already in the collection!")
        else:
            pieces_dictionary[piece] = []
            pieces_dictionary[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif data[0] == 'Remove':
        piece = data[1]
        if piece in pieces_dictionary:
            del pieces_dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif data[0] == 'ChangeKey':
        piece = data[1]
        key = data[2]
        if piece in pieces_dictionary:
            print(f"Changed the key of {piece} to {key}!")
            pieces_dictionary[piece][1] = key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()


for piece, value in pieces_dictionary.items():
    composer = value[0]
    key = value[1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
