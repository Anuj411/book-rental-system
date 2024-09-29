sudo apt update
sudo apt-get install python3-pip python3-dev git-core virtualenv redis-server default-libmysqlclient-dev build-essential pkg-config telnet nginx

pip install -r ../requirements/production.txt

sudo cp ./deployment/nginx.conf /etc/nginx/sites-available/project
sudo cp ./deployment/gunicorn.conf /etc/systemd/system/gunicorn.service

sudo ln -s /etc/nginx/sites-available/project /etc/nginx/sites-enabled
sudo nginx -t

python manage.py collectstatic
python manage.py seed

sudo systemctl start redis-server
sudo systemctl enable redis-server

sudo systemctl daemon-reload

sudo systemctl restart nginx
sudo systemctl start gunicorn
sudo systemctl enable gunicorn