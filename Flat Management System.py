import mysql.connector
FMS = mysql.connector.connect(host="localhost", user="root", passwd="Your password")
csr = FMS.cursor()

# Creating database
csr.execute("create database if not exists FMS")
csr.execute("use FMS")

# Table -- details
csr.execute("""create table if not exists details(RegNo int,Name varchar(15),
Occupation varchar(15),PhoneNo varchar(15),Members int,FlatNo int,FlatType varchar(15),
FlatDesign varchar(15),Price varchar(15))""")

# Table -- prices
csr.execute("""create table if not exists prices(Basic int,Fur int,
bhk1 int,bhk2 int,area_400 int,area_800 int)""")

# prices = (1bhk + basic= 8 lac) (2bhk + basic = 12 lac)
# (1bhk + Fur = 10 lac) (2bhk + Fur = 14 lac)


def gb():
    print("                                  |-------------------------------------------------------------------|")
    print("                                                     #-----------------------------#")
    print("                                                     |     1. Go To Main Menu      |")
    print("                                                     |     2. Exit The Database    |")
    print("                                                     #-----------------------------#")
    gb1 = int(input(
        "                                                          Enter Your Choice : "))
    print("#------------------------------------------------------------------------------------------------------------------------------------#")
    if gb1 == 1:
        main()
    elif gb1 == 2:
        print("                                                       +--------------------------+")
        print("                                                       |Did You Like The Database?|")
        print("                                                       +--------------------------+")
        print("                                                       |1. Like                   |")
        print("                                                       |2. Dislike                |")
        print("                                                       +--------------------------+")
        like = int(input(
            "                                                       |Enter Your Choice Here : "))
        if like == 1:
            print(
                "                                                       +--------------------------+")
            print(
                "                                                       |  Thanks For Liking It!   |")
            print(
                "                                                       +--------------------------+")
        else:
            print(
                "                                            +------------------------------------------------+")
            print(
                "                                            | Thanks For Feedback, I Will Try To Improve It! |")
            print(
                "                                            +------------------------------------------------+")
        print("                                                          +--------------------+")
        print("                                                          |Exited The Database.|")
        print("                                                          +--------------------+")
    else:
        print("                                                         ------------------------")
        print("                                                         Wrong choice, Type Again")


# Inserting Data
def insert():
    print("                                                To Buy New Flat, Kindly Fill The Details.")
    print("                                                -----------------------------------------")
    sql = "select max(RegNo) from details"
    csr.execute(sql)
    recsr = csr.fetchone()
    if recsr[0] == None:
        rno = 1
    else:
        rno = recsr[0]+1
    name = input(
        "                                                    Enter Your Name : ")
    print("                                                    ---------------------------------")
    ocp = input(
        "                                                    Enter Occupation : ")
    print("                                                    ---------------------------------")
    pno = input(
        "                                                     Enter Phone No. : ")
    print("                                                    ---------------------------------")
    mem = int(input(
        "                                                    Enter No. Of Family Members : "))
    print("                                                    ---------------------------------")
    fn = "select max(FlatNo) from details"
    csr.execute(fn)
    fncsr = csr.fetchone()
    if fncsr[0] == None:
        fno = 1
    else:
        fno = fncsr[0]+1
    print("""                                                    Choose Flat Type -
                                                    1. 1BHK
                                                    2. 2BHK 
                                                    ---------------------------------""")
    ft = int(input(
        "                                                    Enter Your Choice : "))
    if ft == 1:
        flat = "1BHK"
    elif ft == 2:
        flat = "2BHK"
    else:
        print("                                                    ---------------------------------")
        print("                                                         Wrong Choice, Try Again")
        print("                                                    ---------------------------------")
        insert()
    print("                                                    ---------------------------------")
    print("""                                                    Choose Flat Design -
                                                    1. BASIC
                                                    2. FURNITURED
                                                    ---------------------------------""")
    che = int(input(
        "                                                    Enter Your Choice : "))
    if che == 1:
        des = "BASIC"
    elif che == 2:
        des = "FURNITURED"
    else:
        print("                                                    ---------------------------------")
        print("                                                         Wrong Choice, Try Again")
        print("                                                    ---------------------------------")
        insert()
    if ft == 1 and che == 1:
        price = "8 Lakhs"
    elif ft == 1 and che == 2:
        price = "10 Lakhs"
    elif ft == 2 and che == 1:
        price = "12 Lakhs"
    elif ft == 2 and che == 2:
        price = "14 Lakhs"
    else:
        price = "Not Specified"
    print("                                                    ---------------------------------")
    sql = "insert into details values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (rno, name, ocp, pno, mem, fno, flat, des, price)
    csr.execute(sql, val)
    FMS.commit()
    print("                                                      #---------------------------#")
    print("                                                      | Flat Bought Successfully! |")
    print("                                                      #---------------------------#")
    gb()


