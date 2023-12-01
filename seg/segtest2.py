import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.mixture import GaussianMixture

def plot_histogram(image):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256], density=True)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    plt.hist(image.flatten(), bins=256, range=[0, 256], density=True, color='black', alpha=0.5)
    return hist, bin_centers

def fit_distributions(data, num_components):
    if num_components == 1:
        # 如果只有一个分量，使用单个正态分布
        mean = np.mean(data)
        std = np.std(data)
        weight = 1.0  # 权重为1
        return [mean], [std], [weight]
    else:
        # 使用混合高斯模型
        gmm = GaussianMixture(n_components=num_components, random_state=100)
        # 将数据重塑为列向量
        data = data.reshape(-1, 1)
        gmm.fit(data)
        means = gmm.means_.flatten()
        stds = np.sqrt(gmm.covariances_).flatten()
        weights = gmm.weights_

        return means, stds, weights

def separate_distributions(image, num_components, min_mean_difference):
    min_difference = 0
    num_components = num_components+1
    while min_difference < min_mean_difference:

        num_components -= 1
        if num_components == 0:
            break

        hist, bin_centers = plot_histogram(image)
        means, stds, weights = fit_distributions(image, num_components)

        # 遍历拟合后的正态分布均值，找到两个均值之间的最小差值
        temp = float('inf')
        min_index_i, min_index_j = -1, -1

        for i in range(num_components):
            for j in range(i + 1, num_components):
                difference = abs(means[i] - means[j])
                if difference < temp:
                    temp = difference
                    min_index_i, min_index_j = i, j
        min_difference = temp
    for i in range(num_components):
        lower_bound = means[i] - 3.291 * stds[i]  # 2.576 对应于正态分布的95%置信度
        upper_bound = means[i] + 3.291 * stds[i]

        print(f"99% Distribution Range for Component {i + 1}: [{lower_bound}, {upper_bound}]")

        plt.plot(bin_centers, norm.pdf(bin_centers, means[i], stds[i]) * weights[i], '--', label=f'Component {i + 1}')

    plt.legend()
    plt.show()

def grayscale_and_fit_distributions(image_path, num_components, min_mean_difference):
    original_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    separate_distributions(gray_image, num_components, min_mean_difference)

# 用法示例
image_path = "image/image8.jpg"
num_components = 4  # 替换为你想要的初始分布个数
min_mean_difference = 40  # 替换为你想要的均值差异阈值
grayscale_and_fit_distributions(image_path, num_components, min_mean_difference)
