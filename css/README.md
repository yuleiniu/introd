# CSS+IntroD

This code provides the implementation of IntroD on top of LMH and CSS on the VQA task. This code is modified from [css](https://github.com/yanxinzju/CSS-VQA) and [lmh](https://github.com/chrisc36/bottom-up-attention-vqa). The data is provided by the authors of "Counterfactual Samples Synthesizing for Robust VQA".

## Prerequisites

(Follow [css](https://github.com/yanxinzju/CSS-VQA))

Make sure you are on a machine with a NVIDIA GPU and Python 2.7 with about 100 GB disk space. <br>
h5py==2.10.0 <br>
pytorch==1.1.0 <br>
Click==7.0 <br>
numpy==1.16.5 <br>
tqdm==4.35.0 <br>

## Data Setup

(The data is provided by [css](https://github.com/yanxinzju/CSS-VQA).)

You can use
```
bash tools/download.sh
```
to download the data <br>
and the rest of the data and trained model can be obtained from [BaiduYun](https://pan.baidu.com/s/1oHdwYDSJXC1mlmvu8cQhKw)(passwd:3jot) or [GoogleDrive](https://drive.google.com/drive/folders/13e-b76otJukupbjfC-n1s05L202PaFKQ?usp=sharing)
unzip feature1.zip and feature2.zip and merge them into data/rcnn_feature/ <br>
use
```
bash tools/process.sh 
```
to process the data <br>

## CSS+IntroD

### Step 1: train the teacher model

(Follow [css](https://github.com/yanxinzju/CSS-VQA))

Run
```
CUDA_VISIBLE_DEVICES=0 python main.py --dataset cpv2 --mode q_v_debias --debias learned_mixin --topq 1 --topv -1 --qvp 5 --output ./logs/vqacp2/css/
```
to train a teacher model on VQA-CP v2.

Or

Run
```
CUDA_VISIBLE_DEVICES=0 python main.py --dataset v2 --mode q_v_debias --debias learned_mixin --topq 1 --topv -1 --qvp 5 --output ./logs/vqacp2/css/
```
to train a teacher model on VQA v2.

### Step 2: train the student model

Run
```
CUDA_VISIBLE_DEVICES=0 python main_introd.py --dataset cpv2 --output ./logs/vqacp2/css_introd/ --source ./logs/vqacp2/css/
```
to train a student model on VQA-CP v2.

Or

Run
```
CUDA_VISIBLE_DEVICES=0 python main_introd.py --dataset v2 --output ./logs/vqa2/css_introd/ --source ./logs/vqa2/css/
```
to train a student model on VQA v2.

## LMH+IntroD

### Step 1: train the teacher model

(Follow [css](https://github.com/yanxinzju/CSS-VQA))

Run
```
CUDA_VISIBLE_DEVICES=0 python main.py --dataset cpv2 --mode updn --debias learned_mixin --output ./logs/vqacp2/lmh/
```
to train a teacher model on VQA-CP v2.

Or

Run
```
CUDA_VISIBLE_DEVICES=0 python main.py --dataset v2 --mode updn --debias learned_mixin --output ./logs/vqa2/lmh/
```
to train a teacher model on VQA v2.


### Step 2: train the student model

Run
```
CUDA_VISIBLE_DEVICES=0 python main_introd.py --dataset cpv2 --output ./logs/vqacp2/lmh_introd/ --source ./logs/vqacp2/lmh/
```
to train a student model on VQA-CP v2.

Or

Run
```
CUDA_VISIBLE_DEVICES=0 python main_introd.py --dataset v2 --output ./logs/vqa2/lmh_introd/ --source ./logs/vqa2/lmh/
```
to train a student model on VQA v2.