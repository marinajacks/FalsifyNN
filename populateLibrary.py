# Filling up the Library with the roads and cars


from PIL import Image, ImageDraw
from scipy import misc
from collections import namedtuple
from modify_primitives.components import ImageFile
from modify_primitives import library
import numpy as np
from ml_primitives import uniform_sampling
from modify_primitives.utils import coord, rect, scale_image, fit_image, generateImage, shift_xz, modifyImageLook, cluster_in_abstract

def populateLibrary():
    # Create a Library
    Lib = library()

    # Populate the library with roads
    Lib.addRoad(ImageFile(Image.open("./pics/roads/desert.jpg"), "Desert Road"), coord(800, 540), coord(100, 950), coord(1500,950), [coord(800,950)])
    Lib.addRoad(ImageFile(Image.open("./pics/roads/countryside.jpg"), "Countryside Road"), coord(810, 540),coord(100, 1000), coord(1500, 1000), [coord(775,1000)])
    Lib.addRoad(ImageFile(Image.open("./pics/roads/city.jpg"), "City Road"), coord(810, 675), coord(100, 925), coord(1500, 925), [coord(508, 925), coord(1025, 925)])
    Lib.addRoad(ImageFile(Image.open("./pics/roads/cropped_desert.jpg"), "Cropped Desert Road"), coord(75, 120), coord(100,500), coord(1400, 500), [coord(66,500)])

    for i in range(134,182):
        Lib.addRoad(ImageFile(Image.open("./pics/roads/forest/0000000" + str(i) + ".png"), "Forest Road"), coord(675, 238),
                    coord(80, 500), coord(840, 504), [coord(340, 499)])







    # Populate the library with cars
    Lib.addCar(ImageFile(Image.open("./pics/cars/bmw_rear.png"), "BMW"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/tesla_rear.png"), "Tesla"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/suzuki_rear.png"), "Suzuki"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/modified_bmw.png"), "Modified BMW"))

    return Lib

print(cluster_in_abstract(rect(coord(100,500), coord(75, 120), coord(75, 120), coord(1400, 500)), rect(coord(0.2, 0.2), coord(0.2, 0.4), coord(0.4, 0.4), coord(0.4, 0.2))))