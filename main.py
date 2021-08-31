def count(data):
    new_dict={}

    data=data.split()
    for i in data:
        if i in new_dict.keys():
            new_dict[i]=new_dict.get(i)+1
        else:
            new_dict[i]=0

    print(new_dict)

def map_reduce_job():
    pass

    #TODO write a map reduce job for word counter
def mapper():
    pass
def reducer():
    pass



if __name__ == '__main__':
    with open('data.txt') as f:
        data=f.read()
    count(data)


