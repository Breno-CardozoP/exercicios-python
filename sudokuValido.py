numbers=[1,2,3,4,5,6,7,8,9]
board = []
#criando a matriz
print("--- Preencha o Sudoku ---")
for y in range(9):
  print(f"Digite os valores da linha {y+1} (um por um):")
  row = [int(input(f"Coluna {x+1}: ")) for x in range(9)]
  board.append(row)


def CheckRow(grid):
  #percorre as linhas
  for row in grid:
    numCheck = []
    for x in row:
      if x not in numbers or x in numCheck:
        return False
      numCheck.append(x)
  return True


def checkCollum(grid):
  #percorre as colunas
  for col in range(9):
    numCheck = []
    for row in range(9):
      x = grid[row][col]
      if x not in numbers or x in numCheck:
        return False
      numCheck.append(x)
  return True


def checkArea(grid):
  # Percorre cada bloco 3x3
  for box_row in range(0, 9, 3):
    for box_col in range(0, 9, 3):
      numCheck = []
      for r in range(3):
        for c in range(3):
          x = grid[box_row + r][box_col + c]
          if x not in numbers or x in numCheck:
            return False
          numCheck.append(x)
  return True

def exibir():
    if CheckRow(board) and checkCollum(board) and checkArea(board):
        print("sudoku valido")
    else: print("sudoku invalido")
             
exibir()

            

