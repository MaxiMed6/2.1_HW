adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")



# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())




# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

h_count = adwentures_of_tom_sawer.count("h")
print(h_count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()
capital_count = sum(1 for word in words if word[0].isupper())
print(capital_count)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
words = adwentures_of_tom_sawer.split()
count = 0
second_tom_position = -1

for i, word in enumerate(words):
    if word == "Tom":
        count += 1
        if count == 2:
            second_tom_position = i
            break

print("Позиція другого 'Tom':", second_tom_position)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
import re
sentences_with_delimiters = re.split(r'([.!?])', adwentures_of_tom_sawer)
adwentures_of_tom_sawer_sentences = []
for i in range(0, len(sentences_with_delimiters) - 1, 2):
    sentence = sentences_with_delimiters[i].strip()
    if sentence:
        adwentures_of_tom_sawer_sentences.append(sentence)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print("Четверте речення:", fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
by_the_time = any(sentence.strip().startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print(by_the_time)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-1].strip()
word_count = len(last_sentence.split()) if last_sentence else 0
print(word_count)
