def on_button_pressed_a():
    microIoT.microIoT_SendMessage(convert_to_text(pins.analog_read_pin(AnalogPin.P0)),
        microIoT.TOPIC.TOPIC_0)
    microIoT.microIoT_showUserText(2,
        "Light:" + convert_to_text(pins.analog_read_pin(AnalogPin.P0)))
    basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

wifi_name = "izowifi"
password = "izo1234@"
iot_id = "lmZB9bXGR"
iot_pwd = "liWfrxXMgz"
topic_0 = "qwPmNL37g"
basic.show_number(0)
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI(wifi_name, password)
basic.show_number(1)
microIoT.microIoT_MQTT(iot_id, iot_pwd, topic_0, microIoT.SERVERS.ENGLISH)
basic.show_number(2)
microIoT.microIoT_showUserText(0, wifi_name)

def on_forever():
    pass
basic.forever(on_forever)
