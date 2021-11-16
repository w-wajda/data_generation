import pandas as pd

kostiumy = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/Halloween.csv', header=2)
print(kostiumy.head())
print('\n')

# Wyszukanie wartości za pomocą pętli for
# znaleźć wszystkie regiony, w których najpopularniejszym kostiumem na Halloween jest 'Rabbit’ (kolumna 1)
for index, wartosc in kostiumy.iterrows():
    if wartosc['1'] == 'Rabbit':
        print(wartosc['region'])
# jest to efekt dobry na małe zbiory, przy większych by się zawiesiło, stąd stosowanie maski

print(kostiumy['1'] == 'Rabbit')
# wynik możemy wykorzystać jako maskę, która nałożymy na DataFrame
print(kostiumy[kostiumy['1'] == 'Rabbit'])
print('\n')

# Maski bardziej rozbudowane

# znajdź regiony w których najpopularniejszym kostiumem jest 'Rabbit’ lub 'Dinosaur’.
print(kostiumy[(kostiumy['1'] == 'Rabbit') | (kostiumy['1'] == 'Dinosaur')])
print('\n')

# znajdź regiony w których najpopularniejszym kostiumem jest 'Rabbit’, a drugim najpopularniejszym 'Pirate’.
print(kostiumy[(kostiumy['1'] == 'Rabbit') & (kostiumy['2'] == 'Pirate')])





