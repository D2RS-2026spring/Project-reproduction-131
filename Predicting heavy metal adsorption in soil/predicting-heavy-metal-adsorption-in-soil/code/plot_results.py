import matplotlib.pyplot as plt
import numpy as np

# 从终端输出中提取的 10 折交叉验证结果（Train/Valid/Test RMSE）
train_rmse = [0.1887, 0.1704, 0.1774, 0.2073, 0.1979, 0.1857, 0.1661, 0.1720, 0.1985, 0.2071]
valid_rmse = [0.0916, 0.0261, 0.0393, 0.0439, 0.0402, 0.0330, 0.0268, 0.0259, 0.0385, 0.0344]
test_rmse = [0.0388, 0.0182, 0.0007, 0.0404, 0.0319, 0.0210, 0.0170, 0.0186, 0.0187, 0.0358]

folds = np.arange(1, len(train_rmse)+1)

plt.figure(figsize=(10, 6))
plt.plot(folds, train_rmse, marker='o', label='Train RMSE', color='#1f77b4')
plt.plot(folds, valid_rmse, marker='s', label='Validation RMSE', color='#ff7f0e')
plt.plot(folds, test_rmse, marker='^', label='Test RMSE', color='#2ca02c')

plt.title('Random Forest Cross-Validation RMSE', fontsize=14)
plt.xlabel('Fold Number', fontsize=12)
plt.ylabel('RMSE', fontsize=12)
plt.xticks(folds)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# 直接保存到当前文件夹
plt.savefig('rmse_comparison.png', dpi=300)
plt.show()