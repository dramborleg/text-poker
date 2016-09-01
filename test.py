import parser
import testbot

game_creation = [('-c mango', 0), ('--create mango', 0), ('c mango', 0),
                 ('-c Uguisu', 0), ('--create kiwi c guava lemon', 0),
                 ('--create GAME_4', 0), ('-c', 0)]
add_players = [('-c mango', 0), ('-j', 0), ('--join mango', 0), ('j mango', 0),
               ('-j mango', 'dramborleg'), ('-j mang0', 1), ('-j mango', 0),
               ('-t ringil', 'dramborleg'), ('-t kiwi -j mango', 1)]
game_ops = [('-c mango -j mango -t せんぱい', 0), ('-j mango -t こうはい', 1),
            ('-s --deal 2 -f -o', 0), ('-o', 0), (' -p', 0), ('-q', 1), ('-q', 0)]

tests = [('GAME CREATION', game_creation), ('ADDING PLAYERS', add_players),
         ('GAME OPERATIONS', game_ops)]

bot = testbot.TestBot()
for test in tests:
    p = parser.Parser()
    print('TESTING TEST: %s' % test[0])
    for i in test[1]:
        ret = p.parse(i[0], i[1], bot)
        print('--------')
        print(i)
        print(ret)
        print('--------')
    print('\n\n')
