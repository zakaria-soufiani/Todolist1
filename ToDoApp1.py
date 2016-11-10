

import datetime
import time

DATE_FORMAT = '%d/%m/%Y'
TODAY = datetime.datetime.today()
NEXT_WEEK = TODAY + datetime.timedelta(days=7)

def as_datetime(date_string):
    try:
        return datetime.datetime.strptime(date_string, DATE_FORMAT)
    except ValueError:
        # The date string was invalid
        return None

def as_date_string(date):
    return date.strftime(DATE_FORMAT)



def load_list(fname):
    ''' The load_list function takes in the name of the file in the form of namefila.txt in this
        case todo.txt and prints out a list in the form of datetime.datetime(0000,00,00,00,0,0),'task'''
    fhand= open(fname,'rU')#Opens file
    todos = []#Set up an empty list'''
    for line in fhand:   #Rearange the cotents of the file in the correct format
        line =line.rstrip()
        line2=line.split(',')
        line2 = line2[::-1]
        todos.append((as_datetime(line2[0]),line2[1]))#Append the rearranged dates and tasks to the empty list
    return todos



def save_list(todolist,filename):
    ''' The save_list function takes in a list and a file name to then write a file same as the todo.txt in the directory'''
    myfile=open(filename,'w')#Opens file
    formatted_dates=[(item[0].strftime(DATE_FORMAT),item[1]) for item in todolist]#convert dates from the datetime.datetime format to the given DATE_FORMAT
    seq=[]
    for date,task in formatted_dates:
        result='{},{}'.format(task,date)+'\n'
        seq.append(result)
    myfile.writelines(seq)#save the modified file 
    
    
   
    
        



def display(todolist,show_all):
    '''The display function takes in a list and a boolean value to then display a set of lines, in this case a date and a task'''
    if show_all == True:
        
        date_list=todolist
        date_list.sort()#sorting the list datewise 
        formatted_dates=[(item[0].strftime(DATE_FORMAT),item[1]) for item in date_list]#convert the dates from the datetime.datetime format to the DATE_FORMAT
        
        
        for date, task in formatted_dates:
            print '{}: {}'.format(date,task)#Print the lines in the appropriate format 
            
        
    elif show_all == False:
        date_list = todolist
        date_list.sort()
        tasks_in_a_week = filter(lambda x: x[0] > TODAY and x[0] < NEXT_WEEK , date_list)#filtering the dates to get the tasks due within a week 
        formatted_dates=[(item[0].strftime(DATE_FORMAT),item[1]) for item in tasks_in_a_week]
        for date, task in formatted_dates:
            print '{}: {}'.format(date,task)

def remove_item(todolist,item):
    ''' the romove_item function takes in a list and an a string and returns a boolean value after running the code'''
    
    if item in zip(*todolist)[1]:
        result = filter (lambda k: item in k, todolist)#filter the list to get the desired item
        j=result[0]#find the item's index
        ind = todolist.index(j)
        del todolist[ind]#delete the item from the list
        return True
        
        
        
    else:
        return False

def add_item(thing_to_add):
    
    ''' the add_item function takes in '''
    todolist.append(thing_to_add)
    return True


def parse_command(command):
    ''' The parse command takes in a str and ives a tuple of a str and a list '''
    what_is_entered_2=' '
    what_is_entered = command 
    new_string=what_is_entered.split(' ',1)#split the imput at the first space
    
    if what_is_entered == 'q':
        return ('q',[])
    elif what_is_entered == 'all on':
        
        return (new_string[0],[new_string[1]])
    elif what_is_entered == 'all off':
        
        return (new_string[0],[new_string[1]])          
    
    elif 'rm' in (what_is_entered) and len(new_string)!=1:
        
        return (new_string[0],[new_string[1]])
       
       
    elif 'add' in (what_is_entered) and len(new_string)!=1:
        
        if ',' in new_string[1]:
            what_is_entered_2=new_string[1].split(',')
            what_is_entered_2[1]=what_is_entered_2[1].strip()
            try:
                time.strptime(what_is_entered_2[1],DATE_FORMAT)#check if the str is a date 
                
                return (new_string[0],[what_is_entered_2[0],as_datetime(what_is_entered_2[1])])
            except ValueError:
                
                 return (None,None)  
                
        
        
       
    else: return (None, None)
                       


def interact():

    ''' the interact function is the function used to prompt the user for commands that are then transfered to the parse command to get a tuple
        the tuple from the parse command contains a str which will define which function to use and a list which is the imput in the function '''
    program_running = True
    file_name=raw_input('Filename: ')
    todolist=load_list(str(file_name))
    display(todolist,True)
    widget = True
    new_todo_list=[]
    

    
    
     
    
    while program_running == True:
        
        what_is_entered=  raw_input('Command: ')
    
        tuple_parse=parse_command(what_is_entered)
            
        if tuple_parse == (None,None):
            print ('Invalid command: '+ what_is_entered)
            display(todolist,widget)
            
            
        elif tuple_parse== ('all',['off']):
            widget=False
            display(todolist,False)
           
            
        elif tuple_parse== ('all',['on']):
            widget=True
            display(todolist,True)
           
            
        elif tuple_parse[0]==('rm'):
            if remove_item(todolist,tuple_parse[1][0])== True:
                display(todolist,True)
                
            else:
                print'Error: No such item'
                
            
        if tuple_parse[0] == ('add'):
            if tuple_parse != 'invalid command':
                task= tuple_parse[1][0]
                date= tuple_parse[1][1]
                combined = (date,task)
                todolist.append(combined)
                display(todolist,True)
            elif tuple_parse == 'invalid command':
                print 'Invalid command: '+what_is_entered
         
           
        elif parse_command(what_is_entered) == ('q',[]):
            
            save_list(todolist,file_name)
            
            
            break
        
    
if __name__ == '__main__':
    interact()
            
