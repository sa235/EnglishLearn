from random import shuffle
from random import choice

verbs = ['love', 'watch', ['see', 'saw'], ['go', 'went']]


def get_random_verb():
    verb = choice(verbs)
    return verb


def get_verb_form(verb, formkey):
    if isinstance(verb, list):
        return verb[formkey]
    else:
        return verb


def verb_format(verb):
    if isinstance(verb, list):
        return '{} ({})'.format(verb[0], verb[1])
    else:
        return verb


def get_correct_answer(form, time, pronounse, verb):
    if form == '+':
        if time == 'Present simple':
            if pronounse == 'He' or pronounse == 'She':
                return '{} {}s'.format(pronounse, get_verb_form(verb, 0))
            else:
                return '{} {}'.format(pronounse, get_verb_form(verb, 0))
        elif time == 'Past simple':
            if isinstance(verb, list):
                return '{} {}'.format(pronounse, get_verb_form(verb, 1))
            else:
                return '{} {}d'.format(pronounse, get_verb_form(verb, 0))
        elif time == 'Future simple':
            return '{} will {}'.format(pronounse, get_verb_form(verb, 0))
        else:
            print('ERROR: time')

    elif form == '-':
        if time == 'Present simple':
            if pronounse == 'He' or pronounse == 'She':
                return '{} doesn`t {}'.format(pronounse, get_verb_form(verb, 0))
            else:
                return '{} don`t {}'.format(pronounse, get_verb_form(verb, 0))
        elif time == 'Past simple':
            return '{} didn`t {}'.format(pronounse, get_verb_form(verb, 0))
        elif time == 'Future simple':
            return '{} will not {}'.format(pronounse, get_verb_form(verb, 0))
        else:
            print('ERROR: time')
    elif form == '?':
        if time == 'Present simple':
            if pronounse == 'He' or pronounse == 'She':
                return 'Does {} {}?'.format(pronounse, get_verb_form(verb, 0))
            else:
                return 'Do {} {}?'.format(pronounse.lower(), get_verb_form(verb, 0))
        elif time == 'Past simple':
            return 'Did {} {}?'.format(pronounse.lower(), get_verb_form(verb, 0))
        elif time == 'Future simple':
            return 'Will {} {}?'.format(pronounse.lower(), get_verb_form(verb, 0))
        else:
            print('ERROR: time')
    else:
        print('ERROR: form')


if __name__ == '__main__':

    pronounses = ['I', 'You', 'We', 'They', 'He', 'She']
    times = ['Present simple', 'Past simple', 'Future simple']
    forms = ['+', '-', '?']

    questions = []

    for form in forms:
        for time in times:
            for pronounse in pronounses:
                verb = choice(verbs)
                correct_answer = get_correct_answer(form, time, pronounse, verb)
                questions.append(('{} {} | {} {}'.format(time, form, pronounse, verb_format(verb)), correct_answer))

shuffle(questions)

true_answer = 0
false_answer = 0
#
# for ex in questions:
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
