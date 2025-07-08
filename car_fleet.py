# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.

# Example 1:

# Input: target = 10, position = [1,4], speed = [3,2]

# Output: 1
# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# Example 2:

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3
# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.



class Solution:
    def carFleet(self ,target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort(reverse = True)
        stack = []
        for position , speed in cars:
            stack.append((target - position) / speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)




# Compute Time to Target:
    # For each car, calculate the time it will take to reach the target using the formula:
    # ( target − position) / speed

# Sort Cars by Position:
    # Sort the cars in descending order of position (from closest to the target to farthest), because:

    # Cars can't overtake each other.

    # This ensures we evaluate cars from front to back.

# Initialize a Stack:
    # Use a stack to keep track of car fleets based on their time to reach the target.

# Iterate Through Cars:

    # Push the calculated time for each car onto the stack.

    # If the new time is less than or equal to the time at the top of the stack:

    # It means this car will catch up to the one in front and join the same fleet.

    # So, pop the new time (don't create a new fleet).

# Final Result:

    # The number of remaining times in the stack equals the number of distinct car fleets that will arrive at the target.