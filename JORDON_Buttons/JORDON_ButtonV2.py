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
        self.Buttons = "00000000000"

    def bin(self):
        Buttons = bin(self.gp.get_pressed())
        MyString = '0' * (10 - len(Buttons))
        return MyString + Buttons[2:]

    def refresh(self):
        self.LastState = self.Buttons
        self.Buttons = self.bin()

    def __pressed(self,index):
        #index = 1
        #self.refresh() # take out when running
        if self.LastState[index] == "0" and self.Buttons[index] == "1":
            return "PRESSED"
        else:
            return False

    def B(self):
        return self.__pressed(7)

    def A(self):
        return self.__pressed(6)

    def START(self):
        return self.__pressed(5)

    def SELECT(self):
        return self.__pressed(4)

    def RIGHT(self):
        return self.__pressed(3)

    def DOWN(self):
        return self.__pressed(2)

    def UP(self):
        return self.__pressed(1)

    def LEFT(self):
        return self.__pressed(0)