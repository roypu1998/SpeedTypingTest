from random_sentences import random_choice
import PySimpleGUI as sg

size=(0, 1)
font=('Helvetica', 14,'bold')
text = f'{random_choice()} {random_choice()} {random_choice()}'
sg.theme('DarkBrown1')
counter = 1
layout1 = [
    [sg.Text(f"Sentence {counter}", size=size, font=font, key='-TEXT-'),sg.VerticalSeparator(), sg.Text(text,size=size, font=font,text_color='white',justification='center', key='-TEXT-GENERATE-')],
    [sg.Text("Time:", size=size, font=font), sg.VerticalSeparator(),sg.Text("00:00.00",size=size, font=font,justification='center', key='-TIME-COUNT-')],
    [sg.Text("Typing Text Here",size=size, font=font),sg.VerticalSeparator(), sg.In(size=(25, 1), enable_events=True, key ='-IN-GENERATE-')],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator(),sg.Button("START", key='-START-'),sg.VerticalSeparator(),sg.Button("⌫", key='-RESET-')],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.VerticalSeparator("")],
    [sg.Text("Grade",size=size, font=font),sg.VerticalSeparator(), sg.In(size=(5, 1), enable_events=True, key ='-GRADE-IN-')]
]
layout2 = [
    [sg.Multiline(size=(50, 30), key='-OUTPUT-', autoscroll=True)],
]

layout = [[sg.Column(layout1,element_justification='left', key='-COL1-'), sg.Column(layout2, visible=True,element_justification='right', key='-COL2-')]]

window = sg.Window(title="Speed Typing Test",text_justification='l', layout=layout)

timer_running, timer = False, 0
text_generate = window['-TEXT-GENERATE-'].DisplayText
flag, flagText = 0, 0
time_stop = ""

while True:
    event, values = window.read(timeout=10)
    val_text = values['-IN-GENERATE-']

    if event == sg.WIN_CLOSED:
        exit(1)

    if event == '-IN-GENERATE-' and len(val_text) == 1:
        flagText = 1

    if event == '-RESET-':
        timer_running, timer = False, 0
        window['-TIME-COUNT-'].update('{:02d}:{:02d}.{:02d}'.format(0, 0, 0))
        window['-IN-GENERATE-'].update("")

    if val_text == text_generate or val_text == text_generate.lower() :
        output_text = window['-OUTPUT-'].get()
        timer_running = False
        time_stop = window['-TIME-COUNT-'].DisplayText
        window.FindElement('-OUTPUT-').Update(f'{output_text}\n[SUCCESS]: {val_text} --> [TIME]: {time_stop}')
        flag = 1
        flagText = 0
        time_stop = time_stop[3:8]

    if event == '-START-' or flagText == 1:
        timer_running = True

    if timer_running:
        window['-TIME-COUNT-'].update('{:02d}:{:02d}.{:02d}'.format((timer // 100) // 60, (timer // 100) % 60, timer % 100))
        timer+=1

    if flag == 1 :
        text = f'{random_choice()} {random_choice()} {random_choice()}'
        counter+=1
        window['-TEXT-'].update(f"Sentence {counter}")
        window['-TEXT-GENERATE-'].update(text)
        text_generate = window['-TEXT-GENERATE-'].DisplayText
        flag = 0
    if len(time_stop) > 0:
        if float(time_stop) > 5 :
            window.FindElement('-GRADE-IN-').Update('F')
        elif float(time_stop) > 4.5 :
            window.FindElement('-GRADE-IN-').Update('E')
        elif float(time_stop) > 4 :
            window.FindElement('-GRADE-IN-').Update('D')
        elif float(time_stop) > 3.5:
            window.FindElement('-GRADE-IN-').Update('C')
        elif float(time_stop) > 3  :
            window.FindElement('-GRADE-IN-').Update('B')
        elif float(time_stop) > 2.5  :
            window.FindElement('-GRADE-IN-').Update('B+')
        elif float(time_stop) > 2  :
            window.FindElement('-GRADE-IN-').Update('A')
        else:
            window.FindElement('-GRADE-IN-').Update('A+')

