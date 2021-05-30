import paramiko
import PySimpleGUI as sg
ssh = paramiko.SSHClient()
g = 0

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
layout1 = [[sg.Text("Enter IP: "), sg.InputText()],[sg.Text("Enter Port: "), sg.InputText()],[sg.Text("Enter Username: "), sg.InputText()],[sg.Text('Password: '), sg.InputText()],[sg.Button("CONNECT")]]
window = sg.Window('Log In', layout1, size=(600,200))
values = window.read()

try:
    ssh.connect(values[1][0], values[1][1], values[1][2], values[1][3])
    g = 1
except:
    print("--SSH Connection FAILED--")
if g == 1:
    sg.theme('Dark Blue 13')

    layout2 = [[sg.Text("SSH Connected")],[sg.Text('Command:'), sg.InputText()],[sg.Button("RUN")]]

    window = sg.Window('Run Commands', layout2, size=(600,200))

    while True:
        event, values = window.read()
        if event == 'RUN':
            ssh.exec_command(values[0])
            print("command: " + values[0] + " executed")





