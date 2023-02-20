
conda create -n django-tasks


git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/PredictIf/mogas-video-tasks.git
git push -u origin main

# TODO: #1 install django
# TODO: #2 setup admin

git fetch origin
git checkout 1-install-django


docker run -itd \
    -p 9999:8888 \
    --name devbox-x64 \
    --restart always \
    --privileged \
    --platform linux/amd64 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.aws:/root/.aws \
    -v ~/Dropbox/work-0/-general/qc:/root/notebooks/QC \
    -v /Users/marian.dumitrascu/Dropbox/work-P/video-tasks:/root/video-tasks \
    predictif/devbox-x64:001 /bin/bash -c "\
    jupyter notebook \
    --notebook-dir=~/notebooks --ip='*' --port=8888 \
    --no-browser --allow-root"

# ################################################################################
# install django

pip install django

django-admin startproject mainsite .

python manage.py startapp video_tasks

python manage.py runserver 8080

python manage.py runserver

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

# password is: ....123
