import numpy as np
import matplotlib.pyplot as plt
import random

if __name__ != "__main__":
    power1 = 100
    power2 = 300
    power3 = 500
    size = 100
    #массив для хранения координат вышек
    towers = np.zeros((10, 2), dtype='int')
    towers_area = np.zeros((size, size), dtype='int')
    signal_level = np.zeros((size, size))
    #генерируем население случайным образом
    density = np.random.randint(100, size=(size, size))
    gradient_color = 'nipy_spectral_r'
    x = []
    y = []