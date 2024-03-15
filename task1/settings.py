import numpy as np
import pygame as pg
import moderngl as mgl
import sys
import math

WIN_RES = np.array([1280, 720])
H_RES = WIN_RES // 2
FPS = 60

CONTROL_SPEED = 1

#colors
RED  = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (224, 196, 150)