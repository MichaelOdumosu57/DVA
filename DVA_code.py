'''redid table method to accomodate for any amount nodes also included extra quicksort method in supermap'''
from collections import OrderedDict
from Distance_vect import *
from supermap import *
import time
global debug
debug = True
global debug_table
debug_table = True
global snap_this
snap_this = ''
class digit():
    
            
    def __init__(self,name):

        self.name = name
        self.innerlist = [] #hold all information about the objects neighbors
        
    def add(self,neighbor = [],value = [],human_input = False): #made to handle any amount of neighbors now

        try:
            neigh = neighbor
            n_val = value
            
            if human_input:
                while True:
                    neighbor = str(input("What is the name of the neighbor?"))
                    neigh.append(neighbor)
                    value = int(input("How far is it from?"))
                    n_val.append(value)
                    done = input("Have you finish adding?")
                    if done.find('y') ==-1:
                        break

            
            for i in range(len(neigh)):
                a = ['neighbor',neigh[i]]
                b = ['neigh_value',n_val[i]]
                ab= [a,b]
                self.innerlist.append(ab)

            return
        
        except:
            print("it didn't go through correctly try again")
            self.add()
    

    def __str__(self):

        node = self.name + '\n'
        for i in self.innerlist:
            i = str(i)
            i = i.strip("[")
            i = i.strip("]")
            node += i + '\n'
        return node
    
    def valt (self,value = ''):
        
        for i in self.innerlist:
            for k in i:
                for l in k:
                    print(l)
                    if value == l:
                        
                        return k[1]
            
    def __iter__(self):
        self.__i__= 0
        return self
        

def DVB(source_ltr, dest_ltr,KTL_R=[],KM_P = []):

    if debug:
        print('source_ltr, dest_ltr,KTL_R,KM_P')
        print(source_ltr, dest_ltr,KTL_R,KM_P)
    KMP = [] #keep moving foward
    KMP += KM_P
    KMP.append(source_ltr)
    if debug:
        print('after we append KM_P')
        print('source_ltr, dest_ltr,KMP')
        print(source_ltr, dest_ltr,KMP)
    
    if source_ltr == dest_ltr:
        my_dest =0
        if debug:
            print('equal',my_dest)
        return my_dest
    
    else:
        KTLR = [] #memory of neighbors
        
        TLFT = [] #memory of paths
        choices = [] #memory of lengths 
        path_sum = 0 #gets the sum
        
        xylis= DVA_table.find(source_ltr)
        if debug:
            print('KTLR,TLFT,choices,path_sum\n,xylis('+ source_ltr +')')
            print(KTLR,TLFT,choices,path_sum)
        i = 0
        for i in xylis.innerlist:
            if i[0][1] != None:
                if debug:
                    print('===========')
                    print(i[0][0])
                    print(i[0][1])
                    print(KMP)
                    print(KTLR)
                    print('in xylis('+ source_ltr+')')
                    print('\n')
                
                if i[0][1] not in KMP:
                    if debug:
                        print('not in KMP')
                        print(KTL_R)
                    if i[0][1] not in KTL_R or i[0][1] not in KTLR :
                        if debug:
                            print('Not in KTL_R lets go')
                            print(KTLR)
                        
                        KTLR.append(i[0][1])
                        if debug:

                            print(i)
                            print('KTLR')
                            print(KTLR)
                            print('\n')
                        try:
                            path_sum += i[1][1] + DVB(KTLR[-1],dest_ltr,KTLR,KMP)
                        
                            if debug:
                                print('in source_ltr    ' + source_ltr)
                                print('\n')
                                print('path_sum from  ' + source_ltr+ ' to ' + dest_ltr)
                                print(i[1][0])
                                print(path_sum, i[1][1],path_sum-i[1][1])
                            choices.append(path_sum)
                            path_sum = 0
                            if debug:
                                print(i)
                                print('choices')
                                print(choices)
                                print('\n')
            
                        except:
                            pass
                            
                        
        
        #DVC(source_ltr,dest_ltr,xylis,TLFT,KMP,choices,path_sum)
        if len(choices) == 0:
            if debug:
                print('this path goes nowhere')
            return 'this path goes nowhere'
        if debug:
            print('here are you choices and here is the shortest neighbor')
            print(choices,min(choices))
        return min(choices)
        

def table(network):

    table = "%15s" % "/   "
    values = network.getKeys()
    
    if debug_table:
        print(values)
    #width = ""
    #length = ""
    for i in values:
        table +=   "%-5s" % i
        table +=   "%-5s" % "/"  
    for i in values:
        t = 0
        while t != 3:
            if t ==2:
                table += "%6s" % i
                table += "%6s" % "/"
                table += "%-5s" % "/"  
                for j in values:
                    table += "%-5s" % str(DVB(j,i))
                    table += "%-5s" % "/"  
                table += "\n"
            else:
                table += "%12s" % "/"
                table += "\n"
            
            t += 1
        
    print(table)
    return
            
    


    print("     /   u    /    v    /    x    /    y    /    z")
    print("     /")
    print("  u  /__"+str(DVB(a,a))+"_____"+str(DVB(a,b))+"______"+str(DVB(a,c))+"____"+str(DVB(a,d))+"________"+str(DVB(a,e))+"_________________")
    print("     /")
    print("     /")
    print("  v  /__"+str(DVB(b,a))+"_____"+str(DVB(b,b))+"_____"+str(DVB(b,c))+"____"+str(DVB(b,d))+"_______"+str(DVB(b,e))+"_________________")
    print("     /")
    print("     /")
    print("  x  /__"+str(DVB(c,a))+"_____"+str(DVB(c,b))+"______"+str(DVB(c,c))+"____"+str(DVB(c,d))+"________"+str(DVB(c,e))+"________________")
    print("     /")
    print("     /")
    print("  y  /__"+str(DVB(d,a))+"_____"+str(DVB(d,b))+"______"+str(DVB(d,c))+"____"+str(DVB(d,d))+"________"+str(DVB(d,e))+"_________________")
    print("     /")
    print("     /")
    print("  z  /__"+str(DVB(e,a))+"_____"+str(DVB(e,b))+"______"+str(DVB(e,c))+"____"+str(DVB(e,d))+"________"+str(DVB(e,e))+"_________________")
    print("     /")
    print("     /")
    print("     /")
    print("     /")

if __name__ == "__main__":
    debug = False

    global DVA_table
    DVA_table= SuperMap(5)
    u = digit('u')
    v = digit('v')
    x = digit('x')
    y = digit('y')
    z = digit('z')
    '''g = digit('g')
    g.add(['q','g'],[7,5],True)
    print(g)'''
    u.add(['v','y'],[1,2])
    v.add(['u','z','x'],[1,6,3])
    x.add(['y','z','v'],[3,2,3])
    y.add(['x','u'],[3,2])
    z.add(['x','v'],[2,6])



    DVA_table['v'] = v
    DVA_table['u'] = u
    DVA_table['x'] = x
    DVA_table['y'] = y
    DVA_table['z'] = z


    #print(DVA_table)
    #print(DVA_table.getKeys())
    #print(u.valt('right'))
    #print(str(DVB('v','z')))
    table(DVA_table)
