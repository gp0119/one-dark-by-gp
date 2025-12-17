# One Dark by GP

JetBrains IDE 主题插件

## 安装方法

1. 下载 `one-dark-by-gp.jar`
2. 打开 IDE → Settings → Plugins → ⚙️ → Install Plugin from Disk...
3. 选择 JAR 文件 → 重启 IDE
4. Settings → Appearance → Theme → 选择 "one dark by gp"

## 打包命令

```bash
cd /path/to/one-dark-by-gp
jar -cfM one-dark-by-gp.jar -C resources .
```

---

## theme.json 配置说明

### 基础信息

```json
{
  "name": "one dark by gp", // 主题名称
  "dark": true, // 是否为暗色主题
  "author": "gp", // 作者
  "editorScheme": "/onedarkbygp.xml" // 编辑器配色方案文件路径
}
```

---

### colors - 颜色变量定义

在这里定义颜色变量，可以在 `ui` 部分引用，修改一处全局生效。

#### 🎨 强调色

| 变量              | 说明                               |
| ----------------- | ---------------------------------- |
| `accentColor`     | 主强调色（按钮、链接、选中状态等） |
| `accentColorDark` | 深强调色（聚焦边框等）             |
| `linkColor`       | 链接颜色                           |

#### 🖼️ 背景色

| 变量                   | 说明                                              |
| ---------------------- | ------------------------------------------------- |
| `editorBackground`     | 编辑器背景（需同步修改 xml 中的 TEXT.BACKGROUND） |
| `panelBackground`      | 主面板/侧边栏背景                                 |
| `toolWindowBackground` | 工具窗口背景（项目树面板等）                      |
| `popupBackground`      | 弹出框/工具提示背景                               |
| `inputBackground`      | 输入框/文本框背景                                 |
| `comboBoxBackground`   | 下拉框背景                                        |
| `tableBackground`      | 表格/列表背景                                     |
| `headerBackground`     | 标题栏/标签栏背景                                 |

#### 🎯 交互状态

| 变量                          | 说明               |
| ----------------------------- | ------------------ |
| `hoverBackground`             | 鼠标悬停背景       |
| `selectionBackground`         | 选中项背景（蓝色） |
| `selectionBackgroundInactive` | 非活动选中背景     |
| `selectionBackgroundLight`    | 浅色选中背景       |

#### ✏️ 前景色

| 变量              | 说明                     |
| ----------------- | ------------------------ |
| `foreground`      | 主文字颜色               |
| `foregroundDim`   | 次要/灰色文字            |
| `foregroundInfo`  | 信息提示文字             |
| `foregroundWhite` | 白色文字（用于选中状态） |

#### 🔲 边框色

| 变量               | 说明       |
| ------------------ | ---------- |
| `borderColor`      | 默认边框色 |
| `borderColorLight` | 浅边框色   |
| `borderColorDark`  | 深边框色   |
| `separatorColor`   | 分隔线颜色 |

#### 🚦 状态色

| 变量                | 说明                 |
| ------------------- | -------------------- |
| `successColor`      | 成功/添加（绿色）    |
| `errorColor`        | 错误文字（红色）     |
| `errorBackground`   | 错误背景             |
| `warningColor`      | 警告文字（黄色）     |
| `warningBackground` | 警告背景             |
| `matchColor`        | 搜索匹配高亮（橙色） |
| `disabledColor`     | 禁用状态颜色         |

---

### ui - 界面组件配置

#### `*` - 全局默认值

所有组件的默认样式，会被具体组件覆盖。

```json
"*": {
  "background": "panelBackground",           // 默认背景
  "foreground": "foreground",                // 默认前景
  "selectionBackground": {...},              // 选中背景（支持按系统区分）
  "selectionForeground": {...},              // 选中前景
  "borderColor": "borderColor",              // 默认边框
  "focusedBorderColor": "accentColor",       // 聚焦边框
  "errorForeground": "errorColor",           // 错误文字
  "separatorColor": "separatorColor"         // 分隔线
}
```

#### `ActionButton` - 操作按钮

工具栏上的图标按钮。

```json
"ActionButton": {
  "hoverBackground": "...",     // 悬停背景
  "pressedBackground": "..."    // 按下背景
}
```

#### `Button` - 普通按钮

```json
"Button": {
  "foreground": "...",          // 文字颜色
  "startBackground": "...",     // 背景（渐变起始）
  "endBackground": "...",       // 背景（渐变结束）
  "default": {                  // 主按钮（蓝色）
    "startBackground": "accentColor",
    ...
  }
}
```

#### `ComboBox` - 下拉框

```json
"ComboBox": {
  "background": "...",              // 下拉框背景
  "nonEditableBackground": "...",   // 只读时背景
  "selectionBackground": "...",     // 选中项背景
  "ArrowButton": {                  // 箭头按钮
    "iconColor": "..."
  }
}
```

