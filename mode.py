def frequency_list(data):
    """
    Creates a frequency list dictionary.

    Returns: {unique value: # of appearances}

    The keys are each unique value, and the key's values are the number of times that
    unique value appears in the list. If a value is a list, each value in the list is considered.
    """
    freq_dict = {}

    for value in data:
        # value is a list
        if isinstance(value, list):
            list_freq_dict = frequency_list(value)
            for k, v in list_freq_dict.items():
                if k in freq_dict:
                    freq_dict[k] += v
                else:
                    freq_dict[k] = v

        # value is not a list
        elif value in freq_dict:
            freq_dict[value] += 1
        else:
            freq_dict[value] = 1

    return freq_dict

def frequency(data):
    """
    Finds how often each unique value appears and sorts them in descending order
    by number of appearances.

    Returns: [[value, # of appearances], ...]

    The values are stored in lists, in which [0] is
    the value and [1] is the number of appearances.
    """
    freq_dict = frequency_list(data)

    result = [[value, freq] for value, freq in sorted(freq_dict.items(), key=lambda value: value[1], reverse=True)]
    return result

def mode(data):
    """
    Finds the mode value in a list.

    Returns: {'value': [mode value(s)], 'frequency': # of appearances}

    If a value is a list, every value in the list is considered.
    If there are multiple modes, all are included in the 'value' list

    """
    freq_dict = frequency_list(data)
    mode = {'value': [], 'frequency': 0}

    for value, frequency in freq_dict.items():
        if frequency == mode['frequency']:
            mode['value'].append(value)
        elif frequency > mode['frequency']:
            mode['frequency'] = frequency
            mode['value'] = [value]

    return mode

def mean(data):
    """
    Finds the mean value in a list.

    Returns: {'mean': mean value, 'count': values in the list}

    If a value is a list, every value in the list is considered.
    """
    result = 0
    count = 0

    if len(data) == 0:
        return 0

    for value in data:
        if isinstance(value, list):
            list_mean = mean(value)
            result += list_mean['mean'] * list_mean['count']
            count += list_mean['count']
        else:
            result += value
            count += 1

    result /= count

    return {'mean': result, 'count': count}
