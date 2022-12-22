# credit card generator (mastercard and visa)

# part a (determines last digit)
def luhn_last_digit(n):
    n = list(n)
    n = [int(i) for i in n]
    n[-1::-2] = [i * 2 for i in n[-1::-2]]
    n = [(i - 9) if i > 9 else i for i in n]
    digit, n = 0, sum(n)
    while n % 10 != 0: [digit , n] = [digit + 1, n + 1]
    return digit 

# part b (generates card number)
def generate_card_number(card_type):
    import random 
    initial = []
    if card_type.lower() == "v": 
        initial.append(4)
        integers = [random.randint(0,9) for i in range(random.randrange(11, 17, 3))]
        integers.append(luhn_last_digit("".join(map(str, initial + integers))))
        return "".join(map(str, initial + integers))
    elif card_type.lower() == "m":
        x = [random.randint(51,55), random.randint(222100,272099)]
        initial.append(random.choice(x))
        integers = [random.randint(0,9) for i in range(16 - ((len(str(initial)) - 2) + 1))]
        integers.append(luhn_last_digit("".join(map(str, initial + integers))))
        return "".join(map(str, initial + integers))
    else: 
        return "goodbye"

# part c 
card_type = ''
while card_type.lower() != "quit":
    card_type = input("please enter v for a visa or m for a mastercard, or 'quit' to exit: ")
    print(generate_card_number(card_type))