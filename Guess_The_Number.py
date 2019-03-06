
import random
class Guessing():
    def gen_num(self):
        while True:


            try:
                self.n= int(input("How many numbers you want to generate"))
                if self.n > 9:
                    print("Limit is upto 9")
                    continue
                else:
                    pass
            except ValueError:
                print("Please provide a num")
                continue

            else:

                #self.n=int(num)
                rand= random.sample(range(10),self.n)
                       #self.ran=my_randoms
                self.ran=[str(num)for num in rand]
                       #ran=ran
                #print(self.ran)
                return self.ran






    def get_guess(self):
       while True:
            self.guess =(input("Enter {} different numbers".format(self.n)))
            if self.guess.isnumeric():
                try:

                    if len(self.guess)!= self.n:
                        print("Please eneter only {} numbers".format(self.n))
                        continue
                    else:
                        print("So you entered{}".format(guess))
                except:
                    pass
            else:
                print('Please enter number')
                continue

            self.guesss=list(self.guess)

            print(self.guesss)
            return self.guesss
    def comparing(self):
        guess1= self.guesss

        ra= self.ran
        #guess1=ran
        #ra=guess


        if guess1==ra:
            print ( "Success")

        counter=0
        for i,num in enumerate (guess1):
            #print(num,i)

            if num in ra:
                counter+=1
        print(str(counter)+" number  correct")
        pos=0
        if counter >0:
            for j,r in enumerate (ra):
                for y,g in enumerate(guess1):
                    if j==y:
                        if r==g:
                            pos+=1
            print(str(pos)+" number is in correct position")

        if pos!=self.n :
            self.get_guess()
            self.comparing()
        elif pos == self.n :
            again = input("Play again? y/n")
            if(again == 'y') :
                self.gen_num()
                self.get_guess()
                self.comparing()


g=Guessing()
g.gen_num()
g.get_guess()
g.comparing()
