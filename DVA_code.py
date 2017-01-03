'''using a linked list implementation to keep values associated with the node
because lists cannot keep the type of the other nodes without explicitly
writing it in as a value, hit and infinite recursion, could implement
a counter so recursion stops when the same node is encountered'''


from Distance_vect import * 
from supermap import *
class digit():
    
            
    def __init__(self,value):
    

        self.left= ''
        self.right = ''
        self.up = ''
        self.down = ''
        self.l_value = 0
        self.r_value = 0
        self.u_value = 0
        self.d_value =0

    def add(self,left,right,up,down,l,r,u,d):


        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.l_value= l
        self.r_value = r
        self.u_value = u
        self.d_value = d

    def __str__(self):

        return str(self.left) + str(self.right) + str(self.up) + str(self.down) + "\n" + str(self.l_value) + str(self.r_value) + str(self.u_value) + str(self.d_value)  

DVA_table = []

    
        

def table(a,b,c,d,e):

        print("     /   u    /    v    /    x    /    y    /    z")
        print("     /")
        print("  u  /__"+str(DVA(a,a))+"___"+str(DVA(a,b))+"________________________________________")
        print("     /")
        print("     /")
        print("  v  /_____________________________________________")
        print("     /")
        print("     /")
        print("  x  /_____________________________________________")
        print("     /")
        print("     /")
        print("  y  /_____________________________________________")
        print("     /")
        print("     /")
        print("  z  /_____________________________________________")
        print("     /")
        print("     /")for al:
        
        print("     /")
        print("     /")

if __name__ == "__main__":

    DVA_table = SuperMap()
    u = digit()
    v = digit()
    x = digit()
    y = digit()
    z = digit()

    DVA_table.append(u.add(None,'v',None,'y',0,1,0,2))
    DVA_table.append(v.add('u','z',None,'x',1,6,0,3))
    DVA_table.append(x.add('y','z','v',None,3,3,2,0))
    DVA_table.append(y.add(None,'x','u',None,0,3,2,0))
    DVA_table.append(z.add('x',None,'v',None,2,0,6,0))


    for i in DVA_table:
        print(i)
    
    #table(u,v,x,y,z)
