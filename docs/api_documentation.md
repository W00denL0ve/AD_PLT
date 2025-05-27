# 广告管理平台 API 文档

## 1. 接口规范

### 1.1 基础信息
- 基础URL: `http://api.example.com/v1`
- 请求方式: REST
- 数据格式: JSON
- 认证方式: Bearer Token

### 1.2 通用响应格式
```json
{
    "code": 200,
    "message": "success",
    "data": {}
}
```

### 1.3 错误码说明
- 200: 成功
- 400: 请求参数错误
- 401: 未授权
- 403: 权限不足
- 404: 资源不存在
- 500: 服务器内部错误

## 2. 用户管理接口

### 2.1 用户注册
- 请求路径: `/users/register`
- 请求方式: POST
- 请求参数:
```json
{
    "username": "string",
    "email": "string",
    "password": "string",
    "confirm_password": "string"
}
```
- 响应示例:
```json
{
    "code": 200,
    "message": "注册成功",
    "data": {
        "user_id": 1,
        "username": "test_user"
    }
}
```

### 2.2 用户登录
- 请求路径: `/users/login`
- 请求方式: POST
- 请求参数:
```json
{
    "username": "string",
    "password": "string"
}
```
- 响应示例:
```json
{
    "code": 200,
    "message": "登录成功",
    "data": {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "user_info": {
            "user_id": 1,
            "username": "test_user",
            "role": "user"
        }
    }
}
```

### 2.3 获取用户信息
- 请求路径: `/users/info`
- 请求方式: GET
- 请求头: `Authorization: Bearer {token}`
- 响应示例:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "user_id": 1,
        "username": "test_user",
        "email": "test@example.com",
        "role": "user",
        "created_at": "2024-01-01T00:00:00Z"
    }
}
```

## 3. 广告管理接口

### 3.1 创建广告
- 请求路径: `/advertisements`
- 请求方式: POST
- 请求头: `Authorization: Bearer {token}`
- 请求参数:
```json
{
    "title": "string",
    "type": "banner",
    "content": "string",
    "budget": 1000.00,
    "start_date": "2024-01-01T00:00:00Z",
    "end_date": "2024-01-31T23:59:59Z"
}
```
- 响应示例:
```json
{
    "code": 200,
    "message": "广告创建成功",
    "data": {
        "ad_id": 1,
        "title": "测试广告",
        "status": "pending"
    }
}
```

### 3.2 获取广告列表
- 请求路径: `/advertisements`
- 请求方式: GET
- 请求头: `Authorization: Bearer {token}`
- 请求参数:
  - page: 页码（默认1）
  - size: 每页数量（默认10）
  - status: 广告状态（可选）
  - type: 广告类型（可选）
- 响应示例:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "total": 100,
        "page": 1,
        "size": 10,
        "items": [
            {
                "ad_id": 1,
                "title": "测试广告",
                "type": "banner",
                "status": "active",
                "budget": 1000.00,
                "start_date": "2024-01-01T00:00:00Z",
                "end_date": "2024-01-31T23:59:59Z"
            }
        ]
    }
}
```

### 3.3 更新广告状态
- 请求路径: `/advertisements/{ad_id}/status`
- 请求方式: PUT
- 请求头: `Authorization: Bearer {token}`
- 请求参数:
```json
{
    "status": "active"
}
```
- 响应示例:
```json
{
    "code": 200,
    "message": "状态更新成功",
    "data": {
        "ad_id": 1,
        "status": "active"
    }
}
```

## 4. 支付管理接口

### 4.1 创建支付订单
- 请求路径: `/payments`
- 请求方式: POST
- 请求头: `Authorization: Bearer {token}`
- 请求参数:
```json
{
    "amount": 1000.00,
    "payment_method": "alipay",
    "description": "广告投放费用"
}
```
- 响应示例:
```json
{
    "code": 200,
    "message": "订单创建成功",
    "data": {
        "order_id": "PAY202401010001",
        "amount": 1000.00,
        "payment_url": "https://pay.example.com/..."
    }
}
```

### 4.2 查询支付状态
- 请求路径: `/payments/{order_id}`
- 请求方式: GET
- 请求头: `Authorization: Bearer {token}`
- 响应示例:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "order_id": "PAY202401010001",
        "amount": 1000.00,
        "status": "success",
        "payment_method": "alipay",
        "paid_at": "2024-01-01T12:00:00Z"
    }
}
```

## 5. 发票管理接口

### 5.1 申请发票
- 请求路径: `/invoices`
- 请求方式: POST
- 请求头: `Authorization: Bearer {token}`
- 请求参数:
```json
{
    "type": "company",
    "title": "公司名称",
    "tax_number": "91110000123456789X",
    "amount": 1000.00,
    "email": "invoice@example.com"
}
```
- 响应示例:
```json
{
    "code": 200,
    "message": "发票申请成功",
    "data": {
        "invoice_id": "INV202401010001",
        "status": "pending"
    }
}
```

### 5.2 查询发票状态
- 请求路径: `/invoices/{invoice_id}`
- 请求方式: GET
- 请求头: `Authorization: Bearer {token}`
- 响应示例:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "invoice_id": "INV202401010001",
        "type": "company",
        "title": "公司名称",
        "amount": 1000.00,
        "status": "issued",
        "issued_at": "2024-01-02T00:00:00Z"
    }
}
```

## 6. 数据统计接口

### 6.1 广告效果统计
- 请求路径: `/statistics/advertisements`
- 请求方式: GET
- 请求头: `Authorization: Bearer {token}`
- 请求参数:
  - start_date: 开始日期
  - end_date: 结束日期
  - ad_id: 广告ID（可选）
- 响应示例:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "total_impressions": 10000,
        "total_clicks": 500,
        "total_conversions": 50,
        "ctr": 0.05,
        "conversion_rate": 0.1,
        "daily_stats": [
            {
                "date": "2024-01-01",
                "impressions": 1000,
                "clicks": 50,
                "conversions": 5
            }
        ]
    }
}
```

### 6.2 收入统计
- 请求路径: `/statistics/revenue`
- 请求方式: GET
- 请求头: `Authorization: Bearer {token}`
- 请求参数:
  - start_date: 开始日期
  - end_date: 结束日期
  - group_by: 分组方式（day/month）
- 响应示例:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "total_revenue": 10000.00,
        "daily_revenue": [
            {
                "date": "2024-01-01",
                "revenue": 1000.00
            }
        ]
    }
}
```

## 7. 系统管理接口

### 7.1 获取系统配置
- 请求路径: `/system/config`
- 请求方式: GET
- 请求头: `Authorization: Bearer {token}`
- 响应示例:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "ad_types": ["banner", "popup", "video", "native"],
        "payment_methods": ["alipay", "wechat", "bank_transfer"],
        "invoice_types": ["personal", "company"]
    }
}
```

### 7.2 更新系统配置
- 请求路径: `/system/config`
- 请求方式: PUT
- 请求头: `Authorization: Bearer {token}`
- 请求参数:
```json
{
    "ad_types": ["banner", "popup", "video", "native", "new_type"],
    "payment_methods": ["alipay", "wechat", "bank_transfer", "new_payment"],
    "invoice_types": ["personal", "company", "new_invoice"]
}
```
- 响应示例:
```json
{
    "code": 200,
    "message": "配置更新成功",
    "data": {
        "ad_types": ["banner", "popup", "video", "native", "new_type"],
        "payment_methods": ["alipay", "wechat", "bank_transfer", "new_payment"],
        "invoice_types": ["personal", "company", "new_invoice"]
    }
}
``` 