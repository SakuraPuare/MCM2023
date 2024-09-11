import numpy as np
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
from keras.models import Sequential
from matplotlib import pyplot as plt


# 构建卷积神经网络
# 输入三维数据，输出一维数据
def build_cnn_model(input_shape, output_shape):
    """

    :param input_shape: 输入数据的形状
    :param output_shape: 输出数据的形状
    :return:  返回一个模型
    """
    model = Sequential()
    # 卷积层 32个卷积核，卷积核大小为3，激活函数为relu，输入数据形状为input_shape
    model.add(Conv1D(filters=16, kernel_size=3, activation='relu', input_shape=input_shape))
    model.add(MaxPooling1D(pool_size=1))
    model.add(Flatten())
    model.add(Dense(50, activation='relu'))
    model.add(Dense(output_shape, activation='linear'))
    model.compile(loss='mse', optimizer='adam')
    return model


model = build_cnn_model((3, 1), 1)
# 编译模型
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

x = [(0.148888889, 287.9, 180),
     (0.633846154, 289, 211.1111111),
     (0.165294118, 291.8, 97.22222222),
     (0.537058824, 297.8, 140.5555556),
     (0.281333333, 296.7058824, 118.3333333),
     (0.058235294, 300.44, 131.1111111),
     (0.017222222, 300, 203.8888889),
     (0.324444444, 300.5176471, 130.5555556),
     (0.372857143, 301.3333333, 58.88888889),
     (0.413333333, 296.144, 51.25),
     (0.108235294, 291.7142857, 66.42857143),
     (0.82, 283.6666667, 204.4444444),
     (0.22, 283.52, 73.33333333),
     (0.48, 290.24, 115),
     (0.703333333, 294.92, 127.7777778),
     (0.257142857, 296.3176471, 200.5555556),
     (0.319444444, 298.4631579, 97.22222222),
     (0.693333333, 301.55, 130),
     (0.5725, 300.7538462, 69.375),
     (0.228823529, 302.12, 58.125),
     (0.02875, 300.8857143, 65),
     (0.884, 298.5636364, 82.77777778),
     (0.64125, 290.7636364, 93.33333333),
     (0.023888889, 289.5, 147.2222222),
     (0.506666667, 285.8, 107.2222222),
     (0.385333333, 287.3, 107.7777778),
     (0.097, 296.25, 95),
     (0.077058824, 298.8235294, 160),
     (0.43375, 300.1, 109.4444444),
     (0.420769231, 302, 72.5),
     (0.561176471, 301.8, 101.6666667),
     (0.533333333, 302.57, 108.3333333),
     (0.46, 300.5692308, 72.22222222),
     (0.002857143, 297.3777778, 59.375),
     (0.007647059, 292.1789474, 154.4444444),
     (0, 289.88, 261.6666667),
     (0, 285.2, 125.5555556),
     (0.13875, 289.6666667, 148.3333333),
     (0.1775, 294.1333333, 101.1111111),
     (0.83, 298.2, 141.6666667),
     (0.50625, 300.02, 52.85714286),
     (0.728571429, 304.8636364, 71.875),
     (0.703333333, 304.04, 91.66666667),
     (0.02875, 303.0421053, 94.44444444),
     (0.016666667, 303.0090909, 55),
     (0.448823529, 300.71, 71.875),
     (0.204444444, 294.9894737, 68.88888889),
     (0.36, 289.46, 203.3333333),
     (0.0125, 286.8615385, 91.11111111),
     (0.5375, 292.34, 96.11111111),
     (0.129411765, 297.4, 164.4444444),
     (0, 298.61, 234.4444444),
     (0.24, 299.6545455, 126.1111111),
     (0.124117647, 301.28, 114.4444444),
     (0.301111111, 301.8363636, 97.22222222),
     (0.29, 299.7826087, 135),
     (0.338333333, 298.0888889, 145),
     (0.188333333, 293.7090909, 73.75),
     (0, 284.6, 75.71428571),
     (0.045, 280.9769231, 146.25),
     (0.27, 289.9684211, 106.6666667),
     (0, 291.1625, 115),
     (0.228333333, 295.9368421, 154.4444444),
     (0.53, 301.15, 101.1111111),
     (0.547142857, 300.7181818, 114.4444444),
     (0.415, 301.3454545, 114.4444444),
     (0.5775, 302.0818182, 77.5),
     (0, 301.925, 95),
     (0.772, 298.1, 163.125),
     (0.428888889, 288.0384615, 222.7777778),
     (0.856363636, 287.1411765, 145),
     (0.386666667, 284.36, 146.6666667),
     (0.193333333, 290.15, 83.88888889),
     (0.213529412, 293.1894737, 117.7777778),
     (0, 297.9, 78.33333333),
     (0.139166667, 299.8, 111.6666667),
     (0.763333333, 302.4235294, 89.375),
     (0.99, 305.4333333, 75),
     (0.945, 305, 100),
     (0.4325, 292.9625, 125),
     (0.488, 291.86, 94.44444444),
     (0.973333333, 286.0823529, 124.4444444),
     (0, 287, 173.8888889),
     (0, 288.8, 261.6666667),
     (0.098823529, 294.6, 168.3333333),
     (0.270769231, 297.2352941, 172.7777778),
     (0.072941176, 298.7272727, 82.22222222),
     (0.271764706, 301.4428571, 77.22222222),
     (0.712666667, 301.0142857, 81.66666667),
     (0.362142857, 301.2615385, 108.8888889),
     (0.056666667, 299.96, 85.55555556),
     (0.549090909, 297.9333333, 136.1111111),
     (0.373333333, 292.3, 90.625),
     (0, 288.14, 72.77777778),
     (0.637142857, 288.725, 89.44444444),
     (0.763333333, 292.8235294, 70.55555556),
     (0.3525, 295.1, 156.6666667),
     (0.173888889, 297.6615385, 97.5),
     (0.141818182, 298.34, 99.44444444),
     (0.742857143, 300.0941176, 158.3333333),
     (0.975, 301.3666667, 173.3333333),
     (0.14625, 301.22, 130),
     (0.275, 298.6823529, 94.44444444),
     (0.432777778, 296.9, 83.33333333),
     (0.869, 291.6588235, 52.5),
     (0.325294118, 292.9571429, 101.1111111),
     (0.2975, 289.1882353, 93.88888889),
     (0.345, 296.0461538, 168.3333333),
     (0.66, 298.34, 95.55555556),
     (0.480909091, 299.4, 77.77777778),
     (0.302941176, 301.36, 71.11111111),
     (0.453333333, 301.94, 120.5555556),
     (0.308235294, 301.92, 114.4444444),
     (0.11, 300.56, 67.14285714),
     (0.200833333, 298.9666667, 64.375),
     (0.293529412, 296.2666667, 103.3333333),
     (0.495, 286.52, 73.33333333)]
