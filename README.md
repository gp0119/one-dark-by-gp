# One Dark by GP

JetBrains IDE 主题插件，提供 One Dark 和 One Light 两套配色。

## One Light by GP

浅色主题使用同一暖白色系的编辑区和侧栏，以轻微明暗差区分区域，搭配蓝色强调。代码颜色沿用当前 dark 主题的分类，调整明度以适应浅色背景；选中区域保留深色文字。

| 用途 | 配色 |
| --- | --- |
| 编辑器 / 侧栏 / 标题栏 | `#FCFAF6` / `#FAF7F1` / `#F8F5EF` |
| 正文 / 次要文字 | `#374151` / `#5B6575` |
| 主按钮 / 选中背景 | `#3566AD` / `#D5E3F7` |
| 局部变量 | 红色 `#B2384B` |
| 函数参数（通用 / JS / TS） | 粉色 `#A02A73` |
| 实例成员属性 | 蓝灰色 `#426A94` |
| 全局 / 导出变量、类声明 | 偏黄的亮金色 `#9B6A00` |
| 静态成员（通用 / JS / TS） | 灰蓝色 `#536375` |
| 常量、组件 / 自定义标签 | 珊瑚橙 `#B83B10` |
| 关键字 / 通用类型引用 | 紫色 `#8A36B3` |
| 函数 / 方法 | 蓝色 `#0063B5` |
| 接口 / 抽象类 / 字符串 | 绿色 `#467225` |
| 数字 / Python 参数 | 棕橙色 `#9C4F1C` |
| TypeScript 基本类型 | 橙色 `#A34A22` |
| JSON 键 | 淡紫色 `#8847A8` |
| 注释 | `#677180` |

金黄色符号和组件使用偏黄的亮金色、珊瑚橙，保持现有分类及原有字重。`value:` 等内联提示使用深蓝灰文字和浅蓝灰底色，与后面的代码实参区分；同时配置通用类型提示和参数提示，以覆盖 IDE 的不同提示绘制方式。

分类以 `resources/onedarkbygp.xml` 为准，保留声明与引用、静态与实例及语言专属类别的差异。例如 Java 静态方法保留金黄色，Java 枚举常量保留淡紫色，TypeScript 类型参数保留金黄色；注释、代码片段等的字体样式也与 dark 对齐。

变量类别由 IDE 的语言分析决定，JS/TS 的 `const` 仍按局部或全局作用域着色。本方案默认关闭 JS/TS 的彩虹着色，避免按变量名分配的颜色覆盖角色配色。

UI 配置为 `resources/onelightbygp.theme.json`，编辑器方案为 `resources/onelightbygp.xml`，以 JetBrains 的 `Default` 浅色方案为基础。

## IDE 一键预览与打包

在 IntelliJ IDEA 或 WebStorm 中打开本项目，顶部运行配置下拉框会读取 `.run/` 中的共享配置。选中后点击旁边的 ▶：

| 运行配置 | 操作 |
| --- | --- |
| 预览深色 | 打开深色主题的 WebStorm 欢迎页，自行选择项目后实时预览 |
| 预览浅色 | 打开浅色主题的 WebStorm 欢迎页，自行选择项目后实时预览 |
| 打包插件 | 编译项目树扩展，将代码、主题资源和 LICENSE 打包到根目录 `one-dark-by-gp.jar`，覆盖原 JAR |

这些配置使用 IDE 自带的 Shell Script 插件；预览和打包需要 Python 3、WebStorm 及其自带的 JDK。预览在 IDE 终端中运行，按 `Ctrl+C` 停止；切换深浅色前先停止当前预览。配置参数可在 **Run → Edit Configurations…** 中修改。

## 在 WebStorm 中自动预览（macOS）

适用于 macOS 上的 WebStorm 2026.3，需要 Python 3；无须安装额外依赖或 Plugin DevKit。

在项目根目录运行：

```bash
./preview.command
```

预览浅色主题：

```bash
./preview.command --theme light
```

也可以在 Finder 中双击 `preview.command`。脚本会启动独立的 WebStorm 欢迎页，点击 **Open** 或最近项目即可选择要预览的项目；不会自动恢复上次打开的项目。首次启动时按提示完成授权，打开项目时按提示确认信任。

