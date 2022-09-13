import random

def coinflip(n):
	if n <= 0:
		return n
	else:
		return coinflip(n-1) + random.choice([True, False])


def main():

	n = int(input("Enter a value for n: "))
	print(coinflip(n))



main()
