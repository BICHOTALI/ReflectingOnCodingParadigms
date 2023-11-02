# FUNCTIONAL PROMPT

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