y = [0.388569444,
     0.363805556,
     0.36673913,
     0.463819444,
     0.649972222,
     0.683111111,
     0.664763889,
     0.679,
     0.629138889,
     0.597013889,
     0.493680556,
     0.417222222,
     0.399833333,
     0.382083333,
     0.391708333,
     0.476666667,
     0.664152778,
     0.69043662,
     0.658944444,
     0.664208333,
     0.645944444,
     0.580347222,
     0.481875,
     0.407222222,
     0.381027778,
     0.367722222,
     0.388819444,
     0.596388889,
     0.672430556,
     0.683875,
     0.667277778,
     0.666166667,
     0.634848485,
     0.556944444,
     0.473958333,
     0.430347222,
     0.406055556,
     0.399583333,
     0.418680556,
     0.603625,
     0.674236111,
     0.669513889,
     0.676309859,
     0.664492958,
     0.616805556,
     0.57952381,
     0.478121212,
     0.40725,
     0.369303571,
     0.398447761,
     0.4625,
     0.664180556,
     0.696833333,
     0.684888889,
     0.669208333,
     0.631597222,
     0.594722222,
     0.521944444,
     0.445763889,
     0.414902778,
     0.408722222,
     0.425,
     0.552847222,
     0.669263889,
     0.675944444,
     0.682680556,
     0.676819444,
     0.62125,
     0.604097222,
     0.534791667,
     0.440625,
     0.441222222,
     0.426361111,
     0.424236111,
     0.566527778,
     0.672236111,
     0.670694444,
     0.683236111,
     0.642986111,
     0.61375,
     0.540277778,
     0.500694444,
     0.430666667,
     0.409,
     0.422166667,
     0.473680556,
     0.641263889,
     0.641888889,
     0.650041667,
     0.651666667,
     0.633888889,
     0.604930556,
     0.571736111,
     0.499375,
     0.4425,
     0.407055556,
     0.297125,
     0.346388889,
     0.708863636,
     0.737,
     0.737142857,
     0.756875,
     0.683478261,
     0.744,
     0.490333333,
     0.423369565,
     0.417984127,
     0.415194444,
     0.405833333,
     0.500694444,
     0.665972222,
     0.677888889,
     0.703625,
     0.643069444,
     0.642986111,
     0.584930556,
     0.492361111,
     ]

x = np.array(x)
y = np.array(y)

x_train = x[:int(len(x) * 0.8)]
y_train = y[:int(len(y) * 0.8)]
x_test = x[int(len(x) * 0.8):]
y_test = y[int(len(y) * 0.8):]

# 训练模型
model.fit(x_train, y_train, epochs=1000, batch_size=12, verbose=1)
# 其中，x_train和y_train是训练数据，epochs是训练的轮数，batch_size是每次训练的样本数，verbose是日志显示，0为不在标准输出流输出日志信息，1为输出进度条记录，2为每个epoch输出一行记录。
# x_train 的格式为 (samples, time steps, features) ，y_train 的格式为 (samples, features) 。

yp_test = model.predict(x_test)
yp = model.predict(x)


# 评估模型
loss, accuracy = model.evaluate(x_test, y_test)
print('test loss', loss)
print('test accuracy', accuracy)

# 画图
plt.plot(y, 'r')
plt.plot(yp, 'b')
# plt.plot(y_test, 'g')
# plt.plot(yp_test, 'y')
plt.show()
pass