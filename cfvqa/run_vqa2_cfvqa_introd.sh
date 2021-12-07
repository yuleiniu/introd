python -m bootstrap.run -o cfvqa/options/vqa2/smrl_cfvqa_sum.yaml
mkdir ./logs/vqa2/smrl_cfvqaintrod_sum/
cp ./logs/vqa2/smrl_cfvqa_sum/ ./logs/vqa2/smrl_cfvqaintrod_sum/
python -m run -o ./cfvqa/options/vqa2/smrl_cfvqaintrod_sum.yaml