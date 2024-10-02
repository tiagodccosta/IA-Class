import random
import time

# Definição do ambiente - grelha de 2x2 (pode ser expandida)
class Environment:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice(['clean', 'dirty']) for _ in range(cols)] for _ in range(rows)]

    def display_grid(self, agent_position=None):
        for i, row in enumerate(self.grid):
            row_str = ""
            for j, cell in enumerate(row):
                if agent_position and agent_position == [i, j]:
                    row_str += "A"  # Representa a posição do agente
                elif cell == 'clean':
                    row_str += "C"  # Célula limpa
                else:
                    row_str += "D"  # Célula suja
            print(row_str)
        print()

    def is_clean(self):
        # Verifica se todas as células estão limpas
        for row in self.grid:
            if 'dirty' in row:
                return False
        return True

# Definição do agente - o aspirador
class VacuumAgent:
    def __init__(self, env):
        self.env = env
        self.position = [0, 0]  # O agente começa no canto superior esquerdo

    def clean(self):
        # Se a célula atual estiver suja, o agente limpa
        if self.env.grid[self.position[0]][self.position[1]] == 'dirty':
            self.env.grid[self.position[0]][self.position[1]] = 'clean'
            print("Célula limpa!")
            print(" ")
        

    def move(self):
        # Move o agente para a próxima célula
        if self.position[1] < self.env.cols - 1:
            self.position[1] += 1
        elif self.position[0] < self.env.rows - 1:
            self.position[0] += 1
            self.position[1] = 0    

        return

# Inicializa o ambiente e o agente
env = Environment()
vacuum = VacuumAgent(env)

# Mostrar o estado inicial da grelha
print("Estado inicial da grelha:")
env.display_grid(agent_position=vacuum.position)

# Loop até a grelha estar completamente limpa
while not env.is_clean():
    vacuum.clean()  # O agente limpa a célula atual
    env.display_grid(agent_position=vacuum.position)  # Mostrar o estado atual da grelha com o agente
    vacuum.move()  # O agente move-se para a próxima célula
    time.sleep(1)

print("Todas as células estão limpas!")
