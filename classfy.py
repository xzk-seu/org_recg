

def get_list(filename):
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i = i.strip('\n')
            result.append(i)
    return result


def write_result(filename, result):
    with open(filename, 'w', encoding='utf-8') as fw:
        for r in result:
            r = r+'\n'
            fw.write(r)
    return result


if __name__ == '__main__':
    companies = []
    noncompanies = []
    name_list = get_list('list.txt')
    feature_list = get_list('noncompany_feature.txt')
    for item in name_list:
        for feature in feature_list:
            if feature in item:
                print('item = ', item)
                noncompanies.append(item)
                break
    all_set = set(name_list)
    noncompanies_set = set(noncompanies)
    companies_set = all_set - noncompanies_set
    companies = sorted(list(companies_set))
    noncompanies = sorted(list(noncompanies_set))
    write_result('companies.txt', companies)
    write_result('noncompanies.txt', noncompanies)
