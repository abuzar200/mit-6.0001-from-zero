# Raising your own exceptions


def getratios(l1, l2):
    """assumes l1 and l2 are list
    returns  ratios of list 1 upon list2"""
    ratio = []
    for index in range(len(l1)):
        try:
            ratio.append(l1[index] / l2[index])
        except ZeroDivisionError:
            print(f"Index {index}: Cannot divide by zero!")
            ratio.append(float("nan"))
        except Exception as e:
            raise ValueError("Function called with bad arguments") from e
        else:
            print("sucess")
        finally:
            print(f"Iteration {index + 1} cleanup done.")
        return ratio


print(getratios([1, 4, 0], [2, 1, 3]))
