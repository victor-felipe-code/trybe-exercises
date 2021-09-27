map_dict: dict = {"a": 2, "b": 1, "g": 5}

maior = sorted(map_dict.items(), key=lambda x: x[1], reverse=True)[0]
print(maior)
