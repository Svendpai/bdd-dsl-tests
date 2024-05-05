# Compilation Errors

## 1.bdd

**Line Number**: 4

* **Line**: `actions: view, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 5

* **Line**: `states: viewed, in cart, in wishlist`
* **Error Type**: Invalid use of preposition in state definition - in cart; Invalid use of preposition in state definition - in wishlist

**Line Number**: 11

* **Line**: `states: checked out`
* **Error Type**: Use restricted keywords in state definition - checked out

**Line Number**: 28

* **Line**: `When I view the details of the product "ErgoChair"`
* **Error Type**: Use action on property instead of entity - view the details

**Line Number**: 33

* **Line**: `Then the product "ErgoChair" details are viewed`
* **Error Type**: Invalid sentence structure - details should be before product, details -> product -> viewed; Lack of interactive statements - missing all interactive statements for the Then clause
  
**Line Number**: 45

* **Line**: `When I add the product "ErgoChair" to the cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 50

* **Line**: `Then the product "ErgoChair" is in cart`
* **Error Type**: Lack of interactive statements - missing all interactive statements for the Then clause; Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 57

* **Line**: `Given the product "ErgoChair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 62

* **Line**: `When I checkout the cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 67

* **Line**: `Then the cart is checked out`
* **Error Type**: Lack of interactive statements - missing all interactive statements for the Then clause; Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something; Spaces in state reference - checked out

**Line Number**: 79

* **Line**: `When I add the product "ErgoChair" to the wishlist`
* **Error Type**: Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something

**Line Number**: 84

* **Line**: `Then the product "ErgoChair" is in wishlist`
* **Error Type**: Lack of interactive statements - missing all interactive statements for the Then clause; Check if Entity is in another entity - is in wishlist, however this is likely a snowball error from the state definition; Spaces in state reference - in wishlist

## 2.bdd

**Line Number**: 4

* **Line**: `actions: add to cart, add to wishlist, view details, buy`
* **Error Type**: Invalid use of preposition in action definition - add to wishlist

**Line Number**: 5

* **Line**: `states: in cart, in wishlist, details viewed`
* **Error Type**: Invalid use of preposition in state definition - in cart; Invalid use of preposition in state definition - in wishlist

**Line Number**: 6

* **Line**: `properties: picture, name, price, more information, reviews`
* **Error Type**: Spaces in property definition - more information

**Line Number**: 11

* **Line**: `states: checked out`
* **Error Type**: Use restricted keywords in state definition - out

**Line Number**: 22

* **Line**: `Given the product "ErgoChair" is displayed on the home page`
* **Error Type**: Invalid sentence structure - displayed on the home page; Referencing undefined state - displayed

**Line Number**: 25

* **Line**: `When I click on the Image of the product "ErgoChair"`
* **Error Type**: Missing entity identifier - Image is an entity, and should therefore be identified with "ProductImage" or something

**Line Number**: 26

* **Line**: `Then the product "ErgoChair" details are viewed`
* **Error Type**: Invalid sentence structure - details are viewed, likely a mistake trying to reference the state "details viewed"

**Line Number**: 29

* **Line**: `Given the BrowserWindow "Product Details" for "ErgoChair" is displayed`
* **Error Type**: Invalid sentence structure - for "ErgoChair"

**Line Number**: 30

* **Line**: `Then the Text of the "More Information" is displayed`
* **Error Type**: Lack of interactive statements - missing When clause before this line; Invalid sentence structure - 'Text of the "More Information"', should be 'Text "More Information"'

**Line Number**: 31

* **Line**: `And the Grid of the "Reviews" is displayed`
* **Error Type**: Invalid sentence structure - 'Grid of the "Reviews" is displayed', should be 'Grid "Reviews" is displayed'

**Line Number**: 32

* **Line**: `Then the product "ErgoChair" details are viewed`
* **Error Type**: Invalid sentence structure - details are viewed, likely a mistake trying to reference the state "details viewed"

**Line Number**: 34

* **Line**: `Given the BrowserWindow "Product Details" for "ErgoChair" is displayed`
* **Error Type**: Invalid sentence structure - for "ErgoChair"

**Line Number**: 35

* **Line**: `Then the Text of the "More Information" is displayed`
* **Error Type**: Lack of interactive statements - missing When clause before this line; Invalid sentence structure - 'Text of the "More Information"', should be 'Text "More Information"'

**Line Number**: 36

* **Line**: `And the Grid of the "Reviews" is displayed`
* **Error Type**: Invalid sentence structure - 'Grid of the "Reviews" is displayed', should be 'Grid "Reviews" is displayed'

**Line Number**: 39

* **Line**: `Given the product "ErgoChair" details are viewed`
* **Error Type**: Invalid sentence structure - details are viewed, likely a mistake trying to reference the state "details viewed"

**Line Number**: 41

