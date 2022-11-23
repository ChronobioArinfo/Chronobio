PORT=$(python -c "import random; print(random.randint(2000, 3000))")

git clone git@github.com:vpoulailleau/chronobio.git
cd chronobio
python -m chronobio.game.server -p $PORT &
cd -
sleep 2
python -m player.player -u Vincent -p $PORT &