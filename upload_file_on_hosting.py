import ftplib

host = 'YOUR HOSTING IP'
 
 #Its better to create a new user for technical operations. 
user = 'YOUR FTP USER'
password = 'YOUR FTP USER PASSWORD'

#Folder To Upload
upload_folder = 'Example: /html/folder/'

#path to file
file_path = r'C:\test\test.txt'
#new file name 
file_name = 'test_file_name.txt'


def ftp_upload(path=file_path,name=file_name):
    with ftplib.FTP(host) as ftp:
        ftp.login(user=user,passwd=password)
        ftp.cwd(upload_folder)
        file = open(path, 'rb')
        ftp.storbinary('STOR '+ name, file)
        file.close()

def file_exist_on_hosting(folder=upload_folder,file_name=file_name):
    with ftplib.FTP(host) as ftp:
        ftp.login(user=user,passwd=password)
        ftp.cwd(folder)
        return file_name in ftp.nlst()
        
ftp_upload()
asssert file_exist_on_hosting(), 'Not Such File On Hosting!!!'
