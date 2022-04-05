# shellcheck shell=sh

export https_proxy=http://me.niracler.com:1080 http_proxy=http://me.niracler.com:1080 all_proxy=socks5://me.niracler.com:1080
python bot.py "$1"
