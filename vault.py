import os
import webbrowser
jpgimage="FFD8FF"
pngimage="89504E"
def clear():
    print("\n" * 100)
    return True
def calc_XOR(image_file,type):
    print("Generating Key...")
    try:
        fin = open(image_file, "rb")
        data = fin.read(3)
        fin.close()
        data=data.hex()
        if type=='jpg':
            final_xor=hex(int(data,16)^int(jpgimage,16))
            final_xor=final_xor[:4]
        elif type=='png':
            final_xor = hex(int(data, 16) ^ int(pngimage, 16))
            final_xor = final_xor[:4]
        else:
            print("Not Supported in This Version:")
            exit(-1)

    except IOError:
        print("FAILED TO OPEN .BIN FILE TRY USING ADMINISTRATOR" % image_file)
        raise SystemExit
    return final_xor

def start_bulk_opertion(decode_xor,asps,filetype):

    for file_name in asps:
        barr=[]
        i=0
        print("Decoding  "+file_name)
        with open(file_name, "rb") as f:
            byte = f.read(1)
            while byte:
                if i < 128:
                    bytem = int(byte.hex(), 16) ^ int(decode_xor ,16)
                    barr.append(bytem)
                else:
                    barr.append(int(byte.hex(), 16))
                i = i + 1
                byte = f.read(1)
        barr=bytes(barr)
        a=file_name[:-3]+filetype
        path = os.getcwd()+"/Decrypted/"
        if not os.path.exists(path):
            os.makedirs(path)

        with open(os.path.join(path,a), 'wb') as temp_file:
            temp_file.write(barr)



    return True

def read_files(type):
    path=os.getcwd()
    input_xor=""
    print("The Current Path is \nAll Encrypted .Bin Should be Here \n"+ path +'\npress Enter to Continue')
    input()
    asps = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.bin'):
                asps.append(file)
    if (asps):
        decode_xor=calc_XOR(asps[0],type)
        print(decode_xor)
        start_bulk_opertion(decode_xor,asps,type)
        print("TotalfileDecoded="+str(len(asps)))
        webbrowser.open('https://www.facebook.com/akashthakur05')
    else:
        print("NO ENCRYPTED FILE AT:"+path)
        main()
    return True

def bulkoperation():
    print('\x1bc')
    clear()
    type_jpg="jpg"
    type_png="png"
    type_custom=""
    print("\033[1;31;47m[Only for Same Type of Image]")
    print("1.) jpg images")
    print("2.) png images")
    print("3.) Custom file [for Video]")
    choise=input("=>")
    if choise=='1':
        read_files(type_jpg)
    elif choise == '2':
        read_files(type_png)
    elif choise == '3':
        read_files(input("Enter file extension without (.) ex: png ,mp4"))
    else:
        print("Wrong Input!!!")
        main()

    return True



def disclamer():
    info='''
    Changeing Code wont make You Author
Vault Decrypt is was created as a simple program which can be used to recover original data from the files encrypted by the NQ Vault app.
Still if you're in trouble or looking to decrypt your files, here is a simple tutorial for you all :
Copy all the encrypted(.bin) files from your phone to pc.
These files can be found in /sdcard/SystemAndroid/data, 
Copy script in same directory and run it ..
contact:akashkumarsngh9@protonmail.com

 
    '''
    print(info)
    webbrowser.open('https://www.facebook.com/akashthakur05')
    return
def main():
    print("\033[1;32;44m -=[Auto NQ-Vault Decryptor]=-  \n")
    print("1)Start Decryption:")
    print("2)Read Instructions:")
    print("3)Exit:")
    choise=input("=>")
    if choise=='1':
        bulkoperation()
    elif choise=='2':
        disclamer()
    elif choise=='3':
        exit()
        webbrowser.open('https://www.facebook.com/akashthakur05')
    else:
        print("\033[1;32;44mWrong Input !!!!!!")
        main()
    return

if __name__ == "__main__":
    main()