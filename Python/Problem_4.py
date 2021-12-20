def check_palindrome(num):
    digit_list = [char for char in str(num)]
    rev_digit_list = []
    for i in range(1,len(digit_list)+1):
        rev_digit_list.append(digit_list[-i])
    if num == int(''.join(rev_digit_list)):
        return True
    else:
        return False

def largest_palindromic_product(d): # made from product of d-digit numbers
    palindrome_list = []
    for i in range(int(d*'9'), 1, -1):
        for j in range(int(d*'9'), 1, -1):
            if check_palindrome(i*j):
                palindrome_list.append(i*j)
    palindrome_list.sort()
    return palindrome_list[-1]

print(largest_palindromic_product(3))
