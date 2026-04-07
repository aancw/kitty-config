#!/usr/bin/env bash
set -euo pipefail

url="${1:-}"
[ -n "$url" ] || exit 0

cols="$(tput cols 2>/dev/null || echo 80)"
rows="$(tput lines 2>/dev/null || echo 24)"

line1="Open this URL?"
line2="$url"
line3="[y/N] "

content_height=5
top_pad=$(( (rows - content_height) / 2 ))
if [ "$top_pad" -lt 0 ]; then
  top_pad=0
fi

center_line() {
  local text="$1"
  local text_len="${#text}"
  local left_pad=$(( (cols - text_len) / 2 ))
  if [ "$left_pad" -lt 0 ]; then
    left_pad=0
  fi
  printf "%*s%s\n" "$left_pad" "" "$text"
}

center_prompt() {
  local text="$1"
  local text_len="${#text}"
  local left_pad=$(( (cols - text_len) / 2 ))
  if [ "$left_pad" -lt 0 ]; then
    left_pad=0
  fi
  printf "%*s%s" "$left_pad" "" "$text"
}

printf "\033[2J\033[H"
for ((i=0; i<top_pad; i++)); do
  printf "\n"
done
center_line "$line1"
center_line ""
center_line "$line2"
center_line ""
center_prompt "$line3"

IFS= read -r -n 1 answer || true
printf "\n"

case "$answer" in
  y|Y)
    open "$url"
    ;;
  *)
    exit 0
    ;;
esac
