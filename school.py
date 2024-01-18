class Caesar_cipher:

    def encryption(self):
        alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s1 = int(input())
        message = input().upper()
        result = ''
        for i in message:
            if i in alf:
                result += alf[alf.find(i) + s1]  # Задаем значения в итог
            else:
                return 'Ошибка'
        return result

    def decryption(self):
        alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s1 = int(input())
        message = input().upper()
        result = ''
        for i in message:
            if i in alf:
                result += alf[alf.find(i) - s1]
            else:
                return 'Ошибка'
        return result


class Vigenère_cipher:

    def form_dict(self):
        d = {}
        iter = 0
        for i in range(0, 127):
            d[iter] = chr(i)
            iter = iter + 1
        return d

    def encode_val(self, word):
        list_code = []
        d = self.form_dict()

        for w in range(len(word)):
            for value in d:
                if word[w] == d[value]:
                    list_code.append(value)
        return list_code

    def comparator(self, value, key):
        len_key = len(key)
        dic = {}
        iter = 0
        full = 0

        for i in value:
            dic[full] = [i, key[iter]]
            full = full + 1
            iter = iter + 1
            if (iter >= len_key):
                iter = 0
        return dic

    def full_encode(self, value, key):
        dic = self.comparator(value, key)
        lis = []
        d = self.form_dict()

        for v in dic:
            go = (dic[v][0] + dic[v][1]) % len(d)
            lis.append(go)
        return lis

    def decode_val(self, list_in):
        list_code = []
        lent = len(list_in)
        d = self.form_dict()
        for i in range(lent):
            for value in d:
                if list_in[i] == value:
                    list_code.append(d[value])
        return list_code

    def full_decode(self, value, key):
        dic = self.comparator(value, key)
        d = self.form_dict()
        lis = []

        for v in dic:
            go = (dic[v][0] - dic[v][1] + len(d)) % len(d)
            lis.append(go)
        return lis


class Polybius_square:
    def __init__(self):
        self.hard_dictionary = {"А": "11", "Б": "12", "В": "13",
                           "Г": "14", "Д": "15", "Е": "16", "Ё": "21",
                           "Ж": "22", "З": "23", "И": "24", "Й": "25",
                           "К": "26", "Л": "31", "М": "32", "Н": "33",
                           "О": "34", "П": "35", "Р": "36", "С": "41",
                           "Т": "42", "У": "43", "Ф": "44", "Х": "45",
                           "Ц": "46", "Ч": "51", "Ш": "52", "Щ": "53",
                           "Ъ": "54", "Ы": "55", "Ь": "56", "Э": "61",
                           "Ю": "62", "Я": "63"}

    def code(self, fraze):
        new_txt = ""
        list_fraze = list(fraze)
        for x in fraze:
            if x in self.hard_dictionary:
                new_txt += self.hard_dictionary.get(x)
        return new_txt

    def decode(self, fraze):
        new_txt = ""
        list_fraze = []
        step = 2
        for i in range(0, len(fraze), 2):
            list_fraze.append(fraze[i:step])
            step += 2
        key_hard_dictionary_list = list(self.hard_dictionary.keys())
        val_hard_dictionary_list = list(self.hard_dictionary.values())

        for x in list_fraze:
            if x in val_hard_dictionary_list:
                i = val_hard_dictionary_list.index(x)
                new_txt += key_hard_dictionary_list[i]
            else:
                new_txt += x[0:1]
        return new_txt


if __name__ == "__main__":
    print('Шифор Виженера')
    word = input('Слово-  ')
    key = input('Ключ-  ')
    b1 = Vigenère_cipher()
    key_encoded = b1.encode_val(key)
    value_encoded = b1.encode_val(word)
    shifre = b1.full_encode(value_encoded, key_encoded)
    print('Шифр-  ', ''.join(b1.decode_val(shifre)))
    decoded = b1.full_decode(shifre, key_encoded)
    decode_word_list = b1.decode_val(decoded)
    print('Расшифровка-  ', ''.join(decode_word_list))

    print('')
    print('Квадрат Полибия')
    b2 = Polybius_square()
    print(b2.code(input()))
    print(b2.decode(input()))

    print('')
    print('Шифр Цезаря')
    b3 = Caesar_cipher()
    print(b3.encryption())
    print(b3.decryption())
