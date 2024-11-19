print('Welcome to LTDPYTHON STORE')
purchase_amount = float(input('Enter purchase amount: $'))
print(f'Original purshase amount: {purchase_amount}')

if purchase_amount < 100:
    discount = 0
    print('No disccount')
# elif purchase_amount <= 500:
# elif purchase_amount >= 100 and purchase_amount <= 500:
elif purchase_amount == 100 or purchase_amount <= 500:
    discount = 10/100 * purchase_amount
    print(f'Discount of 10%: ${discount:.2f}')
elif purchase_amount > 500:
    discount = 20/100 * purchase_amount
    print(f'Discount of 20%: ${discount:.2f}')

discounted_amount = purchase_amount - discount

print(f'Discounted amount: ${discounted_amount:.2f}')
if discounted_amount < 200:
    tax = discounted_amount * 0.05
    print(f'Tax for discount less than $200: ${tax:.2f}')
else:
    tax = discounted_amount * 0.08
    print(f'Tax for discount above $200: ${tax:.2f}')

final_amount = discounted_amount + tax
print(f'Final amount: ${final_amount:.2f}')