# Compilation Errors

## 1.bdd

* **Action Definition Convention**: Uses both 'remove item [from]' and 'addToCart' in different entities.

**Line Number**: 60

* **Line**: `Given the Cart "MyCart" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 62

* **Line**: `Then the List "CartItems" includes "OfficeChairDeluxe"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 67

* **Line**: `Given the Cart "MyCart" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 69

* **Line**: `Then the List "CartItems" includes "OfficeChairDeluxe"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 94

* **Line**: `Given the Wishlist "MyWishlist" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 96

* **Line**: `Then the List "WishlistItems" includes "OfficeChairDeluxe"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - includes; Use made-up keywords - includes

### 2.bdd

* **Action Definition Convention**: Correctly adheres to the guidelines.

**Line Number**: 34

* **Line**: `Then the details of the Item "ErgonomicChair" are shown`
* **Error Type**: Referencing undefined state - shown

**Line Number**: 35

* **Line**: `And the reviews of the Item "ErgonomicChair" are shown`
* **Error Type**: Referencing undefined state - shown

**Line Number**: 59

* **Line**: `Then the Text "CartItems" displays "1 Item"`
* **Error Type**: Use made-up keywords - displays

**Line Number**: 61

* **Line**: `Scenario: Checking Out from Shopping Cart`
* **Error Type**: Use restricted keywords in Scenario name - from

**Line Number**: 67

* **Line**: `Then the Text "CartItems" displays "1 Item"`
* **Error Type**: Use made-up keywords - displays

## 3.bdd

* **Action Definition Convention**: Correctly adheres to the guidelines.
* Has trailing text at the end of the file

**Line Number**: 42

* **Line**: `Then the description and reviews of the Item "ErgonomicChair" are shown`
* **Error Type**: Chaining properties - chaining properties with 'and' is unsupported; Referencing undefined state - shown

**Line Number**: 55

* **Line**: `When I add the Item "ErgonomicChair" to ShoppingCart "MyCart"`
* **Error Type**: Missing keyword - missing 'the' before 'ShoppingCart'

**Line Number**: 64

* **Line**: `Then the Item "ErgonomicChair" is displayed in the Widget "CartItems"`
* **Error Type**: Referencing undefined state - displayed; Check if Entity is in another entity - is displayed in

**Line Number**: 70

* **Line**: `When I view the Widget "CartItems"`
* **Error Type**: Referencing undefined action - view

**Line Number**: 71

* **Line**: `Then the Widget "CartItems" is notEmpty`
* **Error Type**: Referencing undefined state - notEmpty

**Line Number**: 80

* **Line**: `When I view the Widget "OrderSummary"`
* **Error Type**: Referencing undefined action - view

**Line Number**: 87

* **Line**: `When I view the Item "ErgonomicChair"`
* **Error Type**: Referencing undefined action - view

**Line Number**: 89

* **Line**: `When I add the Item "ErgonomicChair" to Wishlist "MyWishlist"`
* **Error Type**: Missing keyword - the

**Line Number**: 98

* **Line**: `Then the Item "ErgonomicChair" is displayed in the Widget "WishlistItems"`
* **Error Type**: Referencing undefined state - displayed; Check if Entity is in another entity - is displayed in

## 4.bdd

* **Action Definition Convention**: Uses both 'remove item [from]' and 'addToCart' in different entities.
* Ran into the limit of output generation and was prompted with the 'Continue generating' button.
* This happened on the very last sentence, and the original output was just `Then`.
* `the List "Items in Wishlist" does not include the Item "Ergonomic Office Chair"` was added to the output after clicking the 'Continue generating' button.

**Line Number**: 48

* **Line**: `When I view the Text "Details" and "Reviews"`
* **Error Type**: Chaining entity identifiers - chaining entity identifiers with 'and' is unsupported; Referencing undefined action - view

**Line Number**: 49

* **Line**: `Then the details and reviews of the Item "Ergonomic Office Chair" are shown`
* **Error Type**: Chaining properties - chaining properties with 'and' is unsupported; Referencing undefined state - shown

**Line Number**: 50

* **Line**: `Then the details* of the Item "Ergonomic Office Chair" are displayed`
* **Error Type**: Invalid symbol in property reference - '*'; Referencing undefined state - displayed

