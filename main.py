# FUNCTIONAL PROMPT

# defining funtion
def flatten_and_sort(arr):
    # Use a list comprehension to flatten the nested arrays
    flattened = [element for sublist in arr for element in sublist]

    # Use the sorted function to sort the flattened list in ascending order
    sorted_list = sorted(flattened)

    return sorted_list

# Example usage:
nested_array = [[3, 1, 2], [6, 4, 5], [9, 7, 8]]
result = flatten_and_sort(nested_array)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''''
-How does this solution ensure data immutability?

This solution ensures data immutability by not modifying the original input arr. Instead, it creates new lists (flattened and sorted_list) to store the intermediate and final results. The original input remains unchanged, adhering to the principle of immutability.

-Is this solution a pure function? Why or why not?

Yes, this solution is a pure function. A pure function is a function that, given the same input, will always produce the same output and has no side effects. 

-Is this solution a higher-order function? Why or why not?

No, this is not a higher-order function. A higher-order function takes one or more functions as arguments or returns a function as its result. The flatten_and_sort function in the provided code does not take or return any functions; it operates on lists only. Therefore, not a higher-order function.

-Would it have been easier to solve this problem using a different programming style?

The choice of programming style depends on the problem and the programmer's familiarity with a particular paradigm. 

-Why is functional programming a helpful paradigm when solving this problem?

Functional programming is helpful in solving this problem because it promotes a clear and declarative way of handling data transformations. Functional programming encourages immutability, which reduces the risk of bugs and makes the code more readable. It also makes it easier to reason about the code and test it since pure functions produce consistent results.
            '''''



# OBJECT ORIENTED PROMPT


# Setting up initial Podracer class with max_speed, condition, & price attributes
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Setting up a repair method that updates condition of Podracer to 'repaired'
    def repaired(self):
        self.condition = "repaired"


# Anikin's Podracer to inherit(super) Podracer class attributes; also contains a speed booster!
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2


# Sebulba's Podracer is trashed now, so we're setting the condition as such.
class SebulbasPod(Podracer):
    def __init__(max_speed, condition, price):
        super.init(max_speed, condition, price)

    def flame_jet(self, other_pod):
        other_pod.condition = "trashed"

'''
-How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

Encapsulation is used while the classes encapsulate their attributes of max_speed, condition, and price; as well as their methods repair, boost, and flame_jet.
Inheritance is used as AnakinsPod and SebulbasPod inherit their attributes and methods from the initial Podracer class.

-Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

If there had been rock-solid data involved, Functional programming may have been the way to go. However, the podracer objects had unique encapsulated attributes and behaviors that OOP was much more suited to modeling.

-How in particular did Object Oriented Programming assist in the solving of this problem?

OOP was more suited for modeling the podracer objects, handling encapsulated attributes, and defining their behaviors.
'''