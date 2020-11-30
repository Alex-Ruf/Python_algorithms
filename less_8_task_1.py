import hashlib


def func(text):
    array = []
    for i in range(1, len(text)):
        for j in range(len(text) - i + 1):
            b = text[j:j + i]
            hash_ = hashlib.sha256(f'{b}'.encode('utf-8')).hexdigest()
            if hash_ not in array:
                array.append(hash_)
    return len(array)


print(f'Количество подстрок - {func("papa") = }')
print(f'Количество подстрок - {func("sova") = }')
