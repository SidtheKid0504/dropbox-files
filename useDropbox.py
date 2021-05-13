import os
import dropbox
from dropbox.files import WriteMode

class TransferToDropbox:
    def __init__(self, access_key):
        self.access_key = access_key

    def upload_file(self, fromDir, toDir):
        dbx = dropbox.Dropbox(self.access_key)
        with open(fromDir, 'rb') as f:
            dbx.files_upload(f.read(), toDir)
    
    def upload_folder(self, fromDir, toDir):
        dbx = dropbox.Dropbox(self.access_key)
        for root, Dirs, files in os.walk(fromDir):
            for fileName in files:
                localPath = os.path.join(root, fileName)
                relativePath = os.path.relpath(localPath, fromDir)
                dropboxPath = os.path.join(toDir, relativePath)
                
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode("overwrite"))
       

    
def main():
    access_token = "sl.Awt20aNa2s6uPXUCzefd_E3_dBJVcGLHSVgErZJcbay-UGI9-6zt2_TajewHHRaTPCDTVB4wFPMOb4wVDvw1UfosEkPfu7zu7F8qbvf2BVKWO9lQlIAnHv1ux5-kW8dYta5n1bE"
    transferToDropBox = TransferToDropbox(access_token)
    fileFrom = "./files/c101"
    fileTo = "/cS101/myFiles"

    # transferToDropBox.upload_file(fileFrom, fileTo)
    transferToDropBox.upload_folder(fileFrom, fileTo)
    print("Files Loaded Successfully")

if __name__ == '__main__':
    main()
