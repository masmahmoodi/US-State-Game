import  turtle
import pandas
screen = turtle.Screen()
screen.title("us-states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed_states = []
data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()
x = data["x"].to_list()
y = data["y"].to_list()
while len(guessed_states)<50:
        answer = screen.textinput(f" {len(guessed_states)}/50 Guess the state", "What's another state's name?").title()
        for num in range(len(list_of_states)):
            states = list_of_states[num]
            if answer == states:
                guessed_states.append(answer)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(x[num], y[num])
                t.write(answer)
        if answer == "Exit":
            missing_states = [sate for sate in list_of_states if sate not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break



# def get_mouse_click_coor(x,y):
#    print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()