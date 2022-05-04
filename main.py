import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        if answer_state not in guessed_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]    # retrieve the row of guessed state
            t.goto(int(state_data.x), int(state_data.y))   # tap into the row's attributes x, y
            t.write(state_data.state.item())  # write state name on the map based on the x, y location
            guessed_states.append(answer_state)  # add guessed state to the guessed_states list

states_to_learn_list = list(set(all_states) - set(guessed_states))  # created a list of missed states
df = pd.DataFrame(states_to_learn_list)  # convert the list to a dataframe
print(df)
df.to_csv("states_to_learn.csv")  # convert and save the dataframe to a cvs file
