python -m bootstrap.run -o cfvqa/options/vqa2/smrl_cfvqasimple_rubi.yaml
mkdir ./logs/vqa2/smrl_cfvqasimpleintrod_rubi/
cp ./logs/vqa2/smrl_cfvqasimple_rubi/ ./logs/vqa2/smrl_cfvqasimpleintrod_rubi/
python -m run -o ./cfvqa/options/vqa2/smrl_cfvqasimpleintrod_rubi.yaml