* **Line**: `Given the BrowserWindow "Product Details" for "ErgoChair" is displayed`
* **Error Type**: Invalid sentence structure - for "ErgoChair"

**Line Number**: 42

* **Line**: `Then the Text of the "More Information" is displayed`
* **Error Type**: Lack of interactive statements - missing When clause before this line; Invalid sentence structure - 'Text of the "More Information"', should be 'Text "More Information"'

**Line Number**: 43

* **Line**: `And the Grid of the "Reviews" is displayed`
* **Error Type**: Invalid sentence structure - 'Grid of the "Reviews" is displayed', should be 'Grid "Reviews" is displayed'

**Line Number**: 44

* **Line**: `When I add the product "ErgoChair" to cart`
* **Error Type**: Referencing undefined entity - cart is not an entity, shoppingCart is, 'to cart' likely comes from the action definition "add to cart"; Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something;

**Line Number**: 46

* **Line**: `Given the BrowserWindow "Product Details" for "ErgoChair" is displayed`
* **Error Type**: Invalid sentence structure - for "ErgoChair"

**Line Number**: 49

* **Line**: `Then the product "ErgoChair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 52

* **Line**: `Then the Image of the product "ErgoChair" is displayed in the Grid "Cart Items"`
* **Error Type**: Lack of interactive statements - missing When clause before this line; Invalid sentence structure - is displayed in the Grid "Cart Items"; Referencing undefined property - Image, should be picture; Referencing undefined state - displayed

**Line Number**: 55

* **Line**: `Given the product "ErgoChair" details are viewed`
* **Error Type**: Invalid sentence structure - details are viewed, likely a mistake trying to reference the state "details viewed"

**Line Number**: 57

* **Line**: `Given the BrowserWindow "Product Details" for "ErgoChair" is displayed`
* **Error Type**: Invalid sentence structure - for "ErgoChair"

**Line Number**: 58

* **Line**: `Then the Text of the "More Information" is displayed`
* **Error Type**: Lack of interactive statements - missing When clause before this line; Invalid sentence structure - 'Text of the "More Information"', should be 'Text "More Information"'

**Line Number**: 59

* **Line**: `And the Grid of the "Reviews" is displayed`
* **Error Type**: Invalid sentence structure - 'Grid of the "Reviews" is displayed', should be 'Grid "Reviews" is displayed'

**Line Number**: 60

* **Line**: `When I add the product "ErgoChair" to wishlist`
* **Error Type**: Missing entity identifier - 'to wishlist' likely comes from the action definition "add to wishlist"; Missing keyword - the

**Line Number**: 62

* **Line**: `Given the BrowserWindow "Product Details" for "ErgoChair" is displayed`
* **Error Type**: Invalid sentence structure - for "ErgoChair"

**Line Number**: 65

* **Line**: `Then the product "ErgoChair" is in wishlist`
* **Error Type**: Check if Entity is in another entity - is in wishlist, however this is likely a snowball error from the state definition; Spaces in state reference - in wishlist

**Line Number**: 68

* **Line**: `Then the Image of the product "ErgoChair" is displayed in the Grid "Wishlist Items"`
* **Error Type**: Lack of interactive statements - missing When clause before this line; Invalid sentence structure - is displayed in the Grid "Wishlist Items"; Referencing undefined property - Image, should be picture; Referencing undefined state - displayed

**Line Number**: 70

* **Line**: `Scenario: Checking out from shopping cart`
* **Error Type**: Use restricted keywords in Scenario name - from

**Line Number**: 71

* **Line**: `Given the product "ErgoChair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 74

* **Line**: `Then the Image of the product "ErgoChair" is displayed in the Grid "Cart Items"`
* **Error Type**: Lack of interactive statements - missing When clause before this line; Invalid sentence structure - is displayed in the Grid "Cart Items"; Referencing undefined property - Image, should be picture; Referencing undefined state - displayed

**Line Number**: 76

* **Line**: `When I checkout from the shoppingCart`
* **Error Type**: Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something

**Line Number**: 80

* **Line**: `Then the shoppingCart is checked out`
* **Error Type**: Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something; Spaces in state reference - checked out

**Line Number**: 83

* **Line**: `Then the Text "Thank you for your purchase!" is displayed`
* **Error Type**: Lack of interactive statements - missing When clause before this line

## 3.bdd

**Line Number**: 4

* **Line**: `actions: view details, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 5

* **Line**: `states: viewed, in cart, in wishlist`
* **Error Type**: Invalid use of preposition in state definition - in cart; Invalid use of preposition in state definition - in wishlist

**Line Number**: 11

* **Line**: `states: checked out`
* **Error Type**: Use restricted keywords in state definition - checked out

**Line Number**: 30

* **Line**: `When I look at the Text "Ergonomic Executive Chair Description"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 31

* **Line**: `And look at the Text "Ergonomic Executive Chair Reviews"`
* **Error Type**: Referencing undefined action - look at; Lack of interactive statements - missing Then clause after this line

