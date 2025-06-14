# 广告平台版本管理文档 v1.1.0

## 版本号说明

采用语义化版本号规则：主版本号.次版本号.修订号

- 主版本号：不兼容的API修改
- 次版本号：向下兼容的功能性新增
- 修订号：向下兼容的问题修正

## 当前版本：v1.1.2 (2025-05-30)

## 版本历史
### v1.1.3 (2025-06-06)

#### 问题修复
- 当广告预算大于用户余额时，系统会提示用户充值并跳转到充值界面
- 当用户输入的预算小于等于0时，系统会提示用户输入正确的预算金额

### v1.1.2 (2025-05-30)
#### 优化改进

- 充值界面加入金额预输入按钮
- 部分界面调整了按钮的位置，方便用户点击
- 当用户退出登录时会跳出弹窗，避免用户误操作
- 导航界面会根据当前用户所在界面高亮显示，方便用户定位

#### 问题修复

- 修复了部分错误的页面跳转逻辑

### v1.1.1 (2025-05-27)
#### 优化改进

- 界面之间跳转逻辑优化
- 将用户名也显示在最上方
- 添加了更多的按钮，使用户能更快捷地访问相应界面

### v1.1.0 (2025-05-20)

#### 新增功能

- 广告数据导出（CSV/Excel格式）
- 广告效果预览功能

#### 优化改进

- 优化数据统计性能
- 改进广告审核流程
- 提升页面加载速度

#### 问题修复

- 修复统计数据准确性问题
- 解决浏览器兼容性问题
- 修复发票申请异常

### v1.0.1 (2025-05-13)

#### 优化改进

- 优化数据库查询性能
- 改进用户界面交互
- 增强系统安全性

#### 问题修复

- 修复用户注册验证问题
- 解决支付状态更新延迟
- 修复广告图片上传异常

### v1.0.0 (2025-05-16)

#### 初始版本

- 基础广告管理功能
- 用户登录注册系统
- 基本数据统计
- 支付功能集成
- 开具发票功能
- api介绍

## 版本规划

### v1.2.0 (计划于2025-05-23)

#### 计划功能

- [ ] 广告素材库
- [ ] 自定义数据报表
- [ ] 广告A/B测试系统
- [ ] 广告投放优化

### v1.3.0 (计划于2025-06-06)

#### 重要更新

- [ ] 基于ai的广告推荐系统
- [ ] 基础用户画像分析
- [ ] 实时数据统计
- [ ] 高级数据可视化
