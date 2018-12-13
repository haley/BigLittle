# Homework 3: Mongodb

1. What are the different collections in the Northwind database?

      ```
      db.getCollectionNames()
      [
          "categories",
          "customers",
          "employee-territories",
          "employees",
          "northwind",
          "order-details",
          "orders",
          "products",
          "regions",
          "shippers",
          "suppliers",
          "territories"
      ]
      ```
2. How many documents are in the "categories" collection?

   ```
   > db.categories.count()
   8
   ```

3. How many documents are in the "orders" collection?

   ```
   > db.orders.count()
   830
   ```

4. How many orders were handled by the person with EmployeeID number 8?

   ```
   > db.orders.find({ "EmployeeID" : 8 }).count()
   104
   ```

5. What is the last name of the employee who has the EmployeeID number 1?

   ```
   > db.employees.find({ "EmployeeID": 1 }, { "LastName": 1, "_id": 0 })
   { "LastName" : "Davolio" }
   ```

6. What are the EmployeeID numbers on orders which have an OrderID less than 10300?

   ```
   > db.orders.distinct("EmployeeID", { "OrderID": { $lt: 10300 }})
   [ 5, 4, 6, 3, 9, 1, 8, 2, 7 ]
   ```

7. What are the Company Names of the suppliers?

   ```
   > db.suppliers.distinct("CompanyName", {})
   [
   	"Exotic Liquids",
   	"Tokyo Traders",
   	"New Orleans Cajun Delights",
   	"Grandma Kelly's Homestead",
   	"Cooperativa de Quesos 'Las Cabras'",
   	"Mayumi's",
   	"Pavlova",
   	"Specialty Biscuits",
   	"Refrescos Americanas LTDA",
   	"PB Knäckebröd AB",
   	"Heli Süßwaren GmbH & Co. KG",
   	"Nord-Ost-Fisch Handelsgesellschaft mbH",
   	"Plutzer Lebensmittelgroßmärkte AG",
   	"Formaggi Fortini s.r.l.",
   	"Norske Meierier",
   	"Bigfoot Breweries",
   	"Svensk Sjöföda AB",
   	"Aux joyeux ecclésiastiques",
   	"New England Seafood Cannery",
   	"Leka Trading",
   	"Lyngbysild",
   	"Zaanse Snoepfabriek",
   	"Karkki Oy",
   	"G'day",
   	"Ma Maison",
   	"Pasta Buttini s.r.l.",
   	"Gai pâturage",
   	"Escargots Nouveaux",
   	"Forêts d'érables"
   ]
   ```

8. How many suppliers are there?

   ```
   > db.suppliers.count()
   29
   ```

9. What is the supplier ID and phone number for the supplier in Boston, Mass.? Be sure NOT to include the ID of the document

   ```
   > db.suppliers.find({ "Region": "MA", "City": "Boston" }, {"SupplierID": 1, "Phone": 1, "_id": 0 })
   
   { "SupplierID" : 19, "Phone" : "(617) 555-3267" }
   ```

10. What employee is responsible for the largest number of orders, and for how many orders is that  employee responsible?

  ```
  Not possible
  ```

11. How many territories have the RegionID value of "2"?  What are their territory descriptions? Be sure NOT to include the ID of the document, and ONLY show the territory descriptions.

    ```
    > db.territories.find({ "RegionID": 2 }).count()
    15
    
    > db.territories.find({ "RegionID": 2 }, { "TerritoryDescription": 1, "_id": 0 })
    { "TerritoryDescription" : "HoffmanEstates" }
    { "TerritoryDescription" : "Chicago" }
    { "TerritoryDescription" : "Denver" }
    { "TerritoryDescription" : "ColoradoSprings" }
    { "TerritoryDescription" : "Phoenix" }
    { "TerritoryDescription" : "Scottsdale" }
    { "TerritoryDescription" : "SantaMonica" }
    { "TerritoryDescription" : "MenloPark" }
    { "TerritoryDescription" : "SanFrancisco" }
    { "TerritoryDescription" : "Campbell" }
    { "TerritoryDescription" : "SantaClara" }
    { "TerritoryDescription" : "SantaCruz" }
    { "TerritoryDescription" : "Redmond" }
    { "TerritoryDescription" : "Bellevue" }
    { "TerritoryDescription" : "Seattle" }
    ```

12. What is the phone number of the shipper with the company name "United Package"? Be sure NOT to include the ID of the document in the output, ONLY the phone number.

```
> db.shippers.find({ "CompanyName" : "Speedy Express" }, { "Phone": 1, "_id": 0 })
{ "Phone" : "(503) 555-9831" }
```

***BONUS:***

   13. How many documents are in the "order-details" collection?  How many in the
       "employee-territories" collection?

       ```
       > db["order-details"].count()
       2155
       
       > db["employee-territories"].count()
       49
       ```

   14. How many orders were shipped to Albuquerque, NM?  What are the order numbers?
       Be sure NOT to include the ID of the document in the output, ONLY the Order ID numbers.

```
> db.orders.find({ "ShipCity": "Albuquerque", "ShipRegion": "NM" }).count()
18

> db.orders.find({ "ShipCity": "Albuquerque", "ShipRegion": "NM" }, { "_id": 0, "OrderID": 1 })
{ "OrderID" : 10262 }
{ "OrderID" : 10272 }
{ "OrderID" : 10294 }
{ "OrderID" : 10314 }
{ "OrderID" : 10316 }
{ "OrderID" : 10346 }
{ "OrderID" : 10401 }
{ "OrderID" : 10479 }
{ "OrderID" : 10564 }
{ "OrderID" : 10569 }
{ "OrderID" : 10598 }
{ "OrderID" : 10761 }
{ "OrderID" : 10820 }
{ "OrderID" : 10852 }
{ "OrderID" : 10889 }
{ "OrderID" : 10988 }
{ "OrderID" : 11000 }
{ "OrderID" : 11077 }
```



