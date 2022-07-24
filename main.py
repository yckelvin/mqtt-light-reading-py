wifi_name = "izowifi"
password = "izo1234@"
iot_id = "lmZB9bXGR"
iot_pwd = "liWfrxXMgz"
topic_0 = "qwPmNL37g"
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI(wifi_name, password)
microIoT.microIoT_MQTT(iot_id, iot_pwd, topic_0, microIoT.SERVERS.ENGLISH)
microIoT.microIoT_showUserText(0, wifi_name)

def on_forever():
    microIoT.microIoT_SendMessage(convert_to_text(pins.analog_read_pin(AnalogPin.P0)),
        microIoT.TOPIC.TOPIC_0)
    microIoT.microIoT_showUserText(2,
        "Light:" + convert_to_text(pins.analog_read_pin(AnalogPin.P0)))
basic.forever(on_forever)
