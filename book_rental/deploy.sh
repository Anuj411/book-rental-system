sudo apt update
sudo apt-get install python3-pip git-core virtualenv redis-server telnet nginx

sudo systemctl start redis-server
sudo systemctl enable redis-server

cd /documents/projects/
git clone https://github.com/Anuj411/book-rental-system.git
sudo virtualenv venv
source ./venv/bin/activate

cd book-rental-system/book_rental

pip install -r ../requirements/production.txt

mv deployment/nginx.conf /etc/nginx/sites-available/project
mv deployment/gunicorn.conf /etc/systemd/system/gunicorn.service

python manage.py collectstatic
python manage.py seed

sudo systemctl daemon-reload

sudo systemctl restart nginx
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

sudo systemctl daemon-reload