def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0

    for character in s:
        if character in vowels:
            count += 1

    return count

def main():
    input_str = input().split()
    result = count_vowels(input_str)
    print(result)

if __name__ == "__main__":
    main()

