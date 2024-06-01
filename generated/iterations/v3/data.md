# Compilation Errors

## 1.bdd

**Line Number**: 48

* **Line**: `Then the picture of the Product "MyProduct" is shown,`
* **Error Type**: Referencing undefined state - shown; Invalid symbol in statement - ","

**Line Number**: 49

* **Line**: `And the name of the Product "MyProduct" is visible,`
* **Error Type**: Referencing undefined state - visible; Invalid symbol in statement - ","

**Line Number**: 50

* **Line**: `And the price of the Product "MyProduct" is visible`
* **Error Type**: Referencing undefined state - visible

**Line Number**: 60

* **Line**: `Then the description of the Product "MyProduct" is visible,`
* **Error Type**: Referencing undefined state - visible; Invalid symbol in statement - ","

**Line Number**: 61

* **Line**: `And the reviews of the Product "MyProduct" are visible`
* **Error Type**: Referencing undefined state - visible

**Line Number**: 73

* **Line**: `Then the ShoppingCart "MyShoppingCart" containsProducts`
* **Error Type**: Missing keyword - 'is'

**Line Number**: 76

* **Line**: `Given the ShoppingCart "MyShoppingCart" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 78

* **Line**: `Then the items of the ShoppingCart "MyShoppingCart" include the Product "MyProduct"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 90

* **Line**: `Then the Wishlist "MyWishlist" containsProducts`
* **Error Type**: Missing keyword - 'is'

**Line Number**: 93

* **Line**: `Given the Wishlist "MyWishlist" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 95

* **Line**: `Then the items of the Wishlist "MyWishlist" include the Product "MyProduct"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 98

* **Line**: `Given the ShoppingCart "MyShoppingCart" containsProducts`
* **Error Type**: Missing keyword - 'is'

**Line Number**: 100

* **Line**: `Given the ShoppingCart "MyShoppingCart" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 102

* **Line**: `Then the items of the ShoppingCart "MyShoppingCart" include the Product "MyProduct"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 105

* **Line**: `Given the ShoppingCart "MyShoppingCart" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 112

* **Line**: `Then the totalPrice of the ShoppingCart "MyShoppingCart" is calculated,`
* **Error Type**: Referencing undefined state - calculated; Invalid symbol in statement - ","

**Line Number**: 113

* **Line**: `And the ShoppingCart "MyShoppingCart" is void`
* **Error Type**: Referencing undefined state - void

## 2.bdd

**Line Number**: 47

* **Line**: `Given the ProductPage "ProductDetailsPage" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 49

* **Line**: `Then the details of the ProductPage "ProductDetailsPage" are displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 54

* **Line**: `Then the ProductPage "ProductDetailsPage" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 61

* **Line**: `Then the details of the ProductPage "ProductDetailsPage" are displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 67

* **Line**: `Then the TextArea "ReviewInput" is empty`
* **Error Type**: Referencing undefined state - empty

**Line Number**: 68

* **Line**: `And the reviews of the ProductPage "ProductDetailsPage" include "Excellent product"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 69

* **Line**: `Then the reviews of the ProductPage "ProductDetailsPage" include "Excellent product"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 73

* **Line**: `Then the Text "Reviews" includes "Excellent product"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 80

* **Line**: `Then the details of the ProductPage "ProductDetailsPage" are displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 85

* **Line**: `Then the items of the Cart "MyCart" include the ProductPage "ProductDetailsPage"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 89

* **Line**: `When I view the List "CartItems"`
* **Error Type**: Referencing undefined entity - List

**Line Number**: 90

