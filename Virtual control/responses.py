import random
import pydirectinput
import time
import re
import webbrowser
import emoji
import os



def get_response(message) -> str:
    p_message = message.lower()

    discord_to_pc_commands = {
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l',
    'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x',
    'y': 'y', 'z': 'z',

    '0': '0', '1': '1', '2': '2','3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 

    'f1': 'f1', 'f2': 'f2', 'f3': 'f3', 'f4': 'f4', 'f5': 'f5', 'f6': 'f6', 'f7': 'f7', 'f8': 'f8', 'f9': 'f9', 'f10': 'f10', 'f11': 'f11', 'f12': 'f12',

    ')': ')', '!': '!', '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '&': '&', '*': '*', '(': '(', '`': '`', '\\': '\\',

    'up': 'up', 'down': 'down', 'left': 'left', 'right': 'right', 'enter': 'enter',
    'esc': 'esc', 'tab': 'tab', 'caps': 'capslock', 'rshift': 'rshift', 'lshift': 'lshift', 'rctrl': 'rctrl',
    'lctrl': 'lctrl', 'ralt': 'ralt', 'lalt': 'lalt', 'backspace': 'backspace', 'space': 'space',
    'delete': 'delete', 'insert': 'insert', 'home': 'home', 'end': 'end', 'pageup': 'pageup', 'pagedown': 'pagedown',
    'windows': 'win'     
}
       
    repetition_count = 1
    
    parts = p_message.split('xc')

    if len(parts) > 1:

        try:
            repetition_count = int(parts[-1])
            p_message = parts[0]
            
        except ValueError:

            repetition_count = 1
    
    if p_message in discord_to_pc_commands:
        pc_command = discord_to_pc_commands[p_message]

        for _ in range(repetition_count):
            pydirectinput.press(pc_command)

        
    if p_message.startswith('hold'):
        p_message = p_message[4:].strip()
        pc_command = discord_to_pc_commands[p_message]

        for _ in range(repetition_count):
            pydirectinput.keyDown(pc_command)


    if p_message.startswith('release'):
        p_message = p_message[7:]
        pc_command = discord_to_pc_commands[p_message]

        for _ in range(repetition_count):
            pydirectinput.keyUp(pc_command)


    #allows you to write out messages instead of one input at a time
    elif p_message.startswith('string'):
        p_message = p_message[6:].strip()
        pydirectinput.write(p_message)


    #has the bot repeat what you said to it
    elif p_message.startswith('say'):
        p_message = p_message[3:].strip()
        return p_message


    #allows users to type a link and have host pc open it
    elif p_message.startswith('link'):
        p_message = p_message[4:].strip()
        webbrowser.open(p_message)


    #opens a file on the host pc.... Not working yet
    elif p_message.startswith('open'):    
        p_message = p_message[4:].strip()
        f = open((p_message), 'r')
   
    #moves mouse to given cords
    elif p_message.startswith('move cursor'):
        coordinates_match = re.search(r'(\d+),\s*(\d+)', p_message)

        if coordinates_match:
            x = int(coordinates_match.group(1))
            y = int(coordinates_match.group(2))
            pydirectinput.moveTo(x, y)


    elif p_message.startswith('music'):
        song = p_message[5:].strip()
        run = f'start {song}'
        os.system(run)


    #left click on mouse
    elif p_message == 'click':
        pydirectinput.click()   


    #right click on moouse
    elif p_message == 'rclick':
        pydirectinput.rightClick()


    #middle click on mouse
    elif p_message == 'mclick':
        pydirectinput.middleClick()


    if p_message == 'hello':
        return 'Hey there!'
    

    #random dice roll from 1-6
    elif p_message == 'roll':
        return str(random.randint(1, 6))
    

    #I probably should modify this
    elif p_message == '!help':
        return "`This is a help message that you can modify.`" 
    

    #parses message to get two commands and inputs them in the order given
    elif p_message.startswith('x2'):
        p_message = p_message[2:].strip()
        parts = p_message.split()

    if len(parts) >= 2:
        part1 = parts[0]
        part2 = parts[1]
        hold_duration = 0.1
        
        pydirectinput.keyDown(part1)
        pydirectinput.keyDown(part2)
        time.sleep(hold_duration)
        pydirectinput.keyUp(part1)
        pydirectinput.keyUp(part2)
    

    #same as above but for 3 commands 
    elif p_message.startswith('x3'):
        p_message = p_message[2:].strip()
        parts = p_message.split()

    if len(parts) >= 3:
        part1 = parts[0]
        part2 = parts[1]
        part3 = parts[2]
        hold_duration = 0.1
        
        pydirectinput.keyDown(part1)
        pydirectinput.keyDown(part2)
        pydirectinput.keyDown(part3)
        time.sleep(hold_duration)
        pydirectinput.keyUp(part1)
        pydirectinput.keyUp(part2)
        pydirectinput.keyUp(part3)
    
    #allows users to have the bot send an emoji
    elif p_message.startswith('emoji'):
        p_message = p_message[5:]
        p_message1 = f":{p_message}:"
        emoji1 = emoji.emojize(p_message1)
        return emoji1
    

    elif p_message == 'size':
        return "1,1 is the top left corner \n1950,1 is the top right \n1, 1500 is bottom left \n1950, 1100 is bottom right!"
    



    
        

 

    

    
