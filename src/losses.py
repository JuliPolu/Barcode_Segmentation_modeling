from dataclasses import dataclass
from typing import List
from torch import nn
import torch.nn.functional as F
from config import LossConfig
from utils import load_object


@dataclass
class Loss:
    name: str
    weight: float
    loss: nn.Module


def get_losses(losses_cfg: List[LossConfig]) -> List[Loss]:
    return [
        Loss(
            name=loss_cfg.name,
            weight=loss_cfg.weight,
            loss=load_object(loss_cfg.loss_fn)(),
        )
        for loss_cfg in losses_cfg
    ]
