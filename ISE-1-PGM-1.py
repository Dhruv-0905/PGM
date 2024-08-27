import random

def simulate_dice_rolls(trials):
    ones = 0
    sixes = 0
   
    for _ in range(trials):
        roll = random.randint(1, 6)
        if roll == 1:
            ones += 1
        elif roll == 6:
            sixes += 1
            
    ones_proportion = ones / trials
    sixes_proportion = sixes / trials
    
    return ones_proportion, sixes_proportion

theoretical_one = 1/6  
theoretical_six = 1/6  

trial_numbers = [1000, 10000, 100000]
for trials in trial_numbers:
    ones_prop, sixes_prop = simulate_dice_rolls(trials)
    print(f"For {trials} trials:")
    print(f"Proportion of ones: {ones_prop:.4f} (Theoretical: {theoretical_one:.4f})")
    print(f"Proportion of sixes: {sixes_prop:.4f} (Theoretical: {theoretical_six:.4f})")
    print('-' * 50)
