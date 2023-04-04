import pandas as pd
import numpy as np
from scipy.stats import chi2


chat_id = 1841341924 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    return (-min(-x) - 1/2)*2/38**2, (-np.log(alpha)/len(x) - min(-x) - 1/2)*2/38**2
