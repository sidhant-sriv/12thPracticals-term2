DELETE FROM Hospital;
INSERT INTO `Hospital` 
 VALUES (1,"Sandeep", 55, "Surgery", "1998-02-23", 300, "M"),
        (2, "Ravina", 24, "Orthopedic", "1998-01-20", 200, "F"),
        (3, "Karan", 45, "Orthopedic", "1998-02-19", 200, "M"),
        (4, "Tarun",12, "Surgery","1998-01-01", 300, "M"),
        (5, "Zubin",36, "ENT", "1998-01-12", 250, "M");

DELETE FROM School_Bus;
INSERT INTO School_Bus
 VALUES (1, "Vasant Nagar", 100, 120, 10, "Anand Travels", 25000),
        (2, "Rohini Apt", 90, 80, 10, "Yadav Co", 20000),
        (3, "Yamuna Tower", 60, 55, 30, "Anand Travels", 28000),
        (4, "Krishna Apt", 100, 105, 35, "Yadav Co", 30000),
        (5,"Vasant Vihar", 50, 40, 15, "Anand Travels", 23000);

DELETE FROM Coach;
INSERT INTO Coach
 VALUES (1, "Karan", 34, "Karate", "1996-03-07", 1000, "M"),
        (2, "Tarun", 36, "Squash", "1998-01-20",2000, "M"),
        (3, "Zubin", 38, "Karate", "1998-02-19", 2000, "M"),
        (4, "Ravina", 31,"Swimming", "1998-01-01", 1500, "F"),
        (5, "Shailaja", 34, "Basketball", "1997-04-23", 1200, "F");

DELETE FROM Worker;
INSERT INTO Worker
 VALUES (11, "RadheShyam", "Supervisior","P001", "1981-08-23"),
        (12, "ChanderNath", "Operator","P003", "1987-07-12"),
        (13, "Fizza", "Operator", "P003", "1983-10-14"),
        (15, "Ammen Ahmed",  "Mechanic", "P002", "1984-03-13"),
        (18, "Sanya", "Clerk", "P002", "1983-06-09");

DELETE FROM Movie;
INSERT INTO MOVIE
 VALUES (1, "Gone with the wind", "Drama", "G", "Gable", 4, 39.95),
        (2, "Friday the 13th", "Horror", "R", "Jason", 2, 89.95),
        (3, "Top Gun", "Drama", "PG", "Cruise", 7, 49.95),
        (4, "Splash", "Comedy", "G", "Hanks", 3, 29.95),
        (5, "Risky Business", "Comedy", "R", "Cruise", 2, 44.95);

DELETE FROM Sports_Master;
INSERT INTO Sports_Master 
 VALUES ("100 mts run", 1001, 1, "2001-01-01",  "Junior"),
        ("Volley ball", 1002, 9, "2001-01-02", "Senior"),
        ("Cricket", 1003, 11, "2001-01-12", "Senior"),
        ("Shot put", 1004, 1, "2001-01-13", "Junior"),
        ("Javalin", 1005, 1, "2001-01-02", "Senior");

DELETE FROM Employee;
INSERT INTO Employee
 VALUES (1, "Deepali",  101, "MCA", "F"),
        (2, "Rajat",  101,   "BCA", "M"),
        (3, "Harita",  102, "B.A",  "F"),
        (4, "Harry",  102, " M.A",  "M"),
        (5, "Sumit",  103, " B.Tech",  "M");

DELETE FROM Items;
INSERT INTO Items
 VALUES (1, "Computer",  60000,  9, "1996-05-21"),
        (2, "Printer", 15000, 3, "1997-05-21"),
        (3, "Scanner", 18000, 1, "1998-08-29"),
        (4, "Camera", 21000, 2,  "1996-10-13"),
        (5, "Switch", 8000, 1, "1999-10-31");

DELETE FROM Stationery;
INSERT INTO Stationery 
 VALUES ("DP01", "Dot Pen", "ABC", 10),
        ("PL02", "Pencil", "XYZ", 6),
        ("ER05", "Eraser", "XYZ", 7),
        ("PL01", "Pencil", "CAM", 5),
        ("GP02", "Gel Pen", "ABC", 15);

DELETE FROM Voter;
INSERT INTO Voter
 VALUES (1, "Rohit", 22, "Rohini", 7045249),
        (2, "Smith", 24, "PaschimVihar", 5580438),
        (3, "Arpit", 21, "Multan Nagar", 5585643),
        (4, "Sumit", 23, "VikasPuri", 5565127),
        (5, "Shobhit", 23, "Rohini", 7057845),
        (6, "Rohit", 24, "Rohini", 7057845);

DELETE FROM INTERIORS;
INSERT INTO INTERIORS
 VALUES (1, "Red rose", "Double Bed", "2023-02-02", 32000, 15),
        (2, "Soft touch", "Baby cot", "2020-01-02", 9000, 10),
        (3, "Jerry's home", "Baby cot", "2019-02-02", 8500, 10);

DELETE FROM WATCHES;
INSERT INTO WATCHES 
 VALUES ("W001",  "HighTime",  10000,  "Unisex", 100),
        ("W002", "LifeTime", 15000, "Ladies", 150),
        ("W003", "Wave", 20000, "Gents", 200),
        ("W004", "HighFashion", 7000, "Unisex", 250),
        ("W005",  "GoldenTime",  25000, "Gents", 100);

DELETE FROM CUSTOMER_INFO;
INSERT INTO CUSTOMER_INFO
 VALUES (1, 1001001, "Ram", "Vasundhara Enclave", "New Delhi", 8710557614),
        (2, 1001002, "Kavita", "Punjabi Bagh", "New Delhi", 7123545233),
        (3, 1001003, "Raj",  "Civil Lines", "Allahabad", 9872136576),
        (4, 1001004, "Sohan", "Krishnanagar", "Kanpur", 9921305453);

DELETE FROM TRANSACTION_DETAIL;
INSERT INTO TRANSACTION_DETAIL
 VALUES ("T001", 1001001, "Credit", 5000),
        ("T002", 1001002, "Credit", 10000),
        ("T003", 1001001, "Debit", 2000),
        ("T004", 1001004, "Credit", 6000),
        ("T005", 1001001, "Credit", 4000);

DELETE FROM FLIGHTS;
INSERT INTO FLIGHTS
 VALUES ("IC301", "MUMBAI", "BANGALORE", 3, 2),
        ("IC799", "BANGALORE", "KOLKATA", 8, 3),
        ("MC101", "DELHI", "VARANASI", 6, 0),
        ("IC302", "MUMBAI", "KOCHI", 1, 4),
        ("AM812", "LUCKNOW", "DELHI", 4, 0),
        ("MU499", "DELHI", "CHENNAI", 3, 3);

DELETE FROM FARES;
INSERT INTO FARES
 VALUES ("IC301", "Indian Airlines", 9425, 5),
        ("IC799", "Spice Jet", 8846, 10),
        ("MC101", "Deccan Airlines", 4210, 7),
        ("IC302", "Jet Airways", 13894, 5),
        ("AM812", "Indian Airlines", 4500, 6),
        ("MU499", "Sahara", 12000, 4);
