# CLIENT RADAR BACKEND

## STARTED
### ENVIRONTMENT
```bash
conda create --name project15 python=3.9
conda activate project15
conda deactivate
```

### START PROJECT
```bash
git clone git@github.com:Trycatch-tv/team-44-project-15-clientRadar-backend.git
cd team-44-project-15-clientRadar-backend
pip install --no-cache-dir --upgrade -r requirements.txt
uvicorn app.main:app --reload
```

## BUILD DOCKER IMAGE

```bash
pip3 freeze > requirements.txt
docker build . -t user/team-44-project-15-s:0.0.1
```

## START DATABASE
```bash
docker run --name mysql_db -d  -e MYSQL_ROOT_PASSWORD=password --restart=always mysql
docker exec -it mysql_db mysql -u root -p
```
