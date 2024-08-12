### Run project

1. clone repo
2. create in root folder .env file like .env_sample and put data in it 
3. create and activate venv with python 3.11
    python3 -m venv venv
    source venv/bin/activate
4. setup requirements
    pip install -r requirements.txt
5. run database with docker
    cd docker
    bash start.sh
6. To start server run - fossils_collection/src/main.py


### Run autoformat

black src/