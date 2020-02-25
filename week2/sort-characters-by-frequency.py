from operator import itemgetter, attrgetter
def frequencySort(s):
    counter = {}
    res = ''
    '''
    if s = 'tree'
    counter = {'t': 1, 'r': 1, 'e': 2}
    '''
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    '''
    sorted_counter = sorted(counter.items(), key = lambda x: x[1], reverse = True)
    sorted_counter = sorted(counter.items(), key = itemgetter(1), reverse = True)
    '''
    sorted_counter = sorted(counter.items(), key = itemgetter(0))
    print(sorted_counter)
    '''
    sorted_counter = [('e', 2), ('t', 1), ('r', 1)]
    '''
    for char, count in sorted_counter:
        res += char * count
        
    return res

frequencySort('tree')