import random  # AVAZ SHODAN JAYE MOOSH VA PANIR

# ANASOR MAZE
EMPTY = 1
WALL = '+'
MOUSE = "\U0001F401"
CHEESE = "\U0001F9C0"

# SIZE MAZE / GHABEL TAGHIR
ROWS = 10
COLS = 10

MATRIX = []
for _ in range(ROWS):
    row = [EMPTY] * COLS
    MATRIX.append(row)

for i in range(ROWS): # DIVAR HA SOTON :))))
    MATRIX[i][0] = WALL
    MATRIX[i][COLS - 1] = WALL

    for j in range(COLS): # DIVAR HA SATR :))))
        if i == 0 or i == ROWS - 1:
            MATRIX[i][j] = WALL


# MOOSH VA PANIR
mouse_row = random.randint(1, ROWS - 2) # JASHONO AVAZ KON \ -2 TA TO DIVAR NARE
mouse_col = random.randint(1, COLS - 2)
MATRIX[mouse_row][mouse_col] = MOUSE # JA GOZARI

cheese_row = random.randint(1, ROWS - 2)
cheese_col = random.randint(1, COLS - 2)
MATRIX[cheese_row][cheese_col] = CHEESE

for row in MATRIX: # JA GOZARI MOSH VA PANIR DAR ZAMIN BAZI
    print("\t".join(map(str, row)) ,"\n")

while True: # KHOD BAZIMON
    direction = input("Harkat khod ra entekhab konid (W/A/S/D): ").upper()
    if direction in ['W', 'A', 'S', 'D']:
    
        if direction == 'W': # BALA
            new_row = mouse_row - 1
            new_col = mouse_col
            EMPTY = 0 # KE JAYE GHABLI RO 0 KONE

        elif direction == 'A': # CHAP
            new_row = mouse_row
            new_col = mouse_col - 1
            EMPTY = 0

        elif direction == 'S': # PAEEN
            new_row = mouse_row + 1
            new_col = mouse_col
            EMPTY = 0

        elif direction == 'D': # RAST
            new_row = mouse_row
            new_col = mouse_col + 1
            EMPTY = 0

        # CHECK KONE KE TO DIVAR NABASHIM
        if 0 <= new_row < ROWS and 0 <= new_col < COLS and MATRIX[new_row][new_col] != WALL:
            MATRIX[mouse_row][mouse_col] = EMPTY # JAYE GHABLE MOOSH KHALI SHE
            # VA CHON BALA TARIF KARDIM JAYE GHABLI 0 MISHE :)))
            MATRIX[new_row][new_col] = MOUSE # JAYE JADID MOOSH
            mouse_row, mouse_col = new_row, new_col # JAYE FELI

            for row in MATRIX: #PRINT
                print("\t".join(map(str, row)) ,"\n")

            if (mouse_row, mouse_col) == (cheese_row, cheese_col):
                print("PEYDASH KARDI!!!\U0001F929") # MOOSH BE PANIR RESID????????
                break #!!!
            else:
                pass #:((((((

        else:
            print("!!! SHOMA BE DIVAR KHORDID !!!")
            break
    else:
        print("!!!HARKAT NADOROST!!! AZ BAYNE (W/A/S/D).")
