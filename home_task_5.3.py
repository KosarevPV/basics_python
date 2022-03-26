tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Анна']
klasses = ['9А', '7В', '9Б', '9В', '11Г']


def gen(n, m):
    for tutor, klass in zip(tutors, klasses):
        yield (tutor, klass)
    for i in range(len(klasses), len(tutors)):
        yield (n[i], None)


tut_gen = gen(tutors, klasses)

print(*tut_gen, sep='\n')
print(type(tut_gen))

# истощаем генератор
tut_gen_2 = gen(tutors, klasses)

print(next(tut_gen_2))
print(next(tut_gen_2))
print(next(tut_gen_2))
print(next(tut_gen_2))
print(next(tut_gen_2))
print(next(tut_gen_2))
print(next(tut_gen_2))
print(next(tut_gen_2))
print(next(tut_gen_2))