**Line Number**: 53

* **Line**: `When I view the Text "Details"`
* **Error Type**: Referencing undefined action - view

**Line Number**: 54

* **Line**: `Then the details of the Item "Ergonomic Office Chair" are shown`
* **Error Type**: Referencing undefined state - shown

**Line Number**: 71

* **Line**: `Then the list of items includes the Item "Ergonomic Office Chair"`
* **Error Type**: Invalid sentence structure - 'list of items' is invalid; Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 75

* **Line**: `And the items* of the Cart "MyCart" includes the Item "Ergonomic Office Chair"`
* **Error Type**: Invalid symbol in property reference - '*'; Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 78

* **Line**: `When I view the List "Items in Cart"`
* **Error Type**: Referencing undefined action - view; Referencing undefined entity - List

**Line Number**: 79

* **Line**: `Then the List "Items in Cart" includes the Item "Ergonomic Office Chair"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 106

* **Line**: `Then the list of items includes the Item "Ergonomic Office Chair"`
* **Error Type**: Invalid sentence structure - 'list of items' is invalid; Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 108

* **Line**: `Scenario: Removing Item from Wishlist`
* **Error Type**: Use restricted keywords in Scenario name - from

**Line Number**: 112

* **Line**: `When I view the List "Items in Wishlist"`
* **Error Type**: Referencing undefined action - view; Referencing undefined entity - List

**Line Number**: 113

* **Line**: `Then the List "Items in Wishlist" includes the Item "Ergonomic Office Chair"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 114

* **Line**: `When I remove item [from] the Wishlist "MyWishlist"`
* **Error Type**: Invalid action reference - It is referencing the entire action name, although the action defintion is valid syntax, you can only use 2 words when referencing, also using an invalid symbol in the action reference []

**Line Number**: 122

* **Line**: `When I view the List "Items in Wishlist"`
* **Error Type**: Referencing undefined action - view; Referencing undefined entity - List

**Line Number**: 123

* **Line**: `Then the List "Items in Wishlist" does not include the Item "Ergonomic Office Chair"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - include; Use made-up keywords - include

## 5.bdd

* **Action Definition Convention**: Correctly adheres to the guidelines, however, 'check out' is not \<verb> \<noun>.
* Formulated the sentence `When I remove the Product "MyProduct" from the Cart "MyCart"`, which is totally correct and different from the provided examples. This is great.

**Line Number**: 26

* **Line**: `Then the Product "MyProduct" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 32

* **Line**: `Then the profilePicture, name, priceTag, reviewText* of the Product "MyProduct" are displayed`
* **Error Type**: Chaining properties - chaining properties with commas is unsupported; Referencing undefined state - displayed

**Line Number**: 35

* **Line**: `Then the Image "ProfilePicture", Text "ProductName", Label "PriceTag", TextArea "ReviewText" are shown`
* **Error Type**: Chaining entities - chaining entities with commas is unsupported; Lack of interactive statements - missing 'When' statement before the 'Then' statement

**Line Number**: 53

* **Line**: `Then the List "Cart Items" contains the Product "MyProduct"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - contains; Use made-up keywords - contains

**Line Number**: 55

* **Line**: `Scenario: Removing item from shopping cart`
* **Error Type**: Use restricted keywords in Scenario name - from

**Line Number**: 60

* **Line**: `Then the List "Cart Items" contains the Product "MyProduct"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - contains; Use made-up keywords - contains

**Line Number**: 70

* **Line**: `Then the List "Cart Items" does not contain the Product "MyProduct"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - contains; Use made-up keywords - contains

**Line Number**: 72

* **Line**: `Scenario: Checking out from shopping cart`
* **Error Type**: Use restricted keywords in Scenario name - from

**Line Number**: 78

* **Line**: `When I check out the Cart "MyCart"`
* **Error Type**: Invalid action reference - out is a keyword and cannot be used in an action reference

**Line Number**: 104

* **Line**: `Then the List "Wishlist Items" contains the Product "MyProduct"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - contains; Use made-up keywords - contains

## 6.bdd

* **Action Definition Convention**: Uses both 'add item [to]' and 'add to Cart' in different entities. This is incorrect.

