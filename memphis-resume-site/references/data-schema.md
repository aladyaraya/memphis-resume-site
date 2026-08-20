# RESUME_DATA 字段定义

这是 `assets/template.html` 中 `defaultData` 对象的完整字段说明。解析简历时，把简历内容映射为这个结构；缺失的信息留空（`""` 或 `[]`），不要编造。

## 顶层结构总览

```js
{
  personal:   { name, nameEn, title, photo },
  education:  [ { school, degree, period, gpa, courses } ],
  work:       { company, role, period, summary, projects[] },
  internships:[ { company, role, period, details[] } ],
  projects:   [ { name, role, period, intro, details[], result } ],
  awards:     { recent[], university[] },
  skills:     { programming?, ai?, embedded?, vision?, os?, other? },
  certificates: [ "证书名" ],
  industryExperience: [ "行业活动" ],
  contact:    { wechat, github, phone, email, blog, location }
}
```

## 逐字段说明

### personal — 个人信息
| 字段 | 类型 | 说明 |
|------|------|------|
| name | string | **必填**。姓名，逐字取自简历 |
| nameEn | string | 英文名/拼音，无则留 `""` |
| title | string | 头衔，如"嵌入式工程师/哈工大微电子和机器人双学位" |
| photo | string | 照片 dataURL 或网络 URL；本地路径无效，留 `""`（用户可在页面点击头像上传） |

### education — 教育背景
数组，按时间倒序，每项：
| 字段 | 类型 | 说明 |
|------|------|------|
| school | string | 学校名 |
| degree | string | 专业/学位，如"计算机科学与技术（本科）" |
| period | string | 时间段 |
| gpa | string | GPA/排名，无则 `""` |
| courses | string | 主修课程，无则 `""` |

无教育信息时置 `[]`（页面会自动隐藏该板块）。

### work — 工作经历（正式工作，1 段或空对象）
| 字段 | 类型 | 说明 |
|------|------|------|
| company / role / period | string | 公司、职位、时间段 |
| summary | string | 一段话概述 |
| projects[] | array | 工作期间的代表项目 `{ name, description }` |

没有正式工作时写 `{ company:"", role:"", period:"", summary:"", projects:[] }`。
**多段正式工作**：最近一段放 `work`，其余段落放 `internships`（页面渲染成同款时间轴卡片；生成后提示用户可把"实习经历"标题在页面上直接改掉）。

### internships — 实习经历
数组，每项 `{ company, role, period, details[] }`。`details` 是工作要点字符串数组，每条一句话。按时间倒序排列。

### projects — 项目经历
数组，每项：
| 字段 | 说明 |
|------|------|
| name | 项目名称 |
| role | 担任角色（如"语音算法负责人"） |
| period | 时间段 |
| intro | 一句话项目介绍 |
| details[] | 职责要点数组，每条一句话 |
| result | 项目成果（如获奖/上线），无则 `""` |

### awards — 竞赛获奖
分两栏展示，各自按时间倒序：
- `recent[]`：近期黑客松 & 企业奖项 `{ name, date }`
- `university[]`：大学 & 传统竞赛 `{ name, date }`

若简历没分两类，把全部奖项放进 `recent`，`university` 置 `[]`。

### skills — 技能
对象，键固定为以下分类（没有的分类省略）：
| 键 | 含义 | 例子 |
|----|------|------|
| programming | 编程语言 | ["C", "C++", "Python"] |
| ai | AI 能力 | ["AI Agent开发", "RAG"] |
| embedded | 单片机 & 嵌入式 | ["单片机", "嵌入式技术"] |
| vision | 机器视觉 | ["OpenCV", "Halcon"] |
| os | 操作系统 | ["Linux", "ROS2"] |
| other | 其他 | ["CAD", "项目管理"] |

每项 `{ label: "分类中文名", tags: ["技能词", ...] }`。

### certificates — 证书
字符串数组，如 `["无线电操作证A类及电台执照", "C1驾驶执照"]`。

### industryExperience — 行业经历
字符串数组，如 `["2026百度AI开发者大会演说嘉宾"]`。

### contact — 联系方式
| 字段 | 说明 |
|------|------|
| wechat | 微信号（无则 ""，页面会隐藏） |
| github | GitHub 地址（有值时页面渲染为链接） |
| phone | 电话 |
| email | 邮箱 |
| blog | 博客地址（渲染为链接） |
| location | 所在地 |

**规则**：`email` 和 `phone` 至少有一个；简历里没有就留 `""`，不要生造。`github`/`blog` 无协议前缀时页面会自动补 `https://`。

## 编写数据时的注意

1. 数据直接内嵌为 JS 对象字面量（不是 JSON 文件），字符串里的英文双引号要转义为 `\"`；中文引号 "" 无需转义。
2. 数据中不要出现 `</script>` 字样，写成 `<\/script>`。
3. 数字和事实必须与简历原文一致（GPA、百分比、dB、奖项级别、日期等）。
