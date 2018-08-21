#!/usr/bin/env python3
"""
Building on the previous example, let's also assume that you have saved $918 to fund your new
adventure. You wonder how many days you can keep one server running before your money
runs out. Of course, you hope your social network becomes popular and requires 20 servers to
keep up with the demand. How much will it cost to operate at that point?
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per month?
How much does it cost to operate twenty servers per day?
How much does it cost to operate twenty servers per month?
How many days can I operate one server with $918?
"""
# The cost of one server per hour.
cost_per_hour = 0.51
# Compute the costs for one server.
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day
# Compute the costs for twenty servers
cost_per_day_twenty = 20 * cost_per_day
cost_per_month_twenty = 20 * cost_per_month
# Budgeting
budget = 918
operational_days = budget / cost_per_day
# Display the results.
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))
print('Cost to operate twenty servers per day is ${:.2f}.'.format(cost_per_day_twenty))
print('Cost to operate twenty servers per month is ${:.2f}.'.format(cost_per_month_twenty))
print('A server can operate on a ${0:.2f} budget for {1:.0f} days.'.format(budget, operational_days))