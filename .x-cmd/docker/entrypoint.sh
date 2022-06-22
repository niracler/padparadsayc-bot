# shellcheck shell=sh

export https_proxy=http://me.niracler.com:2087 http_proxy=http://me.niracler.com:2087 all_proxy=socks5://me.niracler.com:2080
python bot "$1"
