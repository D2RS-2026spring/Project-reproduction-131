import matplotlib.pyplot as plt
import numpy as np

# 所有模型测试集结果（从你的运行结果提取）
models = [
    'Linear', 'Ridge', 'SVM', 'CART',
    'KNN', 'RF', 'ET', 'GB'
]

test_rmse = [
    0.0810, 0.0810, 0.1111, 0.0815,
    0.0676, 0.0678, 0.0458, 0.0369
]

test_r2 = [
    0.4023, 0.4030, 0.2035, 0.3942,
    0.5939, 0.5605, 0.8081, 0.8677
]

# 画图
plt.figure(figsize=(12,5))

# RMSE
plt.subplot(1,2,1)
plt.bar(models, test_rmse, color='#ff7f0e')
plt.title('Test RMSE of All Models')
plt.xticks(rotation=45)
plt.ylabel('RMSE')

# R2
plt.subplot(1,2,2)
plt.bar(models, test_r2, color='#2ca02c')
plt.title('Test R² of All Models')
plt.xticks(rotation=45)
plt.ylabel('R²')

plt.tight_layout()
plt.savefig('all_models_compare.png', dpi=300)
plt.show()