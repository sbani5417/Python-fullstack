daily_visitors=[1200,2000,1500,2900,1234]
highest_traffic=max(daily_visitors)
lowest_traffic=min(daily_visitors)
highest_day=daily_visitors.index(highest_traffic)+1
lowest_day=daily_visitors.index(lowest_traffic)+1
print("highest_traffic",highest_traffic)
print("lowest_traffic",lowest_traffic)