也可以直接指定项目，先退出已有预览实例，再传入项目目录：

```bash
./preview.command "/你的项目路径"
```

浅色主题也可以传入项目目录：`./preview.command --theme light "/你的项目路径"`。

不传目录时停留在欢迎页，等待你选择项目。预览窗口运行期间也可以通过 **File → Open** 在当前窗口打开其他项目。无论打开哪个项目，自动预览始终监听本仓库 `resources` 下的主题 JSON 和编辑器 XML；指定项目中不会被创建示例文件或资源链接。

在本仓库的 `resources` 目录中编辑主题 JSON 或编辑器 XML 并保存，约 0.5 秒后预览界面和代码区一起刷新，无须点击 Preview Theme、重新导入配色或切换窗口。也可以在其他编辑器中修改并保存这些文件，预览窗口同样会更新。需要语法高亮示例时，可自行打开仓库中的 `preview/sample.ts`。

编辑器背景由所选主题 XML 的 `TEXT` → `BACKGROUND` 控制；界面颜色由对应的 `.theme.json` 控制。只改 JSON 中的 `editorBackground` 不会修改 XML 中的代码背景。

深色主题按版本控制的忽略状态淡化目录图标，使用对应的文字颜色，并保留现有图标形状；普通目录不受影响。Git 忽略和 `.ignore` 插件的忽略状态均支持。项目树扩展在预览启动时编译加载，修改 `src` 中的代码后需要重启预览；配色仍可实时刷新。

预览配置、缓存和编译结果都保存在被 Git 忽略的 `.preview/` 中。退出预览 WebStorm（`⌘Q`），或在启动脚本的终端按 `Ctrl+C` 即可停止。JSON/XML 格式错误时保留上次有效预览；修正并保存后会继续更新。详细日志位于 `.preview/log/idea.log`。

脚本自动寻找 `~/Applications/WebStorm.app` 或 `/Applications/WebStorm.app`。安装在其他位置时指定：

```bash
WEBSTORM_APP="/你的路径/WebStorm.app" ./preview.command
```

预览加载器直接读取 JSON 和 XML，在内存中关联并应用界面主题和编辑器方案，避免 JAR 资源缓存或编辑器副本遮蔽修改。原主题文件和根目录的发布 JAR 不会被启动脚本改写。预览仅监听上述两个配色文件；修改插件元数据或替换资源文件需要另行打包安装验证。

## 安装方法

1. 下载 `one-dark-by-gp.jar`
2. 打开 IDE → Settings → Plugins → ⚙️ → Install Plugin from Disk...
3. 选择 JAR 文件 → 重启 IDE
4. Settings → Appearance → Theme → 选择 "one dark by gp" 或 "one light by gp"

## 打包命令

```bash
cd /path/to/one-dark-by-gp
python3 build.py
```

脚本复用预览的 WebStorm 查找规则，可通过 `WEBSTORM_APP` 指定安装位置。JAR 中包含项目树扩展、主题资源和 MIT 许可证；预览加载器及商店截图不会打入插件。编译和打包使用临时目录，结束后自动清理。

## 发布到 JetBrains Marketplace

插件名称为 **One Dark by GP**，当前版本为 **1.0.5**，插件 ID 保持 `one-dark-by-gp`。
英文介绍、更新说明及项目链接位于 `resources/META-INF/plugin.xml`；许可证为 [MIT](LICENSE)。

商店表单使用以下内容：

| 项目 | 内容 |
| --- | --- |
| 插件文件 | `one-dark-by-gp.jar` |
| Vendor | `gp`，使用自己拥有的 Vendor profile |
| 标签 | `Theme` |
| License | `MIT` |
| Source code | https://github.com/gp0119/one-dark-by-gp |
| License URL | https://github.com/gp0119/one-dark-by-gp/blob/master/LICENSE |
| Issue tracker | https://github.com/gp0119/one-dark-by-gp/issues |

发布前先将本次改动推送到 GitHub，确认源码和 License URL 可公开访问。
主题插件必须提供真实 IDE 效果截图，将 [WebStorm 展示截图](marketplace/editor.jpg) 上传到商店的 Media 区域。
截图来自 WebStorm 2026.3 的独立主题预览实例，展示 UI 及 TypeScript 配色。

