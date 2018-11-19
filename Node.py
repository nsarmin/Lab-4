class Word:
    def __init__(self, key, embed):
        self.key= key
        self.embed= embed
        self.H_num= self.base_conv(key + "   ")

    def get_embed(self):
        if self.embed is not None :
            return self.embed

    def set_embed(self, array):
        self.embed = array

    def get_key(self):
        if self.key is not None:
            return self.key

    def set_key(self, word):
        self.key=word

    def get_H_num(self):
        if self.H_num is not None:
            return self.key

    def set_H_num(self, H_num):
        self.H_num = H_num

    def base_conv(self,key):
        w= self.base27_to_10(key[0])* 27* 27* 27
        x= self.base27_to_10(key[1])* 27 * 27
        y= self.base27_to_10(key[2])* 27
        z= self.base27_to_10(key[3])
        H_num = w + x + y + z
        return H_num
                   
    def base27_to_10(self,letter):
        if letter is "a":
            return 0
        elif letter is "b":
            return 1
        elif letter is "c":
            return 2
        elif letter is "d":
            return 3
        elif letter is "e":
            return 4
        elif letter is "f":
            return 5
        elif letter is "g":
            return 6
        elif letter is "h":
            return 7
        elif letter is "i":
            return 8
        elif letter is "j":
            return 9
        elif letter is "k":
            return 10
        elif letter is "l":
            return 11
        elif letter is "m":
            return 12
        elif letter is "n":
            return 13
        elif letter is "o":
            return 14
        elif letter is "p":
            return 15
        elif letter is "q":
            return 16
        elif letter is "r":
            return 17
        elif letter is "s":
            return 18
        elif letter is "t":
            return 19
        elif letter is "u":
            return 20
        elif letter is "v":
            return 21
        elif letter is "w":
            return 22
        elif letter is "x":
            return 23
        elif letter is "y":
            return 24
        elif letter is "z":
            return 25
        else:
            return 26
                       
            
	
	
	
