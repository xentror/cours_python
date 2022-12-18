import os
import time
import random
from pynput.keyboard import Key, Listener


logo1 = """
           /^\/^\\
         _|__|  O|
\/     /~     \_/ \\
 \____|__________/  \\
        \_______      \\
                `\     \                 \\
                  |     |                  \\
                 /      /                    \\
                /     /                       \\\\
              /      /                         \ \\
             /     /                            \  \\
           /     /             _----_            \   \\
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~"""

logo = """
      _    _
   ,-(|)--(|)-.
   \_   ..   _/
     \______/
       V  V                                  ____
       `.^^`.                               /^,--`
         \^^^\                             (^^\\
         |^^^|                  _,-._       \^^\\
        (^^^^\      __      _,-'^^^^^`.    _,'^^)
         \^^^^`._,-'^^`-._.'^^^^__^^^^ `--'^^^_/
          \^^^^^ ^^^_^^^^^^^_,-'  `.^^^^^^^^_/
           `.____,-' `-.__.'        `-.___.'"""

def print_with_tab(n, s, end = '\n'):
    print(" " * n + s, end = end)

def on_press(key):
    #print('{0} pressed'.format( key))
    global entries
    entries.append(str(key.char))

def on_release(key):
    #print('{0} release'.format( key))
    #if key == Key.esc:
    #    # Stop listener
    #    return False
    pass

class Snake:
    def __init__(self, body_coord):
        self.body_coord = body_coord

    def get(self, n):
        return self.body_coord[n]

    def get_tail(self):
        return self.body_coord[0]

    def get_head(self):
        return self.body_coord[len(self.body_coord) - 1]

    def move(self, x, y, grow):
        for i in range(len(self.body_coord)):
            (curr_x, curr_y) = self.body_coord[i]
            if curr_x == x and curr_y == y:
                return False

        new_head = (x, y)
        self.body_coord.append(new_head)
        if not grow:
            self.body_coord = self.body_coord[1:]

        return True

    def grow(self, x, y):
        (head_x, head_y) = self.get_head()
        new_head = (head_x + x, head_y + y)

        self.body_coord.append(new_head)

    def print(self):
        print(self.body_coord)

    def len(self):
        return len(self.body_coord)

class Map:
    def __init__(self, nb_row, nb_col, snake_coord):
        self.score = 0
        self.nb_col = nb_col
        self.nb_row = nb_row
        self.matrix = [ [ 0 for a in range(nb_col) ] for i in range(nb_row)]
        self.snake = Snake(snake_coord)
        self.fruit = self.generate_fruit_coord()

        self.place_snake()
        self.place_fruit()

    def place_snake(self):
        for i in range(self.snake.len()):
            (x, y) = self.snake.get(i)

            if i == self.snake.len() - 1:
                self.matrix[x][y] = 3
            else:
                self.matrix[x][y] = 1

    def place_fruit(self):
        (x, y) = self.fruit
        self.matrix[x][y] = 2

    def generate_fruit_coord(self):
        isOnSnake = True

        x = 0
        y = 0
        while isOnSnake:
            isOnSnake = False

            x = random.randint(0, self.nb_row - 1)
            y = random.randint(0, self.nb_col - 1)
            for i in range(self.snake.len()):
                (curr_x, curr_y) = self.snake.get(i)
                if curr_x == x and curr_y == y:
                    isOnSnake = True
                    break
        self.score += 1
        return (x, y)


    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def print(self):
        self.cls()

        print(logo, end = "\n\n")

        tab = 20
        print_with_tab(tab, f"  SCORE: {self.score}")
        print_with_tab(tab, " " + "_" * self.nb_col)
        for i in range(0, len(self.matrix)):
            print_with_tab(tab, "|", end='')
            for j in range(0, len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    print(" ", end = '')
                elif self.matrix[i][j] == 1:
                    print("x", end = '')
                elif self.matrix[i][j] == 2:
                    print("*", end = '')
                else:
                    print("o", end = '')
            print("|")
        print_with_tab(tab, " " + "-" * self.nb_col)

    def print_snake_coords(self):
        self.snake.print()

    def compute_next_head_coord(self, entry):
        (head_x, head_y) = self.snake.get_head()
        (tail_x, tail_y) = self.snake.get_tail()

        if entry == "q":
            if head_y <= 0:
                head_y = self.nb_col - 1
            else:
                head_y = head_y - 1
        if entry == "d":
            if head_y >= self.nb_col - 1:
                head_y = 0
            else:
                head_y = head_y + 1
        if entry == "z":
            if head_x <= 0:
                head_x = self.nb_row - 1
            else:
                head_x = head_x - 1
        if entry == "s":
            if head_x >= self.nb_row - 1:
                head_x = 0
            else:
                head_x = head_x + 1
        return (head_x, head_y)

    def move_snake(self, entry):
        (head_x, head_y) = self.compute_next_head_coord(entry)

        is_on_fruit = self.matrix[head_x][head_y] == 2
        if not self.snake.move(head_x, head_y, is_on_fruit):
            return False

        if is_on_fruit:
            self.fruit = self.generate_fruit_coord()
        self.update()

        return True

    def update(self):
        for i in range(self.nb_row):
            for j in range(self.nb_col):
                self.matrix[i][j] = 0

        self.place_fruit()
        self.place_snake()

def run_game():
    m = Map(20, 20, [(0, 0), (0, 1), (0, 2), (0, 3)])
    listener = Listener(on_press=on_press, on_release=on_release,suppress=True)
    listener.start()

    entry = "s"
    while True:
        m.print()
        time.sleep(0.2)

        #m.print_snake_coords()
        if len(entries) != 0:
            entry = entries.pop(0)

        if not m.move_snake(entry):
            print("game over")
            exit(0)


entries = []
run_game()
