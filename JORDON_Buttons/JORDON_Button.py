import board
import digitalio
import gamepadshift

class Buttons:
    #self.gp = gamepadshift.GamePadShift(1,1,1)
    
    def __init__(self):
        data = digitalio.DigitalInOut(board.BUTTON_OUT)
        clock = digitalio.DigitalInOut(board.BUTTON_CLOCK)
        latch = digitalio.DigitalInOut(board.BUTTON_LATCH)
        self.gp = gamepadshift.GamePadShift(clock, data, latch)

    def bin(self):
        Buttons = bin(self.gp.get_pressed())
        MyString = ""
        for i in range(10 - len(Buttons)):
            MyString = MyString + "0"
        return MyString + Buttons[2:]

    def B(self):
        MyVar = self.bin()
        if MyVar[7] == "1":
            return True
        else:
            return False

    def A(self):
        MyVar = self.bin()
        if MyVar[6] == "1":
            return True
        else:
            return False

    def START(self):
        MyVar = self.bin()
        if MyVar[5] == "1":
            return True
        else:
            return False

    def SELECT(self):
        MyVar = self.bin()
        if MyVar[4] == "1":
            return True
        else:
            return False

    def RIGHT(self):
        MyVar = self.bin()
        if MyVar[3] == "1":
            return True
        else:
            return False

    def DOWN(self):
        MyVar = self.bin()
        if MyVar[2] == "1":
            return True
        else:
            return False

    def UP(self):
        MyVar = self.bin()
        if MyVar[1] == "1":
            return True
        else:
            return False

    def LEFT(self):
        MyVar = self.bin()
        if MyVar[0] == "1":
            return True
        else:
            return False