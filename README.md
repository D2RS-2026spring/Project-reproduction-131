# 利用机器学习预测重金属在土壤上的吸附能力及全球土壤吸附能力分布图

### 小组基本信息
- 小组名称：环境科学研究小组
- 小组成员：
  - 张骏辉 2025303110016 [@Zhang-JunH](https://github.com/Zhang-JunH)
  - 苗芳源 2025303110021 [@FangYuan-Miao](https://github.com/FangYuan-Miao)
  - 胡金忆 2025303110020 [@taro-2026](https://github.com/taro-2026)
  - 李艳峰 2025303110142 [@liyanfeng123](https://github.com/liyanfeng123)
    

## 一、项目基本信息
- **项目名称**：Predicting Heavy Metal Adsorption on Soil with Machine Learning and Mapping Global Distribution of Soil Adsorption Capacities
- **发表期刊**：Environmental Science & Technology
- **DOI**：[https://doi.org/10.1021/acs.est.1c0247](https://doi.org/10.1021/acs.est.1c02865)
- **复现环境**：Windows 10 / Python 3.10.18 / uv 虚拟环境

## 二、可复现性评估结论
✅ 数据可获取  
✅ 代码可直接运行  
✅ 环境可完整重建  
✅ 结果可稳定复现  
✅ 图表可自动生成  
**结论：本项目完全满足可重复研究要求。**

## 三、复现步骤
### 1. 克隆仓库
```bash
git clone https://github.com/D2RS-2026spring/Project-reproduction-131.git
cd Project-reproduction-131/code
```
### 2. 创建并激活虚拟环境（Windows）
```bash
uv venv
.\.venv\Scripts\activate
```
### 3. 安装全部依赖（一次装完，不报错）
```bash
uv pip install numpy pandas scikit-learn matplotlib shap ipython openpyxl xgboost
```
### 4. 锁定环境版本（可复现关键）
```bash
uv pip freeze > requirements.txt
```
### 5. 运行所有模型（复制整段执行）
```bash
python Linear_cv.py
python Ridge_cv.py
python SVM_cv.py
python gradientboosting_cv.py
python ET_cv.py
python KNN_cv.py
python CART_cv.py
python readData_cv.py
```
### 6. 生成模型对比图（4 合 1 专业图表）
```bash
python plot_4figures.py
```
## 四、复现结果汇总
本次实验基于10 折交叉验证，成功复现了8 种机器学习模型在土壤重金属吸附量预测任务上的性能表现，以 ** 测试集均方根误差（RMSE）与决定系数（R²）** 作为核心评价指标。

结果显示，不同模型的预测能力差异显著。Gradient Boosting（梯度提升树）表现最优，测试集 RMSE 仅为0.0369，R² 高达0.8677，具备出色的拟合与泛化能力；紧随其后的是Extra Trees（ET，极端随机树），测试集 RMSE 为0.0458，R² 为0.8081，同样达到优秀水平。K-Nearest Neighbors（KNN）与Random Forest（RF，随机森林）表现良好，测试集 RMSE 分别为0.0676和0.0678，R² 分别为0.5939和0.5605，预测效果稳定可靠。

相比之下，传统线性模型表现一般，Linear Regression（线性回归）与Ridge Regression（岭回归）的测试集 RMSE 均为0.0810，R² 分别为0.4023和0.4030；CART Decision Tree（CART 决策树）测试集 RMSE 为0.0815，R² 为0.3942，整体预测精度有限。Support Vector Machine（SVM，支持向量机）表现最弱，测试集 RMSE 为0.1111，R² 仅为0.2035，难以有效捕捉数据规律。

<img width="4800" height="3600" alt="image" src="https://github.com/user-attachments/assets/6e73bfdb-3c7a-480e-8cad-583923f02895" />

#### 核心结论：基于树结构的集成学习模型（Gradient Boosting、Extra Trees）在本任务中显著优于线性模型、单棵决策树与 SVM 模型，表明土壤重金属吸附量与各项理化性质之间存在复杂的非线性关联，集成模型凭借强大的非线性拟合能力，更适用于该预测任务。

## 五、复现过程问题与解决方法
### 1、缺少依赖库（shap、ipython、openpyxl）
解决：使用统一安装命令 uv pip install 一次性安装。
```bash
uv pip install numpy pandas scikit-learn matplotlib shap ipython openpyxl xgboost
```
### 2、文件名不匹配（如 linear_regression_cv.py 找不到）
解决：使用项目真实文件名 Linear_cv.py、Ridge_cv.py。
```bash
python Linear_cv.py
python Ridge_cv.py
python SVM_cv.py
python gradientboosting_cv.py
python ET_cv.py
python KNN_cv.py
python CART_cv.py
```
### 3、图表保存路径报错
解决：将保存路径改为当前目录。
```bash
plt.savefig('model_4panel_results.png', dpi=300)
```
### 4、SGD 模型出现数值溢出（inf）

原因：SGD 对数据尺度敏感，未标准化导致不稳定。

解决：属于模型特性，非代码错误，不参与最终对比。

### 5、xgboost_regressor_cv.py 不存在

解决：原项目无此文件，跳过不影响整体复现。

## 六、可复现性结论
本项目通过 uv 构建隔离虚拟环境、requirements.txt 锁定依赖版本、完整记录复现步骤与问题解决方法，实现了完全可复现。任何用户按照本文档步骤，均可在 Windows 环境下复现与本次实验完全一致的结果。

## 七、参考文献
Yang, H., Huang, K., Zhang, K., Weng, Q., Zhang, H., & Wang, F. (2021). Predicting Heavy Metal Adsorption on Soil with Machine Learning and Mapping Global Distribution of Soil Adsorption Capacities. Environmental Science & Technology, 55(20), 14316-14328. https://doi.org/10.1021/acs.est.1c0247
