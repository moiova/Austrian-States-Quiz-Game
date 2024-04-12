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
states_as_list = csv_data.state.to_list()

guessed_states = 0
score = Score()

while guessed_states < 9:
    state = t.textinput("Austrian State", "Give a state")

    if state in states_as_list:
        guessed_states += 1
        score.update_score(guessed_states)

        index = states_as_list.index(state)
        new_state = State(state=state, x_pos=csv_data.x[index], y_pos=csv_data.y[index])
        print('index: ', index)

    elif state is None:
        score.game_over()
        guessed_states = 99

if guessed_states == 9:
    score.congrats()

# screen.update()
# t.mainloop()
t.exitonclick()
