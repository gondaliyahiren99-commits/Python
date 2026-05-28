import math

# ============================================================
#   MATH MODULE — Senior Backend Developer Level
#   Hinglish mein samjho, pro level pe socho!
# ============================================================

# ─── 1. CONSTANTS ───────────────────────────────────────────
print("=" * 50)
print(">>> MATH CONSTANTS")
print("PI (circle ka raaz)       :", math.pi)         # 3.14159...
print("Infinity                  :", math.inf)         # ∞
print("NaN (Not a Number)        :", math.nan)         # invalid result

# ─── 2. ROUNDING — ceil / floor / trunc ─────────────────────
print("\n>>> ROUNDING FUNCTIONS")
value = 45.78

print(f"math.ceil({value})  →", math.ceil(value))     # upar wala integer = 46
print(f"math.floor({value}) →", math.floor(value))    # niche wala integer = 45
print(f"math.trunc({value}) →", math.trunc(value))    # sirf integer part = 45

# Real use: invoice mein paise round karna
price = 199.49
final_price = math.ceil(price)                         # hamesha upar round karo
print(f"\nInvoice price ceil → ₹{final_price}")

# ─── 3. POWER & ROOTS ───────────────────────────────────────
print("\n>>> POWER & ROOTS")
print("sqrt(144)  →", math.sqrt(144))                  # √144 = 12
print("pow(2, 10) →", math.pow(2, 10))                 # 2^10 = 1024.0 (float)
print("isqrt(50)  →", math.isqrt(250))                  # integer sqrt = 7 (fast!)
print("cbrt(27)   →", math.cbrt(27))                   # cube root = 3.0 (Python 3.11+)


# ─── 6. FACTORIAL & COMBINATIONS ────────────────────────────
print("\n>>> FACTORIAL & COMBINATORICS")
print("5! =", math.factorial(5))                       # 120
print("10! =", math.factorial(10))                     # 3628800


# ─── 7. GCD & LCM ───────────────────────────────────────────
print("\n>>> GCD & LCM")
a, b = 48, 180
print(f"GCD({a}, {b}) →", math.gcd(a, b))             # 12
print(f"LCM({a}, {b}) →", math.lcm(a, b))             # 720 (Python 3.9+)

# Real use: data pipeline mein invalid numeric values filter karna
raw_data = [1.5, float('inf'), float('nan'), 3.14, -2.0]
clean_data = [x for x in raw_data if math.isfinite(x)]
print(f"\nRaw  data : {raw_data}")
print(f"Clean data: {clean_data}")

print("MATH MODULE — Done! 🎯")