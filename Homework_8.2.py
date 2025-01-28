# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
#
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
#
# Функція приймає на вхід рядок, та повертає булеве значення True або False
#
# Приклад:
def is_palindrome(text):
    purified_text = ''.join(char.lower() for char in text if char.isalnum())
    return purified_text == purified_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
