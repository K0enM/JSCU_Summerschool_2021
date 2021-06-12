with open('127.0.0.1.pwdump') as f:
    lines = f.readlines()
    hashes = ''
    for i in lines:
        hashes += i.split(':')[2] + ':' + i.split(':')[3]        
    with open('hashes.txt', 'w') as fw:
        fw.write(hashes)
