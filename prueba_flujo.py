from gpiozero import Button, LED

FLOW_SENSOR_GPIO = 23
count = 0

def count_pulse():
    global count
    count += 1
    print(count)

print("inicio")
flujometro = Button(FLOW_SENSOR_GPIO)
flujometro.when_pressed = count_pulse

flujometro.wait_for_press()

