#!/usr/bin/env sh
# Assumes it is running in the build folder.

echo "../data/ic_adb_48px.svg;output.png;480" | ./asset_conv 2>/dev/null
if md5sum --quiet -c ../scripts/test_single.md5; then
    echo "OK"
    return 0
else
    return 1
fi
