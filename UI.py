import PySimpleGUI as sg


def preliminaire(x, y, order):
    if order == 'x':
        return x * y
    elif order == '+':
        return x + y
    elif order == '/':
        if y == 0:
            return "Error: Division by zero"
        return x / y
    elif order == '//':
        if y == 0:
            return "Error: Division by zero"
        return x // y
    

layout = [
      [sg.Input(key='-DISPLAY-', readonly=True, use_readonly_for_disable=True, 
              text_color='white', background_color='black')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*')],
    [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('/')],
    [sg.Button("C"), sg.Button("Done")]
]

window = sg.Window('Calculator', layout, margins=(100, 50))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Done":
        break

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.']:
        current_value = values['-DISPLAY-']
        new_value = current_value + event
        window['-DISPLAY-'].update(new_value)

    elif event == 'C':
        window['-DISPLAY-'].update('')

    elif event == '=':
        expression = values['-DISPLAY-']
        for op in ['+', '-', '*', '/', '//']:
            if op in expression:
                x, y = expression.split(op)
                result = preliminaire(float(x), float(y), op.replace('*', 'x'))  # Ensure the correct operator is passed
                if isinstance(result, str):  # Check if result is an error message
                    window['-DISPLAY-'].update(result)
                else:
                    window['-DISPLAY-'].update(str(result))
                break
window.close()
