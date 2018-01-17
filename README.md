# LyterAi

*An experiment to investigate the implementation of machine learning models on webservers.*
<hr>

## Setup
Requirements outside of Conda env:
```bash
nodejs
npm
bower
gulp: ^3.9.1
gulp-connect: ^5.0.0
gulp-sass: ^3.1.0
```
Create a conda environment.
```bash
conda env create -f environment.yml
```
Install bower packages.
```bash
bower install
```
Make migrations and migrate:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Optional:
Seed test data.
```bash
make seed
```

## Run server
Run gulp for compiling static files (sass).
```bash
gulp
```
Run django development server.
```bash
make server
