def replace_occurence(string, old, new, occurence):
    return string.replace(old, '$$$', occurence - 1).replace(old, new, 1).replace('$$$', old)

def part_a(data):
    *maps, _, element = data.split('\n')
    maps = [item.split(' => ') for item in maps]

    new_strings = set()
    for old, new in maps:
        count = element.count(old)
        for occurence in range(1, count + 1):
            new_string = element.replace(old, '$$$', occurence - 1).replace(old, new, 1).replace('$$$', old)
            new_strings.add(new_string)
    return len(new_strings)


def part_b(data, **_):
    *maps, _, molecule = data.split('\n')
    maps = [item.split(' => ') for item in maps]
    inrep = [i[0] for i in maps]
    outrep = [i[1] for i in maps]
    in_unique = set(inrep)
    import re
    regex = r'(\w+) => (\w+)'
    inrep = []
    outrep = []
    # in_unique = set()
    # for line in data.split('\n'):
    #     line = line.replace('=>', '', )
    #     print(line)
    #
    #     e1, e2 = line.replace('=>', '').split('  ')
    #     inrep.append(e1)
    #     outrep.append(e2)
    #     in_unique.add(e1)

    # Only ONE step is required for calibration
    out_unique = set()
    for j in range(len(inrep)):
        elem = inrep[j]
        t = re.finditer(inrep[j], data)
        for i in t:
            newstring = data[:i.start()] + outrep[j] + data[i.end():]
            out_unique.add(newstring)

    # Create dictionary of reversed replacements
    replacements = {outrep[x][::-1]: inrep[x][::-1] for x in range(len(inrep))}
    print(replacements)

    # Function to return string for a regex match group
    def repfunction(x):
        print(x)
        return replacements[x.group()]

    count = 0
    while molecule != 'e':
        molecule = re.sub('|'.join(replacements.keys()), repfunction, molecule,
                          1)  # one replacement per key in reps
        count += 1
    return count
