def function_with_uncommon_bug(data):
    # This function demonstrates a subtle bug related to mutable default arguments.
    results = []
    for item in data:
        results.append(item * 2)
    return results

data1 = [1, 2, 3]
results1 = function_with_uncommon_bug(data1)  # Works as expected
print(f"Results 1: {results1}")

data2 = [4, 5, 6]
results2 = function_with_uncommon_bug(data2)  # Also works as expected
print(f"Results 2: {results2}")

# The bug is revealed here:
results3 = function_with_uncommon_bug([])  # Unexpected results!
print(f"Results 3: {results3}")