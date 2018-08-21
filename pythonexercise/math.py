blah = '1'
# The cost of one server per hour.
cost_per_hour = 0.51
# Compute the costs for one server.
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day
# Display the results.
# Use {} to print value within text. and use .2f to extend decimals
print('Cost to operate one server per day is ${}'.format(cost_per_day))
print('Cost to operate one server per month is ${}'.format(cost_per_month))
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))

