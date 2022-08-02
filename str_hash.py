def main():
    s = 'Python Bootcamp'
    print(hash_str(s))


def hash_str(string: str) -> int:
    mod = 10**9 + 9
    pow_base = 256 - ord(' ')
    p = 1
    hash_value = 0
    for char in string:
        hash_value = (hash_value + (ord(char) - ord(' ') + 1) * p) % mod
        p = (p * pow_base) % mod
    return hash_value


if __name__ == '__main__':
    main()
