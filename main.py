import matplotlib.pyplot as plt

from datetime import datetime

def read_date(spl):
	return datetime.strptime(spl[0], "%Y-%m-%d")
	
def read_price(spl):
	return float(spl[4])

avg_months = 10
    
f = open("us_data.csv")
f.next()
dates = []
prices = []
avg_prices = []
strategy_prices = []
i = 0
for line in reversed(list(f)):
    spl = line.split(",")
    dt = read_date(spl)
    price = read_price(spl)
    dates.append(dt)
    prices.append(price)

    if i >= avg_months:
        past_x_prices = prices[-avg_months-1:-1]
        avg_price = sum(past_x_prices) / len(past_x_prices)
        avg_prices.append(avg_price)
        if prices[-2] >= avg_prices[-2]:
            prev_price = prices[-2]
            ret = (price - prev_price) / prev_price
            strategy_prices.append(strategy_prices[-1] * (1 + ret))
        else:
            strategy_prices.append(strategy_prices[-1])
    else:
        avg_prices.append(0)
        strategy_prices.append(price)

    i += 1
f.close()

plt.plot_date(dates, prices, "b-", label="Price")
plt.plot_date(dates, avg_prices, "r-", label="Average price of last " + str(avg_months) + " months")
plt.plot_date(dates, strategy_prices, "g-", label="The Strategy")
plt.legend()
plt.show()