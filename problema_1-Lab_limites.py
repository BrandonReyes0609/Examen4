import numpy as np

def monty_hall_simulation(change_choice):
    n = 1000000  
    wins = 0
    
    for _ in range(n):
        door_with_car = np.random.randint(0, 3)
        initial_choice = np.random.randint(0, 3)
        
        remaining_doors = [door for door in range(3) if door != initial_choice]
        
        if door_with_car in remaining_doors:
            door_opened = next(door for door in remaining_doors if door != door_with_car)
        else:
            door_opened = np.random.choice(remaining_doors)
        
        final_choice = next(door for door in remaining_doors if door != door_opened)
        
        if change_choice:
            final_choice = final_choice
        else:
            final_choice = initial_choice
        
        if final_choice == door_with_car:
            wins += 1

    return wins / n
prob_no_change = monty_hall_simulation(False)
prob_change = monty_hall_simulation(True)

prob_no_change, prob_change
print("probabilidad que no cambia:", prob_no_change)
print("probabilidad que cambia: ",prob_change)