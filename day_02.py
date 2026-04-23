paragraph = input("Enter a paragraph: ")
sorted_paragraph = sorted(paragraph)

search_char = input("Enter a character to search for: ")

low = 0
high = len(sorted_paragraph) - 1
while low <= high:
    mid = (low + high) // 2
    if sorted_paragraph[mid] == search_char:
        print("found at index", mid)
        break
    elif sorted_paragraph[mid] > search_char:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("not found")
