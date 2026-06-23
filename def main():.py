def main():
    dict_a = dict()
    dict_a = {'a':"aa"}
    print(type(dict_a))
    dict_a['b'] = "bbb"
    print(dict_a)
    print(dict_a['a'],dict_a['b'], dict_a.get('c', 'not found'))

    print(dict_a.pop("a"))
    print(dict_a)

    for key in dict_a.keys():
        print(f"key: {key}, value: {dict_a[key]}")  
    for key, value in dict_a.items():
        print(f"key: {key}, value: {value}")


if __name__ == "__main__":
    main()
