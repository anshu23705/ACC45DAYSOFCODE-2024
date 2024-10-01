def longest_common_prefix(strs):
    if not strs:
        return "", 0

    common_prefix = strs[0]

    for string in strs[1:]:
        while string[:len(common_prefix)] != common_prefix:
            common_prefix = common_prefix[:-1]
            if not common_prefix:
                return "", 0

    count = sum(1 for s in strs if s.startswith(common_prefix))
    return common_prefix, count

if __name__ == "__main__":
    n = int(input("Enter the number of strings: "))
    input_str = input(f"Enter {n} strings separated by space: ")
    strs = input_str.split()

    result, count = longest_common_prefix(strs)
    print(f"The longest common prefix is: '{result}' which appears {count} times")