**Line Number**: 6

* **Line**: `add to Cart`
* **Error Type**: Invalid use of preposition in action definition - to

**Line Number**: 7

* **Line**: `add to Wishlist`
* **Error Type**: Invalid use of preposition in action definition - to

**Line Number**: 39

* **Line**: `Given the Product "ErgoChair2" is available`
* **Error Type**: Referencing undefined state - available

**Line Number**: 49

* **Line**: `Then the reviewText of the Product "ErgoChair2" is shown`
* **Error Type**: Referencing undefined state - shown

**Line Number**: 52

* **Line**: `Then the Text "Review" is shown`
* **Error Type**: Lack of interactive statements - missing 'When' statement before the 'Then' statement

**Line Number**: 55

* **Line**: `Given the Product "ErgoChair2" is available`
* **Error Type**: Referencing undefined state - available

**Line Number**: 60

* **Line**: `When I add the Product "ErgoChair2" to Cart`
* **Error Type**: Missing entity identifier - Cart; Missing keyword - missing 'the' before 'Cart'

**Line Number**: 69

* **Line**: `Then the Product "ErgoChair2" is listed`
* **Error Type**: Referencing undefined state - listed

**Line Number**: 76

* **Line**: `Then the Product "ErgoChair2" is listed`
* **Error Type**: Referencing undefined state - listed

**Line Number**: 85

* **Line**: `When I confirm the purchase`
* **Error Type**: Invalid sentence structure - not following the grammar at all

**Line Number**: 89

* **Line**: `Given the Product "ErgoChair2" is available`
* **Error Type**: Referencing undefined state - available

**Line Number**: 94

* **Line**: `When I add the Product "ErgoChair2" to Wishlist`
* **Error Type**: Missing entity identifier - Wishlist; Missing keyword - missing 'the' before 'Wishlist'

**Line Number**: 103

* **Line**: `Then the Product "ErgoChair2" is listed`
* **Error Type**: Referencing undefined state - listed

## 7.bdd

* **Action Definition Convention**: Uses both 'remove item [from]' and 'addToCart' in different entities.
* Has trailing text at the end of the file

**Line Number**: 46

* **Line**: `And the Text "Name" is "OfficeChairDeluxe"`
* **Error Type**: Setting an entity to a value instead of a state - entities can only be states, not values

**Line Number**: 47

* **Line**: `And the Text "Price" is "$499"`
* **Error Type**: Setting an entity to a value instead of a state - entities can only be states, not values

**Line Number**: 67

* **Line**: `Then the Text "Cart" is "Empty"`
* **Error Type**: Setting an entity to a value instead of a state - entities can only be states, not values

**Line Number**: 80

* **Line**: `Scenario: Buying items directly from details`
* **Error Type**: Use restricted keywords in Scenario name - from

**Line Number**: 92

* **Line**: `Then the Item "OfficeChairDeluxe" is purchased`
* **Error Type**: Referencing undefined state - purchased

**Line Number**: 95

* **Line**: `When I confirm the purchase`
* **Error Type**: Invalid sentence structure - not following the grammar at all

**Line Number**: 98

* **Line**: `Scenario: Adding and removing items from wishlist`
* **Error Type**: Use restricted keywords in Scenario name - and / from

**Line Number**: 104

* **Line**: `Then the Text "Wishlist" is "Empty"`
* **Error Type**: Setting an entity to a value instead of a state - "Empty"

**Line Number**: 116

* **Line**: `When I remove item from the Wishlist "MyWishlist"`
* **Error Type**: Invalid action reference - It is referencing the entire action name, although the action defintion is valid syntax, you can only use 2 words when referencing; Invalid domain statements - line 116 to 125 features an additional 'When' and 'Then'.

**Line Number**: 125

* **Line**: `Then the Text "Wishlist" is "Empty"`
* **Error Type**: Setting an entity to a value instead of a state - entities can only be states, not values

## 8.bdd

* **Action Definition Convention**: Uses both 'remove item [from]' and 'add to cart' in different entities. This is wrong. It also uses 'view item details', which is not \<verb> \<noun> \<prepostion>.

**Line Number**: 15

