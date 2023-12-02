#!/bin/sh

dir=$(find "/Users/akasnir/Documents/loblaw/Stories/GCP-list-of-VMs/sh_file_test/u01" -type d)

if [ -d /Users/akasnir/Documents/loblaw/Stories/GCP-list-of-VMs/sh_file_test/u01/ ]; then
    echo "test"
    else
      echo "test-2"
fi

mkdir -p /Users/akasnir/Documents/loblaw/Stories/GCP-list-of-VMs/sh_file_test/u/a/b
