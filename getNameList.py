import json
import os

# 数据来源于https://pan.baidu.com/s/1Ch7mUGF0ln9jaiI31h3q0A
path_dir = os.path.join(os.getcwd(), "microsoft patents - 917")


def get_set(file_name):
    print('file_name: ', file_name)
    path = os.path.join(path_dir, file_name)
    with open(path, 'r') as f:
        result_set = set()
        for line in f.readlines():
            if len(line) < 1:
                continue
            l = line.split('|')[-1].strip()
            try:
                for item in json.loads(l)["aa"]:
                    dafn = item.setdefault("dAfN", None)
                    if dafn is not None:
                        result_set.add(dafn)
            except json.decoder.JSONDecodeError:
                continue
            except KeyError:
                continue

    print(len(result_set))
    print(result_set)
    return result_set


if __name__ == '__main__':
    s = set()
    for name in os.listdir(path_dir):
        s = s.union(get_set(name))
    name_list = sorted(list(s))
    with open('list.txt', 'w', encoding='utf-8') as fw:
        for i in name_list:
            i = i+'\n'
            fw.write(i)

