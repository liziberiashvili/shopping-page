import random


class GameNumbers:
    my_score = 0

    def choose_game_level(self):
        answer = input("easy or hard?")
        if answer == "easy":
            self.guess_choosed_number_easy()
        else:
            self.guess_choosed_number_hard()

    def choose_random_number(self):
        min_numb = 0
        max_numb = 10
        random_number = random.randint(min_numb, max_numb)
        return random_number

    def guess_choosed_number_easy(self):
        for i in range(5):

            a = self.choose_random_number()
            print(a)
            x = int(input("guess number"))
            if x == a:
                self.my_score += 1

            print(self.my_score)

    def guess_choosed_number_hard(self):
        while 1 > 0:
            b = self.choose_random_number()
            print(b)
            x = int(input("guess number"))

            if x > b + 3 or x < b - 3:
                self.my_score -= 1
            elif x == b:
                self.my_score += 1
            if x == 0:
                break
            print(self.my_score)


game_number = GameNumbers()
game_number.choose_game_level()
