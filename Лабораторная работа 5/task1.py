from pprint import pprint


dict_hex = [{"bin":bin(num), "dec":num, "hex":hex(num), "oct":oct(num)} for num in range(16)]
pprint(dict_hex)
#  Комментарий для пустой строки в конце кода