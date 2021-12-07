python -m bootstrap.run -o cfvqa/options/vqa2/smrl_rubi.yaml
mkdir ./logs/vqa2/smrl_rubiintrod/
cp ./logs/vqa2/smrl_rubi/ ./logs/vqa2/smrl_rubiintrod/
python -m run -o ./cfvqa/options/vqa2/smrl_rubiintrod.yaml