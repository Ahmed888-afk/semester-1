"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Ahmed DAHRAOUI
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
order = list(states)
time_in_state = 0

while systime < maxtime:
    systime += 1
    time_in_state += 1
    if time_in_state >= states[state]:
        state = order[(order.index(state) + 1) % len(order)]
        time_in_state = 0
# At the end of each step you should output the time and state using the statement on line 14
    print(f"Time {systime:03} State {state}")