* **Line**: `add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - to

**Line Number**: 51

* **Line**: `When I view item details of the Item "OfficeChair1"`
* **Error Type**: Invalid action reference - It is referencing the entire action name, although the action defintion is valid syntax, you can only use 2 words when referencing

**Line Number**: 56

* **Line**: `Then the details of the Item "OfficeChair1" are shown`
* **Error Type**: Referencing undefined state - shown

**Line Number**: 59

* **Line**: `When I see the Text "OfficeChair1Details"`
* **Error Type**: Referencing undefined action - see

**Line Number**: 66

* **Line**: `When I see the Button "Add to Cart"`
* **Error Type**: Referencing undefined action - see

**Line Number**: 76

* **Line**: `When I see the Button "Remove from Cart"`
* **Error Type**: Referencing undefined action - see

**Line Number**: 79

* **Line**: `Scenario: Removing Item from Wishlist`
* **Error Type**: Use restricted keywords in Scenario name - from

**Line Number**: 85

* **Line**: `When I remove item from the Wishlist "OfficeChair1"`
* **Error Type**: Invalid action reference - It is referencing the entire action name, although the action defintion is valid syntax, you can only use 2 words when referencing

**Line Number**: 93

* **Line**: `When I see the Button "Add to Wishlist"`
* **Error Type**: Referencing undefined action - see

**Line Number**: 97

* **Line**: `Given the Cart "MyCart" containsItems`
* **Error Type**: Missing keyword - missing 'is' keyword before the state 'containsItems'

**Line Number**: 100

* **Line**: `When I see the Grid "ItemsInCart"`
* **Error Type**: Referencing undefined action - see

**Line Number**: 110

* **Line**: `When I complete the Form "PaymentInformation"`
* **Error Type**: Referencing undefined entity - Form; Referencing undefined action - complete

## 9.bdd

* **Action Definition Convention**: Uses only 'addToCart'.
* Has trailing text at the end of the file

**Line Number**: 38

* **Line**: `And the value of the TextArea "Reviews" contains "OfficeChair1 reviews"`
* **Error Type**: Check if Entity is in another entity - contains; Referencing undefined property - TextArea does not have the property "value" it has "text"; Use made-up keywords - contains

**Line Number**: 47

* **Line**: `When I review the details of the Item "OfficeChair1"`
* **Error Type**: Referencing undefined action - review; Invalid sentence structure - Cannot use actions on properties

**Line Number**: 48

* **Line**: `Then the TextField "Details" shows "Full details of OfficeChair1"`
* **Error Type**: Use made-up keywords - shows

**Line Number**: 54

* **Line**: `When I view the Item "OfficeChair2"`
* **Error Type**: Referencing undefined action - view

**Line Number**: 64

* **Line**: `When I view the Cart "MyCart"`
* **Error Type**: Referencing undefined action - view

**Line Number**: 65

* **Line**: `Then the ListItem "OfficeChair2" is displayed in the ListView "Cart Items"`
* **Error Type**: Check if Entity is in another entity - is displayed in; Referencing undefined entity - ListItem; Referencing undefined state - displayed

## 10.bdd

* **Action Definition Convention**: Uses 'add [to]'. It is also seen using 'view item details', which is not \<verb> \<noun> \<prepostion>.
* Very close to being accurate, but there is a lack of interactive statements in the scenario and it also wrongly uses actions.

**Line Number**: 26

* **Line**: `Given the Catalog "MyCatalog" has items*`
* **Error Type**: Use made-up keywords - has

**Line Number**: 31

* **Line**: `which means`
* **Error Type**: Lack of interactive statements - line 29 to 35
  
**Line Number**: 48

* **Line**: `When I look at the Item "MyItem"`
* **Error Type**: Referencing undefined action - look at

**Line Number**: 77

* **Line**: `When I view the items of the Cart "MyCart"`
* **Error Type**: Invalid sentence structure - Cannot use actions on properties

**Line Number**: 85

* **Line**: `When I view the items in the Cart "MyCart"`
* **Error Type**: Invalid sentence structure - Cannot use actions on properties

**Line Number**: 112

* **Line**: `When I view the items in the Wishlist "MyWishlist"`
* **Error Type**: Invalid sentence structure - Cannot use actions on properties
