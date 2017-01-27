# Train all the models from datasets/ folder
DATASETS_FOLDER='../datasets'
VERSION_NAME='v1'

for entry in $DATASETS_FOLDER/*.txt; do
    echo 'Dataset: '$entry
    python ../code/trainer.py $VERSION_NAME $entry
done
