python -m bootstrap.run -o cfvqa/options/vqacp2/smrl_cfvqasimple_rubi.yaml
mkdir ./logs/vqacp2/smrl_cfvqasimpleintrod_rubi/
cp ./logs/vqacp2/smrl_cfvqasimple_rubi/ ./logs/vqacp2/smrl_cfvqasimpleintrod_rubi/
python -m run -o ./cfvqa/options/vqacp2/smrl_cfvqasimpleintrod_rubi.yaml