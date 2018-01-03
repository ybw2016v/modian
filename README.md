# modian
生成模电实验报告的自动化工具

-----

## 功能
基于python3编写的面向对象的模电实验报告自动化生成工具。该工具可以自动读取双路输入示波器自动保存的波形数据，可以自动检测出峰峰值，频率（可能不准）。自动生成出markdown格式的数据表格。可以应用在模电实验报告实验数据处理方面。

## 使用方法
首先应该有`python3 matplotlib`等常用python工具。程序中涉及到文件路径的部分均采用Linux风格，Windows用户请自行更改或联系作者。

在bash中输入。
```
git clone https://github.com/ybw2016v/modian.git
cd modian
```
将示波器输出的文件复制到modian目录下。
```
python3 mo.py
```

## 输出示例

### 积分电路
|频率|v1|v1波形|v2|v2波形|
|---|----|----|----|----|
|100|2.04|![ALL0001/F0001CH2.jpg](ALL0001/F0001CH2.jpg)|3.36|![ALL0001/F0001CH1.jpg](ALL0001/F0001CH1.jpg)|
|200|2.04|![ALL0002/F0002CH2.jpg](ALL0002/F0002CH2.jpg)|1.74|![ALL0002/F0002CH1.jpg](ALL0002/F0002CH1.jpg)|
|398|2.04|![ALL0003/F0003CH2.jpg](ALL0003/F0003CH2.jpg)|0.94|![ALL0003/F0003CH1.jpg](ALL0003/F0003CH1.jpg)|
|20|2.04|![ALL0004/F0004CH2.jpg](ALL0004/F0004CH2.jpg)|17.40|![ALL0004/F0004CH1.jpg](ALL0004/F0004CH1.jpg)|
|50|2.08|![ALL0006/F0006CH2.jpg](ALL0006/F0006CH2.jpg)|9.20|![ALL0006/F0006CH1.jpg](ALL0006/F0006CH1.jpg)|
|100|2.04|![ALL0007/F0007CH2.jpg](ALL0007/F0007CH2.jpg)|5.44|![ALL0007/F0007CH1.jpg](ALL0007/F0007CH1.jpg)|
|200|2.04|![ALL0008/F0008CH2.jpg](ALL0008/F0008CH2.jpg)|2.64|![ALL0008/F0008CH1.jpg](ALL0008/F0008CH1.jpg)|
|400|2.04|![ALL0009/F0009CH2.jpg](ALL0009/F0009CH2.jpg)|3.36|![ALL0009/F0009CH1.jpg](ALL0009/F0009CH1.jpg)|
