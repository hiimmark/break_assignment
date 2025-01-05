# Chongtian Ma, 1/5/2024

n = 4 # number of schools
m = 6 # number of distinct types of essays

data = [[] for _ in range(n)]

# input types of essays for each school
data[0] = [0, 2, 3] 
data[1] = [1, 3, 4]
data[2] = [0, 2, 4]
data[3] = [2, 4, 5]

# obtain bitmasks for each school
v = [0] * n
for i in range(n):
	for j in data[i]:
		v[i] |= 1 << j

# initialize recurrence array
inf = int(1e9)
dp = [[-inf] * (1 << m) for _ in range(n)]

# base cases
dp[0][0] = 0
dp[0][v[0]] = 1

for i in range(0, n - 1):
	for msk in range(0, 1 << m):
		# case 1: don't take the next school
		dp[i+1][msk] = max(dp[i+1][msk], dp[i][msk])
		# case 2: take the next school
		dp[i+1][msk | v[i+1]] = max(dp[i+1][msk | v[i+1]], dp[i][msk] + 1)

# function to find max school given we want to write k essays
def write_k_essays(k):
	ans = 0
	for msk in range(1 << m):
		if msk.bit_count() == k:
			ans = max(ans, dp[n-1][msk])
	return ans

for i in range(1, m+1):
	print(f'If I write {i} essays, then I can apply to {write_k_essays(i)} schools')