**Line Number**: 32

* **Line**: `Then the product "Ergonomic Executive Chair" details are shown`
* **Error Type**: Invalid sentence structure - details are shown; Referencing undefined state - shown; Referencing undefined property - details

**Line Number**: 35

* **Line**: `Then the Text "Ergonomic Executive Chair Description" is visible`
* **Error Type**: Lack of interactive statements - missing When clause before this line; Referencing undefined state - visible

**Line Number**: 36

* **Line**: `And the Text "Ergonomic Executive Chair Reviews" is visible`
* **Error Type**: Referencing undefined state - visible

**Line Number**: 42

* **Line**: `When I look at the Text "Ergonomic Executive Chair Description"`
* **Error Type**: Referencing undefined action - look at; Lack of interactive statements - missing Then clause after this line

**Line Number**: 43

* **Line**: `Then I add the product "Ergonomic Executive Chair" to cart`
* **Error Type**: Lack of domain statements - this should have been a 'When' clause; Lack of interactive statements - should have included a Then statement above it; Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something, could be a snowball effect from the incorrect action definition 'add to cart'; Missing keyword - the

**Line Number**: 47

* **Line**: `Then the product "Ergonomic Executive Chair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 50

* **Line**: `When I look at the Grid "Cart Products"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 51

* **Line**: `Then the Text "Ergonomic Executive Chair" is in the Grid "Cart Products"`
* **Error Type**: Check if Entity is in another entity - is in the Grid "Cart Products"

**Line Number**: 54

* **Line**: `Given the product "Ergonomic Executive Chair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 57

* **Line**: `When I look at the Grid "Cart Products"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 58

* **Line**: `Then the Text "Ergonomic Executive Chair" is in the Grid "Cart Products"`
* **Error Type**: Check if Entity is in another entity - is in the Grid "Cart Products"

**Line Number**: 59

* **Line**: `When I checkout the cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 63

* **Line**: `Then the cart is checked out`
* **Error Type**: Lack of interactive statements - Then clause before this line; Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something; Spaces in state reference - checked out

**Line Number**: 66

* **Line**: `Then the Text "Thank you for your purchase!" is visible`
* **Error Type**: Lack of interactive statements - missing When clause before this line; Referencing undefined state - visible

**Line Number**: 72

* **Line**: `When I look at the Text "Ergonomic Executive Chair Description"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 73

* **Line**: `Then I add the product "Ergonomic Executive Chair" to wishlist`
* **Error Type**: Lack of domain statements - this should have been a 'When' clause; Lack of interactive statements - should have included a Then statement above it; Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something, could be a snowball effect from the incorrect action definition 'add to wishlist'; Missing keyword - the

**Line Number**: 77

* **Line**: `Then the product "Ergonomic Executive Chair" is in wishlist`
* **Error Type**: Check if Entity is in another entity - is in wishlist, however this is likely a snowball error from the state definition; Spaces in state reference - in wishlist; Lack of interactive statements - missing Then statement above this line

**Line Number**: 80

* **Line**: `When I look at the Grid "Wishlist Products"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 81

* **Line**: `Then the Text "Ergonomic Executive Chair" is in the Grid "Wishlist Products"`
* **Error Type**: Check if Entity is in another entity - is in the Grid "Wishlist Products"

## 4.bdd

**Line Number**: 5

* **Line**: `view details, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 7

* **Line**: `in cart, in wishlist`
* **Error Type**: Invalid use of preposition in state definition - in cart; Invalid use of preposition in state definition - in wishlist

**Line Number**: 34

* **Line**: `checked out`
* **Error Type**: Use restricted keywords in state definition - checked out

**Line Number**: 49

* **Line**: `Given the catalog is displayed`
* **Error Type**: Missing entity identifier - catalog is an entity, and should therefore be named "MyCatalog" or something

**Line Number**: 50

* **Line**: `And the product "ErgoChair" is in the catalog`
* **Error Type**: Check if Entity is in another entity - is in the catalog;

**Line Number**: 53

* **Line**: `When I view the catalog`
* **Error Type**: Missing entity identifier - catalog is an entity, and should therefore be named "MyCatalog" or something

**Line Number**: 54

* **Line**: `Then the product "ErgoChair" is displayed with its picture, name, and price`
* **Error Type**: Referencing undefined state - displayed; Use made-up keywords - with; Chaining properties - picture, name, and price; Invalid sentence structure - displayed with its picture, name, and price

**Line Number**: 59

* **Line**: `Then the detailsPage "ErgoChair Details" is displayed with productDetails and reviews`
* **Error Type**: Chaining properties - productDetails and reviews; Use made-up keywords - with; Invalid sentence structure - displayed with productDetails and reviews

**Line Number**: 60

* **Line**: `Then the detailsPage "ErgoChair Details" is displayed`
* **Error Type**: Lack of interactive statements - missing all interactive statements for the Then clause

