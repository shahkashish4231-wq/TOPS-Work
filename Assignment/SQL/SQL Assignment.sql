SQL Assignment

Statement to create the contact table.

	create table Contact (ContactID int primary key,
    	CompanyID int,
	foreign key (CompanyID) references Company(CompanyID),
    	FirstName varchar(45),
    	LastName varchar(45),
    	Street varchar(45),
    	City varchar(45),
    	State varchar(2),
    	Zip varchar(10),
    	Email varchar(45),
    	Phone varchar(12));


2. Statement to create the Employee table.

	create table Employee (EmployeeID int primary key,
    	FirstName varchar(45),
    	LastName varchar(45),
    	Salary int,
    	HireDate date,
    	JobTitle varchar(25),
    	Email varchar(45),
    	Phone varchar(12));


3. Statement to create ContactEmployee table.

	create table ContactEmployee (ContactEmployeeID varchar(10) primary key,
    	ContactID int,
	foreign key (ContactID) references Contact(ContactID),
    	EmployeeID int,
    	foreign key (EmployeeID) references Employee(EmployeeID),
    	ContactDate date,
    	Description varchar(100));

4. In the Employee table, the statement that changes Lesley Bland's phone number

	update Employee set Phone=2155558800 where FirstName='Lesley';



5. In the Company table, the statement that changes the name of "Urban outfitters"

	update Company set CompanyName = 'Urban Outfitters' where CompanyName = 'Urban Outfitters Inc';


8. What is the significance of "%" and "_" operations in the like statement?

	The "%" means, it gives the remaining characters from the queries. If want to print the names starts from "A" then we can use the "%" operator. The "_" operator suggest the number of characters we want to print. Ex. If I want to find the name which has only 4 character so that I can write like "select * from Employee where FirstName like '____';


9. Explain Normalization in the context of database.