* **Line**: `Then the List "CartItems" includes items from the Cart "MyCart"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include; Referencing undefined entity - List

**Line Number**: 96

* **Line**: `When I view the List "CartItems"`
* **Error Type**: Referencing undefined entity - List

**Line Number**: 97

* **Line**: `Then the List "CartItems" includes items`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include; Referencing undefined entity - List

**Line Number**: 106

* **Line**: `When I view the List "CartItems"`
* **Error Type**: Referencing undefined entity - List

**Line Number**: 107

* **Line**: `Then the List "CartItems" is empty`
* **Error Type**: Referencing undefined entity - List; Referencing undefined state - empty

## 3.bdd

**Line Number**: 59

* **Line**: `And the picture of the Product "MyProduct" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 65

* **Line**: `Then the Image of the Product "MyProduct" is shown`
* **Error Type**: Referencing undefined state - shown; Referencing undefined property - Image

**Line Number**: 66

* **Line**: `And the Text of the Product "MyProduct" name is "Ergonomic Office Chair"`
* **Error Type**: Referencing undefined property - Text; Invalid sentence structure - Product "MyProduct" name

**Line Number**: 67

* **Line**: `And the Text of the Product "MyProduct" price is "$350"`
* **Error Type**: Referencing undefined property - Text; Invalid sentence structure - Product "MyProduct" price

**Line Number**: 71

* **Line**: `When I click on the Image of the Product "MyProduct"`
* **Error Type**: Invalid sentence structure - Image of the Product "MyProduct"

**Line Number**: 77

* **Line**: `Then the Text of the Product "MyProduct" description is shown`
* **Error Type**: Referencing undefined property - Text; Invalid sentence structure - Product "MyProduct" description; Referencing undefined state - shown

**Line Number**: 78

* **Line**: `And the Review "MyReview" of the Product "MyProduct" is viewed`
* **Error Type**: Referencing undefined state - viewed; Invalid sentence structure - Review "MyReview" of the Product "MyProduct"

**Line Number**: 88

* **Line**: `Given the Button "Add to Cart" of the Product "MyProduct" is enabled`
* **Error Type**: Referencing undefined property - Button; Invalid sentence structure - Button "Add to Cart" of the Product "MyProduct"; Referencing undefined state - enabled

**Line Number**: 89

* **Line**: `Then the Cart "MyCart" totalItems is increased`
* **Error Type**: Invalid sentence structure - Cart "MyCart" totalItems; Referencing undefined state - increased

**Line Number**: 91

* **Line**: `Then the totalItems of the Cart "MyCart" is increased`
* **Error Type**: Referencing undefined state - increased

**Line Number**: 95

* **Line**: `Then the Text of the Cart "MyCart" totalItems is "1"`
* **Error Type**: Referencing undefined property - Text; Invalid sentence structure - Cart "MyCart" totalItems

**Line Number**: 105

* **Line**: `Given the Button "Checkout" of the Cart "MyCart" is enabled`
* **Error Type**: Referencing undefined property - Button; Invalid sentence structure - Button "Checkout" of the Cart "MyCart"; Referencing undefined state - enabled

## 4.bdd

**Line Number**: 46

* **Line**: `Given the ProductItem "ChairModelX" is shown on the CatalogPage "MyCatalog"`
* **Error Type**: Check if Entity is in another entity - is shown on; Use made-up keywords - shown

**Line Number**: 53

* **Line**: `Then the description of the ProductDetail "DetailChairModelX" is displayed,`
* **Error Type**: Invalid symbol in statement - ","

**Line Number**: 54

* **Line**: `And the reviews of the ProductDetail "DetailChairModelX" are displayed,`
* **Error Type**: Invalid symbol in statement - ","

**Line Number**: 55

* **Line**: `And the buy option of the ProductDetail "DetailChairModelX" is available`
* **Error Type**: Invalid property reference - buy option

**Line Number**: 67

* **Line**: `Then the ShoppingCart "MyCart" is updated`
* **Error Type**: Referencing undefined state - updated

**Line Number**: 68