# Updating Data
def update():
    rno = int(input(
        "                                                     Enter Your Registration No. : "))
    print("                                                      #---------------------------#")
    print("                                                      |Update Your Details Below -|")
    print("                                                      #---------------------------#")
    print("                               #-------------------------------------------------------------------------#")
    print("                               | Note : If You Don't Want To Update a Particular Detail, Use a Period(.) |")
    print("                               #-------------------------------------------------------------------------#")
    print()
    name = input(
        "                                                      Enter Your Name : ")
    print("                                                      -----------------------------")
    ocp = input(
        "                                                      Enter Occupation : ")
    print("                                                      -----------------------------")
    pno = (input("                                                      Enter Phone No. : "))
    print("                                                      -----------------------------")
    mem = (input("                                                      Enter No. Of Family Members : "))
    if name == ".":
        csr.execute("select Name from details where RegNo=%s", (rno,))
        na = csr.fetchone()
        for i in na:
            name = na[0]
    if ocp == ".":
        csr.execute("select Occupation from details where RegNo=%s", (rno,))
        oc = csr.fetchone()
        for i in oc:
            ocp = oc[0]
    if pno == ".":
        csr.execute("select PhoneNo from details where RegNo=%s", (rno,))
        pn = csr.fetchone()
        for i in pn:
            pno = pn[0]
    if mem == ".":
        csr.execute("select Members from details where RegNo=%s", (rno,))
        me = csr.fetchone()
        for i in me:
            mem = me[0]
    sql = "update details set name=%s,occupation=%s,phoneno=%s,members=%s where RegNo=%s"
    val = (name, ocp, pno, mem, rno)
    csr.execute(sql, val)
    FMS.commit()
    print("                                                     #-----------------------------#")
    print("                                                     |Details Updated Successfully!|")
    print("                                                     #-----------------------------#")
    print()
    gb()


# Deleting Details
def delete():
    print("                                                  #-----------------------------------#")
    print("                                                  |      To Cancel Flat Booking       |")
    print("                                                  | Enter Your Registration No. Below |")
    print("                                                  #-----------------------------------#")
    print()
    rno = int(input(
        "                                                             Enter Here : "))
    csr.execute("delete from details where RegNo=%s", (rno,))
    FMS.commit()
    print("                                               #-----------------------------------------#")
    print("                                               | Your Details Were Deleted Successfully! |")
    print("                                               #-----------------------------------------#")
    print()
    gb()


# Display All Details
def display():
    sql = "select * from details"
    csr.execute(sql)
    dis = csr.fetchall()
    if not dis:
        print("                                                         #----------------------#")
        print("                                                         |   No Details Found!  |")
        print("                                                         #----------------------#")
        print()
    else:
        print("                                                         #----------------------#")
        print("                                                         |    All Details -     |")
        print("                                                         #----------------------#")
        print("               +--------+--------------+---------------+------------+---------+---------+-----------+-------------+---------+")
        print("               | Reg No |     Name     |  Occupation   | Phone No   | Members | Flat No | Flat Type | Flat Design |  Price  |")
        print("               +--------+--------------+---------------+------------+---------+---------+-----------+-------------+---------+")
        for i in dis:
            print("               |", "{0:<6}{1:>15}{2:>16}{3:>13}{4:>10}{5:>10}{6:>12}{7:>14}{8:>10}".format(
                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]), "|")
            print("               +--------+--------------+---------------+------------+---------+---------+-----------+-------------+---------+")
        print()
    gb()


