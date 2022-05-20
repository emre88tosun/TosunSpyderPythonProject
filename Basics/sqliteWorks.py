"""
@author: emretosun

"""
import sqlite3;
def selectOperations():
    connection = sqlite3.connect("chinook.db");
    # cursor = connection.execute("select * from customers");
    # cursor = connection.execute("select FirstName,LastName from customers");
    # cursor = connection.execute("select FirstName,LastName from customers where city = 'Prague' or city = 'Berlin'");
    # for row in cursor:
    #     print("First name:",row[0]);
    #     print("Last name:",row[1]);
    #     print("*********");
    # cursor = connection.execute("""select CustomerId, FirstName, LastName
    #                             from customers
    #                             where city='Prague' or city='Berlin'
    #                             order by FirstName desc
    #                             """);
    # cursor = connection.execute("""select City, count(*) from customers
    #                             group by City
    #                             having count(*) > 1
    #                             order by count(*) desc
    #                             """);
    # for row in cursor:
    #     print(row[0] + ": " + str(row[1]) + " customers.");
    #     print("****************");
    # cursor = connection.execute("""
    #                             select FirstName, LastName
    #                             from customers
    #                             where FirstName like '%a%'
    #                             """);
    # cursor = connection.execute("""
    #                             select FirstName, LastName
    #                             from customers
    #                             where FirstName like 'a%'
    #                             """);
    cursor = connection.execute("""
                                select FirstName, LastName
                                from customers
                                where FirstName like '%a'
                                """);
    for row in cursor:
        print(row[0] + " " + row[1]);
        print("****************");
    connection.close();
def insertCustomer():
    connection = sqlite3.connect("chinook.db");
    connection.execute("""
                       insert into customers(FirstName, LastName, Email, City)
                       values('Emre', 'Tosun', 'emre88tosun@gmail.com', 'Ankara')
                       """);
    connection.commit();
    connection.close();
def updateCustomers():
    connection = sqlite3.connect("chinook.db");
    connection.execute("""
                       update customers
                       set City='Istanbul'
                       where City='Ankara'
                       """);
    connection.commit();
    connection.close();
# insertCustomer();
# updateCustomers();
def deleteCustomers():
    connection = sqlite3.connect("chinook.db");
    connection.execute("""
                       delete from customers
                       where CustomerId=63
                       """);
    connection.commit();
    connection.close();
# deleteCustomers();
def withJoin():
    connection = sqlite3.connect("chinook.db");
    cursor = connection.execute("""
                                select albums.Title, artists.Name from artists inner join albums
                                on artists.ArtistId = albums.ArtistId
                                """);
    for row in cursor:
        print("Band= " + row[1] + ", Album= " + row[0]);
        print("********************");
    connection.close();
withJoin();