* **Line**: `Then the items of the ShoppingCart "MyCart" include the ProductItem "ChairModelX"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 72

* **Line**: `Then the items of the ShoppingCart "MyCart" are listed,`
* **Error Type**: Invalid symbol in statement - ","; Referencing undefined state - listed

**Line Number**: 73

* **Line**: `And the totalCost of the ShoppingCart "MyCart" is updated`
* **Error Type**: Referencing undefined state - updated

**Line Number**: 76

* **Line**: `Given the ShoppingCart "MyCart" contains the ProductItem "ChairModelX"`
* **Error Type**: Check if Entity is in another entity - contains; Use made-up keywords - contains

**Line Number**: 80

* **Line**: `Then the items of the ShoppingCart "MyCart" are listed`
* **Error Type**: Referencing undefined state - listed

**Line Number**: 85

* **Line**: `Then the ShoppingCart "MyCart" is emptied`
* **Error Type**: Referencing undefined state - emptied

**Line Number**: 86

* **Line**: `Then the ShoppingCart "MyCart" is empty`
* **Error Type**: Referencing undefined state - empty

**Line Number**: 102

* **Line**: `Then the Wishlist "MyWishlist" is updated`
* **Error Type**: Referencing undefined state - updated

**Line Number**: 103

* **Line**: `Then the items of the Wishlist "MyWishlist" include the ProductItem "ChairModelX"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 107

* **Line**: `Then the items of the Wishlist "MyWishlist" are listed`
* **Error Type**: Referencing undefined state - listed

## 5.bdd

**Line Number**: 33

* **Line**: `When I viewProductDetails the ProductCatalog "MyProductCatalog" productName "ErgoChair"`
* **Error Type**: Invalid sentence structure - viewProductDetails the ProductCatalog "MyProductCatalog" productName "ErgoChair"

**Line Number**: 36

* **Line**: `When I click on the Product "ErgoChair"`
* **Error Type**: Referencing undefined entity - Product

**Line Number**: 54

* **Line**: `Then the ShoppingCart "MyShoppingCart" items includes "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes; Invalid sentence structure - ShoppingCart "MyShoppingCart" items includes "ErgoChair"

**Line Number**: 55

* **Line**: `Then the ShoppingCart "MyShoppingCart" items includes "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes; Invalid sentence structure - ShoppingCart "MyShoppingCart" items includes "ErgoChair"

**Line Number**: 58

* **Line**: `Then the List "items" contains "ErgoChair"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - contains; Use made-up keywords - contains

**Line Number**: 62

* **Line**: `Given the ShoppingCart "MyShoppingCart" items includes "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes; Invalid sentence structure - ShoppingCart "MyShoppingCart" items includes "ErgoChair"

**Line Number**: 72

* **Line**: `Then the ShoppingCart "MyShoppingCart" is void`
* **Error Type**: Referencing undefined state - void

**Line Number**: 76

* **Line**: `Then the List "items" is empty`
* **Error Type**: Referencing undefined entity - List; Referencing undefined state - empty

**Line Number**: 88

* **Line**: `Then the Wishlist "MyWishlist" savedItems includes "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes; Invalid sentence structure - Wishlist "MyWishlist" savedItems includes "ErgoChair"

**Line Number**: 89

* **Line**: `Then the Wishlist "MyWishlist" savedItems includes "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes; Invalid sentence structure - Wishlist "MyWishlist" savedItems includes "ErgoChair"

**Line Number**: 93

* **Line**: `Then the List "savedItems" contains "ErgoChair"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - contains; Use made-up keywords - contains

**Line Number**: 96

* **Line**: `Given the Wishlist "MyWishlist" savedItems includes "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes; Invalid sentence structure - Wishlist "MyWishlist" savedItems includes "ErgoChair"

**Line Number**: 105

* **Line**: `Then the ShoppingCart "MyShoppingCart" items includes "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes; Invalid sentence structure - ShoppingCart "MyShoppingCart" items includes "ErgoChair"

**Line Number**: 106

* **Line**: `Then the ShoppingCart "MyShoppingCart" items includes "ErgoChair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes; Invalid sentence structure - ShoppingCart "MyShoppingCart" items includes "ErgoChair"

