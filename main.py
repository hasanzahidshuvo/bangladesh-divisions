import turtle
import pandas as pd

# Creating Screen
screen = turtle.Screen()
# Giving Name
screen.title("Bangladesh Divisions")
# importing Map Image
image = "Bangladesh_Empty_map.gif"

# Giving Screenshape as the map image
screen.addshape(image)
turtle.shape(image)

# Reading from CSV file
data = pd.read_csv('bd_divisions.csv')

# Creating division list
all_divisions = data.division.to_list()


guessed_divisions = []

# Creating a loop to write all 8 divisions
while len(guessed_divisions) < 8:
    
    user_input = screen.textinput(title =f"{len(guessed_divisions)}/8 Divisions", prompt="What's another Division's name? ").title()
    
    # Type exit to break out of the loop
    if user_input == "Exit":
        break
    

    if user_input in all_divisions:
        
        guessed_divisions.append(user_input)
        
        bd = turtle.Turtle()
        bd.hideturtle()
        bd.penup()
        # Getting x,y coordinates
        div_data = data[data.division == user_input]
       
        # Converting x,y coordinates to string
        bd.goto(int(div_data.x), int(div_data.y))
        # Writing division name
        bd.write(div_data.division.item())

