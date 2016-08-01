import parser

game_creation = [('-c mango', 0), ('--create mango', 0), ('c mango', 0),
                 ('-c Uguisu', 0), ('--create kiwi c guava lemon', 0),
                 ('--create GAME_4', 0), ('-c', 0)]
add_players = [('-c mango', 0), ('-j', 0), ('--join mango', 0), ('j mango', 0),
               ('-j mango', 'dramborleg'), ('-j mang0', 1), ('-j mango', 0),
               ('-t ringil', 'dramborleg'), ('-t kiwi', 1), ('-j mango', 1)]

tests = [('GAME CREATION', game_creation), ('ADDING PLAYERS', add_players)]

for test in tests:
    p = parser.Parser()
    print('TESTING TEST: %s' % test[0])
    for i in test[1]:
        ret = p.parse(i[0], i[1])
        print('--------')
        print(i)
        print(ret)
        print('--------')
