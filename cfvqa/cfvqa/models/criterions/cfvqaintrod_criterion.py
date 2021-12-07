import torch.nn as nn
import torch
import torch.nn.functional as F
from bootstrap.lib.logger import Logger
from bootstrap.lib.options import Options

class CFVQAIntroDCriterion(nn.Module):

    def __init__(self):
        super().__init__()

        self.cls_loss = nn.CrossEntropyLoss(reduction='none')
     
    def forward(self, net_out, batch):
        out = {}
        logits_all = net_out['logits_all']
        class_id = batch['class_id'].squeeze(1)

        # KD
        logits_t = net_out['logits_cfvqa']
        logits_s = net_out['logits_stu']
        p_t = torch.nn.functional.softmax(logits_t, -1).clone().detach()
        kd_loss = - p_t*F.log_softmax(logits_s, -1)    
        kd_loss = kd_loss.sum(1)

        cls_loss = self.cls_loss(logits_s, class_id)
    
        # weight estimation
        cls_loss_ood = self.cls_loss(logits_t, class_id)
        cls_loss_id = self.cls_loss(logits_all, class_id)        
        weight = cls_loss_ood/(cls_loss_ood+cls_loss_id)
        weight = weight.detach()

        loss = (weight*kd_loss).mean() + ((1-weight)*cls_loss).mean()

        out['loss'] = loss
        return out
