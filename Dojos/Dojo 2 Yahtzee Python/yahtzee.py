class Yahtzee:

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        return d1 + d2 + d3 + d4 + d5

    @staticmethod
    def yahtzee(dice):
        if dice.count(dice[0]) == 5:
            return 50
        else:
            return 0

    @staticmethod
    def ones(d1,  d2,  d3,  d4,  d5):
        lista = [d1, d2, d3, d4, d5]
        return lista.count(1)

    @staticmethod
    def twos(d1,  d2,  d3,  d4,  d5):
        lista = [d1, d2, d3, d4, d5]
        return 2*lista.count(2)

    @staticmethod
    def threes(d1,  d2,  d3,  d4,  d5):
        lista = [d1, d2, d3, d4, d5]
        return 3*lista.count(3)

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    def fours(self):
        return 4*self.dice.count(4)

    def fives(self):
        return 5*self.dice.count(5)

    def sixes(self):
        return 6*self.dice.count(6)

    @staticmethod
    def score_pair(d1,  d2,  d3,  d4,  d5):
        counts = Yahtzee.contador(d1, d2, d3, d4, d5)
        lista = []
        for i in range(5, -1, -1):
            if (counts[i] >= 2):
                return (i+1)*2
        else:
            return 0

    @staticmethod
    def two_pair(d1,  d2,  d3,  d4,  d5):
        counts = Yahtzee.contador(d1, d2, d3, d4, d5)
        n = score = 0
        for i in range(6):
            if (counts[i] >= 2):
                n = n+1
                score += (i+1)
            if (n == 2):
                return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(d1,  d2,  d3,  d4,  d5):
        lista = [d1, d2, d3, d4, d5]
        if lista.count(lista[0]) >= 4:
            return lista[0]*4
        elif lista.count(lista[1]) >= 4:
            return lista[1]*4
        else:
            return 0

    @staticmethod
    def three_of_a_kind(d1,  d2,  d3,  d4,  d5):
        lista = [d1, d2, d3, d4, d5]
        if lista.count(lista[0]) >= 3:
            return lista[0]*3
        elif lista.count(lista[1]) >= 3:
            return lista[1]*3
        elif lista.count(lista[2]) >= 3:
            return lista[2]*3
        else:
            return 0

    @staticmethod
    def smallStraight(d1,  d2,  d3,  d4,  d5):
        if sorted((d1, d2, d3, d4, d5)) == [1, 2, 3, 4, 5]:
            return 15
        else:
            return 0

    @staticmethod
    def largeStraight(d1,  d2,  d3,  d4,  d5):
        if sorted((d1, d2, d3, d4, d5)) == [2, 3, 4, 5, 6]:
            return 20
        else:
            return 0

    @staticmethod
    def fullHouse(d1,  d2,  d3,  d4,  d5):
        counts = Yahtzee.contador(d1, d2, d3, d4, d5)
        if 2 in counts and 3 in counts:
            return (counts.index(2)+1)*2    +      (counts.index(3)+1)*3
        else:
            return 0

    @staticmethod
    def contador(d1, d2, d3, d4, d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        return counts