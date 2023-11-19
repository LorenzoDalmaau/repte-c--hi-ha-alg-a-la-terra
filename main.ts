input.onButtonPressed(Button.A, function () {
    radio.sendString("UWU")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
