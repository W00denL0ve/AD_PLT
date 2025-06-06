# 广告管理系统

这是一个基于Python Flask的广告管理系统，提供广告购买、审核、充值、展示等功能。

## 功能特点

- 广告购买和审核
- 广告充值（模拟支付）
- 充值历史查询
- 广告客户管理
- 广告展示统计
- 广告API接口
- 发票管理

## 技术栈

- 后端：Python Flask
- 数据库：MySQL
- 前端：HTML + CSS + JavaScript (Bootstrap)

## 安装说明

1. 安装Python依赖：
```bash
pip install -r requirements.txt
```

2. 配置数据库：
- 创建MySQL数据库
- 修改.env文件中的数据库配置

3. 运行应用：
```bash
python run.py
```

## 项目结构

```
ad_platform/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── static/
│   └── templates/
├── config.py
├── requirements.txt
└── run.py
``` 