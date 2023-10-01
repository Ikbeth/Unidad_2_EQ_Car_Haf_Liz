from keras.utils import load_img, img_to_array, array_to_img, save_img #alternative 2

def getArrayImagen(nombre_archivo, largo = 500, alto = 500):
    img_original = load_img(file, target_size = (largo, alto),color_mode = "grayscale")
    img_en_arreglo = img_to_array(img_original)  # filas, columnas, canales de colores
    return img_en_arreglo

def convolucionar(img_a_convolucinar, kernel_type="blur",largo = 500, alto = 500):
    break_convolution = 1
    match kernel_type:
        case "blur":
            kernel = [
                [-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]
            ]
            div = 1
            break_convolution = 0
        case _:
            print("kernel no valido")
            break_convolution = 1

    if not break_convolution:
        img_convolucionada = []
        for filas in range(1, alto - 1):
            new_fila = []
            for columnas in range(1, largo - 1):

                pixelConvulucionado = 0
                for f_kernel in range(len(kernel)):
                    for c_kernel in range(len(kernel)):
                        pixelConvulucionado += kernel[f_kernel][c_kernel] \
                                               * img_a_convolucinar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)]
                pixelConvulucionado = pixelConvulucionado / div
                new_fila.append(pixelConvulucionado)
            img_convolucionada.append(new_fila)
        return img_convolucionada
    else:
        return None

def plotImages(imgOrginal, imgConvolucionada):
    #plot - 2 imagenes
    import matplotlib.pyplot as plt
    plt.figure(figsize=(5, 5))

    plt.subplot(1, 2, 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(array_to_img(imgOrginal), cmap='gray')

    plt.subplot(1, 2, 2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imgConvolucionada, cmap='gray')

    plt.show()

def maxPooling(stride, img_array, largo, alto):
    img_max_pooling = []
    for filas in range(1, alto - 1, stride):
        new_fila = []
        for columnas in range(1, largo - 1, stride):
            max_pixel = -1
            for f_kernel in range(stride):
                for c_kernel in range(stride):
                    pixel = img_array[filas + f_kernel][columnas + c_kernel]
                    if pixel > max_pixel:
                        max_pixel = pixel
            new_fila.append(float(max_pixel))
        img_max_pooling.append(new_fila)

    # img = array_to_img(img_max_pooling)

    return img_max_pooling


file = './Gato.jpg'
# file = './FIT V.jpg'
# file = './gato.jpeg'

img_array = getArrayImagen(file)
print(img_array.shape)

img_conv = convolucionar(img_array, kernel_type="blur")
img = array_to_img(img_conv)
if not img is None:
    print(img.size)

    plotImages(img_array, img_conv)


img_mp = maxPooling(2, img_conv, 498, 498)
# print(img_mp)
# img = array_to_img(img_mp)
# if not img is None:
#     print(img.size)

plotImages(img_array, img_mp)

save_img('mp.jpg', img_to_array(img_mp))