locations = {
	(35.324, 23.239): "Tokyo Office",
	(87.123, 24.593): "Helsinki Office",
	(58.304, 90.234): "New York Office"
}

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
    i -= 1