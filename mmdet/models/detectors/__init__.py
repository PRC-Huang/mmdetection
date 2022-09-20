# Copyright (c) OpenMMLab. All rights reserved.
from .gfl import GFL
from .single_stage import SingleStageDetector

__all__ = [
    'BaseDetector', 'SingleStageDetector', 'GFL']
