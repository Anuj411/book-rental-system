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