import numpy as np

def monty_hall_simulation(num_trials, change_door):
    # Contadores para los resultados
    win_count = 0
    lose_count = 0
    
    for _ in range(num_trials):
        # Configuración inicial
        doors = np.zeros(10)
        prize_door = np.random.randint(0, 10)
        doors[prize_door] = 1
        
        # Elección inicial del concursante
        initial_choice = np.random.randint(0, 10)
        
        # El presentador abre 8 puertas sin premio (excluyendo la puerta del concursante)
        remaining_doors = [i for i in range(10) if i != initial_choice and doors[i] != 1]
        opened_doors = np.random.choice(remaining_doors, 8, replace=False)
        
        # Elección final del concursante
        if change_door:
            # Cambia la puerta
            final_choice = [i for i in range(10) if i != initial_choice and i not in opened_doors][0]
        else:
            # No cambia la puerta
            final_choice = initial_choice
        
        # Verifica si ganó el premio
        if doors[final_choice] == 1:
            win_count += 1
        else:
            lose_count += 1
    
    win_probability = win_count / num_trials
    lose_probability = lose_count / num_trials
    
    return win_probability, lose_probability

# Parámetros de la simulación
num_trials = 100000

# Simulación sin cambiar de puerta
win_prob_no_change, lose_prob_no_change = monty_hall_simulation(num_trials, change_door=False)
print(f"Sin cambiar de puerta: Probabilidad de ganar = {win_prob_no_change:.4f}, Probabilidad de perder = {lose_prob_no_change:.4f}")

# Simulación cambiando de puerta
win_prob_change, lose_prob_change = monty_hall_simulation(num_trials, change_door=True)
print(f"Cambiando de puerta: Probabilidad de ganar = {win_prob_change:.4f}, Probabilidad de perder = {lose_prob_change:.4f}")