#### `Editor` - 编辑器区域

```json
"Editor": {
  "background": "editorBackground",  // 编辑器背景
  "foreground": "foreground",        // 文字颜色
  "SearchField": {                   // 搜索框
    "background": "..."
  }
}
```

#### `EditorTabs` - 编辑器标签页

```json
"EditorTabs": {
  "background": "...",                  // 标签栏背景
  "underlinedTabBackground": "...",     // 当前标签背景
  "inactiveUnderlineColor": "..."       // 非活动下划线
}
```

#### `List` - 列表

```json
"List": {
  "selectionBackground": "...",   // 选中项背景
  "selectionForeground": "..."    // 选中项文字
}
```

#### `Popup` - 弹出窗口

```json
"Popup": {
  "background": "...",              // 弹出窗口背景
  "borderColor": "...",             // 边框
  "Header.activeBackground": "..."  // 标题栏背景
}
```

#### `ToolWindow` - 工具窗口（项目树等）

```json
"ToolWindow": {
  "background": "toolWindowBackground",  // 工具窗口背景
  "Header": {
    "background": "...",                 // 标题栏背景
    "inactiveBackground": "..."          // 非活动标题栏
  }
}
```

#### `Tree` - 文件树

```json
"Tree": {
  "selectionBackground": "...",        // 选中文件背景
  "modifiedItemForeground": "...",     // 修改过的文件颜色
  "rowHeight": 20.0                    // 行高
}
```

#### `Table` - 表格

```json
"Table": {
  "background": "...",              // 表格背景
  "selectionBackground": "...",     // 选中行背景
  "stripeColor": "..."              // 斑马纹颜色
}
```

#### `TextField` / `TextArea` - 输入框

```json
"TextField": {
  "background": "inputBackground",     // 输入框背景
  "selectionBackground": "..."         // 选中文字背景
}
```

#### `ProgressBar` - 进度条

```json
"ProgressBar": {
  "trackColor": "...",          // 轨道颜色
  "progressColor": "...",       // 进度颜色
  "passedColor": "...",         // 成功颜色（绿）
  "failedColor": "..."          // 失败颜色（红）
}
```

#### `Notification` - 通知

```json
"Notification": {
  "background": "...",           // 通知背景
  "errorBackground": "...",      // 错误通知背景
  "ToolWindow": {                // 工具窗口通知
    "informativeBackground": "...",
    "warningBackground": "...",
    "errorBackground": "..."
  }
}
```

#### `WelcomeScreen` - 欢迎页面

```json
"WelcomeScreen": {
  "SidePanel.background": "...",     // 侧边栏背景
  "Details.background": "..."        // 详情区背景
}
```

---

### icons - 图标配置

#### `ColorPalette` - Checkbox 复选框

```json
"icons": {
  "ColorPalette": {
    "Checkbox.Background.Default.Dark": "...",   // 复选框背景
    "Checkbox.Border.Default.Dark": "...",       // 复选框边框
    "Checkbox.Foreground.Selected.Dark": "...",  // 勾选颜色
    "Checkbox.Background.Disabled.Dark": "..."   // 禁用状态
  }
}
```

---

## onedarkbygp.xml 说明

编辑器配色方案文件，控制代码语法高亮、编辑器背景等。

### 重要配置

| 属性                      | 说明                         |
| ------------------------- | ---------------------------- |
| `EDITOR_BACKGROUND_COLOR` | 编辑器背景（不带#）          |
| `TEXT.BACKGROUND`         | 文本背景（需与上面保持一致） |
| `CARET_COLOR`             | 光标颜色                     |
| `CARET_ROW_COLOR`         | 当前行高亮                   |
| `SELECTION_BACKGROUND`    | 选中文字背景                 |
| `LINE_NUMBERS_COLOR`      | 行号颜色                     |
| `GUTTER_BACKGROUND`       | 行号区域背景                 |

### 修改编辑器背景

需要同时修改两处：

```xml
<!-- 第14行 -->
<option name="EDITOR_BACKGROUND_COLOR" value="你的颜色" />

<!-- 约第3747行 -->
<option name="TEXT">
  <value>
    <option name="BACKGROUND" value="你的颜色" />
  </value>
</option>
```

⚠️ **注意**：XML 中的颜色值不带 `#` 号！

---

## 文件结构

```
one-dark-by-gp/
├── resources/
│   ├── META-INF/
│   │   ├── plugin.xml          # 插件配置
│   │   └── pluginIcon.svg      # 插件图标
│   ├── onedarkbygp.theme.json  # UI 主题配置
│   └── onedarkbygp.xml         # 编辑器配色方案
├── one-dark-by-gp.jar          # 打包后的插件
└── README.md
```
