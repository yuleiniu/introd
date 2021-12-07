from bootstrap.lib.options import Options
from block.models.criterions.vqa_cross_entropy import VQACrossEntropyLoss
from .rubi_criterion import RUBiCriterion
from .cfvqa_criterion import CFVQACriterion
from .cfvqaintrod_criterion import CFVQAIntroDCriterion
from .rubiintrod_criterion import RUBiIntroDCriterion

def factory(engine, mode):
    name = Options()['model.criterion.name']
    split = engine.dataset[mode].split
    eval_only = 'train' not in engine.dataset
    
    opt = Options()['model.criterion']
    if split == "test" and 'tdiuc' not in Options()['dataset.name']:
        return None
    if name == 'vqa_cross_entropy':
        criterion = VQACrossEntropyLoss()
    elif name == "rubi_criterion":
        criterion = RUBiCriterion(
            question_loss_weight=opt['question_loss_weight']
        )
    elif name == "cfvqa_criterion":
        criterion = CFVQACriterion(
            question_loss_weight=opt['question_loss_weight'],
            vision_loss_weight=opt['vision_loss_weight'],
            is_va=True,
        )
    elif name == "cfvqasimple_criterion":
        criterion = CFVQACriterion(
            question_loss_weight=opt['question_loss_weight'],
            is_va=False,
        )
    elif name == "cfvqaintrod_criterion":
        criterion = CFVQAIntroDCriterion()
    elif name == "rubiintrod_criterion":
        criterion = RUBiIntroDCriterion()
    else:
        raise ValueError(name)
    return criterion
