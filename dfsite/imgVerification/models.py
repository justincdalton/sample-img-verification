from PIL import Image, ImageFont, ImageDraw, ImageOps
import random

# Helper class to create a random verification image
class ImgVerificationHelper:
    borderThick = 2
    imgWidth = 96 - (borderThick * 2)
    imgHeight = 36 - (borderThick * 2)
    numChars = 5

    def __init__(self):
        self.numString = ""
        self.minX = 2
        self.minY = 2
        self.create_img()

    def create_img(self):
        random.seed()

        self.img = Image.new("RGB", (self.imgWidth, self.imgHeight), "#FFFFFF")

        draw = ImageDraw.Draw(self.img)

        for i in range(0, self.numChars):
            fontSize = random.randint(11,16)
            font = ImageFont.truetype("imgVerification/resources/DroidSans.ttf", fontSize)

            if (font > 13):
                char = random.randint(0,9)
            else:
                char = random.randint(1,9)

            char = str(char)

            fontWidth, fontHeight = font.getsize(char)

            self.numString += char

            xOffset = self.minX + random.randint(3,10)
            self.minX = xOffset + fontWidth

            maxY = self.imgHeight - self.borderThick - fontHeight
            yOffset = random.randint(self.minY, maxY)

            draw.text((xOffset, yOffset), char, "#000000", font=font)

        self.img = ImageOps.expand(self.img, border=self.borderThick,fill='#000000')