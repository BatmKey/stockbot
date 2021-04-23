## 部分效果展示
![stockbot](https://media.giphy.com/media/gYbyHRMfm1AJCEPGfV/giphy.gif)

#### 技术实现
提取用户意图并且构建实体, 提取stock entity查询EXI获得数据并响应
预测用户意图，并且提供缺省回答
状态机的多轮多次查询技术，正则表达式提取用户意图日期

利用historical data Panda数据利用MATLAB作图生成图片并且返回给用户
准确提取实体中的日期并进行处理返回
其他无法直观展示的见代码

### 文件说明

```jsx
├── AAPL.png
├── README.md
├── __pycache__
│   ├── actions.cpython-37.pyc
│   └── price.cpython-37.pyc
├── actions.py --> 存储用户自定义行为，用来调用
├── asdf.png --> matlib作图文件，生成外链转给用户
├── config.yml --> 配置文件，Spacy等处理pipline以及Rasa机器的Memory管理等基础设置
├── credentials.yml --> 外部鉴权部署文件
├── data --> 训练集
│   ├── nlu.yml
│   └── stories.yml --> 可以用story中的steps来展示&&训练
├── domain.yml --> 相当于rasa的处理器 && 🧠
├── endpoints.yml
├── events.db
├── events.db-shm
├── events.db-wal
├── iexfiance_bacis.ipynb -->  IEX api调用测试
├── models --> 训练集模型存放
│   ├── 20210422-181738.tar.gz
│   ├── 20210422-182540.tar.gz
│   └── 20210422-190529.tar.gz
├── price.py --> 接口查询
├── rasa.db --> RASA机器人自然语言训练数据库
└── tests
    └── conversation_tests.md
```

### 使用说明
```
安装依赖
pip install -r requirements.txt
训练模型
rasa train 
本地测试图形化模型
rasa x
本地测试shell模型
rasa shell

运行方法
1. 安装依赖
2. rasa run actions
3. rasa x
4. enjoy it !
```
