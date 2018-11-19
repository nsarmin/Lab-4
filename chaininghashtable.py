class ChainingHashTable:
    def __init__(self, capacity):
        self.table = []
        for i in range(capacity):
            self.table.append ([])
    
    def insert(self, Word):
        bucket=Word.H_num % len(self.table)
        bucket_list=self.table[bucket]
                               
        bucket_list.append(Word)
    
    def search(self, word):
        bucket = self.base_conv(word+ "       ") % len(self.table)
        bucket_list=self.table[bucket]

        for Word in bucket_list:
            if word==Word.key:
                item_index=bucket_list.index(Word)
                node=bucket_list[item_index]
                return node
        else:
            return None
                               
    def Avrg_comparisons(self):
        i=0
        count = 0
        buckets=0
        while i < len(self.table):
            bucket_list=self.table[i]
            if len(bucket_list) > 0:
                for Word in bucket_list:
                    count += 1
                buckets += 1
            i += 1
            aver= count/buckets
            print("The Avrg No. of Comparisons is "+ str(aver))
   
    def load_factor(self):
        i=0
        count = 0
        while i < len(self.table):
            bucket_list = self.table[i]
            for Word in bucket_list:
                count += 1
            i+=1
        load=count/ len(self.table)
        print("the load factor of this table is: "+ str(load))

    def remove(self, word):
        bucket=self.base_conv(word+"    ") % len(self.table)
        bucket_list=self.table[bucket]
        for Word in bucket_list:
            if word== Word.key:
                bucket_list.remove(Word)

    def base_conv(self,key):
        w= self.base27_to_10(key[0])*27*27*27
        x= self.base27_to_10(key[1])*27*27
        y= self.base27_to_10(key[2])*27
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
                       
            
