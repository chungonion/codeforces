def process(path):
    if path[0] != '/':
        raise EnvironmentError("Syntax not match")

    formatted_path = "/"
    ongoing_slash = True
    for i in range(1, len(path)):
        if path[i] != '/':
            formatted_path = "{}{}".format(formatted_path, path[i])
            ongoing_slash = False
        elif path[i] == '/' and not ongoing_slash:
            formatted_path = "{}{}".format(formatted_path, path[i])
            ongoing_slash = True

    while formatted_path[len(formatted_path)-1] == '/' and len(formatted_path)>1:
        formatted_path = formatted_path[:-1]
    
    return formatted_path


path = input()
print(process(path))
