import matplotlib.pyplot as plt
import numpy as np

def draw_tree(ax, x, y, length, angle, depth):
    if depth == 0:
        return
    
    # 计算树枝的终点
    end_x = x + length * np.cos(angle)
    end_y = y + length * np.sin(angle)
    
    # 绘制树干
    ax.plot([x, end_x], [y, end_y], color='brown', lw=2)
    
    # 画树冠
    tree_crown_radius = length * 0.3
    circle = plt.Circle((end_x, end_y), tree_crown_radius, color='green', alpha=0.7)
    ax.add_patch(circle)
    
    # 递归绘制左右两个分支
    new_length = length * 0.7
    angle_left = angle + np.pi / 6
    angle_right = angle - np.pi / 6

    draw_tree(ax, end_x, end_y, new_length, angle_left, depth - 1)
    draw_tree(ax, end_x, end_y, new_length, angle_right, depth - 1)

def main():
    fig, ax = plt.subplots(figsize=(10, 12))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 初始树干的参数
    initial_length = 10
    initial_angle = np.pi / 2
    initial_depth = 8
    
    # 从树干底部绘制
    draw_tree(ax, 0, 0, initial_length, initial_angle, initial_depth)
    
    plt.show()

if __name__ == "__main__":
    main()