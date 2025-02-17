def function_with_uncommon_bug_fixed(data=None):
    if data is None:
        data = []
    results = []
    for item in data:
        results.append(item * 2)
    return results

data1 = [1, 2, 3]
results1 = function_with_uncommon_bug_fixed(data1) 
print(f"Results 1: {results1}")

data2 = [4, 5, 6]
results2 = function_with_uncommon_bug_fixed(data2) 
print(f"Results 2: {results2}")

results3 = function_with_uncommon_bug_fixed()
print(f"Results 3: {results3}")
results4 = function_with_uncommon_bug_fixed([]) #Handles empty lists correctly
print(f"Results 4: {results4}") 