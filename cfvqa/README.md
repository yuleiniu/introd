# CFVQA+IntroD

This code is implemented as a fork of [CF-VQA][1] and [RUBi][2].

CF-VQA is proposed to capture and mitigate language bias in VQA from the view of causality. CF-VQA (1) captures the language bias as the direct causal effect of questions on answers, and (2) reduces the language bias by subtracting the direct language effect from the total causal effect.

## Summary

* [Installation](#installation)
    * [Setup and dependencies](#1-setup-and-dependencies)
    * [Download datasets](#2-download-datasets)
* [Quick start](#quick-start)
    * [Train a model](#train-a-model)
    * [Evaluate a model](#evaluate-a-model)
* [Useful commands](#useful-commands)
* [Acknowledgment](#acknowledgment)

## Installation


### 1. Setup and dependencies

Install Anaconda or Miniconda distribution based on Python3+ from their downloads' site.

```bash
conda create --name cfvqa python=3.7
source activate cfvqa
pip install -r requirements.txt
```

For the error that `ModuleNotFoundError: No module named 'block.external'`, please follow [this issue](https://github.com/yuleiniu/cfvqa/issues/7) for the solution.


### 2. Download datasets

Download annotations, images and features for VQA experiments:
```bash
bash cfvqa/datasets/scripts/download_vqa2.sh
bash cfvqa/datasets/scripts/download_vqacp2.sh
```


## Overview of commands and result files

### Train a model

The [bootstrap/run.py](https://github.com/Cadene/bootstrap.pytorch/blob/master/bootstrap/run.py) file load the options contained in a yaml file, create the corresponding experiment directory and start the training procedure. For instance, you can train our best model on VQA-CP v2 (CFVQA+SUM+SMRL) by running:
```bash?
python -m bootstrap.run -o cfvqa/options/vqacp2/smrl_cfvqa_sum.yaml
```
Then, several files are going to be created in `logs/vqacp2/smrl_cfvqa_sum/`:
- [options.yaml] (copy of options)
- [logs.txt] (history of print)
- [logs.json] (batchs and epochs statistics)
- **[\_vq\_val\_oe.json] (statistics for the language-prior based strategy, e.g., RUBi)**
- **[\_cfvqa\_val\_oe.json] (statistics for CF-VQA)**
- [\_q\_val\_oe.json] (statistics for language-only branch)
- [\_v\_val\_oe.json] (statistics for vision-only branch)
- [\_all\_val\_oe.json] (statistics for the ensembled branch)
- ckpt_last_engine.pth.tar (checkpoints of last epoch)
- ckpt_last_model.pth.tar
- ckpt_last_optimizer.pth.tar

Many options are available in the options directory. CFVQA represents the complete causal graph while cfvqas represents the simplified causal graph.

### Evaluate a model

There is no test set on VQA-CP v2, our main dataset. The evaluation is done on the validation set. For a model trained on VQA v2, you can evaluate your model on the test set. In this example, [boostrap/run.py](https://github.com/Cadene/bootstrap.pytorch/blob/master/bootstrap/run.py) load the options from your experiment directory, resume the best checkpoint on the validation set and start an evaluation on the testing set instead of the validation set while skipping the training set (train_split is empty). Thanks to `--misc.logs_name`, the logs will be written in the new `logs_predicate.txt` and `logs_predicate.json` files, instead of being appended to the `logs.txt` and `logs.json` files.
```bash
python -m bootstrap.run \
-o ./logs/vqacp2/smrl_cfvqa_sum/options.yaml \
--exp.resume last \
--dataset.train_split ''\
--dataset.eval_split val \
--misc.logs_name test 
```

## Run IntroD

We take CF-VQA+IntroD on VQA-CP v2 as an example. Simply run
```bash?
bash scripts/run_vqacp2_cfvqa_introd.sh
```
The statistics for the final student model are included in `./logs/vqacp2/smrl_cfvqaintrod_sum/_stu_val_oe.json`

## Useful commands

More useful commands can be founded [here](https://github.com/yuleiniu/cfvqa#useful-commands).

## Acknowledgment

Special thanks to the authors of [RUBi][2], [BLOCK][3], and [bootstrap.pytorch][4], and the datasets used in this research project.

[1]: https://github.com/yuleiniu/cfvqa
[2]: https://github.com/cdancette/rubi.bootstrap.pytorch
[3]: https://github.com/Cadene/block.bootstrap.pytorch
[4]: https://github.com/Cadene/bootstrap.pytorch