def search():
    print("                                            #------------------------------------------------#")
    print("                                            | To Search Details, Fill The Information Below- |")
    print("                                            +================================================+")
    print("                                            | 1. Search By Registration Number               |")
    print("                                            | 2. Search By Name                              |")
    print("                                            #------------------------------------------------#")
    print()
    ask = int(
        input("                                                      Enter Choice : "))
    print("                                            +------------------------------------------------+")
    if ask == 1:
        print()
        rno = int(input(
            "                                                      Enter Registration No. : "))
        print("                                            +------------------------------------------------+")
        csr.execute("Select * from details where RegNo LIKE %s", (rno,))
        dis = csr.fetchall()
        for rno in dis:
            for i in dis:
                print(
                    "                                                      #---------------------------#")
                print(
                    "                                                      | Details Related To Search |")
                print(
                    "                                                      #---------------------------#")
                print(
                    "                                                      Reg No      :", str(i[0]))
                print(
                    "                                                      Name        :", i[1])
                print(
                    "                                                      Occupation  :", i[2])
                print(
                    "                                                      Phone No.   :", i[3])
                print(
                    "                                                      Members     :", i[4])
                print(
                    "                                                      Flat No.    :", i[5])
                print(
                    "                                                      Flat Type   :", i[6])
                print(
                    "                                                      Flat Design :", i[7])
                print(
                    "                                                      Price       :", i[8])
    elif ask == 2:
        print()
        name = input(
            "                                                      Enter Name : ")
        print("                                            +------------------------------------------------+")
        csr.execute("Select * from details where Name LIKE %s", (name,))
        dat = csr.fetchall()
        for name in dat:
            for i in dat:
                print(
                    "                                                      #---------------------------#")
                print(
                    "                                                      | Details Related To Search |")
                print(
                    "                                                      #---------------------------#")
                print(
                    "                                                      Reg No      :", str(i[0]))
                print(
                    "                                                      Name        :", i[1])
                print(
                    "                                                      Occupation  :", i[2])
                print(
                    "                                                      Phone No.   :", i[3])
                print(
                    "                                                      Members     :", i[4])
                print(
                    "                                                      Flat No.    :", i[5])
                print(
                    "                                                      Flat Type   :", i[6])
                print(
                    "                                                      Flat Design :", i[7])
                print(
                    "                                                      Price       :", i[8])
    else:
        print()
        print("                                            #------------------------------------------------#")
        print("                                            |    Details Related To Your Search Not Found.   |")
        print("                                            #------------------------------------------------#")
    print("                                                      #---------------------------#")
    print()
    print("                                                      #---------------------------#")
    print("                                                      |     1. Search Again       |")
    print("                                                      |     2. Go To Main Menu    |")
    print("                                                      #---------------------------#")
    tg = int(input("                                                          Enter Your Choice : "))
    print("                                                      #---------------------------#")
    FMS.commit()
    if tg == 1:
        search()
    elif tg == 2:
        main()
    else:
        print("                                                               Wrong Choice")
        print("                                                      #---------------------------#")
        search()
    print()
    gb()


