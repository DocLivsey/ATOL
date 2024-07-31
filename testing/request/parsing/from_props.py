def read_properties(from_file):
    props = {}
    with open(from_file) as properties:
        for line in properties:
            try:
                k, v = line.split('=')
                props[k] = v.rstrip()
            except:
                pass
        return props
