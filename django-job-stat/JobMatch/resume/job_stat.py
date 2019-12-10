import json
from collections import Counter
import re


def top_skills_in(comp, data):
    comp = comp.lower()
    target = []
    for line in data:
        job = line["current_job"].lower()
        if comp in job:
            target.append(line)

    skills = Counter()
    for line in target:
        sk = [line["top_skills"]]
        skills.update(Counter(sk))

    return skills.most_common(5)


def common_attr(attr, data):
    skills = Counter()
    for line in data:
        n = [line[attr]]
        skills.update(Counter(n))
    return skills.most_common((5))


def top_companies(data):
    companies = []
    for line in data:
        job = line['current_job']
        company = re.search(r"\sat\s(.+)", job)
        if company:
            companies.append(company.group(1))

    return Counter(companies).most_common(5)


def top_positions(data):
    positions = []
    for line in data:
        job = line['current_job']
        position = re.search(r"(.+)\sat\s", job)
        if position:
            positions.append(position.group(1))

    return Counter(positions).most_common(5)

