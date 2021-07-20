# First implementation to find the length of the longest substring without repeating characters
def longest_unique_substr(str_val):
    n = len(str_val)

    # Result
    res = 0

    for i in range(n):
        # Default values in visited list are false
        visited = [0] * 256

        for j in range(i, n):
            # If current character is visited, break the loop
            if visited[ord(str_val[j])]:
                break

            # Else update the result if this window is larger, and mark
            # current character as visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(str_val[j])] = True

        # Remove the first character of previous window
        visited[ord(str_val[i])] = False
        # print(visited)

    return res


# Driver code
input_val = "Abcabcdc"
print("The input value is:", input_val)

len_val = longest_unique_substr(input_val)
print("The length of the longest non-repeating character substring is:", len_val)


# Second Implementation
# A simpler script to find/check the length of the longest substring with check_case. May not work on symbols characters.
def longest_unique_substr_v2(str_val, check_case=True):
    # check if case is True
    if check_case:
        str_val = str_val.lower()

    n = len(str_val)
    res = 0
    new_str = []

    # loop over the count of items in str
    for i in range(n):
        # check if each items exist in new_str list & continue -
        # else raise result with +1 and appending new item into new_str
        if str_val[i] in new_str:
            continue
        else:
            res += 1
            new_str.append(str_val[i])

    # print(len(new_str))
    if len(new_str) == res:
        return res

    return False


input_val = "Abcabcdc"
print("The input value is:", input_val)

len_val = longest_unique_substr_v2(input_val)
print("The length of the longest non-repeating character substring is:", len_val)
