import random
import copy

class Camel:
    def __init__(self, color):
        self.color = color
        self.position = 0
        self.stack = []

class CamelRace:
    def __init__(self):
        self.camels = {color: Camel(color) for color in ["red", "yellow", "blue", "green", "white"]}
        self.turn_order = ["red", "yellow", "blue", "green", "white"]
        self.dice_pool = self.turn_order.copy()
        self.dice_results = []
        self.setup_game()

    def setup_game(self):
        positions = {}
        for camel in self.camels.values():
            camel.position = random.randint(1, 3)
            if camel.position not in positions:
                positions[camel.position] = []
            positions[camel.position].append(camel)
        
        for camels in positions.values():
            for i in range(1, len(camels)):
                camels[i - 1].stack.append(camels[i])

    def move_camel(self, color, steps):
        camel = self.camels[color]
        camels_to_move = [camel] + camel.stack
        for c in camels_to_move:
            c.position += steps

        self.update_stacks()

    def update_stacks(self):
        for camel in self.camels.values():
            camel.stack = []

        positions = {}
        for camel in self.camels.values():
            if camel.position not in positions:
                positions[camel.position] = []
            positions[camel.position].append(camel)

        for camels in positions.values():
            for i in range(1, len(camels)):
                camels[i - 1].stack.append(camels[i])

    def play_turn(self):
        if not self.dice_pool:
            self.dice_pool = self.turn_order.copy()
        
        color = random.choice(self.dice_pool)
        self.dice_pool.remove(color)
        
        steps = random.randint(1, 3)
        self.move_camel(color, steps)
        self.dice_results.append((color, steps))

    def is_game_over(self):
        return any(camel.position >= 16 for camel in self.camels.values())

    def get_winner(self):
        max_position = max(camel.position for camel in self.camels.values())
        winning_camels = [camel for camel in self.camels.values() if camel.position == max_position]
        if len(winning_camels) > 1:
            winner = sorted(winning_camels, key=lambda x: len(x.stack), reverse=True)[0]
        else:
            winner = winning_camels[0]
        return winner.color

    def get_state(self):
        return copy.deepcopy(self.camels)

    def get_dice_results(self):
        return self.dice_results[-1] if self.dice_results else None

def simulate_game(state):
    race = CamelRace()
    race.camels = state
    race.dice_pool = ["red", "yellow", "blue", "green", "white"]
    while not race.is_game_over():
        race.play_turn()
    return race.get_winner()

def calculate_win_probabilities(state, num_simulations=1000):
    win_counts = {color: 0 for color in state.keys()}
    for _ in range(num_simulations):
        simulated_state = copy.deepcopy(state)
        winner = simulate_game(simulated_state)
        win_counts[winner] += 1
    return {color: win_counts[color] / num_simulations for color in win_counts}

def record_game_progress(num_simulations=1000):
    race = CamelRace()
    history = []

    initial_state = race.get_state()
    initial_win_rates = calculate_win_probabilities(initial_state, num_simulations)
    history.append((initial_state, initial_win_rates, None))
    
    while not race.is_game_over():
        race.play_turn()
        state = race.get_state()
        win_rates = calculate_win_probabilities(state, num_simulations)
        dice_result = race.get_dice_results()
        history.append((state, win_rates, dice_result))
    
    return history

if __name__ == "__main__":
    game_history = record_game_progress()
    for i, (state, win_rates, dice_result) in enumerate(game_history):
        if dice_result:
            print(f"第 {i} 回合: 擲骰結果 - {dice_result[0]}骰 {dice_result[1]}步")
        else:
            print("初始狀態:")
        print(f"{'駱駝':<6} {'位置':<6} {'堆疊':<20} {'勝率':<10}")
        print('-' * 44)
        for color, camel in state.items():
            stack_colors = ', '.join(c.color for c in camel.stack)
            print(f"{color:<6} {camel.position:<6} {stack_colors:<20} {win_rates[color]:.2%}")
        print()
