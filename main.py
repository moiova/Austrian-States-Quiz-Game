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

# convert 'state' column data to title case
csv_data.state = csv_data.state.str.title()

guessed_states = 0
score = Score()

while guessed_states < 9:
    state = t.textinput(f"{guessed_states}/{len(csv_data.state)} States Correct", "Give a state")

    if state is None:
        score.game_over()
        guessed_states = 99

    else:
        state = state.title()
        for states_from_csv in csv_data.state:
            if states_from_csv == state:
                guessed_states += 1
                score.update_score(guessed_states)
                state_data = csv_data[csv_data.state == state]
                new_state = State(state=state, x_pos=int(state_data.x.iloc[0]), y_pos=int(state_data.y.iloc[0]))

if guessed_states == 9:
    score.congrats()

# screen.update()
# t.mainloop()
t.exitonclick()
