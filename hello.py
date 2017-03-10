# coding: utf-8

def sub(msg):
    reply = 'Hello! ' + msg.upper()
    print(reply)
    return reply

if __name__ == '__main__':
    while True:
        reply = input('Enter text:')
        ret = sub(reply)
        if reply == 'stop': break
    print('Bye')

