from random import shuffle

if __name__ == '__main__':
    verbs = ['love']
    pronounses = ['I', 'You', 'We', 'They', 'He', 'She']
    times = ['Present simple', 'Past simple', 'Future simple']
    times = ['Present simple', 'Past simple', 'Future simple']
    forms = ['Positive', 'Negative', 'Question']

    questions = []

    for form in forms:
        if form == 'Positive':
            for time in times:
                if time == 'Present simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            if pronounse == 'He' or pronounse == 'She':
                                example = '{} {}s'.format(pronounse, verb)
                                questions.append(('Present + (' + pronounse + ' ' + verb + ')', example))
                            else:
                                example = '{} {}'.format(pronounse, verb)
                                questions.append(('Present + (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Past simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = '{} {}d'.format(pronounse, verb)
                            questions.append(('Past + (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Future simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = '{} will {}'.format(pronounse, verb)
                            questions.append(('Future + (' + pronounse + ' ' + verb + ')', example))
                else:
                    print('ERROR: time')

        elif form == 'Negative':
            for time in times:
                if time == 'Present simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            if pronounse == 'He' or pronounse == 'She':
                                example = '{} doesn`t {}'.format(pronounse, verb)
                                questions.append(('Present - (' + pronounse + ' ' + verb + ')', example))
                            else:
                                example = '{} don`t {}'.format(pronounse, verb)
                                questions.append(('Present - (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Past simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = '{} didn`t {}'.format(pronounse, verb)
                            questions.append(('Past - (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Future simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = '{} will not {}'.format(pronounse, verb)
                            questions.append(('Future - (' + pronounse + ' ' + verb + ')', example))
                else:
                    print('ERROR: time')
        elif form == 'Question':
            for time in times:
                if time == 'Present simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            if pronounse == 'He' or pronounse == 'She':
                                example = 'Does {} {}?'.format(pronounse, verb)
                                questions.append(('Present ? (' + pronounse + ' ' + verb + ')', example))
                            else:
                                example = 'Do {} {}?'.format(pronounse, verb)
                                questions.append(('Present ? (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Past simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = 'Did {} {}?'.format(pronounse, verb)
                            questions.append(('Past ? (' + pronounse + ' ' + verb + ')', example))
                elif time == 'Future simple':
                    for pronounse in pronounses:
                        for verb in verbs:
                            example = 'Will {} {}?'.format(pronounse, verb)
                            questions.append(('Future ? (' + pronounse + ' ' + verb + ')', example))
                else:
                    print('ERROR: time')
        else:
            print('ERROR: form')

true_answer = 0
false_answer = 0

shuffle(questions)

# for ex in matrix:
#     print(ex)

i = 0
ml = len(questions)

for question in questions:
    answer = input(question[0] + ': ')
    if answer.lower() == question[1].lower():
        true_answer += 1
        print('Правильно! ')
    else:
        false_answer += 1
        print('Ошибка! ')
        print('Правильный ответ: ', question[1])

    i += 1
    print('Прогресс: {}..{} True: {}  False: {}'.format(i, ml, true_answer, false_answer))


print('true_answer ', true_answer)
print('false_answer ', false_answer)

# for ex in matrix.items():
#     print(ex)

# Прогресс: 54..54 True: 50  False: 4
# true_answer  50
# false_answer  4