**Line Number**: 110

* **Line**: `Then the List "items" contains "ErgoChair"`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - contains; Use made-up keywords - contains

## 6.bdd

**Line Number**: 56

* **Line**: `Then the totalItems of the Cart "MyCart" is increased`
* **Error Type**: Referencing undefined state - increased

**Line Number**: 73

* **Line**: `Then the Cart "MyCart" is empty`
* **Error Type**: Referencing undefined state - empty

**Line Number**: 76

* **Line**: `When I confirm the purchase`
* **Error Type**: Invalid sentence structure - confirm the purchase

**Line Number**: 90

* **Line**: `Then the totalItems of the Wishlist "MyWishlist" is increased`
* **Error Type**: Referencing undefined state - increased

**Line Number**: 108

* **Line**: `Then the allReviews of the ProductDetailsPage "MyProductDetailsPage" include "Great chair!"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

## 7.bdd

**Line Number**: 30

* **Line**: `Then the Text "Name" is "Ergonomic Chair"`
* **Error Type**: Setting an entity to a value instead of a state - Text "Name" is "Ergonomic Chair"

**Line Number**: 31

* **Line**: `And the Text "Price" is "$250"`
* **Error Type**: Setting an entity to a value instead of a state - Text "Price" is "$250"

**Line Number**: 32

* **Line**: `And the Image "Product Picture" is "ergonomic_chair.jpg"`
* **Error Type**: Setting an entity to a value instead of a state - Image "Product Picture" is "ergonomic_chair.jpg"

**Line Number**: 45

* **Line**: `Then the Text "Name" is "Ergonomic Chair"`
* **Error Type**: Setting an entity to a value instead of a state - Text "Name" is "Ergonomic Chair"

**Line Number**: 46

* **Line**: `And the Text "Price" is "$250"`
* **Error Type**: Setting an entity to a value instead of a state - Text "Price" is "$250"

**Line Number**: 51

* **Line**: `Given the Product "MyProduct" is viewed`
* **Error Type**: Referencing undefined state - viewed

**Line Number**: 61

* **Line**: `Then the items of the Cart "MyCart" include "Ergonomic Chair"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 62

* **Line**: `And the total of the Cart "MyCart" is updated`
* **Error Type**: Referencing undefined state - updated

**Line Number**: 66

* **Line**: `Then the Text "Items" includes "Ergonomic Chair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 67

* **Line**: `And the Text "Total" is updated`
* **Error Type**: Referencing undefined state - updated

**Line Number**: 70

* **Line**: `Given the items of the Cart "MyCart" include "Ergonomic Chair"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 75

* **Line**: `Then the Text "Items" includes "Ergonomic Chair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes

**Line Number**: 76

* **Line**: `And the Text "Total" is "$250"`
* **Error Type**: Setting an entity to a value instead of a state - Text "Total" is "$250"

**Line Number**: 82

* **Line**: `Then the Cart "MyCart" is void`
* **Error Type**: Referencing undefined state - void

**Line Number**: 87

* **Line**: `Then the Text "Message" is "Checkout complete"`
* **Error Type**: Setting an entity to a value instead of a state - Text "Message" is "Checkout complete"

**Line Number**: 90

* **Line**: `Given the Product "MyProduct" is viewed`
* **Error Type**: Referencing undefined state - viewed

**Line Number**: 100

* **Line**: `Then the items of the Wishlist "MyWishlist" include "Ergonomic Chair"`
* **Error Type**: Check if Entity is in another entity - include; Use made-up keywords - include

**Line Number**: 104

* **Line**: `Then the Text "Items" includes "Ergonomic Chair"`
* **Error Type**: Check if Entity is in another entity - includes; Use made-up keywords - includes

## 8.bdd

**Line Number**: 22

* **Line**: `Given the picture of the Product "MyProduct" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 23

