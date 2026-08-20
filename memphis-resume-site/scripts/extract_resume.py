#!/usr/bin/env python3
"""提取简历文件中的文本内容，输出纯文本到 stdout。

用法:
    python extract_resume.py <文件路径>

支持格式:
    .docx   需要 python-docx（pip install python-docx）
    .pdf    优先 pandoc，其次 pdftotext
    .txt/.md 直接按 UTF-8 读取
"""
import os
import subprocess
import sys


def extract_docx(path):
    from docx import Document
    doc = Document(path)
    parts = []

    # 段落
    for p in doc.paragraphs:
        if p.text.strip():
            parts.append(p.text)

    # 表格（简历常用表格排版）
    for t in doc.tables:
        for row in t.rows:
            cells = [c.text.strip() for c in row.cells]
            # 合并单元格会重复出现，去重相邻相同值
            dedup = []
            for c in cells:
                if not dedup or dedup[-1] != c:
                    dedup.append(c)
            line = ' | '.join(c for c in dedup if c)
            if line:
                parts.append(line)

    return '\n'.join(parts)


def extract_pdf(path):
    candidates = [
        ['pandoc', path, '-t', 'plain', '--wrap=none'],
        ['pdftotext', path, '-'],
    ]
    for cmd in candidates:
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout
        except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
            continue
    raise RuntimeError(
        'PDF 提取失败：本机缺少 pandoc 或 pdftotext。'
        '请让用户直接粘贴简历文本，或安装 pandoc 后重试。'
    )


def main():
    if len(sys.argv) < 2:
        print('用法: python extract_resume.py <文件路径>', file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f'文件不存在: {path}', file=sys.stderr)
        sys.exit(1)

    ext = os.path.splitext(path)[1].lower()

    if ext == '.docx':
        text = extract_docx(path)
    elif ext == '.pdf':
        text = extract_pdf(path)
    else:
        with open(path, encoding='utf-8-sig', errors='replace') as f:
            text = f.read()

    print(text)


if __name__ == '__main__':
    main()
