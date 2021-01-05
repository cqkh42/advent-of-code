from collections import Counter


def part_a(data):
    messages = data.split('\n')

    answer_1 = ''
    for index in range(len(messages[0])):
        col = Counter(message[index] for message in messages)
        letter = col.most_common(1)[0][0]
        answer_1 += letter
    return answer_1


def part_b(data, **_):
    messages = data.split('\n')

    answer_2 = ''
    for index in range(len(messages[0])):
        col = Counter(message[index] for message in messages)
        letter = col.most_common()[-1][0]
        answer_2 += letter
    return answer_2