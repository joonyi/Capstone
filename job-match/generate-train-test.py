import json


def employee_in(data, comp):
    comp = comp.lower()
    employees = []
    for line in data:
        job = ' '.join(line["current_job"]).lower()
        if comp in job:
            employees.append(line)

    return employees


def extract_top_skills(data):
    res = []
    for line in data:
        A = []
        for k, val in line.items():
            if k == 'name':
                if "," in val:
                    val = val[:val.index(",")]
                A.append(val)
            elif k == 'top_skills':
                A.extend(val[:3])

        if len(A) == 4:
            res.append(A)

    return res  # list of list


def generate_train_data(data, comp):
    # employees hired by comp will be labelled 'Matched', else 'Unmatched'
    company = comp.lower()
    names = [emp['name'] for emp in employee_in(data, company)]
    res = []
    line = []
    with open('train.csv', 'w') as f:
        f.write('Name,Top Skills 1,Top Skills 2,Top Skills 3,Status\n')
        for sbj in extract_top_skills(data):
            if sbj[0] in names:
                line.append(','.join(sbj) + ",Matched")
            else:
                line.append(','.join(sbj) + ",Unmatched")

        f.write('\n'.join(line))


def generate_test_data(data):
    line = []
    with open('test.csv', 'w') as f:
        f.write('Name,Top Skills 1,Top Skills 2,Top Skills 3,Status\n')
        for sbj in extract_top_skills(data):
            line.append(','.join(sbj) + ",Applied")
        f.write('\n'.join(line))


def generate_train_test(data, comp, train_size):
    company = comp.lower()
    n = int(len(data) * train_size)
    generate_train_data(data[:n], company)
    generate_test_data(data[n:])


if __name__ == "__main__":
    with open('resume_data.json', 'r') as json_file:
        data = [json.loads(x) for x in json_file.readlines()]

    company = 'Google'  # one can change the hardcoded names and size here
    train_size = 0.9

    print(f"Generate train or test data for {company}")
    generate_train_test(data, company, train_size)
    print("Done!")
