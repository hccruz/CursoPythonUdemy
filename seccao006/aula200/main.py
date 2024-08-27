# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from pathlib import Path
from PIL import Image

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / "heraldo.jpg"
NEW_IMAGE_PATH = ROOT_FOLDER / "heraldo2.jpg"

image = Image.open(IMAGE_PATH)

width, height = image.size
exif = image.info['exif']

# width new_width
# height    ??
new_width = 640
new_height = round(height * (new_width / width))

new_image = image.resize((new_width, new_height))
new_image.save(NEW_IMAGE_PATH, optimize=True, quality=70, exif=exif)
