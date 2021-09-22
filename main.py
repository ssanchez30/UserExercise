from User import User

adrien = User("Adrien Rosales", "adrien@python.com")
nibbles = User("Mr. Nibbles", "nibbles@python.com")
benny = User("Benny Bob", "benny@python.com")

print("* Adrien transactions*")
adrien.make_deposit(1000)
adrien.make_withdrawal(200)
adrien.make_deposit(3000)
adrien.make_deposit(500)
adrien.display_user_balance()
print("* END Adrien transactions*\n")

print("* Nibbles transactions*")
nibbles.make_deposit(3500)
nibbles.make_withdrawal(500)
nibbles.make_withdrawal(1500)
nibbles.make_withdrawal(8000)  # not enough funds for withdrawal
nibbles.display_user_balance()
print("* END Nibbles transactions*\n")

print("* Benny transactions*")
benny.make_deposit(7000)
benny.make_withdrawal(1000)
benny.make_withdrawal(1900)
benny.make_withdrawal(1300)
benny.display_user_balance()
print("* END Benny transactions*\n")

print("* Transfer Adrien to Benny*")
adrien.transfer_money(benny, 1000)
adrien.display_user_balance()
benny.display_user_balance()
print("* END BONUS*")