* **Line**: `And the name of the Product "MyProduct" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 24

* **Line**: `And the price of the Product "MyProduct" is displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 33

* **Line**: `Then the details of the Product "MyProduct" are displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 34

* **Line**: `And the reviews of the Product "MyProduct" are displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 35

* **Line**: `Then the details of the Product "MyProduct" are displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 36

* **Line**: `And the reviews of the Product "MyProduct" are displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 40

* **Line**: `Then the TextField "Details" shows details of the Product "MyProduct"`
* **Error Type**: Invalid sentence structure - TextField "Details" shows details of the Product "MyProduct"

**Line Number**: 41

* **Line**: `And the TextField "Reviews" shows reviews of the Product "MyProduct"`
* **Error Type**: Invalid sentence structure - TextField "Reviews" shows reviews of the Product "MyProduct"

**Line Number**: 80

* **Line**: `Given the items of the ShoppingCart "MyShoppingCart" are displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 84

* **Line**: `Then the Grid "CartItems" shows items in the ShoppingCart "MyShoppingCart"`
* **Error Type**: Invalid sentence structure - Grid "CartItems" shows items in the ShoppingCart "MyShoppingCart"

**Line Number**: 97

* **Line**: `Given the items of the Wishlist "MyWishlist" are displayed`
* **Error Type**: Referencing undefined state - displayed

**Line Number**: 101

* **Line**: `Then the Grid "WishlistItems" shows items in the Wishlist "MyWishlist"`
* **Error Type**: Invalid sentence structure - Grid "WishlistItems" shows items in the Wishlist "MyWishlist"

## 9.bdd

**Line Number**: 4

* **Line**: `actions: click, add to cart, add to wishlist`
* **Error Type**: Invalid use of preposition in action definition - add to cart; Invalid use of preposition in action definition - add to wishlist

**Line Number**: 26

* **Line**: `Then the Image "Product Picture" is displayed,`
* **Error Type**: Invalid symbol in statement - ","

**Line Number**: 27

* **Line**: `And the Label "Product Name" is displayed,`
* **Error Type**: Invalid symbol in statement - ","

**Line Number**: 38

* **Line**: `Then the Text "Product Reviews" is displayed,`
* **Error Type**: Invalid symbol in statement - ","

**Line Number**: 39

* **Line**: `And the Button "Add to Cart" is displayed,`
* **Error Type**: Invalid symbol in statement - ","

**Line Number**: 77

* **Line**: `Given the Cart "MyCart" containsItems`
* **Error Type**: Missing keyword - 'is'

**Line Number**: 86

* **Line**: `Then the BrowserWindow "Checkout Page" is displayed,`
* **Error Type**: Invalid symbol in statement - ","

## 10.bdd

**Line Number**: 51

* **Line**: `Then the items of the Cart "MyCart" are increased`
* **Error Type**: Referencing undefined state - increased

**Line Number**: 55

* **Line**: `Then the List "Items" in the Cart "MyCart" is increased`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - in; Referencing undefined state - increased

**Line Number**: 58

* **Line**: `Given the items of the Cart "MyCart" are not empty`
* **Error Type**: Referencing undefined state - empty

**Line Number**: 62

* **Line**: `Then the List "Items" in the Cart "MyCart" is not empty`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - in; Referencing undefined state - empty

**Line Number**: 68

* **Line**: `Then the Cart "MyCart" is empty`
* **Error Type**: Referencing undefined state - empty

**Line Number**: 72

* **Line**: `Then the List "Items" in the Cart "MyCart" is empty`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - in; Referencing undefined state - empty

**Line Number**: 85

* **Line**: `Then the items of the Wishlist "MyWishlist" are increased`
* **Error Type**: Referencing undefined state - increased

**Line Number**: 89

* **Line**: `Then the List "Items" in the Wishlist "MyWishlist" is increased`
* **Error Type**: Referencing undefined entity - List; Check if Entity is in another entity - in; Referencing undefined state - increased
