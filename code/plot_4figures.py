import matplotlib.pyplot as plt
import numpy as np

# ====================== 从你的运行结果中提取的真实数据 ======================
models = ['Linear', 'Ridge', 'SVM', 'CART', 'KNN', 'RF', 'ET', 'GB']

# 测试集 RMSE
test_rmse = [0.0810, 0.0810, 0.1111, 0.0815, 0.0676, 0.0678, 0.0458, 0.0369]

# 测试集 R²
test_r2 = [0.4023, 0.4030, 0.2035, 0.3942, 0.5939, 0.5605, 0.8081, 0.8677]

# 训练集 RMSE
train_rmse = [0.0755, 0.0755, 0.0993, 0.0755, 0.0309, 0.0447, 0.0335, 0.0272]

# 训练集 R²
train_r2 = [0.2816, 0.2815, 0.2525, 0.2816, 0.8788, 0.7482, 0.8724, 0.9151]

# ====================== 开始绘制 4 张图 ======================
plt.rcParams['font.sans-serif'] = ['Arial']
plt.figure(figsize=(16, 12))

# 图1：测试集 RMSE
plt.subplot(2, 2, 1)
plt.bar(models, test_rmse, color='#ff7f0e')
plt.title('Test RMSE of All Models', fontsize=14)
plt.ylabel('RMSE', fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)

# 图2：测试集 R²
plt.subplot(2, 2, 2)
plt.bar(models, test_r2, color='#2ca02c')
plt.title('Test $R^2$ of All Models', fontsize=14)
plt.ylabel('$R^2$', fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)

# 图3：训练集 RMSE
plt.subplot(2, 2, 3)
plt.bar(models, train_rmse, color='#1f77b4')
plt.title('Train RMSE of All Models', fontsize=14)
plt.ylabel('RMSE', fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)

# 图4：训练集 R²
plt.subplot(2, 2, 4)
plt.bar(models, train_r2, color='#d62728')
plt.title('Train $R^2$ of All Models', fontsize=14)
plt.ylabel('$R^2$', fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('model_4panel_results.png', dpi=300)
plt.show()