**Line Number**: 63

* **Line**: `Given the detailsPage "ErgoChair Details" is displayed`
* **Error Type**: Lack of interactive statements - missing all interactive statements for the Given clause

**Line Number**: 64

* **Line**: `When I add the product "ErgoChair" to the cart`
* **Error Type**: Referencing undefined entity - cart, the entity is called shoppingCart; Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 69

* **Line**: `Then the product "ErgoChair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart; Lack of interactive statements - missing all interactive statements for the Then clause

**Line Number**: 71

* **Line**: `Scenario: Checking out from shopping cart`
* **Error Type**: Use restricted keywords in Scenario name - from

**Line Number**: 72

* **Line**: `Given the product "ErgoChair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart; Lack of interactive statements - missing all interactive statements for the Given clause

**Line Number**: 73

* **Line**: `And the shoppingCart is displayed`
* **Error Type**: Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something; Lack of domain statements - an And statement by itself is not a valid domain statement

**Line Number**: 76

* **Line**: `When I view the shoppingCart`
* **Error Type**: Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something

**Line Number**: 77

* **Line**: `Then the product "ErgoChair" is listed in the shoppingCart`
* **Error Type**: Check if Entity is in another entity - is listed in the shoppingCart; Spaces in state reference - in the shoppingCart; Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something; Use made-up keywords - listed

**Line Number**: 78

* **Line**: `When I checkout from the shoppingCart`
* **Error Type**: Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something

**Line Number**: 80

* **Line**: `Given the shoppingCart is displayed`
* **Error Type**: Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something

**Line Number**: 83

* **Line**: `Then the shoppingCart is checked out`
* **Error Type**: Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something; Spaces in state reference - checked out; Lack of interactive statements - missing all interactive statements for the Then clause

**Line Number**: 86

* **Line**: `Given the detailsPage "ErgoChair Details" is displayed`
* **Error Type**: Lack of interactive statements - missing all interactive statements for the Given clause

**Line Number**: 90

* **Line**: `When I add the product "ErgoChair" to the wishlist`
* **Error Type**: Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something

**Line Number**: 94

* **Line**: `Then the product "ErgoChair" is in wishlist`
* **Error Type**: Check if Entity is in another entity - is in wishlist, however this is likely a snowball error from the state definition; Spaces in state reference - in wishlist; Lack of interactive statements - missing all interactive statements for the Then clause

## 5.bdd

**Line Number**: 4

* **Line**: `actions: view details, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 23

* **Line**: `And the product "ErgoChair" is displayed with picture, name, and price`
* **Error Type**: Referencing undefined state - displayed; Chaining properties - picture, name, and price; Invalid sentence structure - picture, name, or price should go first; Use made-up keywords - with

**Line Number**: 26

* **Line**: `And the cell "ErgoChair" in the column "Products" is displayed`
* **Error Type**: Check if Entity is in another entity - is in the column "Products"; Invalid sentence structure - in the column; Referencing undefined entity - column; Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 29

* **Line**: `When I click on the cell "ErgoChair" in the column "Products"`
* **Error Type**: Check if Entity is in another entity - is in the column "Products"; Invalid sentence structure - in the column; Referencing undefined entity - column; Lack of interactive statements - missing Given before this line and Then clause after

**Line Number**: 31

* **Line**: `And the picture, name, price, description, and reviews of the product "ErgoChair" are displayed`
* **Error Type**: Chaining properties - picture, name, price, description, and reviews; Referencing undefined state - displayed

**Line Number**: 33

* **Line**: `Then the Image "Product Image" is displayed`
* **Error Type**: Lack of interactive statements - this should have been a Given statement as it is the first one

**Line Number**: 34

* **Line**: `And the Text "Product Name" is "ErgoChair"`
* **Error Type**: Setting an entity to a value instead of a state - is "ErgoChair"

**Line Number**: 37

* **Line**: `And the Grid "Product Reviews" is displayed`
* **Error Type**: Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 41

* **Line**: `And the product "ErgoChair" is displayed with details`
* **Error Type**: Referencing undefined state - displayed; Use made-up keywords - with; Invalid sentence structure - displayed with details

**Line Number**: 43

* **Line**: `Given the Text "Product Name" is "ErgoChair"`
* **Error Type**: Setting an entity to a value instead of a state - is "ErgoChair"

**Line Number**: 44

* **Line**: `And the Button "Add to Cart" is enabled`
* **Error Type**: Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 45

* **Line**: `When I click on the Button "Add to Cart"`
* **Error Type**: Lack of interactive statements - missing Then clause after this line

**Line Number**: 46

* **Line**: `Then the product "ErgoChair" is added to the cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something; Invalid sentence structure - is added to the cart, likely comes from the action definition "add to cart"

**Line Number**: 48

* **Line**: `Then the Notification "Product added to cart" is displayed`
* **Error Type**: Lack of interactive statements - missing Given and When clause before this line

