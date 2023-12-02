#!/bin/sh

directories=$(find "/builds/aps/ansible-test/version_dir" -type d)

for dir in $directories; do
    if [ "$dir" != . ]; then
        for file in "$dir"/*; do
            if [ -f "$file" ]; then
              single_line=$(tr '\n' ',' < $file)
                #cat "$file" >> version.txt
                echo "$single_line,$dir"  >> version.txt
            fi
        done
    fi
done
