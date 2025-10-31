from micropython import const
import framebuf

class SSD1306:
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MONO_VLSB)

    def show(self):
        for page in range(0, self.pages):
            self.i2c.writeto(self.addr, bytearray([0xB0 | page]))
            self.i2c.writeto(self.addr, b'\x00')
            self.i2c.writeto(self.addr, b'\x10')
            self.i2c.writeto(self.addr, self.buffer)

class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        super().__init__(width, height, external_vcc)
