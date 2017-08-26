# LyterAi

*An experiment to bring AI to open source and promote collaboration within the community.*
LyterAi was created to allow the AI community to contribute their data and expertise in collaboration to create models accessible to developers.
<hr>

## Setup (Untested)
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
```