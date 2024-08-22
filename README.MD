### Run project

1. clone repo
2. create in root folder develop.env, production.env, testing.env files
like .env_sample and put data in it 
3. create and activate venv with python 3.11
    **python3 -m venv venv**
    **source venv/bin/activate**
4. setup requirements
    **pip install -r requirements.txt**
5. run database with docker
    **cd docker**
    **bash start.sh**
6. Add env variable APP_ENV=development 
7. To start server run script - %abs_path%/fossils_collection/src/main.py


### Run autoformat

black src/