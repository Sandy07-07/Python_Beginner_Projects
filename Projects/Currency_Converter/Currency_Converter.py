inr = float(input("Enter the Indian Currency amount :- "))
usd = inr*0.012  # To convert to US Dollar
euro = inr*0.011  # To convert to Euro
pound = inr*0.0098  # To convert to British Pound
jpy = inr*1.64  # To convert to Japanese Yen
yuan = inr*0.084  # To convert to Chinese Yuan

print(f"The price in USD is :- {usd}")
print(f"The price in EURO is :- {euro}")
print(f"The price in POUND is :- {pound}")
print(f"The price in JPY is :- {jpy}")
print(f"The price in YUAN is :- {yuan}")
