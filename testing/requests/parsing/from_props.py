def read_properties(from_file):
    props = {}
    with open('props.properties') as properties:
        for line in properties:
            try:
                k, v = line.split('=')
                props[k] = v.rstrip()
            except:
                pass
        return props
