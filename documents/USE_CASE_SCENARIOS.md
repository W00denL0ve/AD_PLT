# 互联网广告平台用例场景说明文档 v1.0

## 1. 广告管理场景

### UC-01：新用户注册并创建第一个广告

#### 用例名称

新用户注册并创建广告

#### 参与者

- 主要参与者：广告主（新用户）
- 次要参与者：系统管理员

#### 触发条件

新用户需要在平台投放广告

#### 前置条件

- 用户未注册账号
- 用户已准备好公司相关资料
- 用户已准备好广告素材

#### 详细过程

1. 用户注册流程
   
   ```
   操作：访问平台首页
   输入：点击"注册"按钮
   系统：显示注册表单
   
   操作：填写注册信息
   输入：用户名、密码、邮箱、公司名称、联系电话
   系统：验证输入信息
   
   操作：提交注册
   系统：创建账户，发送验证邮件
   ```

2. 账户充值流程
   
   ```
   操作：进入充值页面
   输入：选择充值金额和支付方式
   系统：生成支付订单
   
   操作：完成支付
   系统：更新账户余额，生成交易记录
   ```

3. 创建广告流程
   
   ```
   操作：进入广告创建页面
   系统：显示广告创建表单
   
   操作：填写广告信息
   输入：
   - 广告标题：{广告名称}
   - 广告描述：{广告详细说明}
   - 广告类型：{选择广告类型}
   - 上传素材：{图片/视频文件}
   - 目标URL：{广告链接}
   - 投放时间：{开始日期 - 结束日期}
   - 日预算：{预算金额}
   
   系统：验证输入内容和格式
   
   操作：提交广告
   系统：创建广告，进入审核流程
   ```

#### 异常处理

1. 注册异常
   
   ```
   情况：用户名已存在
   处理：提示选择其他用户名
   
   情况：邮箱格式错误
   处理：提示输入正确格式
   ```

2. 充值异常
   
   ```
   情况：支付失败
   处理：显示失败原因，提供重试选项
   
   情况：金额超限
   处理：提示金额范围限制
   ```

3. 广告创建异常
   
   ```
   情况：素材格式不符
   处理：提示支持的格式要求
   
   情况：预算不足
   处理：提示充值或调整预算
   ```

#### 后置条件

- 用户账号创建成功
- 账户余额充足
- 广告进入审核队列

#### 业务规则

- 注册信息必须真实有效
- 首次充值最低100元
- 广告素材必须符合平台规范

### UC-02：管理员广告审核

#### 用例名称

广告内容审核

#### 参与者

- 主要参与者：系统管理员
- 次要参与者：广告主

#### 触发条件

新广告提交审核

#### 前置条件

- 管理员已登录系统
- 存在待审核广告

#### 详细过程

1. 查看审核队列
   
   ```
   操作：进入审核管理页面
   系统：显示待审核广告列表
   显示：
   - 广告ID
   - 提交时间
   - 广告主信息
   - 广告类型
   ```

2. 审核广告内容
   
   ```
   操作：选择待审核广告
   系统：显示广告详细信息
   
   操作：审核内容
   检查项：
   - 内容合规性
   - 素材规范性
   - 描述准确性
   - 链接有效性
   ```

3. 提交审核结果
   
   ```
   操作：选择审核结果
   输入：
   - 审核结果：{通过/拒绝}
   - 审核意见：{具体说明}
   
   系统：更新广告状态
   系统：发送审核结果通知
   ```

#### 异常处理

1. 内容违规
   
   ```
   情况：发现违规内容
   处理：标记违规类型，直接拒绝
   
   情况：需要修改
   处理：返回修改意见
   ```

2. 系统异常
   
   ```
   情况：审核提交失败
   处理：保存草稿，稍后重试
   ```

#### 后置条件

- 广告状态更新
- 广告主收到通知
- 审核记录保存

#### 业务规则

- 24小时内完成审核
- 拒绝必须说明原因
- 保存审核记录

### UC-03：广告效果分析

#### 用例名称

广告数据分析

#### 参与者

