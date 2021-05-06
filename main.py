from random import choice

if __name__ == '__main__':
    verbs = ['love']
    pronounses = ['I', 'You', 'We', 'They', 'He', 'She']
    times = ['Present simple', 'Past simple', 'Future simple']
    times = ['Present simple', 'Past simple', 'Future simple']
    forms = ['Positive', 'Negative', 'Question']

    matrix = []

    for form in forms:
        if form == 'Positive':
            for time in times:
                if time == 'Present simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            if pronounse == 'He' or pronounse == 'She':
                                example = '{} {}s'.format(pronounse, verb)
                                matrix.append(('Present + (' + pronounse + ' ' + verb + ')', example))
                            else:
                                example = '{} {}'.format(pronounse, verb)
                                matrix.append(('Present + (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Past simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = '{} {}d'.format(pronounse, verb)
                            matrix.append(('Past + (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Future simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = '{} will {}'.format(pronounse, verb)
                            matrix.append(('Future + (' + pronounse + ' ' + verb + ')', example))
                else:
                    print('ERROR: time')

        elif form == 'Negative':
            for time in times:
                if time == 'Present simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            if pronounse == 'He' or pronounse == 'She':
                                example = '{} doesen`t {}'.format(pronounse, verb)
                                matrix.append(('Present - (' + pronounse + ' ' + verb + ')', example))
                            else:
                                example = '{} don`t {}'.format(pronounse, verb)
                                matrix.append(('Present - (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Past simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = '{} didn`t {}'.format(pronounse, verb)
                            matrix.append(('Past - (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Future simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = '{} will not {}'.format(pronounse, verb)
                            matrix.append(('Future - (' + pronounse + ' ' + verb + ')', example))
                else:
                    print('ERROR: time')
        elif form == 'Question':
            for time in times:
                if time == 'Present simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            if pronounse == 'He' or pronounse == 'She':
                                example = 'Does {} {}'.format(pronounse, verb)
                                matrix.append(('Present ? (' + pronounse + ' ' + verb + ')', example))
                            else:
                                example = 'Do {} {}'.format(pronounse, verb)
                                matrix.append(('Present ? (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Past simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = 'Did {} {}?'.format(pronounse, verb)
                            matrix.append(('Past ? (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Future simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = 'Will {} {}?'.format(pronounse, verb)
                            matrix.append(('Future ? (' + pronounse + ' ' + verb + ')', example))
                else:
                    print('ERROR: time')
        else:
            print('ERROR: form')

true_answer = 0
false_answer = 0

for i in range(1, 53):
    variant = choice(matrix)
    ask = input(variant[0] + ': ')
    if ask.lower() == variant[1].lower():
        true_answer += 1
        print('Правильно! ', true_answer)
    else:
        false_answer += 1
        print('Ошибка! ', true_answer)
        print('Правильный ответ: ', variant[1])

print('true_answer ', true_answer)
print('false_answer ', false_answer)

# for ex in matrix.items():
#     print(ex)












