# Capstone Project
https://github.com/joonyi/Capstone

## 1. Parse Resume (parse-resume/)
Parse the LinkedIn resumes and the result will be saved to
- parse-resumes/
- upload-db/
- job-match/
```python
python parse-resume.py
```

## 2. Upload into Database (upload-db/)
Upload the output of parse resume into database
```python
python upload-resumes.py
```
Stages data are randomly generated. Here is a [random name generation website](https://www.behindthename.com/random/)
```python
python generate-stages.py  # Generate stages data, requires random name generation
python upload-stages.py  # Upload stages data
```
## 3. Generate Statistics (django-job-stat/JobMatch/)

More on working with Django and postgres db in django-job-stat/JobMatch/README.md

After starting Django, go to urls below to display the statistics

| Feature | Url |
| ------ | ------ |
| Display resumes database | http://localhost:8000/api/resumes/ |
| Display resumes statistic | http://localhost:8000/api/resumes/stat |
| Display stages database | http://localhost:8000/api/stages/ |
| Display stages statistic | http://localhost:8000/api/stages/stat |

#### Resume Statistics
- Top five skills, locations, languages, certifications, publications, honors, education in Jobhax database
- Top five attributes from a specific company
- Top five companies recruiting from Jobhax
- Top five positions recruiting from Jobhax

## 4. Learn and Predict Job Match (job-match/)
First, generate train and test data from the whole dataset. To avoid confusion of giving input, company name and portion of learning data is hardcoded. For demonstration, company is Google (other possible names are amazon, apple, facebook, google, salesforce), training size is 0.9
```python
python generate-train-test.py
```
Train and test data will be saved to train.csv and test.csv. Then it is ready to run the job match python code. Input requires model selection (dt or svm) and output job match prediction to job_match.csv 

```python
python job-match.py
```