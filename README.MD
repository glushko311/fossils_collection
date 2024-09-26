### Project board
https://trello.com/b/ez6SCQZj/fossilscollecton

### Run project

1. clone repo
2. create in %project_path%/src/config folder develop.env, production.env, testing.env files
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
7. Run migrations 
    **alembic upgrade head**
8. To start server run script 
    **%abs_path%/fossils_collection/src/main.py**


### Migrations
Create new migration
    **alembic revision --autogenerate -m "Create first migration"**
Upgrade migrations
    **alembic upgrade head**


### Run autoformat

black src/