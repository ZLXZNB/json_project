def generate_dict_with_initial(key_list, initial=None, initial_deep_copy=False):
    if not initial_deep_copy:
        return dict(zip(key_list, [initial] * len(key_list)))
    else:
        import copy
        length = len(key_list)
        result = {}
        for i in range(0, length):
            result[key_list[i]] = copy.deepcopy(initial)
        return result


def sort_dict_by_value(d, reverse=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))


def sort_dict_by_key(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[0], reverse=reverse))


def group_by(dict_list, key):
    group_key_set = set()
    is_list = isinstance(dict_list[0][key], list)
    if is_list:
        for d in dict_list:
            for value in d[key]:
                group_key_set.add(value)
    else:
        values = [d[key] for d in dict_list]
        for value in values:
            group_key_set.add(value)

    group_dict = generate_dict_with_initial(list(group_key_set), [], True)
    if is_list:
        for d in dict_list:
            for value in d[key]:
                group_dict[value].append(d)
    else:
        for d in dict_list:
            group_dict[d[key]].append(d)

    return sort_dict_by_key(group_dict)
