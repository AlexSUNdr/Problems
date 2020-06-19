# Проверить, что строка является палиндромом. Учитывать только английские буквы, регистр не важен, все остальные символы игнорировать.
# Примеры палиндромов: 'Ab45c_+=\BA', 'Aa0987654.', '45j90' и т.д.

def is_palindrom(line):
    i = 0
    j = len(line) - 1
    while i < len(line):
        if 'A' <= line[i].upper() <= 'Z':
            while ('A' > line[i].upper() or line[j].upper() > 'Z') and j >= i:
                j = j - 1
            if j < i: break
            if line[i].upper() != line[j].upper():
                return 'Is not palindrom'
            else:
                j = j - 1
        i = i + 1
    return 'Is palindrom'


