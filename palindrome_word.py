def palindrome_word():
    word = input("Enter Word : ")
    rev_word = word[::-1]

    if word == rev_word:
        return f"{word} is Palindrome"
    else:
        return f"{word} is not Palindrome"

result = palindrome_word()
print(result) 