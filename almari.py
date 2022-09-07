from asyncio.windows_events import NULL
import itertools
import mysql.connector

conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="test"
    )


class almari:
    def __init__(self, total_space: int):
        self.__total_space=total_space




    def get_totalspace(self):
        return self.__total_space

class put_cloths(almari):
    def __init__(self, total_space: int, put_cloth: int):
        super().__init__(total_space)
        self.put_cloth=put_cloth

    def space_left(self):
        return self.get_totalspace() - self.put_cloth

class Take_out_cloths(almari):
    def __init__(self, total_space: int, take_cloth: int):
        super().__init__(total_space)
        self.takecloth=take_cloth


    def space_left(self):
        return self.get_totalspace() + self.takecloth



l=20 #value of total_space
item_size=0

for x in itertools.count(start=1):
    print("Select Options:")
    print("1. Want to Put cloths")
    print("2. Take out cloths")
    print("3. close")
    operation_select=int(input())
    if (operation_select==1):
        print("Amount of cloths")
        amount_of_cloths=int(input())
        if (amount_of_cloths>l):
            print("Not Enough Space")
        else:
            a_almari=put_cloths(l,amount_of_cloths)
            print("Space left: ", a_almari.space_left())
            l=l-amount_of_cloths
            item_size+=amount_of_cloths
            print("You have " , item_size , "cloths")
    elif(operation_select==2):
        print("Amount of cloths")
        amount_of_cloths=int(input())
        if(item_size<amount_of_cloths):
            print("The amount cloths not exist")
            print("You have " , item_size , "cloths")
        else:
            a_almari=Take_out_cloths(l,amount_of_cloths)
            print(a_almari.space_left())
            l=l+amount_of_cloths
            item_size-=amount_of_cloths
            print("You have " , item_size , "cloths")

    elif(operation_select==3):
        mycursor=conn.cursor()

        sql="INSERT INTO almari (space, spece_left, item_size) VALUES(%s, %s, %s)"
        val=(l, l, item_size)
        mycursor.execute(sql, val)
        conn.commit()

        print(mycursor.rowcount,"record")
        break
    else:
        print("Wrong selection")
    