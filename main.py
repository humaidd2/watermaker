from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class ImageWatermarker:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.watermark_image = self.image.copy()
        self.draw = ImageDraw.Draw(self.watermark_image)
        self.width, self.height = self.image.size

    def add_watermark(self, text, output_path):
        
        # Choose a font and size for the watermark
        font_size = min(self.width, self.height) // 30
        font = ImageFont.truetype("arial.ttf", font_size)

        # Calculate the number of repetitions in both directions
        repetitions_x = int((self.width / font_size) ** 0.5)
        repetitions_y = int((self.height / font_size) ** 0.5)

        # Calculate the spacing between repetitions
        spacing_x = self.width / repetitions_x
        spacing_y = self.height / repetitions_y

        # Add Watermark
        for i in range(repetitions_x):
            for j in range(repetitions_y):
                x = int(i * spacing_x)
                y = int(j * spacing_y)
                self.draw.text((x, y), text, fill=(220, 220, 220), font=font)

        # Save the watermarked image to a file
        self.watermark_image.save(output_path)


image_path = "rainbow.jpg"
watermarker = ImageWatermarker(image_path)

watermark_text = input("What text would you like to display as watermark?: ")
output_path = "watermarked_image.jpg"

watermarker.add_watermark(watermark_text, output_path)