- 主要参与者：广告主
- 次要参与者：系统分析模块

#### 触发条件

广告投放后需要分析效果

#### 前置条件

- 广告已投放一定时间
- 有足够的数据样本

#### 详细过程

1. 查看数据概览
   
   ```
   操作：进入广告统计页面
   系统：显示关键指标
   显示：
   - 展示次数
   - 点击次数
   - 点击率(CTR)
   - 花费金额
   ```

2. 分析详细数据
   
   ```
   操作：选择分析维度
   维度：
   - 时间维度：{小时/天/周/月}
   - 地域维度：{省份/城市}
   - 人群维度：{年龄/性别/兴趣}
   
   系统：生成数据图表
   显示：
   - 趋势图
   - 分布图
   - 对比图
   ```

3. 导出报告
   
   ```
   操作：选择导出选项
   输入：
   - 时间范围
   - 导出格式
   - 包含指标
   
   系统：生成报告文件
   ```

#### 异常处理

1. 数据不足
   
   ```
   情况：样本量太小
   处理：提示数据可能不准确
   
   情况：数据缺失
   处理：显示原因说明
   ```

2. 导出失败
   
   ```
   情况：文件生成失败
   处理：提示重试或切换格式
   ```

#### 后置条件

- 生成分析报告
- 保存查询条件
- 更新数据缓存

#### 业务规则

- 数据实时更新
- 保留30天详细数据
- 支持数据对比分析

### UC-04：账户充值及发票申请

#### 用例名称

充值开票流程

#### 参与者

- 主要参与者：广告主
- 次要参与者：财务管理员、支付系统

#### 触发条件

账户余额不足或需要开具发票

#### 前置条件

- 用户已登录系统
- 有充值记录

#### 详细过程

1. 充值操作
   
   ```
   操作：进入充值页面
   输入：
   - 充值金额：{具体金额}
   - 支付方式：{支付宝/微信/银行转账}
   
   系统：生成支付订单
   
   操作：完成支付
   系统：验证支付结果
   ```

2. 发票申请
   
   ```
   操作：进入发票申请页面
   输入：
   - 发票类型：{普通发票/专用发票}
   - 抬头信息：{公司名称}
   - 税号：{纳税人识别号}
   - 开票金额：{选择充值记录}
   - 邮寄信息：{地址及联系人}
   
   系统：验证信息完整性
   系统：创建开票申请
   ```

3. 发票处理
   
   ```
   操作：财务审核开票申请
   系统：生成发票
   系统：更新发票状态
   系统：通知用户处理结果
   ```

#### 异常处理

1. 支付异常
   
   ```
   情况：支付失败
   处理：提供重试选项
   
   情况：金额错误
   处理：取消订单重新创建
   ```

2. 发票信息异常
   
   ```
   情况：信息不完整
   处理：提示补充信息
   
   情况：金额超限
   处理：提示分开开票
   ```

#### 后置条件

- 账户余额更新
- 发票申请记录创建
- 发送处理通知

#### 业务规则

- 最低充值金额限制
- 发票金额与充值记录匹配
- 专票需要资质审核

## 2. 场景关联说明

### 2.1 场景依赖关系

```
新用户注册 -> 账户充值 -> 创建广告 -> 广告审核 -> 投放分析
```

### 2.2 场景触发条件

- 用户注册：首次使用平台
- 广告审核：新广告创建
- 效果分析：广告投放中
- 发票申请：完成充值

### 2.3 场景优先级

1. 核心场景
   
   - 用户注册
   - 广告创建
   - 广告审核

2. 重要场景
   
   - 账户充值
   - 效果分析
   - 发票申请

3. 辅助场景
   
   - 数据导出
   - 系统设置

## 3. 场景验收标准

### 3.1 功能验收

- 各项功能正常工作
- 流程完整无中断
- 异常处理有效

### 3.2 性能验收

- 响应时间达标
- 并发处理正常
- 数据准确性高

### 3.3 用户体验

- 操作流程清晰
- 界面反馈及时
- 帮助信息完整