def calc():
    csr.execute("Select * from prices")
    fet = csr.fetchall()
    if not fet:
        csr.execute(
            "insert into prices values(0,200000,800000,1200000,200000,400000)")
        FMS.commit()
    else:
        pass
    print("                                             #----------------------------------------------#")
    print("                                             | To Calculate Prices, Pick Your Choices Below |")
    print("                                             #----------------------------------------------#")
    print("""                                                            Choose Flat Type -
                                                            1. 1BHK
                                                            2. 2BHK
                                                        ---------------------------""")
    ft = int(input(
        "                                                           Enter Your Choice : "))
    print("                                                        ---------------------------")
    print("""                                                           Choose Flat Design -
                                                            1. Basic
                                                            2. Furnitured
                                                        ---------------------------""")
    fd = int(input(
        "                                                           Enter Your Choice : "))
    print("                                                        ---------------------------")
    print("                                             #----------------------------------------------#")
    print("""                                                            Choose Flat Area -
                                                            1. 400 Sq.ft
                                                            2. 800 Sq.ft
                                                        ---------------------------""")
    fa = int(input(
        "                                                           Enter Your Choice : "))
    print("                                                        ---------------------------")
    if ft == 1 and fd == 1 and fa == 1:
        sql1 = "select * from prices"
        csr.execute(sql1)
        basic1 = csr.fetchall()
        for i in basic1:
            print(f"""                                                             Your Choice Was -
                                                      #==============+===============#
                                                      | Flat -       | Price -       |
                                                      #==============+===============#
                                                      | Basic        | No Price      |
                                                      +--------------+---------------+
                                                      | 1 BHK        | {i[2]}        |
                                                      +--------------+---------------+
                                                      | 400 Sq.ft    | {i[4]}        |
                                                      +--------------+---------------+""")

            print(
                f"                                                        --> Total Price : {i[0]+i[2]+i[4]}")
    elif ft == 1 and fd == 2 and fa == 1:
        sql1 = "select * from prices"
        csr.execute(sql1)
        basic1 = csr.fetchall()
        for i in basic1:
            print(f"""                                                             Your Choice Was -
                                                      #==============+===============#
                                                      | Flat -       | Price -       |
                                                      #==============+===============#
                                                      | Furnitured   | {i[1]}        |
                                                      +--------------+---------------+
                                                      | 1 BHK        | {i[2]}        |
                                                      +--------------+---------------+
                                                      | 400 Sq.ft    | {i[4]}        |
                                                      +--------------+---------------+""")

            print(
                f"                                                        --> Total Price : {i[1]+i[2]+i[4]}")
    elif ft == 2 and fd == 1 and fa == 1:
        sql1 = "select * from prices"
        csr.execute(sql1)
        basic1 = csr.fetchall()
        for i in basic1:
            print(f"""                                                             Your Choice Was -
                                                      #==============+===============#
                                                      | Flat -       | Price -       |
                                                      #==============+===============#
                                                      | Basic        | No Price      |
                                                      +--------------+---------------+
                                                      | 2 BHK        | {i[3]}       |
                                                      +--------------+---------------+
                                                      | 400 Sq.ft    | {i[4]}        |
                                                      +--------------+---------------+""")

            print(
                f"                                                        --> Total Price : {i[0]+i[3]+i[4]}")
    elif ft == 2 and fd == 2 and fa == 1:
        sql1 = "select * from prices"
        csr.execute(sql1)
        basic1 = csr.fetchall()
        for i in basic1:
            print(f"""                                                             Your Choice Was -
                                                      #==============+===============#
                                                      | Flat -       | Price -       |
                                                      #==============+===============#
                                                      | Furnitured   | {i[1]}        |
                                                      +--------------+---------------+
                                                      | 2 BHK        | {i[3]}       |
                                                      +--------------+---------------+
                                                      | 400 Sq.ft    | {i[4]}        |
                                                      +--------------+---------------+""")

            print(
                f"                                                        --> Total Price : {i[1]+i[3]+i[4]}")
    elif ft == 1 and fd == 1 and fa == 2:
        sql1 = "select * from prices"
        csr.execute(sql1)
        basic1 = csr.fetchall()
        for i in basic1:
            print(f"""                                                             Your Choice Was -
                                                      #==============+===============#
                                                      | Flat -       | Price -       |
                                                      #==============+===============#
                                                      | Basic        | No Price      |
                                                      +--------------+---------------+
                                                      | 1 BHK        | {i[2]}        |
                                                      +--------------+---------------+
                                                      | 800 Sq.ft    | {i[5]}        |
                                                      +--------------+---------------+""")

            print(
                f"                                                        --> Total Price : {i[0]+i[2]+i[5]}")
    elif ft == 1 and fd == 2 and fa == 2:
        sql1 = "select * from prices"
        csr.execute(sql1)
        basic1 = csr.fetchall()
        for i in basic1:
            print(f"""                                                             Your Choice Was -
                                                      #==============+===============#
                                                      | Flat -       | Price -       |
                                                      #==============+===============#
                                                      | Furnitured   | {i[1]}        |
                                                      +--------------+---------------+
                                                      | 1 BHK        | {i[2]}        |
                                                      +--------------+---------------+
                                                      | 800 Sq.ft    | {i[5]}        |
                                                      +--------------+---------------+""")

            print(
                f"                                                        --> Total Price : {i[1]+i[2]+i[5]}")
    elif ft == 2 and fd == 1 and fa == 2:
        sql1 = "select * from prices"
        csr.execute(sql1)
        basic1 = csr.fetchall()
        for i in basic1:
            print(f"""                                                             Your Choice Was -
                                                      #==============+===============#
                                                      | Flat -       | Price -       |
                                                      #==============+===============#
                                                      | Basic        | No Price      |
                                                      +--------------+---------------+
                                                      | 2 BHK        | {i[3]}       |
                                                      +--------------+---------------+
                                                      | 800 Sq.ft    | {i[5]}        |
                                                      +--------------+---------------+""")

            print(
                f"                                                        --> Total Price : {i[0]+i[3]+i[5]}")
    elif ft == 2 and fd == 2 and fa == 2:
        sql1 = "select * from prices"
        csr.execute(sql1)
        basic1 = csr.fetchall()
        for i in basic1:
            print(f"""                                                             Your Choice Was -
                                                      #==============+===============#
                                                      | Flat -       | Price -       |
                                                      #==============+===============#
                                                      | Furnitured   | {i[1]}        |
                                                      +--------------+---------------+
                                                      | 2 BHK        | {i[3]}       |
                                                      +--------------+---------------+
                                                      | 800 Sq.ft    | {i[5]}        |
                                                      +--------------+---------------+""")

            print(
                f"                                                        --> Total Price : {i[1]+i[3]+i[5]}")
    else:
        print("                                                    An Error Occured, Please Try Again.")
        calc()
    print()
    gb()


