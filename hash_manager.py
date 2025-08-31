"""hash_manager.py
it is used to manage the hashing of Excel files
- Strips metadata from Excel files
- Detects changes in content, ignoring metadata
- Uses SHA-256 hashing algorithm

This project is but a small demo, but it can be easily extended
Future improvements could be:
    - more methods for different hashing algorithms
    - implementation of a file type detection mechanism
    - more metadata-rich file types for hashing (eg. docx, jpg, etc.)
"""

import hashlib as hl
import zipfile as zf
from pathlib import Path


class hash_manager:
    """ 
    A class with methods to hash files

    It contains only one public method "hash_file"

    It uses the sha256 algorithm to do so
    It also strips the excel file from any metadata, 
    that way it can detect change in the content of the excel files
    and not just changes in the file metadata
    """

    def hash_file(self, file_path):
        # hashes a single file and returns the hash
        sha256 = hl.sha256()
        
        with zf.ZipFile(file_path, 'r') as zip_ref:
            #strips any excel metadata, so it can compare the content of the excel files

            for file in sorted(zip_ref.namelist()):
                if file.startswith('xl/worksheets/sheet'):
                    # it opens every "sheet" sub-file of the file 
                    # and feeds its data in the hash 

                    with open(file_path, 'rb') as f:
                        while True:
                            # hash methods shouldn't be fed the entire file at once
                            # so we read it bit by bit (64Kb chunks)
                            data = f.read(65536) #It reads 64Kb per loop
                            if not data:
                                # If there's no more data, we break the loop
                                # To check the next sheet
                                break
                            sha256.update(data)

        my_hash = sha256.digest()

        # Uncomment the lines below to print the hash every time something is hashed
        # print("\nSHA256 of file\""+ str(file_path)+ "\" was:\n {0}".format((my_hash.hex())))
        # print("SHA256 of file\""+ str(file_path)+ "\" was: {0}".format(str(bytes.fromhex(my_hash))))

        # return the hash
        return my_hash
    