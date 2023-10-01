
from keras.utils import load_img, img_to_array, array_to_img, save_img
import matplotlib.pyplot as plt
import os
import shutil


base_location = "./"
source_folder = 'Carlos'

rutaImagen = base_location + source_folder + "/"
imgs = [archivo for archivo in os.listdir(rutaImagen) if archivo.endswith(".jpg")]

os.mkdir(base_location + source_folder + '/edits')

for image in imgs:
    print('.', end='')
    nombre = image.split('.')
    ruta = rutaImagen + '/' + image
    img_original = load_img(ruta)

    array = img_to_array(img_original)
    img = array_to_img(array)

    rutaToSave = rutaImagen + "/edits/" + nombre[0] + ".jpeg"
    save_img(rutaToSave, img)

