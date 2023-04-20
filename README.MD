## BACKEND

### START SERVER

```bash
uvicorn app.main:app --reload
```

## ENVIRONTMENT

```bash
conda create --name project15 python=3.9
conda activate project15
conda deactivate
```

## BUILD DOCKER IMAGE

```bash
pip3 freeze > requirements.txt
docker build . -t user/team-44-project-15-s:0.0.1
```
