#!/bin/bash
OLD_DIR=$1
NEW_DIR=$2

cp -R ${OLD_DIR}/annotation_train/. ${NEW_DIR}
cp -R ${OLD_DIR}/annotation_validation/. ${NEW_DIR}
echo "Annotations done"

mkdir ${NEW_DIR}/questions
cp ${OLD_DIR}/train.json ${NEW_DIR}/questions/train.json
cp ${OLD_DIR}/validation.json ${NEW_DIR}/questions/validation.json
cp ${OLD_DIR}/val.json ${NEW_DIR}/questions/validation.json
cp ${OLD_DIR}/test.json ${NEW_DIR}/questions/test.json
echo "Questions done"

cp -R ${OLD_DIR}/derender_proposals/. ${NEW_DIR}/proposals
echo "Proposals done"

python3 process_videos.py ${OLD_DIR} ${NEW_DIR} 25