**Line Number**: 52

* **Line**: `And the cart contains the product "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - contains the product "ErgoChair"; Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 55

* **Line**: `And the cell "ErgoChair" in the column "Products" is displayed`
* **Error Type**: Check if Entity is in another entity - is in the column "Products"; Invalid sentence structure - in the column; Referencing undefined entity - column; Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 56

* **Line**: `When I click on the Button "Checkout"`
* **Error Type**: Lack of interactive statements - missing all interactive statements

**Line Number**: 58

* **Line**: `And the Text "Order Summary" includes "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - includes "ErgoChair";

**Line Number**: 60

* **Line**: `Then the Text "Order Summary" is filled`
* **Error Type**: Lack of interactive statements - this should be a given statement as it is the first one; Referencing undefined state - filled

**Line Number**: 61

* **Line**: `And the Button "Confirm Order" is enabled`
* **Error Type**: Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 65

* **Line**: `And the product "ErgoChair" is displayed with details`
* **Error Type**: Referencing undefined state - displayed; Use made-up keywords - with; Invalid sentence structure - displayed with details

**Line Number**: 67

* **Line**: `Given the Text "Product Name" is "ErgoChair"`
* **Error Type**: Setting an entity to a value instead of a state - is "ErgoChair"

**Line Number**: 68

* **Line**: `And the Button "Add to Wishlist" is enabled`
* **Error Type**: Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 69

* **Line**: `When I click on the Button "Add to Wishlist"`
* **Error Type**: Lack of interactive statements - all interactive statements are missing

**Line Number**: 70

* **Line**: `Then the product "ErgoChair" is added to the wishlist`
* **Error Type**: Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something; Invalid sentence structure - is added to the wishlist, likely comes from the action definition "add to wishlist"

**Line Number**: 72

* **Line**: `Then the Notification "Product added to wishlist" is displayed`
* **Error Type**: Lack of interactive statements - missing Given and When clause before this line

**Line Number**: 76

* **Line**: `And the wishlist contains the product "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - contains the product "ErgoChair"; Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something

**Line Number**: 79

* **Line**: `And the cell "ErgoChair" in the column "Products" is displayed`
* **Error Type**: Check if Entity is in another entity - is in the column "Products"; Invalid sentence structure - in the column; Referencing undefined entity - column; Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 80

* **Line**: `When I view the wishlist`
* **Error Type**: Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something; Lack of interactive statements - missing all interactive statements

**Line Number**: 81

* **Line**: `Then the product "ErgoChair" is displayed in the wishlist with picture, name, and price`
* **Error Type**: Referencing undefined state - displayed; Chaining properties - picture, name, and price; Invalid sentence structure - displayed with picture, name, and price; Use made-up keywords - with; Check if Entity is in another entity - is displayed in the wishlist

**Line Number**: 83

* **Line**: `Then the Image "Product Image" in the row "ErgoChair" is displayed`
* **Error Type**: Lack of interactive statements - This should have been a Given statement as it is the first one; Check if Entity is in another entity - in the row "ErgoChair"; Invalid sentence structure - in the row

**Line Number**: 84

* **Line**: `And the Text "Product Name" in the row "ErgoChair" is "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - in the row "ErgoChair"; Invalid sentence structure - in the row

**Line Number**: 85

* **Line**: `And the Text "Product Price" in the row "ErgoChair" is displayed`
* **Error Type**: Check if Entity is in another entity - in the row "ErgoChair"; Invalid sentence structure - in the row; Lack of interactive statements - missing When and Then clause after this line

## 6.bdd

**Line Number**: 4

* **Line**: `actions: view, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 5

* **Line**: `states: viewed, in cart, in wishlist`
* **Error Type**: Invalid use of preposition in state definition - in cart; Invalid use of preposition in state definition - in wishlist

**Line Number**: 11

* **Line**: `states: checked out`
* **Error Type**: Use restricted keywords in state definition - out

**Line Number**: 25

* **Line**: `When I look at the Grid "Catalog"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 27

* **Line**: `And the Text "Aeron Chair Name" is "Aeron Chair"`
* **Error Type**: Setting an entity to a value instead of a state - is "Aeron Chair"

**Line Number**: 28

* **Line**: `And the Text "Aeron Chair Price" is "$999"`
* **Error Type**: Setting an entity to a value instead of a state - is "$999"

**Line Number**: 34

* **Line**: `And the Text "Product Name" is "Aeron Chair"`
* **Error Type**: Setting an entity to a value instead of a state - is "Aeron Chair"

**Line Number**: 37

* **Line**: `Then the product "Aeron Chair" is viewed`
* **Error Type**: Lack of interactive statements - missing all interactive statements for the Then clause

**Line Number**: 43

* **Line**: `When I look at the Text "Product Name"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 44

* **Line**: `Then the value of the Text "Product Name" is "Aeron Chair"`
* **Error Type**: Referencing undefined property - value

**Line Number**: 45

* **Line**: `When I add the product "Aeron Chair" to cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something, likely comes from the incorrect action definition; Missing keyword - the

