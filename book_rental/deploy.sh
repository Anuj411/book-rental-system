sudo apt update
sudo apt-get install python3-pip git-core virtualenv redis-server telnet nginx

pip install -r ../requirements/production.txt

sudo mv deployment/nginx.conf /etc/nginx/sites-available/project
sudo mv deployment/gunicorn.conf /etc/systemd/system/gunicorn.service

python manage.py collectstatic
python manage.py seed

sudo systemctl start redis-server
sudo systemctl enable redis-server

sudo systemctl daemon-reload

sudo systemctl restart nginx
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

sudo systemctl daemon-reload