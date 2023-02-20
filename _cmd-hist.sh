
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