**Line Number**: 50

* **Line**: `Then the product "Aeron Chair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart; Lack of interactive statements - missing all interactive statements for the Then clause

**Line Number**: 56

* **Line**: `When I look at the Text "Product Name"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 57

* **Line**: `Then the value of the Text "Product Name" is "Aeron Chair"`
* **Error Type**: Referencing undefined property - value

**Line Number**: 58

* **Line**: `When I add the product "Aeron Chair" to wishlist`
* **Error Type**: Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something, likely comes from the incorrect action definition; Missing keyword - the

**Line Number**: 63

* **Line**: `Then the product "Aeron Chair" is in wishlist`
* **Error Type**: Check if Entity is in another entity - is in wishlist, however this is likely a snowball error from the state definition; Spaces in state reference - in wishlist; Lack of interactive statements - missing all interactive statements for the Then clause

**Line Number**: 66

* **Line**: `Given the cart contains the product "Aeron Chair"`
* **Error Type**: Check if Entity is in another entity - contains the product "Aeron Chair"; Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 69

* **Line**: `When I look at the Grid "Cart Items"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 70

* **Line**: `Then the Text "Product Name" is "Aeron Chair"`
* **Error Type**: Setting an entity to a value instead of a state - is "Aeron Chair"

**Line Number**: 71

* **Line**: `And the Text "Product Price" is "$999"`
* **Error Type**: Setting an entity to a value instead of a state - is "$999"

**Line Number**: 72

* **Line**: `When I checkout the cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 77

* **Line**: `And the Text "Confirmation Message" is "Thank you for your purchase!"`
* **Error Type**: Setting an entity to a value instead of a state - is "Thank you for your purchase!"

**Line Number**: 78

* **Line**: `Then the cart is checked out`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something; Spaces in state reference - checked out; Lack of interactive statements - missing all interactive statements for the Then clause

## 7.bdd

**Line Number**: 4

* **Line**: `actions: view details, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 5

* **Line**: `states: viewed, in cart, in wishlist`
* **Error Type**: Invalid use of preposition in state definition - in cart; Invalid use of preposition in state definition - in wishlist

**Line Number**: 11

* **Line**: `states: checkedOut`
* **Error Type**: Use restricted keywords in state definition - checkedOut

**Line Number**: 25

* **Line**: `When I look at the Grid "Products"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 27

* **Line**: `And the Text "ErgoChair Name" is "ErgoChair"`
* **Error Type**: Setting an entity to a value instead of a state - is "ErgoChair"

**Line Number**: 28

* **Line**: `And the Text "ErgoChair Price" is "£499"`
* **Error Type**: Setting an entity to a value instead of a state - is "£499"

**Line Number**: 37

* **Line**: `When I look at the Text "Description"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 47

* **Line**: `When I look at the Button "Add to Cart"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 49

* **Line**: `When I add the product "ErgoChair" to the cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 54

* **Line**: `Then the product "ErgoChair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 57

* **Line**: `When I look at the Grid "Cart Items"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 59

* **Line**: `And the Text "1" is displayed for the Quantity`
* **Error Type**: Invalid sentence structure - is displayed for the Quantity

**Line Number**: 60

* **Line**: `And the Text "£499" is displayed for the Price`
* **Error Type**: Invalid sentence structure - is displayed for the Price

**Line Number**: 66

* **Line**: `When I look at the Button "Add to Wishlist"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 68

* **Line**: `When I add the product "ErgoChair" to the wishlist`
* **Error Type**: Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something

**Line Number**: 73

* **Line**: `Then the product "ErgoChair" is in wishlist`
* **Error Type**: Check if Entity is in another entity - is in wishlist, however this is likely a snowball error from the state definition; Spaces in state reference - in wishlist

**Line Number**: 76

* **Line**: `When I look at the Grid "Wishlist Items"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 81

* **Line**: `Given the cart contains the product "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - contains the product "ErgoChair"; Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 84

* **Line**: `When I look at the Grid "Cart Items"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 86

* **Line**: `And the Text "1" is displayed for the Quantity`
* **Error Type**: Invalid sentence structure - is displayed for the Quantity

**Line Number**: 87

* **Line**: `And the Text "£499" is displayed for the Price`
* **Error Type**: Invalid sentence structure - is displayed for the Price

**Line Number**: 88

* **Line**: `When I checkout the cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 93

* **Line**: `Then the cart is checked out`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something; Spaces in state reference - checked out

**Line Number**: 96

* **Line**: `When I look at the Text "Order Status"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 97

* **Line**: `Then the Text "Order Status" is "Confirmed"`
* **Error Type**: Setting an entity to a value instead of a state - is "Confirmed"

## 8.bdd

**Line Number**: 4

* **Line**: `actions: view, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 5

