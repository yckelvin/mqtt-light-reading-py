input.onButtonPressed(Button.A, function on_button_pressed_a() {
    microIoT.microIoT_SendMessage(convertToText(pins.analogReadPin(AnalogPin.P0)), microIoT.TOPIC.topic_0)
    microIoT.microIoT_showUserText(2, "Light:" + convertToText(pins.analogReadPin(AnalogPin.P0)))
    basic.pause(100)
})
let wifi_name = "izowifi"
let password = "izo1234@"
let iot_id = "lmZB9bXGR"
let iot_pwd = "liWfrxXMgz"
let topic_0 = "qwPmNL37g"
basic.showNumber(0)
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI(wifi_name, password)
basic.showNumber(1)
microIoT.microIoT_MQTT(iot_id, iot_pwd, topic_0, microIoT.SERVERS.English)
basic.showNumber(2)
microIoT.microIoT_showUserText(0, wifi_name)
basic.forever(function on_forever() {
    
})
