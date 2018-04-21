zero = "zero"
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
elevens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ["", "", 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = list(map(lambda x: x + "hundred", ones))

def num_to_word(number):
    if number == 0:
        return zero
    str_number = str(number)
    letters = ""

    if len(str_number) == 3:
        hundreds_digit = int(str_number[0])
        letters += hundreds[hundreds_digit]
        if not number % 100 == 0:
            letters += "and"

    if 10 <= number % 100 < 20:
        teens_one_digit = int(number % 10)
        letters += elevens[teens_one_digit]
    else:
        tens_digit = 0 if len(str_number) < 2 else int(str_number[-2])
        letters += tens[tens_digit]
        letters += ones[number % 10]

    return letters

print(sum((len(num_to_word(i))) for i in range(1, 1000)))