* **Line**: `states: viewed, in cart, in wishlist`
* **Error Type**: Invalid use of preposition in state definition - in cart; Invalid use of preposition in state definition - in wishlist

**Line Number**: 11

* **Line**: `states: checked out`
* **Error Type**: Use restricted keywords in state definition - checked out

**Line Number**: 26

* **Line**: `Then the TextField "Name" is "ErgoChair"`
* **Error Type**: Setting an entity to a value instead of a state - is "ErgoChair"

**Line Number**: 31

* **Line**: `When I click on the Button "View Details"`
* **Error Type**: Lack of interactive statements - missing given statement above this line

**Line Number**: 37

* **Line**: `When I look at the product "ErgoChair"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 47

* **Line**: `When I add the product "ErgoChair" to the cart`
* **Error Type**: Referencing undefined entity - cart, the entity is called shoppingCart; Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 49

* **Line**: `When I click on the Button "Add to Cart"`
* **Error Type**: Lack of interactive statements - missing given statement before this line

**Line Number**: 51

* **Line**: `Then the product "ErgoChair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 54

* **Line**: `When I look at the list "Cart Items"`
* **Error Type**: Referencing undefined action - look at; Referencing undefined entity - list

**Line Number**: 55

* **Line**: `Then the product "ErgoChair" is listed`
* **Error Type**: Referencing undefined state - listed

**Line Number**: 57

* **Line**: `Scenario: Checking out from shopping cart`
* **Error Type**: Use restricted keywords in Scenario name - from

**Line Number**: 58

* **Line**: `Given the shoppingCart contains the product "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - contains the product "ErgoChair"; Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something

**Line Number**: 61

* **Line**: `When I look at the list "Cart Items"`
* **Error Type**: Referencing undefined action - look at; Referencing undefined entity - list

**Line Number**: 62

* **Line**: `Then the product "ErgoChair" is listed`
* **Error Type**: Referencing undefined state - listed

**Line Number**: 63

* **Line**: `When I checkout the shoppingCart`
* **Error Type**: Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something

**Line Number**: 65

* **Line**: `When I click on the Button "Checkout"`
* **Error Type**: Lack of interactive statements - missing given statement before this line

**Line Number**: 67

* **Line**: `Then the shoppingCart is checked out`
* **Error Type**: Missing entity identifier - shoppingCart is an entity, and should therefore be named "MyShoppingCart" or something; Spaces in state reference - checked out

**Line Number**: 70

* **Line**: `When I look at the page`
* **Error Type**: Referencing undefined action - look at; Use action on property instead of entity - look at the page

**Line Number**: 71

* **Line**: `Then the TextField "Order Status" is "Confirmed"`
* **Error Type**: Setting an entity to a value instead of a state - is "Confirmed"

**Line Number**: 79

* **Line**: `When I add the product "ErgoChair" to the wishlist`
* **Error Type**: Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something

**Line Number**: 81

* **Line**: `When I click on the Button "Add to Wishlist"`
* **Error Type**: Lack of interactive statements - missing given statement before this line

**Line Number**: 83

* **Line**: `Then the product "ErgoChair" is in wishlist`
* **Error Type**: Check if Entity is in another entity - is in wishlist, however this is likely a snowball error from the state definition; Spaces in state reference - in wishlist

**Line Number**: 87

* **Line**: `When I look at the list "Wishlist Items"`
* **Error Type**: Referencing undefined action - look at; Referencing undefined entity - list

**Line Number**: 88

* **Line**: `Then the product "ErgoChair" is listed`
* **Error Type**: Referencing undefined state - listed

## 9.bdd

**Line Number**: 4

* **Line**: `actions: view, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 5

* **Line**: `states: viewed, in cart, in wishlist`
* **Error Type**: Invalid use of preposition in state definition - in cart; Invalid use of preposition in state definition - in wishlist

**Line Number**: 11

* **Line**: `states: checked out`
* **Error Type**: Use restricted keywords in state definition - checked out

**Line Number**: 26

* **Line**: `Then the Text "ErgoChair Name" and "ErgoChair Price" are displayed`
* **Error Type**: Chaining entity identifiers - "ErgoChair Name" and "ErgoChair Price"

**Line Number**: 31

* **Line**: `Then the Text "ErgoChair Description" and "ErgoChair Reviews" are displayed`
* **Error Type**: Chaining entity identifiers - "ErgoChair Description" and "ErgoChair Reviews"

**Line Number**: 36

* **Line**: `Then the Text "ErgoChair Description" and "ErgoChair Reviews" are displayed`
* **Error Type**: Chaining entity identifiers - "ErgoChair Description" and "ErgoChair Reviews"

**Line Number**: 44

* **Line**: `When I add the product "ErgoChair" to cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something, likely an effect from the incorrect action definition; Missing keyword - the; Referencing undefined entity - cart, the entity is called shoppingCart

**Line Number**: 49

* **Line**: `Then the product "ErgoChair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 53

