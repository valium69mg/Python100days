import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

""" GET THE COORDINATES OF STATES IN TURTLE WINDOW 
def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)

"""
#DataFrame
data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")

#Functions
def stateExists(state):
    state = state.title() #All letters to lower case
    data_state = data[data["state"] == state]
    return data_state

def alreadyGuessed(input_state,state_list):
    for state in state_list:
        if (state == input_state):
            return True
    return False


# Main loop
states_guessed = []
tries = 0
max_tries = 5
while (tries < max_tries):
    #Input question
    answer_state = screen.textinput(title="Guess The State",prompt="Type a U.S. state")
    data_state = stateExists(answer_state)
    # State data
    if (data_state.empty == True):
        print("No state found.")
        tries+=1 
        print("Tries left: {}".format(max_tries-tries))   
    else:
        #SET STATE VARIABLES
        x_state = data_state["x"].iloc[0]
        y_state = data_state["y"].iloc[0]
        state_name = data_state["state"].iloc[0]
        #CHECK IF STATE IS ALREADY GUESSED
        repeated_guess = alreadyGuessed(state_name,states_guessed)
        if (repeated_guess== True):
            print("State already guessed.")
            pass
        else:
            #LIST OF GUESSED STATES
            states_guessed.append(state_name)
            #DRAW STATE NAME
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_turtle.goto(x=x_state,y=y_state)
            state_turtle.pendown()
            state_turtle.write(state_name)
                

print("Game Over")
print("States guessed: {}".format(len(states_guessed)))         

turtle.mainloop()


