import pygame
import random

# Inicializar pygame
pygame.init()

# Definir constantes
GRID_SIZE = 10
CELL_SIZE = 50
PACMAN_COLOR = (255, 255, 0)
GHOST_COLOR = (255, 0, 0)
WALL_COLOR = (0, 0, 255)
PILL_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Definir posições iniciais
pacman_position = [1, 1]
ghost_positions = [[8, 8], [8, 1]]
pill_position = [5, 5]

# Definir paredes (Exemplo: [(1,1), (2,3)] são posições com muros)
walls = [(3, 3), (4, 4), (6, 6), (7, 7), (2, 5), (5, 2)]

# Definir o ecrã
screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
pygame.display.set_caption('Pac-Man Turn-Based')

# Definir o score inicial
score = 0

# Função para verificar se uma posição é válida
def is_valid_position(position):
    x, y = position
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and (x, y) not in walls

# Função para desenhar o Pac-Man
def draw_pacman(position):
    x, y = position
    center_x = y * CELL_SIZE + CELL_SIZE // 2
    center_y = x * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, PACMAN_COLOR, (center_x, center_y), CELL_SIZE // 2)
    pygame.draw.polygon(screen, BACKGROUND_COLOR, [(center_x, center_y), 
                                                   (center_x + CELL_SIZE // 2, center_y - CELL_SIZE // 4), 
                                                   (center_x + CELL_SIZE // 2, center_y + CELL_SIZE // 4)])

# Função para desenhar um fantasma
def draw_ghost(position):
    x, y = position
    center_x = y * CELL_SIZE + CELL_SIZE // 2
    center_y = x * CELL_SIZE + CELL_SIZE // 2
    # Desenhar corpo do fantasma
    pygame.draw.circle(screen, GHOST_COLOR, (center_x, center_y - CELL_SIZE // 6), CELL_SIZE // 2)
    pygame.draw.rect(screen, GHOST_COLOR, (center_x - CELL_SIZE // 2, center_y - CELL_SIZE // 6, CELL_SIZE, CELL_SIZE // 2))

# Função para desenhar o jogo
def draw_game():
    screen.fill(BACKGROUND_COLOR)
    
    # Desenhar paredes
    for wall in walls:
        x, y = wall
        pygame.draw.rect(screen, WALL_COLOR, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Desenhar Pac-Man
    draw_pacman(pacman_position)

    # Desenhar fantasmas
    for ghost in ghost_positions:
        draw_ghost(ghost)

    # Desenhar a pílula
    pygame.draw.circle(screen, PILL_COLOR, 
                       (pill_position[1] * CELL_SIZE + CELL_SIZE // 2, 
                        pill_position[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)
    
    # Desenhar o layout do labirinto (linhas)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(screen, (50, 50, 50), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # Mostrar o score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

# Função para mover Pac-Man
def move_pacman(action):
    global score
    if action == 'UP':
        new_position = [pacman_position[0] - 1, pacman_position[1]]
    elif action == 'DOWN':
        new_position = [pacman_position[0] + 1, pacman_position[1]]
    elif action == 'LEFT':
        new_position = [pacman_position[0], pacman_position[1] - 1]
    elif action == 'RIGHT':
        new_position = [pacman_position[0], pacman_position[1] + 1]

    # Verificar se a nova posição é válida
    if is_valid_position(new_position):
        pacman_position[:] = new_position
        score -= 1  # Subtrair 1 ponto por cada movimento

# Função para mover fantasmas aleatoriamente
def move_ghosts():
    for ghost in ghost_positions:
        move = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        if move == 'UP':
            new_position = [ghost[0] - 1, ghost[1]]
        elif move == 'DOWN':
            new_position = [ghost[0] + 1, ghost[1]]
        elif move == 'LEFT':
            new_position = [ghost[0], ghost[1] - 1]
        elif move == 'RIGHT':
            new_position = [ghost[0], ghost[1] + 1]

        # Verificar se a nova posição é válida
        if is_valid_position(new_position):
            ghost[:] = new_position

# Função para verificar se o Pac-Man comeu a pílula
def check_pill():
    global score
    if pacman_position == pill_position:
        score += 10  # Adicionar 10 pontos quando come a pílula
        return True
    return False

# Função para verificar se Pac-Man foi capturado por um fantasma
def check_ghosts():
    return pacman_position in ghost_positions

# Ciclo do jogo
def game_loop():
    global score
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_pacman('UP')
                elif event.key == pygame.K_DOWN:
                    move_pacman('DOWN')
                elif event.key == pygame.K_LEFT:
                    move_pacman('LEFT')
                elif event.key == pygame.K_RIGHT:
                    move_pacman('RIGHT')
                
                # Mover os fantasmas depois de Pac-Man
                move_ghosts()

                # Verificar se Pac-Man comeu a pílula
                if check_pill():
                    print("Pac-Man ganhou!")
                    print(f'Score final: {score}')
                    running = False

                # Verificar se Pac-Man foi capturado
                if check_ghosts():
                    print("Pac-Man foi capturado pelos fantasmas!")
                    print(f'Score final: {score}')
                    running = False

        draw_game()
        clock.tick(5)  # Controla o frame rate do jogo (turn-based)

    pygame.quit()

# Iniciar o jogo
game_loop()
