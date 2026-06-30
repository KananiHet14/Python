'''
1] Volatile = data does not persist[save] after the program ends
2] Non-volatile = data persists[save] after the program ends


file types : 1]binary file = .jpg, .png, .mp3, .mp4, .pdf
             2]text file = .txt, .csv, .py, .html, .css, .
'''


# file open function
files = open("file.txt")
data = files.read()
print(data)
files.close()