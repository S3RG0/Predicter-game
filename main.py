from predict import Positive, N_Positive, Neutral, N_Neutral, Negative, N_Negative
import random

class FortuneTeller:
    def __init__(self):
        self.positive = Positive()
        self.n_positive = N_Positive()
        self.neutral = Neutral()
        self.n_negative = N_Negative()
        self.negative = Negative()
        self.n_negative = N_Negative()

    def get_fortune(self):
        all_predictions = [self.positive.predictions, self.n_positive.predictions, self.neutral.predictions, self.n_negative.predictions, self.negative.predictions, self.n_negative.predictions]
        chosen_list = random.choice(all_predictions)
        random_prediction = random.choice(chosen_list)
        return random_prediction
    
    def start(self):
        random_fortune = fortune_teller.get_fortune()
        print(random_fortune)


# создаем экземпляр класса
fortune_teller = FortuneTeller()