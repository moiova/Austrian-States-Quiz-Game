import turtle as t
import pandas
from state import State
from score import Score

screen = t.Screen()
screen.title("Austria States Game")
image = "austria_states_blank.gif"
screen.addshape(image)
t.shape(image)

csv_data = pandas.read_csv("9_states.csv")

guessed_states = 0
score = Score()

while guessed_states < 9:
    state = t.textinput("Austria State", "Give a state").lower()

    index = -1
    for state_from_csv in csv_data.state:
        index += 1
        if state_from_csv.lower() == state:
            guessed_states += 1
            score.update_score(guessed_states)

            new_state = State(state=state_from_csv, x_pos=csv_data.x[index], y_pos=csv_data.y[index])
            print('index: ', index)
    print('guessed_states: ', guessed_states)

score.congrats()

screen.update()
t.mainloop()
