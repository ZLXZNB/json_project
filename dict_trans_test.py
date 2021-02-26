def analysis():
    list_A = [1, 2]
    analysis_test(list_A)
    print(list_A)


def analysis_test(list_A):
    list_A.append(3)
    return None


analysis()