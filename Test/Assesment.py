
import fileinput
class Assesment:
    # function to read and replace text in a file
    def readFile(self,filename,s_text,r_text):
        try:
            file=open(filename,"r+")
            text_lines=file.read()
            search_data=text_lines.replace(s_text,r_text)
            file.seek(0)
            file.truncate()
            file.write(search_data)
            file.close()
            print('Replaced file content-',search_data)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    a=Assesment()
    a.readFile('example.txt','placement','screening')

