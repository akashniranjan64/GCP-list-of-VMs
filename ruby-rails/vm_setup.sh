#!/bin/bash

sudo -s << EOF
yum install -y git-core zlib zlib-devel gcc-c++ patch readline readline-devel libyaml-devel libffi-devel openssl-devel make bzip2 autoconf automake libtool bison curl sqlite-devel
EOF

if [ -d ~/.rbenv ]; then
  echo "ruby is already installed. Upgrading the version"

  rbenv install -v 2.7.7
  rbenv global 2.7.7
else
  git clone https://github.com/rbenv/rbenv.git ~/.rbenv
  echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(rbenv init -)"' >> ~/.bashrc

  git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
  echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc

  rbenv install -v 2.7.7
  rbenv global 2.7.7
fi

ruby -v
exit_status=$?

if [ $exit_status -eq 0 ]; then
    echo "gem: --no-document" > ~/.gemrc
    gem install bundler
    gem install rails
    rbenv rehash
    rails -v
else
    echo "ruby not installed successfully"
fi