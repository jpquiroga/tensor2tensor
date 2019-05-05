# coding=utf-8
#
# Author jdpq (jdpq@gmail.com)

"""Data generators for translation data-sets. English - Spanish."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import translate
from tensor2tensor.utils import registry


_ENES_TRAIN_DATASETS = [
    [
        "https://drive.google.com/file/d/1J77RFV9qyEhF0hKzp2CRX2ybvVT5Au7u/view?usp=sharing",
        ("opensubtitles_translation_60M/en_60M.txt",
         "opensubtitles_translation_60M/es_60M.txt")
    ],
    [
        "https://drive.google.com/file/d/1BG7ILl6VRCSP_vOciVIeB17b-bcYCndv/view?usp=sharing",
        ("opensubtitles_translation_10M/en_10M.txt",
         "opensubtitles_translation_10M/es_10M.txt")
    ],
    [
        "https://drive.google.com/file/d/1WI0NgJ9EWePtVz4ngqvJIn7q5-OiiE-y/view?usp=sharing",
        ("opensubtitles_translation_1M/en_1M.txt",
         "opensubtitles_translation_1M/es_1M.txt")
    ],
]
_ENES_EVAL_DATASETS = [
    [
        "https://drive.google.com/file/d/1TSQZP6WTC05mLIQzo8FS5EwHCNtK1TYw/view?usp=sharing",
        ("opensubtitles_translation_validation/en_val_100K.txt",
         "opensubtitles_translation_validation/es_val_100K.txt")
    ],
]


@registry.register_problem
class TranslateEnesOpensubtitles32k(translate.TranslateProblem):
  """En-es translation trained on opensubtitle corpus."""

  @property
  def additional_training_datasets(self):
    """Allow subclasses to add training datasets."""
    return []

  def source_data_files(self, dataset_split):
    train = dataset_split == problem.DatasetSplit.TRAIN
    train_datasets = _ENES_TRAIN_DATASETS + self.additional_training_datasets
    return train_datasets if train else _ENES_EVAL_DATASETS


@registry.register_problem
class TranslateEnesOpensubtitlesClean32k(TranslateEnesOpensubtitles32k):
  """En-de translation trained on WMT with further cleaning."""

  @property
  def use_vocab_from_other_problem(self):
    return TranslateEnesOpensubtitles32k()

  @property
  def datatypes_to_clean(self):
    return ["txt"]
