#!/bin/bash

REPO_URL="gitlab.xxxx.xx/aps/xxxxxx-playground/playground-aps-sre-sb.git"
TARGET_DIR="/home/lcluser01/scheduler/target_dir"
BRANCH_NAME="SREAPS-5919-vm-scheduler-akash"
GIT_USERNAME="xxxxxxxx"
GIT_PASSWORD="xxxxxxxxxxxxx"
DESTINATION_DIR="/home/lcluser01/scheduler/destination_dir"

if [ -d "${DESTINATION_DIR}" ]; then
      rm -rf ${DESTINATION_DIR}
      git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@${REPO_URL} ${TARGET_DIR} --branch=${BRANCH_NAME} --single-branch --depth=1 --single-branch
      git show-ref --verify --quiet "refs/heads/${BRANCH_NAME}"
      mv "${TARGET_DIR}" "${DESTINATION_DIR}"
      rm -rf ${TARGET_DIR}
      chmod 777 ${DESTINATION_DIR}/deployment.sh
      source ${DESTINATION_DIR}/deployment.sh

else
      git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@${REPO_URL} ${TARGET_DIR} --branch=${BRANCH_NAME} --single-branch --depth=1 --single-branch
      git show-ref --verify --quiet "refs/heads/${BRANCH_NAME}"
      mv "${TARGET_DIR}" "${DESTINATION_DIR}"
      #rm -rf ${TARGET_DIR}
      chmod 777 ${DESTINATION_DIR}/deployment.sh
      source ${DESTINATION_DIR}/deployment.sh

fi

