

def main():
    while True:
        phone_number = input('Enter your phone number:')
        if not phone_number.isnumeric():
            print('Please input a number')
        else:
            break
        
    dictionary = {
        0: 'Zero',
        1:'One',
        2:'Two',
        3:'Three',
        4:'Four',
        5:'Five',
        6:'Six',
        7:'Seven',
        8:'Eight',
        9:'Nine'
        }
    tlf = translate(dictionary, phone_number)
    print(f'Your phone number is: {tlf}.')
    
def translate(dictionary, phone_number):
    out = ''
    for i in phone_number:        
        out += dictionary[int(i)] + ' '      
    return out.strip()
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
   