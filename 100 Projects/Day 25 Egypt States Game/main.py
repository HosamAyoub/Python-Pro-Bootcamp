from turtle import Screen, Turtle, onscreenclick, shape
import pandas

screen = Screen()
screen.title('Egypt States Game')
screen.setup(731, 674)
image = 'Egypt_blank_states.gif'
screen.addshape(image)
shape(image)

# def get_mouse_click_cor(x, y):
#     print(f'{int(x)},{int(y)}')
    
# onscreenclick(get_mouse_click_cor)

data = pandas.read_csv('27_states.csv')
english_list_data = data['english name'].to_list()
arabic_list_data = data['arabic name'].to_list()
text = Turtle()
text.hideturtle()
text.penup()
text.speed(0)
score = 0
while True:
    try:
        answer = screen.textinput(title=f'{score}/27 States correct', prompt="What's the state name?\nor if you are done press Cancel").title()
    except:
        break
    if (answer in english_list_data):
        # A way to access element in csv file
        answer_index = english_list_data.index(answer)
        # Another way
        # state_data = data[data['english name'] == answer]
        text.goto(data.at[answer_index, 'x'], data.at[answer_index, 'y'])
        text.write(answer, align='center', font=('Arial', 8, 'normal'))
        english_list_data[answer_index] = None
        arabic_list_data[answer_index] = None
        score += 1
    elif (answer in arabic_list_data):
        answer_index = arabic_list_data.index(answer)
        text.goto(data.at[answer_index, 'x'], data.at[answer_index, 'y'])
        text.write(answer, align='center', font=('Arial', 10, 'normal'))
        english_list_data[answer_index] = None
        arabic_list_data[answer_index] = None
        score += 1

# states_to_learn = pandas.DataFrame()
english_list_data = list(dict.fromkeys(english_list_data))
arabic_list_data = list(dict.fromkeys(arabic_list_data))
try:
    english_list_data.remove(None)
    arabic_list_data.remove(None)
except:
    pass
missing_states = {'Arabic Name' : arabic_list_data, 'English Name' : english_list_data}
data = pandas.DataFrame(missing_states)
data.to_csv('missing_states.csv')