# ============================================
#       USER-DEFINED MODULE : my_module.py
#       Author  : Hiren
#       Topic   : Custom Module Functions
# ============================================

# # ---------- 1. ADD TWO NUMBERS ----------
# def add(a, b):
#     return a + b

# # ---------- 2. SUBTRACT ----------
# def sub(a, b):
#     return a - b

# # ---------- 3. MULTIPLY ----------
# def mul(a, b):
#     return a * b

# # ---------- 4. DIVIDE ----------
# def div(a, b):
#     if b == 0:
#         return "Error: Division by zero!"
#     return a / b

# # ---------- 5. FACTORIAL ----------
# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# # ---------- 6. EVEN OR ODD ----------
# def even_odd(n):
#     if n % 2 == 0:
#         return f"{n} is EVEN"
#     else:
#         return f"{n} is ODD"

# # ---------- 7. PRIME CHECK ----------
# def is_prime(n):
#     if n < 2:
#         return f"{n} is NOT Prime"
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return f"{n} is NOT Prime"
#     return f"{n} is Prime"

# # ---------- 8. SQUARE & CUBE ----------
# def square(n):
#     return n ** 2

# def cube(n):
#     return n ** 3

# # ---------- 9. GREET USER ----------
# def greet(name):
#     return f"Hello, {name}! Welcome to Python Modules 🎉"

# # ---------- 10. MAX OF THREE ----------
# def max_of_three(a, b, c):
#     return max(a, b, c)

# # ---------- 11. REVERSE A STRING ----------
# def reverse_string(s):
#     return s[::-1]

# # ---------- 12. COUNT VOWELS ----------
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for ch in s:
#         if ch in vowels:
#             count += 1
#     return count

# # ---------- 13. SIMPLE INTEREST ----------
# def simple_interest(p, r, t):
#     si = (p * r * t) / 100
#     return si

# # ---------- 14. CELSIUS TO FAHRENHEIT ----------
# def cel_to_fah(c):
#     return (c * 9/5) + 32

def is_prime(num) :
    flag =1
    for i in range(2,num-1):
        if num%i==0 :
            flag = 0
            break
    return "prime" if flag ==1 else  "Not prime"
