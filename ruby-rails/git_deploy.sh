#!/bin/bash

REPO_URL="gitlab.lblw.ca/aps/tools/lt-aps-sre-tools.git"
TARGET_DIR="/home/lcluser01/scheduler_web/app_repo/target_dir"
BRANCH_TAG_NAME="v1.1.0"
GIT_USERNAME=""
GIT_PASSWORD=""
DESTINATION_DIR="/home/lcluser01/scheduler_web/app_repo/destination_dir"

if [ -d "${DESTINATION_DIR}" ]; then
      rm -rf ${DESTINATION_DIR}
      git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@${REPO_URL} ${TARGET_DIR} --branch=${BRANCH_TAG_NAME} --single-branch --depth=1
      mv "${TARGET_DIR}" "${DESTINATION_DIR}"
      rm -rf ${TARGET_DIR}

else
      git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@${REPO_URL} ${TARGET_DIR} --branch=${BRANCH_TAG_NAME} --single-branch --depth=1
      mv "${TARGET_DIR}" "${DESTINATION_DIR}"
      rm -rf ${TARGET_DIR}
fi
