from random import sample
import string


def get_random_password(num = 8) -> str:
    str = ''
    var = string.ascii_uppercase + string.ascii_lowercase + string.digits
    str = str.join(sample(var, num))
    return str

print(get_random_password())
#  Комментарий для пустой строки в конце кода