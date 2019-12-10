# django-job-stat

Django API that return on how candidates match the job
1. Install python3 on your [OS](https://www.python.org/downloads/):

2. Install Postgres database depending on your [OS](https://www.postgresql.org/download/):

3. Make sure your Postgres is running:
```
# Start Postgres
initdb /usr/local/var/postgres
pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
```

4. Run install script located in root directory:
```
./install.sh
```

5. Start server located in root directory:
```
./start.sh
```

| Feature | Url |
| ------ | ------ |
| Display resumes database | http://localhost:8000/api/resumes/ |
| Display resumes statistic | http://localhost:8000/api/resumes/stat |
| Display stages database | http://localhost:8000/api/stages/ |
| Display stages statistic | http://localhost:8000/api/stages/stat |
