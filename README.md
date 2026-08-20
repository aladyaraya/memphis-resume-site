# 🎨 Memphis Resume Site — 孟菲斯风格简历网站生成技能

> 把一份简历（docx / PDF / 纯文本）一键变成**孟菲斯风格的个人主页网站**。
> 单文件、零依赖、双击即开，内置"点击即改"的编辑模式。

这是一个 [ZCode](https://z.ai) 技能（Skill）：安装后，在对话框里说一句"把简历做成网站"，附上简历文件，AI 就会自动提取简历内容、套用孟菲斯模板、生成一个完整的个人主页。

## ✨ 特性

- **一句话生成**：附上 docx/PDF 简历或直接粘贴文字，AI 自动解析并生成
- **孟菲斯视觉**：奶油底色 + 高饱和几何色块，圆形/三角/波浪线装饰，8 个板块（工作 / 实习 / 项目 / 获奖 / 技能证书 / 行业经历 / 联系方式）
- **零门槛编辑**：页面右下角 ✎ 进入编辑模式，点击任意文字直接修改，自动保存在浏览器本地
- **单文件交付**：生成的是 `index.html`，双击就能打开，不需要装环境、不需要服务器
- **数据可备份**：内置「导出 JSON」备份、"恢复默认"一键重置，头像点击即可更换照片

## 🖼 效果预览

> 📸 把你的网站截图放到 `images/` 目录（如 `preview-1.png`），然后取消下面注释：

<!--
![网站效果](images/preview-1.png)
![编辑模式](images/preview-2.png)
-->

## 📦 安装

前置要求：已安装 [ZCode](https://z.ai)。

### Windows

双击运行 `install.bat`

### macOS / Linux

```bash
bash install.sh
```

### 手动安装

把 `memphis-resume-site` 文件夹整个复制到技能目录：

- Windows：`C:\Users\<用户名>\.agents\skills\`
- macOS / Linux：`~/.agents/skills/`

### 或者直接用 git 克隆

```bash
# Windows (PowerShell)
git clone https://github.com/<你的用户名>/memphis-resume-site.git "$env:USERPROFILE\.agents\skills\memphis-resume-site"

# macOS / Linux
git clone https://github.com/<你的用户名>/memphis-resume-site.git ~/.agents/skills/memphis-resume-site
```

安装后重启 ZCode 或新开一个对话即可生效。

## 🚀 使用

在任意 ZCode 对话框输入类似的话：

> 把这份简历做成个人主页网站（附上 .docx 简历文件）
>
> 帮我做个简历网页，我的简历内容：……（直接粘贴文字）

AI 会在你指定的目录生成 `index.html`。之后：

1. 双击 `index.html` 用浏览器打开
2. 点右下角 **✎** 进入编辑模式
3. 点击任意文字直接修改，点击头像更换照片
4. 点 **💾 保存到本地**，内容存入浏览器 localStorage
5. 想分享？把 `index.html` 上传到 GitHub Pages / Vercel / Netlify 等任意静态托管即可

## 🧹 卸载

删除技能目录即可：

```bash
# Windows
rmdir /s /q "%USERPROFILE%\.agents\skills\memphis-resume-site"

# macOS / Linux
rm -rf ~/.agents/skills/memphis-resume-site
```

## 📁 目录结构

```
memphis-resume-site/
├── README.md                     # 本说明
├── install.bat                   # Windows 一键安装
├── install.sh                    # macOS / Linux 一键安装
├── LICENSE                       # MIT 许可
├── images/                       # 效果截图（自己补充）
└── memphis-resume-site/          # 技能本体（安装时整个复制到 .agents/skills/）
    ├── SKILL.md                  # 技能工作流定义
    ├── assets/
    │   └── template.html         # 孟菲斯网站模板（数据区带标记）
    ├── scripts/
    │   └── extract_resume.py     # 简历文本提取脚本
    └── references/
        └── data-schema.md        # 简历数据结构字段规范
```

## ❓ 常见问题

**Q：生成的网站改不了？**
A：先点右下角 ✎ 按钮进入编辑模式，文字才有虚线框可点击。

**Q：换浏览器/换电脑后我的修改没了？**
A：内容保存在浏览器 localStorage 里，与浏览器绑定。用「📥 导出 JSON」备份，或直接把 `index.html` 里的数据改掉（会改代码的话）。

**Q：想要其他风格（暗色、极简……）？**
A：在技能目录 `assets/` 下添加新模板，并修改 `SKILL.md` 增加模板选择步骤即可，工作流不变。

**Q：生成的内容和简历对不上？**
A：AI 解析简历时偶尔有偏差，直接在页面上点 ✎ 改过来并保存即可。

## 📄 License

[MIT](LICENSE)
