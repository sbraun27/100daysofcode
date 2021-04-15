import random


def get_random_number(low=1, high=20):
    return random.randint(low, high)


class GuessingGame:
    def __init__(self, no_guesses=5, low=1, high=20):
        self.no_guesses = no_guesses
        self.low = low
        self.high = high
        self._guesses = set()
        self._answer = get_random_number(self.low, self.high)
        self._win = False

    def guess(self):
        user_guess = input(
            f"Please enter a number between {self.low} and {self.high} ")

        if not user_guess:
            raise ValueError("Please Enter a Number")
        try:
            user_guess = int(user_guess)
        except ValueError:
            raise ValueError("Please Enter a Number")

        if user_guess not in range(self.low, self.high):
            raise ValueError("Number not in range")

        if user_guess in self._guesses:
            raise ValueError("You already guessed that number")

        self._guesses.add(user_guess)

        return user_guess

    def _validate_guess(self, guess):
        if guess == self._answer:
            print(f"{guess} is correct!")
            return True
        else:
            high_or_low = "low" if guess < self._answer else "high"
            print(f"{guess} is too {high_or_low}")
            return False

    @property
    def num_guesses(self):
        return len(self._guesses)

    def __call__(self):
        while len(self._guesses) < self.no_guesses:
            try:
                guess = self.guess()
            except ValueError as ve:
                print(ve)
                continue

            win = self._validate_guess(guess)
            if win:
                guess_str = self.num_guesses == 1 and "guess" or "guesses"
                print(f"It took you {self.num_guesses} {guess_str}")
                self._win = True
                break

        else:
            print(
                f"Guessed {self.no_guesses} times, and answer was {self._answer}")


if __name__ == "__main__":
    game = GuessingGame()
    game()
