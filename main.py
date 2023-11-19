def on_button_pressed_a():
    radio.send_string("aaaaaaa")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.clear_screen()
radio.on_received_string(on_received_string)
