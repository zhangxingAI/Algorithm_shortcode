import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.mixture import GaussianMixture
import os
import pandas as pd
def apply_grayscale(image_path):
    original_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    return gray_image
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
        print(f"Range {i + 1}: [{int(means[i])}, {int(stds[i])}]")

    return means, stds

def apply_intensity_quantization(gray_image, intervals):
    mapping_table = np.zeros(256, dtype=np.uint8)

    for interval, target_value in intervals:
        lower_bound, upper_bound = interval
        mapping_table[lower_bound:upper_bound+1] = target_value

    result_image = cv2.LUT(gray_image, mapping_table)
    return result_image

def filter_spot(gray_image, spot_threshold):
    height, width = gray_image.shape
    visited = np.zeros((height, width), dtype=bool)
    filtered_spot = []
    del_spot = []
    num =0
    area =0

    def dfs(i, j, current_spot):
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            if 0 <= x < height and 0 <= y < width and not visited[x, y] and gray_image[x, y] == 0:
                visited[x, y] = True
                current_spot.append((x, y))
                stack.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

    for i in range(height):
        for j in range(width):
            if not visited[i, j] and gray_image[i, j] == 0:
                current_spot = []
                dfs(i, j, current_spot)

                if len(current_spot) > spot_threshold:
                    filtered_spot.extend(current_spot)
                    num +=1
                    area += len(current_spot)
                else:
                    del_spot.extend(current_spot)

    filtered_image = gray_image
    for i, j in filtered_spot:
        filtered_image[i, j] = 0
    for i, j in del_spot:
        filtered_image[i, j] = 130

    white_image = np.full_like(gray_image, 255)
    for i, j in filtered_spot:
        white_image[i, j] = 0

    area_p = round(area/(height*width),4)
    return filtered_image,white_image,num,area_p

def interval(means,stds):

    if len(means) >1:
        max_index = np.argmax(means)
        min_index = np.argmin(means)
        m = int(means[min_index] + 1.2 * stds[min_index])
        n = int(means[max_index] + 1.960 * stds[max_index])
    elif stds[0] < 18:
        m = min(int(means[0] - 3.291 * stds[0]),80)
        n = int(means[0] + 1.960 * stds[0])
    else:
        m = max(int(means[0] - 1.96 * stds[0]),100)
        n = int(means[0] + 0.5 * stds[0])

    return m,n

def process(image_path, area_threshold):
    gray_image = apply_grayscale(image_path)
    means, stds = separate_distributions(gray_image, 3, 40)

    # 自定义设置每个区间的范围和目标值
    m,n = interval(means,stds)
    print((0, m, n, 255))
    intervals_and_targets = [((0, m), 0), ((m+1, n), 130), ((n+1, 255), 200)]
    # 对灰度图进行区间化处理
    result_image_quantized = apply_intensity_quantization(gray_image, intervals_and_targets)

    # 进行筛选
    filtered_image,white_image,num,area = filter_spot(result_image_quantized, area_threshold)
    return filtered_image,white_image,num,area
    # 保存结果

def process_images_in_folder(folder_path, area_threshold, savefig):
    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    nums = []
    areas =[]
    names = []
    for image_file in image_files:
        # 构造完整的图片文件路径
        image_path = os.path.join(folder_path, image_file)

        # 读取图片，进行处理，并保存为新文件
        print(image_file.split('.')[0])
        filtered_image,white_image,num,area = process(image_path, area_threshold)
        nums.append(num)
        areas.append(area)
        names.append(image_file.split('.')[0])
        df = pd.DataFrame({'名称': names, '孔隙个数': nums, '孔隙面积占比': areas})
        # 将 DataFrame 写入 CSV 文件
        df.to_csv('孔隙.csv', index=False)

        # 构造保存的文件名，添加"gray"后缀
        filtered_image_name = os.path.splitext(image_file)[0] + '_gray' + os.path.splitext(image_file)[1]
        filtered_image_path = os.path.join(folder_path, filtered_image_name)

        # 构造保存的文件名，添加"gray"后缀
        white_image_name = os.path.splitext(image_file)[0] + '_white' + os.path.splitext(image_file)[1]
        white_image_path = os.path.join(folder_path, white_image_name)

        # 保存处理后的图片
        if savefig:
            cv2.imwrite(filtered_image_path, filtered_image)
            cv2.imwrite(white_image_path, white_image)

# 用法示例
image_path = "image"
area_threshold = 10
savefig = True #False不保存，True保存

process_images_in_folder(image_path, area_threshold, savefig)


