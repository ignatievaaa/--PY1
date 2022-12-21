import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename, "r", encoding="utf-8") as f:
        output_list = []
        for i, n in enumerate(f):
            var = n.strip(new_line).split(delimiter)
            if i == 0:
                heads = var
                continue
            output_list.append({})
            for j, _ in enumerate(heads):
                output_list[-1][heads[j]] = var[j]
    return output_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#  Комментарий для пустой строки в конце кода

