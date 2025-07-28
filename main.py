
import json
import sys
with open("letters.json", "r") as file:
    data = json.load(file)

# DO THIS SO OTHER USERS CAN USE IT AUTOMATICALLY
# if you want to use this code, you need to clone the AsciiFig repository
# and add it to your Python path.
# You can do this by running the following commands in your terminal:
# !pip install git+
# !git clone https://github.com/git-jovah/AsciiFig.git
# import sys
# sys.path.append('./AsciiFig') 

# ITS GIVING OUTPUT DIRECTLY WITHOUT EVEN CALLING THE WRITE METHOD CHANGE THAT !!
# GIVE ANOTHER PARAMETER THE USER CAN CHANGE THE BORDER STYLE
# MAKE A TIME CALCULATOR FOR THE TIME TAKEN TO PRINT THE FIGURE AND MAKE IT PUBLIC SO USER CAN CALL IT


class charNotFoundError(Exception): # make this private!!!
    pass

class AsciiFig:
    """
    AsciiFig is a class that represents an ASCII art figure.
    it is initialized with a text and a style(default is "■").
    
    """

    def __init__(self,text,style="■"):
        self.text = text
        self.style = style
        self.__com = []
        self.__lett = {0:[],1:[],2:[],3:[],4:[]}
        # self.__subs()
        if len(sys.argv)>1:
            self.__write_cmd()
        else:
            self.__subs()
        

    def __str__(self):
        return self.text
    
    def __repr__(self):
        return f"AsciiFig(text={self.text}, style={self.style})"
    
    def __subs(self):
        
        if self.text:
            for i in self.text:
                if i in list(data.keys()):
                    for x,y in enumerate(range(0,5)):
                        self.__lett[x].append(data[i][y])
                else :
                    raise charNotFoundError(f"'{i}' not found")

        for i in range(0,5):
            __temp0 = []
            for j in range(0,len(self.text)):
                __temp0 += [_ for _ in self.__lett[i][j]]
                __temp0.append(0)
            self.__com.extend([__temp0])

    def write(self):
        """
        Writes the ASCII art figure to the Ouput(console).
        
        """
        print("#"*(6*len(self.text)+(6*len(self.text))-3))
        print()
        for x in self.__com:
            for y in x:
                if y == 1:
                    if len(self.style) == 1:
                        print(self.style,end=" ")
                        # sys.stdout.write(self.style)
                    else:
                        raise ValueError("Style must be a single character.")
                else:
                    print(" ",end=" ")
                    # sys.stdout.write(" ")
            print()
        print()
        print("#"*(6*len(self.text)+(6*len(self.text))-3))

    def __write_cmd(self):
        """
        Takes the input from the command line and writes the ASCII art figure.
        """
        self.__subs()
        self.write()

if __name__ == "__main__":
    if len(sys.argv)>1:
        fig = AsciiFig(" ".join(sys.argv[1:]))
    else:
        fig=AsciiFig('git-jovah',"$")
        fig.write()
