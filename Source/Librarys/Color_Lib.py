from colorist import ColorRGB ,BgColorRGB
#https://rgbcolorpicker.com

clear = "\033[0m"

red     : ColorRGB = ColorRGB(255, 000, 000)
green   : ColorRGB = ColorRGB(000, 255, 000)
blue    : ColorRGB = ColorRGB(000, 000, 255)

black   : ColorRGB = ColorRGB(000, 000, 000)
white   : ColorRGB = ColorRGB(255, 255, 255)

yellow  : ColorRGB = ColorRGB(255, 255, 000)
cyan    : ColorRGB = ColorRGB(000, 255, 255)
pink    : ColorRGB = ColorRGB(255, 000, 255)

orange  : ColorRGB = ColorRGB(255, 127, 000)
purple  : ColorRGB = ColorRGB(127, 000, 255)



def RGB(self, red: int, green: int, blue: int) -> None:
    return ColorRGB(red, green, blue)



