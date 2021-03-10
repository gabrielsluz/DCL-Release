#!/bin/bash
OLD_DIR=$1
NEW_DIR=$2

cp -R ${OLD_DIR}/annotation_train/. ${NEW_DIR}
cp -R ${OLD_DIR}/annotation_validation/. ${NEW_DIR}