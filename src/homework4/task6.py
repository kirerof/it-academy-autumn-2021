"""6. Слова
Во входной строке записан текст. Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним или большим числом пробелов или символами
конца строки. Определите, сколько различных слов содержится в этом тексте."""
str_ = 'Каждый     охотник желает\n знать       где  сидит фазан.'
print(len(set(str_.split())))