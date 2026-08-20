#!/usr/bin/env bash
set -e

SKILL_DIR="$(cd "$(dirname "$0")" && pwd)/memphis-resume-site"
TARGET="$HOME/.agents/skills/memphis-resume-site"

echo
echo "============================================"
echo "  Memphis Resume Site - 技能安装"
echo "============================================"
echo

if [ -d "$TARGET" ]; then
  echo "[提示] 检测到已安装，正在覆盖更新..."
  rm -rf "$TARGET"
fi

mkdir -p "$(dirname "$TARGET")"
cp -R "$SKILL_DIR" "$TARGET"

echo "[完成] 安装成功！"
echo "技能位置: $TARGET"
echo
echo "使用方法：打开 ZCode，新开一个对话，输入"
echo "  \"把简历做成网站\"  并附上你的简历文件"
echo
