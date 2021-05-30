

def get_temp():
    try:
        with open('./temp.txt', 'r') as f:
            return f.readlines()[0].strip()
    except Exception as e:
        print(e)
        return "0"


def write_temp(temp):
    with open('./temp.txt', 'w') as f:
        f.write(f"{temp}")