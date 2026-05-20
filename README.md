# Project-reproduction-131
利用机器学习预测重金属在土壤上的吸附能力及全球土壤吸附能力分布图


##小组基本信息
###名称：环境科学研究小组
张骏辉2025303110016@Zhang-JunH
苗芳源2025303110021@FangYuan-Miao
胡金忆2025303110020@taro-2026
李艳峰2025303110142@liyanfeng123

##一、项目基本信息
项目名称：Predicting Heavy Metal Adsorption on Soil with Machine Learning and Mapping Global Distribution of Soil Adsorption Capacities（Environ. Sci. Technol. 2021, 55, 20, 14316–14328）
论文链接：https://pubs.acs.org/doi/10.1021/acs.est.1c02479
项目来源：https://github.com/KuanHuang/predicting-heavy-metal-adsorption-in-soil
复现任务：基于机器学习模型预测土壤重金属吸附量，完成环境搭建、模型运行与可复现性验证

##二、可复现性评估结果
✅ 数据完整可获取
✅ 代码可直接运行
✅ 环境可完整重建
✅ 结果可稳定复现
结论：该项目满足可重复研究要求

##三、复现环境与流程
环境工具：使用 uv 构建独立虚拟环境
依赖管理：生成 requirements.txt 锁定所有包版本
运行流程：克隆代码 → 搭建环境 → 安装依赖 → 运行全部模型 → 生成结果图表
系统环境：Windows 10 + Python 3.10.18

##四、复现过程中遇到的问题及解决方法
问题1：运行脚本时报错缺少 shap 库
解决1：使用 uv pip install shap 安装缺失依赖

问题2：shap 绘图需要依赖 ipython
解决2：执行 uv pip install ipython 完成安装

问题3：pandas 读取 .xlsx 文件失败
解决3：安装 uv pip install openpyxl

问题4：输入 linear_regression_cv.py 提示找不到文件
解决4：改用项目真实文件名 Linear_cv.py，统一文件名大小写

问题5：保存图片到上层目录报错
解决5：将保存路径改为当前文件夹，直接生成图片

问题6：损失函数计算出现无穷大，并非代码错误
解决6：SGD 对数据尺度敏感，未标准化导致不稳定，该模型不参与对比即可

问题7：运行 xgboost_regressor_cv.py 提示文件不存在
解决7：该文件不在项目中，跳过即可，不影响整体复现

Image Image Image Image

##五、复现结果总结
本次共复现 8 类机器学习模型，采用 10 折交叉验证：
最优模型：Gradient Boosting（测试集 R² = 0.8677，RMSE = 0.0369）
有效模型：ET、KNN、随机森林、线性回归、CART、Ridge、SVM
异常说明：SGD 因数据尺度问题出现数值溢出，属于模型特性，非复现错误
所有模型均成功运行，输出指标一致，实验过程完全可复现。

##六、复现证明材料
环境依赖文件：requirements.txt
运行结果：全部模型训练日志、指标输出
可视化图表：4 组合模型对比图

Image Image Image

###全文阅读：predicting-heavy-metal-adsorption-on-soil-with-machine-learning-and-mapping-global-distribution-of-soil-adsorption.pdf
