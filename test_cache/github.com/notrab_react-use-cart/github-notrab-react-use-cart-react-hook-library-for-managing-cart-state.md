---
title: GitHub - notrab/react-use-cart: React hook library for managing cart state
description: React hook library for managing cart state. Contribute to notrab/react-use-cart development by creating an account on GitHub.
url: https://github.com/notrab/react-use-cart
timestamp: 2025-01-20T15:31:29.973Z
domain: github.com
path: notrab_react-use-cart
---

# GitHub - notrab/react-use-cart: React hook library for managing cart state


React hook library for managing cart state. Contribute to notrab/react-use-cart development by creating an account on GitHub.


## Content

react-use-cart
--------------

[](https://github.com/notrab/react-use-cart?screenshot=true#--react-use-cart)

🛒 A lightweight shopping cart hook for React, Next.js, and Gatsby

[![Image 43: Version](https://camo.githubusercontent.com/3d6092886ed8652777d4feefea70b9f9b3455c2ccd80ed5eaf5ce9d239971285/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d7573652d636172742e737667)](https://npmjs.org/package/react-use-cart)[![Image 44: Downloads/week](https://camo.githubusercontent.com/d4035804119a91adb9e044eec8c8ab44812f5be9169bf26815834ab0291f4605/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64772f72656163742d7573652d636172742e737667)](https://npmjs.org/package/react-use-cart)[![Image 45: License](https://camo.githubusercontent.com/d2213a72c03a1dd955c88555bac2aa3129f696489fc7c73421db4b43569dabc5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f72656163742d7573652d636172742e737667)](https://github.com/notrab/react-use-cart/blob/main/package.json)[![Image 46: Forks on GitHub](https://camo.githubusercontent.com/0d2b068407afff9f7127f49572aad00339f103d51fb952f6478de78fb6b3de63/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f6e6f747261622f72656163742d7573652d63617274)](https://github.com/notrab/react-use-cart/network/members)[![Image 47: Forks on GitHub](https://camo.githubusercontent.com/1043057948cc38260b537b7492245dc929c25d57bcc20987982d7783cac8b460/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6e6f747261622f72656163742d7573652d63617274)](https://github.com/notrab/react-use-cart/stargazers)[![Image 48: minified + gzip size](https://camo.githubusercontent.com/40a3a43400ed7ab663e3bac1a9a7451d2d0d75042699167f39c290c2758a7808/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d7573652d63617274)](https://camo.githubusercontent.com/40a3a43400ed7ab663e3bac1a9a7451d2d0d75042699167f39c290c2758a7808/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d7573652d63617274) [![Image 49: Contributors](https://camo.githubusercontent.com/407e3a50d6d1fba38730d0d10d736d8737b07a779a786fc4728c3aca2bcefa63/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616c6c5f636f6e7472696275746f72732d342d6f72616e67652e737667)](https://camo.githubusercontent.com/407e3a50d6d1fba38730d0d10d736d8737b07a779a786fc4728c3aca2bcefa63/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616c6c5f636f6e7472696275746f72732d342d6f72616e67652e737667)

Why?
----

[](https://github.com/notrab/react-use-cart?screenshot=true#why)

*   [![Image 50: Bundle size](https://camo.githubusercontent.com/40a3a43400ed7ab663e3bac1a9a7451d2d0d75042699167f39c290c2758a7808/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d7573652d63617274)](https://camo.githubusercontent.com/40a3a43400ed7ab663e3bac1a9a7451d2d0d75042699167f39c290c2758a7808/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d7573652d63617274)
*   **No dependencies**
*   💳 Not tied to any payment gateway, or checkout - create your own!
*   🔥 Persistent carts with local storage, or your own adapter
*   ⭐️ Supports multiples carts per page
*   🛒 Flexible cart item schema
*   🥞 Works with Next, Gatsby, React
*   ♻️ Trigger your own side effects with cart handlers (on item add, update, remove)
*   🛠 Built with TypeScript
*   ✅ Fully tested
*   🌮 Used by [Dines](https://dines.co.uk/?ref=react-use-cart)

Quick Start
-----------

[](https://github.com/notrab/react-use-cart?screenshot=true#quick-start)

[Demo](https://codesandbox.io/s/react-use-cart-3c7vm)

import { CartProvider, useCart } from "react-use-cart";

function Page() {
  const { addItem } \= useCart();

  const products \= \[
    {
      id: 1,
      name: "Malm",
      price: 9900,
      quantity: 1
    },
    {
      id: 2,
      name: "Nordli",
      price: 16500,
      quantity: 5
    },
    {
      id: 3,
      name: "Kullen",
      price: 4500,
      quantity: 1
    },
  \];

  return (
    <div\>
      {products.map((p) \=\> (
        <div key\={p.id}\>
          <button onClick\={() \=\> addItem(p)}\>Add to cart</button\>
        </div\>
      ))}
    </div\>
  );
}

function Cart() {
  const {
    isEmpty,
    totalUniqueItems,
    items,
    updateItemQuantity,
    removeItem,
  } \= useCart();

  if (isEmpty) return <p\>Your cart is empty</p\>;

  return (
    <\>
      <h1\>Cart ({totalUniqueItems})</h1\>

      <ul\>
        {items.map((item) \=\> (
          <li key\={item.id}\>
            {item.quantity} x {item.name} &mdash;
            <button
              onClick\={() \=\> updateItemQuantity(item.id, (item.quantity ?? 0) \- 1)}
            \>
              -
            </button\>
            <button
              onClick\={() \=\> updateItemQuantity(item.id, (item.quantity ?? 0) + 1)}
            \>
              +
            </button\>
            <button onClick\={() \=\> removeItem(item.id)}\>&times;</button\>
          </li\>
        ))}
      </ul\>
    </\>
  );
}

function App() {
  return (
    <CartProvider\>
      <Page /\>
      <Cart /\>
    </CartProvider\>
  );
}

Install
-------

[](https://github.com/notrab/react-use-cart?screenshot=true#install)

npm install react-use-cart # yarn add react-use-cart

`CartProvider`
--------------

[](https://github.com/notrab/react-use-cart?screenshot=true#cartprovider)

You will need to wrap your application with the `CartProvider` component so that the `useCart` hook can access the cart state.

Carts are persisted across visits using `localStorage`, unless you specify your own `storage` adapter.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage)

import React from "react";
import ReactDOM from "react-dom";
import { CartProvider } from "react-use-cart";

ReactDOM.render(
  <CartProvider\>{/\* render app/cart here \*/}</CartProvider\>,
  document.getElementById("root")
);

#### Props

[](https://github.com/notrab/react-use-cart?screenshot=true#props)

| Prop | Required | Description |
| --- | --- | --- |
| `id` | _No_ | `id` for your cart to enable automatic cart retrieval via `window.localStorage`. If you pass a `id` then you can use multiple instances of `CartProvider`. |
| `onSetItems` | _No_ | Triggered only when `setItems` invoked. |
| `onItemAdd` | _No_ | Triggered on items added to your cart, unless the item already exists, then `onItemUpdate` will be invoked. |
| `onItemUpdate` | _No_ | Triggered on items updated in your cart, unless you are setting the quantity to `0`, then `onItemRemove` will be invoked. |
| `onItemRemove` | _No_ | Triggered on items removed from your cart. |
| `onEmptyCart` | _No_ | Triggered on empty cart. |
| `storage` | _No_ | Must return `[getter, setter]`. |
| `metadata` | _No_ | Custom global state on the cart. Stored inside of `metadata`. |

`useCart`
---------

[](https://github.com/notrab/react-use-cart?screenshot=true#usecart)

The `useCart` hook exposes all the getter/setters for your cart state.

### `setItems(items)`

[](https://github.com/notrab/react-use-cart?screenshot=true#setitemsitems)

The `setItems` method should be used to set all items in the cart. This will overwrite any existing cart items. A `quantity` default of 1 will be set for an item implicitly if no `quantity` is specified.

#### Args

[](https://github.com/notrab/react-use-cart?screenshot=true#args)

*   `items[]` (**Required**): An array of cart item object. You must provide an `id` and `price` value for new items that you add to cart.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-1)

import { useCart } from "react-use-cart";

const { setItems } \= useCart();

const products \= \[
  {
    id: "ckb64v21u000001ksgw2s42ku",
    name: "Fresh Foam 1080v9",
    brand: "New Balance",
    color: "Neon Emerald with Dark Neptune",
    size: "US 10",
    width: "B - Standard",
    sku: "W1080LN9",
    price: 15000,
  },
  {
    id: "cjld2cjxh0000qzrmn831i7rn",
    name: "Fresh Foam 1080v9",
    brand: "New Balance",
    color: "Neon Emerald with Dark Neptune",
    size: "US 9",
    width: "B - Standard",
    sku: "W1080LN9",
    price: 15000,
  },
\];

setItems(products);

### `addItem(item, quantity)`

[](https://github.com/notrab/react-use-cart?screenshot=true#additemitem-quantity)

The `addItem` method should be used to add items to the cart.

#### Args

[](https://github.com/notrab/react-use-cart?screenshot=true#args-1)

*   `item` (**Required**): An object that represents your cart item. You must provide an `id` and `price` value for new items that you add to cart.
*   `quantity` (_optional_, **default**: `1`): The amount of items you want to add.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-2)

import { useCart } from "react-use-cart";

const { addItem } \= useCart();

const product \= {
  id: "cjld2cjxh0000qzrmn831i7rn",
  name: "Fresh Foam 1080v9",
  brand: "New Balance",
  color: "Neon Emerald with Dark Neptune",
  size: "US 9",
  width: "B - Standard",
  sku: "W1080LN9",
  price: 15000,
};

addItem(product, 2);

### `updateItem(itemId, data)`

[](https://github.com/notrab/react-use-cart?screenshot=true#updateitemitemid-data)

The `updateItem` method should be used to update items in the cart.

#### Args

[](https://github.com/notrab/react-use-cart?screenshot=true#args-2)

*   `itemId` (**Required**): The cart item `id` you want to update.
*   `data` (**Required**): The updated cart item object.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-3)

import { useCart } from "react-use-cart";

const { updateItem } \= useCart();

updateItem("cjld2cjxh0000qzrmn831i7rn", {
  size: "UK 10",
});

### `updateItemQuantity(itemId, quantity)`

[](https://github.com/notrab/react-use-cart?screenshot=true#updateitemquantityitemid-quantity)

The `updateItemQuantity` method should be used to update an items `quantity` value.

#### Args

[](https://github.com/notrab/react-use-cart?screenshot=true#args-3)

*   `itemId` (**Required**): The cart item `id` you want to update.
*   `quantity` (**Required**): The updated cart item quantity.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-4)

import { useCart } from "react-use-cart";

const { updateItemQuantity } \= useCart();

updateItemQuantity("cjld2cjxh0000qzrmn831i7rn", 1);

### `removeItem(itemId)`

[](https://github.com/notrab/react-use-cart?screenshot=true#removeitemitemid)

The `removeItem` method should be used to remove an item from the cart.

#### Args

[](https://github.com/notrab/react-use-cart?screenshot=true#args-4)

*   `itemId` (**Required**): The cart item `id` you want to remove.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-5)

import { useCart } from "react-use-cart";

const { removeItem } \= useCart();

removeItem("cjld2cjxh0000qzrmn831i7rn");

### `emptyCart()`

[](https://github.com/notrab/react-use-cart?screenshot=true#emptycart)

The `emptyCart()` method should be used to remove all cart items, and resetting cart totals to the default `0` values.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-6)

import { useCart } from "react-use-cart";

const { emptyCart } \= useCart();

emptyCart();

### `clearCartMetadata()`

[](https://github.com/notrab/react-use-cart?screenshot=true#clearcartmetadata)

The `clearCartMetadata()` will reset the `metadata` to an empty object.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-7)

import { useCart } from "react-use-cart";

const { clearCartMetadata } \= useCart();

clearCartMetadata();

### `setCartMetadata(object)`

[](https://github.com/notrab/react-use-cart?screenshot=true#setcartmetadataobject)

The `setCartMetadata()` will replace the `metadata` object on the cart. You must pass it an object.

#### Args

[](https://github.com/notrab/react-use-cart?screenshot=true#args-5)

*   `object`: A object with key/value pairs. The key being a string.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-8)

import { useCart } from "react-use-cart";

const { setCartMetadata } \= useCart();

setCartMetadata({ notes: "This is the only metadata" });

### `updateCartMetadata(object)`

[](https://github.com/notrab/react-use-cart?screenshot=true#updatecartmetadataobject)

The `updateCartMetadata()` will update the `metadata` object on the cart. You must pass it an object. This will merge the passed object with the existing metadata.

#### Args

[](https://github.com/notrab/react-use-cart?screenshot=true#args-6)

*   `object`: A object with key/value pairs. The key being a string.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-9)

import { useCart } from "react-use-cart";

const { updateCartMetadata } \= useCart();

updateCartMetadata({ notes: "Leave in shed" });

### `items = []`

[](https://github.com/notrab/react-use-cart?screenshot=true#items--)

This will return the current cart items in an array.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-10)

import { useCart } from "react-use-cart";

const { items } \= useCart();

### `isEmpty = false`

[](https://github.com/notrab/react-use-cart?screenshot=true#isempty--false)

A quick and easy way to check if the cart is empty. Returned as a boolean.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-11)

import { useCart } from "react-use-cart";

const { isEmpty } \= useCart();

### `getItem(itemId)`

[](https://github.com/notrab/react-use-cart?screenshot=true#getitemitemid)

Get a specific cart item by `id`. Returns the item object.

#### Args

[](https://github.com/notrab/react-use-cart?screenshot=true#args-7)

*   `itemId` (**Required**): The `id` of the item you're fetching.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-12)

import { useCart } from "react-use-cart";

const { getItem } \= useCart();

const myItem \= getItem("cjld2cjxh0000qzrmn831i7rn");

### `inCart(itemId)`

[](https://github.com/notrab/react-use-cart?screenshot=true#incartitemid)

Quickly check if an item is in the cart. Returned as a boolean.

#### Args

[](https://github.com/notrab/react-use-cart?screenshot=true#args-8)

*   `itemId` (**Required**): The `id` of the item you're looking for.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-13)

import { useCart } from "react-use-cart";

const { inCart } \= useCart();

inCart("cjld2cjxh0000qzrmn831i7rn") ? "In cart" : "Not in cart";

### `totalItems = 0`

[](https://github.com/notrab/react-use-cart?screenshot=true#totalitems--0)

This returns the totaly quantity of items in the cart as an integer.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-14)

import { useCart } from "react-use-cart";

const { totalItems } \= useCart();

### `totalUniqueItems = 0`

[](https://github.com/notrab/react-use-cart?screenshot=true#totaluniqueitems--0)

This returns the total unique items in the cart as an integer.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-15)

import { useCart } from "react-use-cart";

const { totalUniqueItems } \= useCart();

### `cartTotal = 0`

[](https://github.com/notrab/react-use-cart?screenshot=true#carttotal--0)

This returns the total value of all items in the cart.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-16)

import { useCart } from "react-use-cart";

const { cartTotal } \= useCart();

### `metadata = {}`

[](https://github.com/notrab/react-use-cart?screenshot=true#metadata--)

This returns the metadata set with `updateCartMetadata`. This is useful for storing additional cart, or checkout values.

#### Usage

[](https://github.com/notrab/react-use-cart?screenshot=true#usage-17)

import { useCart } from "react-use-cart";

const { metadata } \= useCart();

Contributors ✨
--------------

[](https://github.com/notrab/react-use-cart?screenshot=true#contributors-)

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Metadata

```json
{
  "title": "GitHub - notrab/react-use-cart: React hook library for managing cart state",
  "description": "React hook library for managing cart state. Contribute to notrab/react-use-cart development by creating an account on GitHub.",
  "url": "https://github.com/notrab/react-use-cart?screenshot=true",
  "content": "react-use-cart\n--------------\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#--react-use-cart)\n\n🛒 A lightweight shopping cart hook for React, Next.js, and Gatsby\n\n[![Image 43: Version](https://camo.githubusercontent.com/3d6092886ed8652777d4feefea70b9f9b3455c2ccd80ed5eaf5ce9d239971285/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d7573652d636172742e737667)](https://npmjs.org/package/react-use-cart)[![Image 44: Downloads/week](https://camo.githubusercontent.com/d4035804119a91adb9e044eec8c8ab44812f5be9169bf26815834ab0291f4605/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64772f72656163742d7573652d636172742e737667)](https://npmjs.org/package/react-use-cart)[![Image 45: License](https://camo.githubusercontent.com/d2213a72c03a1dd955c88555bac2aa3129f696489fc7c73421db4b43569dabc5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f72656163742d7573652d636172742e737667)](https://github.com/notrab/react-use-cart/blob/main/package.json)[![Image 46: Forks on GitHub](https://camo.githubusercontent.com/0d2b068407afff9f7127f49572aad00339f103d51fb952f6478de78fb6b3de63/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f6e6f747261622f72656163742d7573652d63617274)](https://github.com/notrab/react-use-cart/network/members)[![Image 47: Forks on GitHub](https://camo.githubusercontent.com/1043057948cc38260b537b7492245dc929c25d57bcc20987982d7783cac8b460/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6e6f747261622f72656163742d7573652d63617274)](https://github.com/notrab/react-use-cart/stargazers)[![Image 48: minified + gzip size](https://camo.githubusercontent.com/40a3a43400ed7ab663e3bac1a9a7451d2d0d75042699167f39c290c2758a7808/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d7573652d63617274)](https://camo.githubusercontent.com/40a3a43400ed7ab663e3bac1a9a7451d2d0d75042699167f39c290c2758a7808/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d7573652d63617274) [![Image 49: Contributors](https://camo.githubusercontent.com/407e3a50d6d1fba38730d0d10d736d8737b07a779a786fc4728c3aca2bcefa63/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616c6c5f636f6e7472696275746f72732d342d6f72616e67652e737667)](https://camo.githubusercontent.com/407e3a50d6d1fba38730d0d10d736d8737b07a779a786fc4728c3aca2bcefa63/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616c6c5f636f6e7472696275746f72732d342d6f72616e67652e737667)\n\nWhy?\n----\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#why)\n\n*   [![Image 50: Bundle size](https://camo.githubusercontent.com/40a3a43400ed7ab663e3bac1a9a7451d2d0d75042699167f39c290c2758a7808/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d7573652d63617274)](https://camo.githubusercontent.com/40a3a43400ed7ab663e3bac1a9a7451d2d0d75042699167f39c290c2758a7808/68747470733a2f2f62616467656e2e6e65742f62756e646c6570686f6269612f6d696e7a69702f72656163742d7573652d63617274)\n*   **No dependencies**\n*   💳 Not tied to any payment gateway, or checkout - create your own!\n*   🔥 Persistent carts with local storage, or your own adapter\n*   ⭐️ Supports multiples carts per page\n*   🛒 Flexible cart item schema\n*   🥞 Works with Next, Gatsby, React\n*   ♻️ Trigger your own side effects with cart handlers (on item add, update, remove)\n*   🛠 Built with TypeScript\n*   ✅ Fully tested\n*   🌮 Used by [Dines](https://dines.co.uk/?ref=react-use-cart)\n\nQuick Start\n-----------\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#quick-start)\n\n[Demo](https://codesandbox.io/s/react-use-cart-3c7vm)\n\nimport { CartProvider, useCart } from \"react-use-cart\";\n\nfunction Page() {\n  const { addItem } \\= useCart();\n\n  const products \\= \\[\n    {\n      id: 1,\n      name: \"Malm\",\n      price: 9900,\n      quantity: 1\n    },\n    {\n      id: 2,\n      name: \"Nordli\",\n      price: 16500,\n      quantity: 5\n    },\n    {\n      id: 3,\n      name: \"Kullen\",\n      price: 4500,\n      quantity: 1\n    },\n  \\];\n\n  return (\n    <div\\>\n      {products.map((p) \\=\\> (\n        <div key\\={p.id}\\>\n          <button onClick\\={() \\=\\> addItem(p)}\\>Add to cart</button\\>\n        </div\\>\n      ))}\n    </div\\>\n  );\n}\n\nfunction Cart() {\n  const {\n    isEmpty,\n    totalUniqueItems,\n    items,\n    updateItemQuantity,\n    removeItem,\n  } \\= useCart();\n\n  if (isEmpty) return <p\\>Your cart is empty</p\\>;\n\n  return (\n    <\\>\n      <h1\\>Cart ({totalUniqueItems})</h1\\>\n\n      <ul\\>\n        {items.map((item) \\=\\> (\n          <li key\\={item.id}\\>\n            {item.quantity} x {item.name} &mdash;\n            <button\n              onClick\\={() \\=\\> updateItemQuantity(item.id, (item.quantity ?? 0) \\- 1)}\n            \\>\n              -\n            </button\\>\n            <button\n              onClick\\={() \\=\\> updateItemQuantity(item.id, (item.quantity ?? 0) + 1)}\n            \\>\n              +\n            </button\\>\n            <button onClick\\={() \\=\\> removeItem(item.id)}\\>&times;</button\\>\n          </li\\>\n        ))}\n      </ul\\>\n    </\\>\n  );\n}\n\nfunction App() {\n  return (\n    <CartProvider\\>\n      <Page /\\>\n      <Cart /\\>\n    </CartProvider\\>\n  );\n}\n\nInstall\n-------\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#install)\n\nnpm install react-use-cart # yarn add react-use-cart\n\n`CartProvider`\n--------------\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#cartprovider)\n\nYou will need to wrap your application with the `CartProvider` component so that the `useCart` hook can access the cart state.\n\nCarts are persisted across visits using `localStorage`, unless you specify your own `storage` adapter.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage)\n\nimport React from \"react\";\nimport ReactDOM from \"react-dom\";\nimport { CartProvider } from \"react-use-cart\";\n\nReactDOM.render(\n  <CartProvider\\>{/\\* render app/cart here \\*/}</CartProvider\\>,\n  document.getElementById(\"root\")\n);\n\n#### Props\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#props)\n\n| Prop | Required | Description |\n| --- | --- | --- |\n| `id` | _No_ | `id` for your cart to enable automatic cart retrieval via `window.localStorage`. If you pass a `id` then you can use multiple instances of `CartProvider`. |\n| `onSetItems` | _No_ | Triggered only when `setItems` invoked. |\n| `onItemAdd` | _No_ | Triggered on items added to your cart, unless the item already exists, then `onItemUpdate` will be invoked. |\n| `onItemUpdate` | _No_ | Triggered on items updated in your cart, unless you are setting the quantity to `0`, then `onItemRemove` will be invoked. |\n| `onItemRemove` | _No_ | Triggered on items removed from your cart. |\n| `onEmptyCart` | _No_ | Triggered on empty cart. |\n| `storage` | _No_ | Must return `[getter, setter]`. |\n| `metadata` | _No_ | Custom global state on the cart. Stored inside of `metadata`. |\n\n`useCart`\n---------\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usecart)\n\nThe `useCart` hook exposes all the getter/setters for your cart state.\n\n### `setItems(items)`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#setitemsitems)\n\nThe `setItems` method should be used to set all items in the cart. This will overwrite any existing cart items. A `quantity` default of 1 will be set for an item implicitly if no `quantity` is specified.\n\n#### Args\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#args)\n\n*   `items[]` (**Required**): An array of cart item object. You must provide an `id` and `price` value for new items that you add to cart.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-1)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { setItems } \\= useCart();\n\nconst products \\= \\[\n  {\n    id: \"ckb64v21u000001ksgw2s42ku\",\n    name: \"Fresh Foam 1080v9\",\n    brand: \"New Balance\",\n    color: \"Neon Emerald with Dark Neptune\",\n    size: \"US 10\",\n    width: \"B - Standard\",\n    sku: \"W1080LN9\",\n    price: 15000,\n  },\n  {\n    id: \"cjld2cjxh0000qzrmn831i7rn\",\n    name: \"Fresh Foam 1080v9\",\n    brand: \"New Balance\",\n    color: \"Neon Emerald with Dark Neptune\",\n    size: \"US 9\",\n    width: \"B - Standard\",\n    sku: \"W1080LN9\",\n    price: 15000,\n  },\n\\];\n\nsetItems(products);\n\n### `addItem(item, quantity)`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#additemitem-quantity)\n\nThe `addItem` method should be used to add items to the cart.\n\n#### Args\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#args-1)\n\n*   `item` (**Required**): An object that represents your cart item. You must provide an `id` and `price` value for new items that you add to cart.\n*   `quantity` (_optional_, **default**: `1`): The amount of items you want to add.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-2)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { addItem } \\= useCart();\n\nconst product \\= {\n  id: \"cjld2cjxh0000qzrmn831i7rn\",\n  name: \"Fresh Foam 1080v9\",\n  brand: \"New Balance\",\n  color: \"Neon Emerald with Dark Neptune\",\n  size: \"US 9\",\n  width: \"B - Standard\",\n  sku: \"W1080LN9\",\n  price: 15000,\n};\n\naddItem(product, 2);\n\n### `updateItem(itemId, data)`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#updateitemitemid-data)\n\nThe `updateItem` method should be used to update items in the cart.\n\n#### Args\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#args-2)\n\n*   `itemId` (**Required**): The cart item `id` you want to update.\n*   `data` (**Required**): The updated cart item object.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-3)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { updateItem } \\= useCart();\n\nupdateItem(\"cjld2cjxh0000qzrmn831i7rn\", {\n  size: \"UK 10\",\n});\n\n### `updateItemQuantity(itemId, quantity)`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#updateitemquantityitemid-quantity)\n\nThe `updateItemQuantity` method should be used to update an items `quantity` value.\n\n#### Args\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#args-3)\n\n*   `itemId` (**Required**): The cart item `id` you want to update.\n*   `quantity` (**Required**): The updated cart item quantity.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-4)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { updateItemQuantity } \\= useCart();\n\nupdateItemQuantity(\"cjld2cjxh0000qzrmn831i7rn\", 1);\n\n### `removeItem(itemId)`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#removeitemitemid)\n\nThe `removeItem` method should be used to remove an item from the cart.\n\n#### Args\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#args-4)\n\n*   `itemId` (**Required**): The cart item `id` you want to remove.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-5)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { removeItem } \\= useCart();\n\nremoveItem(\"cjld2cjxh0000qzrmn831i7rn\");\n\n### `emptyCart()`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#emptycart)\n\nThe `emptyCart()` method should be used to remove all cart items, and resetting cart totals to the default `0` values.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-6)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { emptyCart } \\= useCart();\n\nemptyCart();\n\n### `clearCartMetadata()`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#clearcartmetadata)\n\nThe `clearCartMetadata()` will reset the `metadata` to an empty object.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-7)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { clearCartMetadata } \\= useCart();\n\nclearCartMetadata();\n\n### `setCartMetadata(object)`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#setcartmetadataobject)\n\nThe `setCartMetadata()` will replace the `metadata` object on the cart. You must pass it an object.\n\n#### Args\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#args-5)\n\n*   `object`: A object with key/value pairs. The key being a string.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-8)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { setCartMetadata } \\= useCart();\n\nsetCartMetadata({ notes: \"This is the only metadata\" });\n\n### `updateCartMetadata(object)`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#updatecartmetadataobject)\n\nThe `updateCartMetadata()` will update the `metadata` object on the cart. You must pass it an object. This will merge the passed object with the existing metadata.\n\n#### Args\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#args-6)\n\n*   `object`: A object with key/value pairs. The key being a string.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-9)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { updateCartMetadata } \\= useCart();\n\nupdateCartMetadata({ notes: \"Leave in shed\" });\n\n### `items = []`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#items--)\n\nThis will return the current cart items in an array.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-10)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { items } \\= useCart();\n\n### `isEmpty = false`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#isempty--false)\n\nA quick and easy way to check if the cart is empty. Returned as a boolean.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-11)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { isEmpty } \\= useCart();\n\n### `getItem(itemId)`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#getitemitemid)\n\nGet a specific cart item by `id`. Returns the item object.\n\n#### Args\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#args-7)\n\n*   `itemId` (**Required**): The `id` of the item you're fetching.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-12)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { getItem } \\= useCart();\n\nconst myItem \\= getItem(\"cjld2cjxh0000qzrmn831i7rn\");\n\n### `inCart(itemId)`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#incartitemid)\n\nQuickly check if an item is in the cart. Returned as a boolean.\n\n#### Args\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#args-8)\n\n*   `itemId` (**Required**): The `id` of the item you're looking for.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-13)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { inCart } \\= useCart();\n\ninCart(\"cjld2cjxh0000qzrmn831i7rn\") ? \"In cart\" : \"Not in cart\";\n\n### `totalItems = 0`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#totalitems--0)\n\nThis returns the totaly quantity of items in the cart as an integer.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-14)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { totalItems } \\= useCart();\n\n### `totalUniqueItems = 0`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#totaluniqueitems--0)\n\nThis returns the total unique items in the cart as an integer.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-15)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { totalUniqueItems } \\= useCart();\n\n### `cartTotal = 0`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#carttotal--0)\n\nThis returns the total value of all items in the cart.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-16)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { cartTotal } \\= useCart();\n\n### `metadata = {}`\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#metadata--)\n\nThis returns the metadata set with `updateCartMetadata`. This is useful for storing additional cart, or checkout values.\n\n#### Usage\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#usage-17)\n\nimport { useCart } from \"react-use-cart\";\n\nconst { metadata } \\= useCart();\n\nContributors ✨\n--------------\n\n[](https://github.com/notrab/react-use-cart?screenshot=true#contributors-)\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!",
  "usage": {
    "tokens": 4867
  }
}
```
