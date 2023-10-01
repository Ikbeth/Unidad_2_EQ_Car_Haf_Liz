# import keras as k

k.clear_sesion()

data_entrenamiento = './Entrenamiento'
data_validacion = './Prueba'

# PARAMETROS
epocas = 50
alto, largo, = 300, 300
batch_size = 2
pasos = 90
pasos_validacion = 10

kernel1 = (3, 3)
kernel2 = (2, 2)
kernel3 = (3, 3)

tot_kernel1 = 32
tot_kernel2 = 64
tot_kernel3 = 128

stride = (2, 2)  # MAXPOOLING

clases = 5  # TOTAL DE CLASES A CLASIFICAR

lr = 0.0005  # LEARNING RATE

# steps_per_epoch = len(X_train)//batch_size
# validation_steps = len(X_test)//batch_size

# PREPROCESAMIENTO DE IMGENES

entrenamiento_datagen = ImagenDataGenerator(
    rescale= 1./255,
    shear_range= 0.3,
    zoom_range= 0.3,
    horizontal_flip= True
)

prueba_datagen = ImagenDataGenerator(
    rescale= 1./255
)

imagen_entrenamiento = entrenamiento_datagen.flow_from_directory(

)

# SI DATA GENERATOR DA ERROR -> CLASES MAL DEFINIDA
# LOAD IMAGE ERROR -> IMAGEN CORRUPTA/ NOMBRE MAL ESCRITO
# 70/30 IMG EN ENTRENAMIENTO/PRUEBA
# PROYECTO POR SEPARADO

# VERSIONES
# keras 2.10.0
# keras 2.10.0
