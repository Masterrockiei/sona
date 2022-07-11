if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Masterrockiei/sona.git /sona
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /sona
fi
cd /sona
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
