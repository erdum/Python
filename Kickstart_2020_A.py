# Taking first line which is number of test cases
n_test = int(input())
# Initializing empty lists
n_house = []
budget = []
house_prices = []

# Geting each line for number of test times
if n_test > 1 and n_test < 100000:
	for i in range(0, n_test):
		n, b = input().split(' ')
		n_house.append(int(n))
		budget.append(int(b))
		house_prices.append([int(hp) for hp in input().split(' ')])

# Sorting house_prices
for i in range(0, len(house_prices)):
	house_prices[i].sort()

# Main algorithm
def calc(budget, houses):
	ans = 0
	for i in range(0, len(houses)):
		for n in range(0, len(houses[i])):
			if houses[i][n] <= budget[i]:
				budget[i] -= houses[i][n]
				ans += 1
		print('Case #{}: {}'.format(i + 1, ans))
		ans = 0
		
calc(budget, house_prices)
