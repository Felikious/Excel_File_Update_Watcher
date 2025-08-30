import hashlib as hl
import zipfile as zf
import os
from pathlib import Path




class hash_manager:
    # a class with methods to hash files and compare hashes
    # it uses the sha256 algorithm to hash the files

    def hash_file(self, file_path):
        # hashes a single file and returns the hash
        sha256 = hl.sha256()
        
        with zf.ZipFile(file_path, 'r') as zip_ref:
            for file in sorted(zip_ref.namelist()):
                if file.startswith('xl/worksheets/sheet'):
                    with open(file_path, 'rb') as f:
                        while True:
                            data = f.read(65536) #It reads 64Kb per loop
                            if not data:
                                break
                            sha256.update(data)

        my_hash = sha256.digest()
        print("\nSHA256 of file\""+ str(file_path)+ "\" was:\n {0}".format((my_hash.hex())))
        #print("SHA256 of file\""+ str(file_path)+ "\" was: {0}".format(str(bytes.fromhex(my_hash))))
        return my_hash
    