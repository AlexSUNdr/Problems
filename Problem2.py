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



def _is_english_letter(symbol):
    return 'A' <= symbol.upper() <= 'Z'


def is_palindrome(line):
    line_len = len(line)
    i = 0
    j = line_len - 1

    while True:
        while (i < line_len) and (not _is_english_letter(line[i])):
            i += 1
            
        while (j > i) and (not _is_english_letter(line[j])):
            j -= 1
            
        if i > j:
            break
            
        if line[i].upper() != line[j].upper():
            return False

        j -= 1
        i += 1

    return True