首次发布：登录 [JetBrains Marketplace](https://plugins.jetbrains.com/)，在账户菜单选择 **Upload plugin**，
创建或选择自己的 Vendor profile，填写上述内容、上传 JAR 和截图，再提交审核。
已有插件页面时使用 **Upload Update**，不要创建新的插件 ID。
开发者协议、Vendor 身份及交易者声明由账户持有人按实际情况填写。

后续发布时先更新 `plugin.xml` 中的版本号和更新说明，再重新执行打包命令。
2026-11-14 使用 Plugin Verifier 1.411 检查 1.0.3 版 JAR，WebStorm `WS-263.7307.202`
和 IntelliJ IDEA `IU-263.7307.200`（均为 2026.3）的结果均为 `Compatible`。
兼容范围当前声明为 `since-build="213"`（2021.3 起）；其他版本尚未逐一验证。
每次上传时按商店要求检查 Plugin Verifier 结果，并在目标 IDE 中从磁盘安装 JAR 确认主题效果。
Plugin Verifier 检查二进制兼容性，不能替代对配色和界面效果的检查。

官方要求：[上传流程](https://plugins.jetbrains.com/docs/marketplace/uploading-a-new-plugin.html)、
[审核规范](https://plugins.jetbrains.com/docs/marketplace/jetbrains-marketplace-approval-guidelines.html)。

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
  "foreground": "foregroundInfo",      // 普通文字颜色（#aab4c2）
  "selectionBackground": "...",        // 选中文件背景
  "modifiedItemForeground": "...",     // 修改过的文件颜色
  "rowHeight": 20                      // 行高，使用整数
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
| `TEXT.BACKGROUND`         | 编辑器背景（不带#）          |
| `CARET_COLOR`             | 光标颜色                     |
| `CARET_ROW_COLOR`         | 当前行高亮                   |
| `SELECTION_BACKGROUND`    | 选中文字背景                 |
| `LINE_NUMBERS_COLOR`      | 行号颜色                     |
| `GUTTER_BACKGROUND`       | 行号区域背景                 |
| `CONSOLE_BACKGROUND_KEY`  | 控制台背景                   |
| `CONSOLE_OUTPUT.BACKGROUND` | 控制台输出背景             |

### 修改编辑器背景

在所选主题 XML 的 `attributes` → `TEXT` 中修改 `BACKGROUND`，保留该节点的其他属性：

```xml
<option name="TEXT">
  <value>
    <option name="BACKGROUND" value="你的颜色" />
  </value>
</option>
```

需要让行号区、控制台和界面背景同步时，同时调整 XML 中 `colors` 下的 `GUTTER_BACKGROUND`、`CONSOLE_BACKGROUND_KEY`，`attributes` → `CONSOLE_OUTPUT` 下的 `BACKGROUND`，以及对应主题 JSON 的 `colors.editorBackground`。

⚠️ **注意**：XML 中的颜色值不带 `#` 号！

---

## 文件结构

```
one-dark-by-gp/
├── resources/
│   ├── META-INF/
│   │   ├── plugin.xml          # 插件配置
│   │   └── pluginIcon.svg      # 插件图标
│   ├── onedarkbygp.theme.json  # 深色 UI 主题配置
│   ├── onedarkbygp.xml         # 深色编辑器配色方案
│   ├── onelightbygp.theme.json # 浅色 UI 主题配置
│   └── onelightbygp.xml        # 浅色编辑器配色方案
├── one-dark-by-gp.jar          # 打包后的插件
├── build.py                   # 编译项目树扩展并打包插件
├── src/gp/theme/
│   └── IgnoredDirectoryDecorator.java # 按忽略状态淡化目录图标
├── preview.command            # 双击或命令行启动 WebStorm 自动预览
├── preview.py                 # 编译预览加载器并启动独立实例
├── preview/
│   ├── PreviewRuntime.java    # 在预览实例中刷新界面和编辑器配色
│   └── sample.ts              # 语法高亮示例
└── README.md
```