# Neo4j

1. What are the different collections in the Northwind database?

   ```
   $ MATCH(n) RETURN DISTINCT labels(n)
   ["Order"]
   ["OrderDetails"]
   ["Product"]
   ["Category"]
   ["Supplier"]
   ["Customer"]
   ["Territory"]
   ["Shipper"]
   ["EmployeeTerritories"]
   ["Employee"]
   ["Region"]
   ```

2. How many documents are in the "categories" label set?

   ```
   $ MATCH(n:Category) RETURN count(n)
   8
   ```

3. How many documents are in the "orders" label set?

   ```
   $ MATCH(n:Order) RETURN count(n)
   830
   ```

4. How many orders were handled by the person with EmployeeID number 8?

   ```
   $ MATCH(o:Order) WHERE o.EmployeeID = "8" RETURN count(o)
   104
   ```

5. What is the last name of the employee who has the EmployeeID number 1?

   ```
   $ MATCH(e:Employee) WHERE e.EmployeeID = "1" RETURN e.LastName
   "Davolio"
   ```

6. What are the EmployeeID numbers on orders which have an OrderID less than 10300?

   ```
   $ MATCH(o:Order) WHERE o.OrderID < "10300" RETURN DISTINCT o.EmployeeID
   "3"
   "4"
   "5"
   "9"
   "1"
   "8"
   "6"
   "2"
   "7"
   ```

7. What are the Company Names of the suppliers?

   ```
   $ MATCH(s:Supplier) RETURN s.CompanyName
   "Svensk Sjöföda AB"
   "Aux joyeux ecclésiastiques"
   "New England Seafood Cannery"
   "Leka Trading"
   "Lyngbysild"
   "Zaanse Snoepfabriek"
   "Karkki Oy"
   "G'day"
   "Ma Maison"
   "Pasta Buttini s.r.l."
   "Escargots Nouveaux"
   "Gai pâturage"
   "Forêts d'érables"
   "Exotic Liquids"
   "New Orleans Cajun Delights"
   "Grandma Kelly's Homestead"
   "Tokyo Traders"
   "Cooperativa de Quesos 'Las Cabras'"
   "Mayumi's"
   "Pavlova"
   "Specialty Biscuits"
   "PB Knäckebröd AB"
   "Refrescos Americanas LTDA"
   "Heli Süßwaren GmbH & Co. KG"
   "Plutzer Lebensmittelgroßmärkte AG"
   "Nord-Ost-Fisch Handelsgesellschaft mbH"
   "Formaggi Fortini s.r.l."
   "Norske Meierier"
   "Bigfoot Breweries"
   ```

8. How many suppliers are there?

   ```
   $ MATCH(s:Supplier) RETURN count(s)
    29
   ```

9. What is the supplier ID and phone number for the supplier in Boston, Mass.?

   ```
   $ MATCH(s:Supplier) 
     WHERE s.City = "Boston" AND s.Region = "MA"
     RETURN s.SupplierID, s.Phone
   "19" "(617) 555-3267"
   ```

10. What employee is responsible for the largest number of orders, and for how many orders is that employee responsible?

  ```
  
  ```

11. How many territories have the RegionID value of "2"?  What are their territory descriptions? You can use two queries.  Be sure to ONLY show the territory descriptions for that query.

   ```
   $ MATCH(t:Territory) WHERE t.RegionID = "2" RETURN count(t)
    15
    
   $ MATCH(t:Territory) WHERE t.RegionID = "2" RETURN t.TerritoryDescription
   "HoffmanEstates"
   "Chicago"
   "Denver"
   "ColoradoSprings"
   "Phoenix"
   "Scottsdale"
   "SantaMonica"
   "MenloPark"
   "SanFrancisco"
   "Campbell"
   "SantaClara"
   "SantaCruz"
   "Bellevue"
   "Redmond"
   "Seattle"
   ```

12. What is the phone number of the shipper with the company name "United Package"? Be sure to ONLY include the phone number in the result.

   ```
   $ MATCH(s:Shipper) WHERE s.CompanyName = "United Package" RETURN s.Phone
   "(503) 555-3199"
   ```

***BONUS:***

13. How many relationships are in the "order-details" edges set?  How many in the "employee-territories" edges set?

   ```
   $ MATCH (n:OrderDetails) RETURN count(n)
   2155
   
   $ MATCH (n:EmployeeTerritories) RETURN count(n)
   49
   ```

14. How many orders were shipped to Albuquerque, NM?  What are the order numbers?

    ```
    $ MATCH (n:Order) 
      WHERE n.ShipCity = "Albuquerque" AND n.ShipRegion = "NM" 
      RETURN count(n) 
    18
    
    $ MATCH (n:Order) 
      WHERE n.ShipCity = "Albuquerque" AND n.ShipRegion = "NM" 
      RETURN n.OrderID
    "10262"
    "10272"
    "10294"
    "10314"
    "10316"
    "10346"
    "10401"
    "10479"
    "10564"
    "10569"
    "10598"
    "10761"
    "10820"
    "10852"
    "10889"
    "10988"
    "11000"
    "11077"
    ```
