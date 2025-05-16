def bias(x, disordered_ind=6, scale=1.02):
    y = x.copy()
    y[disordered_ind] = y[disordered_ind] * scale

    return y

