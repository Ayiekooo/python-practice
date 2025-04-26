# reverse_string.py
# Turn a string backwards.

def reverse_string(s):
    # start with empty
    rev = ""
    # go from last letter down to first
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]
    return rev

if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Reversed is:", reverse_string(s))