* **Line**: `Then the Text "ErgoChair Name" and "ErgoChair Price" are displayed in the cart`
* **Error Type**: Chaining entity identifiers - "ErgoChair Name" and "ErgoChair Price"

**Line Number**: 61

* **Line**: `When I add the product "ErgoChair" to wishlist`
* **Error Type**: Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something, likely comes from the incorrect action definition; Missing keyword - the

**Line Number**: 66

* **Line**: `Then the product "ErgoChair" is in wishlist`
* **Error Type**: Check if Entity is in another entity - is in wishlist, however this is likely a snowball error from the state definition; Spaces in state reference - in wishlist

**Line Number**: 70

* **Line**: `Then the Text "ErgoChair Name" and "ErgoChair Price" are displayed in the wishlist`
* **Error Type**: Chaining entity identifiers - "ErgoChair Name" and "ErgoChair Price"

**Line Number**: 73

* **Line**: `Given the shoppingCart "MyCart" contains "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - contains "ErgoChair"

**Line Number**: 78

* **Line**: `Then the Text "ErgoChair Name" and "ErgoChair Price" are displayed in the cart`
* **Error Type**: Chaining entity identifiers - "ErgoChair Name" and "ErgoChair Price"

**Line Number**: 83

* **Line**: `Then the shoppingCart "MyCart" is checked out`
* **Error Type**: Spaces in state reference - checked out

## 10.bdd

**Line Number**: 4

* **Line**: `actions: view, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 5

* **Line**: `states: viewed, in cart, in wishlist`
* **Error Type**: Invalid use of preposition in state definition - in cart; Invalid use of preposition in state definition - in wishlist

**Line Number**: 11

* **Line**: `states: checked out`
* **Error Type**: Use restricted keywords in state definition - checked out

**Line Number**: 34

* **Line**: `Given the homepage  is displayed`
* **Error Type**: Missing entity identifier - homepage is an entity, and should therefore be named "MyHomepage" or something

**Line Number**: 36

* **Line**: `Given the BrowserWindow "Home" is displayed`
* **Error Type**: Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 40

* **Line**: `When I click on the Image "ErgoChair Picture"`
* **Error Type**: Lack of interactive statements - missing Then clause after this line

**Line Number**: 44

* **Line**: `Then the value of the TextField "Product Name" is "ErgoChair"`
* **Error Type**: Lack of interactive statements - missing When clause before this line

**Line Number**: 51

* **Line**: `Given the BrowserWindow "Product Details" is displayed`
* **Error Type**: Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 52

* **Line**: `When I add the product "ErgoChair" to cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something; Missing keyword - the

**Line Number**: 55

* **Line**: `When I click on the Button "Add to Cart"`
* **Error Type**: Lack of interactive statements - missing Then clause after this line

**Line Number**: 56

* **Line**: `Then the product "ErgoChair" is in cart`
* **Error Type**: Check if Entity is in another entity - is in cart, however this is likely a snowball error from the state definition; Spaces in state reference - in cart

**Line Number**: 59

* **Line**: `Then the Text "ErgoChair" is shown`
* **Error Type**: Lack of interactive statements - missing When clause before this line

**Line Number**: 64

* **Line**: `Given the BrowserWindow "Product Details" is displayed`
* **Error Type**: Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 65

* **Line**: `When I add the product "ErgoChair" to wishlist`
* **Error Type**: Missing entity identifier - wishlist is an entity, and should therefore be named "MyWishlist" or something; Missing keyword - the

**Line Number**: 68

* **Line**: `When I click on the Button "Add to Wishlist"`
* **Error Type**: Lack of interactive statements - missing Then clause after this line

**Line Number**: 69

* **Line**: `Then the product "ErgoChair" is in wishlist`
* **Error Type**: Check if Entity is in another entity - is in wishlist, however this is likely a snowball error from the state definition; Spaces in state reference - in wishlist

**Line Number**: 72

* **Line**: `Then the Text "ErgoChair" is shown`
* **Error Type**: Lack of interactive statements - missing When clause before this line

**Line Number**: 75

* **Line**: `Given the cart contains the product "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - contains the product "ErgoChair"; Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 78

* **Line**: `And the Text "ErgoChair" is shown`
* **Error Type**: Lack of interactive statements - missing When and Then clause after this line

**Line Number**: 79

* **Line**: `When I checkout the cart`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something

**Line Number**: 82

* **Line**: `When I click on the Button "Checkout"`
* **Error Type**: Lack of interactive statements - missing Then clause after this line

**Line Number**: 83

* **Line**: `Then the cart is checked out`
* **Error Type**: Missing entity identifier - cart is an entity, and should therefore be named "MyCart" or something; Spaces in state reference - checked out

**Line Number**: 86

* **Line**: `Then the Text "Your order has been placed" is shown`
* **Error Type**: Lack of interactive statements - missing When before this line
