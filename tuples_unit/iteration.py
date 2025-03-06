months = (
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
)

# iterating using for
for month in months:
    print(month)

# printing backwards using while
i = len(months) - 1
while(i >= 0):
    print(months[i])
    i -= 1 # decrement by i, going backwards

# tuple methods (count, index)

x = (1, 2, 2, 2, 3, 4, 5)
x.count(2) # 3
x.index(2) # 1
x.index(1) # 0

nums = (1, 2, 3, (4, 5), 6, 7)
nums[3][0] # 4