python -m bootstrap.run -o cfvqa/options/vqacp2/smrl_rubi.yaml
mkdir ./logs/vqacp2/smrl_rubiintrod/
cp ./logs/vqacp2/smrl_rubi/ ./logs/vqacp2/smrl_rubiintrod/
python -m run -o ./cfvqa/options/vqacp2/smrl_rubiintrod.yaml