def main():
    print("                                                        +------------------------+")
    print("                                                        |        Main Menu       |")
    print("""                                                        +------------------------+
                                                        | 1. Buy New Flat        |
                                                        | 2. Update Any Detail   |
                                                        | 3. Cancel Flat Booking |    
                                                        | 4. Display All Details |    
                                                        | 5. Search Any Detail   |
                                                        | 6. Calculate Prices    |
                                                        | 7. Exit The Database   |
                                                        +________________________+
                                                                    |
                                                                    |
                                                                    |
                                                                =========""")
    print()
    print("""                                                         Type The Number Below To 
                                                     Perform The Corresponding Action.""")
    print()
    ch = int(input(
        "                                                           Enter Your Choice : "))
    print("                                             #----------------------------------------------#")
    print()
    # Choices
    if ch == 1:
        insert()
    elif ch == 2:
        update()
    elif ch == 3:
        delete()
    elif ch == 4:
        display()
    elif ch == 5:
        search()
    elif ch == 6:
        calc()
    elif ch == 7:
        print("                                                       +--------------------------+")
        print("                                                       |Did You Like The Database?|")
        print("                                                       +--------------------------+")
        print("                                                       |1. Like                   |")
        print("                                                       |2. Dislike                |")
        print("                                                       +--------------------------+")
        like = int(input(
            "                                                       |Enter Your Choice Here : "))
        if like == 1:
            print(
                "                                                       +--------------------------+")
            print(
                "                                                       |  Thanks For Liking It!   |")
            print(
                "                                                       +--------------------------+")
        else:
            print(
                "                                            +------------------------------------------------+")
            print(
                "                                            | Thanks For Feedback, I Will Try To Improve It! |")
            print(
                "                                            +------------------------------------------------+")
        print("                                                          +--------------------+")
        print("                                                          |Exited The Database.|")
        print("                                                          +--------------------+")
    else:
        print("Wrong Choice! Type Again")
        main()
    print()


# Welcome Screen
print()
print("#------------------------------------------------------------------------------------------------------------------------------------#")
print("|--------------------------------------------| Hello! Welcome To The Flat Management System.|----------------------------------------|")
print("#------------------------------------------------------------------------------------------------------------------------------------#")
main()
