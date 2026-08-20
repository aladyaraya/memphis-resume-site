---
name: memphis-resume-site
description: 把简历（docx/PDF/纯文本）一键做成孟菲斯风格的简历主页网站。当用户提供简历文件或简历内容、并想要"个人主页 / 简历网页 / 简历网站 / 个人介绍页"时触发，即使用户没有明确说出"网站"或"孟菲斯"二字也应主动使用。生成的网站为单文件 index.html，双击即可打开，内置点击即改的编辑模式。
---

# Memphis Resume Site

把用户提供的简历内容，转换成一个**孟菲斯风格、可自行编辑**的单文件简历网页。

## 工作流总览

1. **提取** — 拿到简历纯文本（docx → 脚本提取；PDF → pandoc；纯文本 → 直接读）
2. **解析** — 把简历内容映射为结构化数据（字段定义见 `references/data-schema.md`）
3. **生成** — 复制 `assets/template.html`，只替换 DATA 标记区之间的内容
4. **验证** — 检查数据完整性、关键功能无缺失

## Step 1: 提取简历文本

先确定用户简历的来源：

- **用户附带了 .docx 文件**：运行
  ```bash
  python "scripts/extract_resume.py" "<文件绝对路径>"
  ```
  如果 python-docx 未安装（报 `ModuleNotFoundError: docx`），先 `pip install python-docx`，或改用 pandoc：`pandoc "<文件>" -t plain --wrap=none`。

- **用户附带了 .pdf 文件**：`pandoc "<文件>" -t plain --wrap=none`；若 pandoc 不可用，尝试 `pdftotext "<文件>" -`。都失败时，礼貌地请用户直接粘贴简历文本。

- **用户在消息里直接给了简历文字**：直接使用，跳过脚本。

## Step 2: 解析为结构化数据

阅读 `references/data-schema.md`，把简历内容映射成 `RESUME_DATA` 对象。

**严格遵守的规则：**

1. **不要编造**。简历里没有的信息，宁可留空字符串或空数组，也不要杜撰。姓名、邮箱、电话、学校、公司、奖项名必须逐字取自原文。
2. **可以整理措辞**。简历原文的要点可以适度压缩、去掉口语连接词，但不要改变事实（数字、奖项级别、时间必须保留）。
3. **必填兜底**：`personal.name` 至少要有值；`contact` 至少要有 email 或 phone 之一。若两者都缺失，`contact` 写 `{}`，不要生造联系方式。
4. **skills 的分类**：按简历实际内容归入 `programming / ai / embedded / vision / os / other` 六个分类，没有的分类省略。每个 `tags` 数组放具体技能词。
5. **配色分配**：卡片颜色按顺序轮换 `pink / blue / purple / mint / yellow`（模板内 accent 类），`skills` 标签颜色同理。这部分由模板渲染逻辑自动处理，无需写进数据。
6. 解析完成后，把 JSON 数据先在回复中展示给用户看一眼（可选），确认无误后再写入。

## Step 3: 生成网站

1. 读取 `assets/template.html` 全文。
2. 模板中有一对标记：
   ```js
   // ============ RESUME_DATA_START ============
   const defaultData = { ... };
   // ============ RESUME_DATA_END ============
   ```
   **只替换这两个标记之间的内容**，替换为 `const defaultData = <解析出的 JSON 对象字面量>;`。模板其余部分（CSS、HTML 结构、编辑逻辑）一律不动。
3. 输出路径：用户指定目录下的 `index.html`；用户没指定时，默认输出到当前工作目录的 `index.html`。如果目标是已有网站（如存在 `data.json`），提示用户可以用网站的「导出 JSON」功能先备份旧数据。
4. **不要**另存 `data.json`——模板是自包含单文件，双击即可打开；`fetch('data.json')` 在 file:// 协议下会失败。

写入数据时的注意：
- JSON 对象字面量直接内嵌为 JS 代码，注意字符串内的引号转义（中文引号 "" 无需转义，英文双引号用 `\"`）。
- 数据里不要出现 `</script>` 字样（会被浏览器截断），如需表达可写成 `<\/script>`。

## Step 4: 验证

生成后自查：

- [ ] `index.html` 中恰好有一对 `RESUME_DATA_START` / `RESUME_DATA_END` 标记
- [ ] `defaultData.personal.name` 非空，contact 至少有一个联系方式
- [ ] 页面包含：头部（姓名/头衔/联系方式）、工作经历、实习经历、项目经历、竞赛获奖、技能 & 证书、行业经历、联系方式、页脚
- [ ] 编辑功能齐全：右下角 ✎ 按钮 → 编辑模式 → 文字可点击修改 → 保存到本地 / 导出 JSON / 恢复默认
- [ ] 用浏览器打开测试（能用浏览器时）；提醒用户：双击 index.html 即可查看，点 ✎ 即可修改内容，数据保存在浏览器 localStorage

## 常见问题

- **docx 提取出的文本乱序**（表格简历常见）：按字段关键词（"教育背景""工作经历""项目经历"等）重新归组，再映射到 schema。
- **简历有照片路径**：`personal.photo` 只支持 dataURL 或网络 URL；本地文件路径无效，留空即可（用户可在页面点击头像自行上传）。
- **用户问"怎么修改网站内容"**：告诉他打开页面点右下角 ✎ 按钮即可直接编辑，无需改代码。
