import cv2
import numpy as np

def apply_grayscale(image_path):
    original_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    return gray_image

def apply_intensity_quantization(gray_image, intervals):
    mapping_table = np.zeros(256, dtype=np.uint8)

    for interval, target_value in intervals:
        lower_bound, upper_bound = interval
        mapping_table[lower_bound:upper_bound+1] = target_value

    result_image = cv2.LUT(gray_image, mapping_table)
    return result_image

def filter_islands(gray_image, island_threshold):
    height, width = gray_image.shape
    visited = np.zeros((height, width), dtype=bool)
    filtered_islands = []

    def dfs(i, j, current_island):
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            if 0 <= x < height and 0 <= y < width and not visited[x, y] and gray_image[x, y] == 0:
                visited[x, y] = True
                current_island.append((x, y))
                stack.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

    for i in range(height):
        for j in range(width):
            if not visited[i, j] and gray_image[i, j] == 0:
                current_island = []
                dfs(i, j, current_island)

                if len(current_island) > island_threshold:
                    filtered_islands.extend(current_island)

    filtered_image = np.full_like(gray_image, 255)
    for i, j in filtered_islands:
        filtered_image[i, j] = 1

    return filtered_image

# 输入图片路径
image_path = "image/image3.jpg"  # 替换为你的图像文件路径

# 对图片进行灰度化处理
gray_image = apply_grayscale(image_path)

# 自定义设置每个区间的范围和目标值
intervals_and_targets = [((0, 30), 0), ((31, 109), 50), ((110, 185), 130), ((186, 255), 200)]

# 对灰度图进行区间化处理
result_image_quantized = apply_intensity_quantization(gray_image, intervals_and_targets)
cv2.imwrite("result_image_custom_quantized.jpg", result_image_quantized)
# 设置岛屿的面积阈值
island_area_threshold = 5

# 进行岛屿搜索和筛选
filtered_image = filter_islands(result_image_quantized, island_area_threshold)

# 保存结果
cv2.imwrite("filtered_image_after_quantization.jpg", filtered_image)
