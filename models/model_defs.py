##Use this file to generate your models and have them stored in a single class so you can just load them into the playground
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, BatchNormalization, Flatten, Dropout, Dense, GlobalMaxPooling2D
from tensorflow.keras import Sequential, Model
from tensorflow.keras.applications.vgg16 import VGG16

'''
    Initial 2-stage convolution followed by some dense layers and a softmax
    Yields about 65-70% accuracy

    Improvements should be made after looking at vgg and others
'''
def basic_conv_2_stage(convolution_window, **kwargs):
    layers = [
        Input(shape=[28, 28, 3]),
    
        Conv2D(32, kernel_size=convolution_window, strides=(2,2), padding='same', activation='relu'),
        Conv2D(32, kernel_size=convolution_window, padding='same', activation='relu'),
        MaxPooling2D(),
        BatchNormalization(),
        Dropout(0.25),
    
        Conv2D(64, kernel_size=convolution_window, padding='same', activation='relu'),
        Conv2D(64, kernel_size=convolution_window, padding='same', activation='relu'),
        MaxPooling2D(),
        BatchNormalization(),
        Dropout(0.4),
    
        Flatten(),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(32, activation='relu'),
        Dropout(0.5),
        Dense(7, activation='softmax')
    ]

    return Sequential(layers)

def modded_VGG():
    vgg_model = VGG16(weights='imagenet')
    vgg_output_layer = vgg_model.output
    

    # o = Dense(7, activation='softmax')(g)
    # return Model(vgg_output_layer, o)
    
