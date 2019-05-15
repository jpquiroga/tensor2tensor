#!/usr/bin/env bash
PROBLEM=translate_ende_wmt32k
MODEL=transformer
HPARAMS=transformer_base_single_gpu

BASE_DIR=$HOME/ssd3
DATA_DIR=$BASE_DIR/t2t_data
TMP_DIR=$BASE_DIR/tmp/t2t_datagen
TRAIN_DIR=$BASE_DIR/t2t_train/$PROBLEM/$MODEL-$HPARAMS

mkdir -p $DATA_DIR $TMP_DIR $TRAIN_DIR

# Generate data
t2t-datagen \
  --data_dir=$DATA_DIR \
  --tmp_dir=$TMP_DIR \
  --problem=$PROBLEM


