---
title: Creating Bento Grid Layouts
description: How to create Bento Grid Layouts with Tailwind CSS and React
url: https://www.julienthibeaut.xyz/blog/create-bento-grid-layouts
timestamp: 2025-01-20T15:43:28.780Z
domain: www.julienthibeaut.xyz
path: blog_create-bento-grid-layouts
---

# Creating Bento Grid Layouts


How to create Bento Grid Layouts with Tailwind CSS and React


## Content

As you browse the web, you've likely come across this type of layout before. It can be called a bento grid layout, bento box layout, or bento box grid. This layout takes its inspiration from the traditional Japanese bento box. 🍱

Bento grids are super versatile, perfect for displaying all sorts of content like images, text, mixed media, and more. They showcase loads of content in a compact and organized way, making your website or app look clean and engaging.

Trends and examples
-------------------

Some people say that it start with Windows 8 and the [metro design](https://en.wikipedia.org/wiki/Metro_(design_language)).

However, the true trendsetter in recent times is Apple. They've been using bento grid layouts extensively in their video presentations and on their website, making it a popular design choice.

![Image 8: Apple 14](https://ibelick.com/blog/bento-box-apple14.jpg)

[Apple 14](https://www.apple.com/iphone-14/)

![Image 9: Linear](https://ibelick.com/blog/bento-box-linear.jpg)

[Linear](https://linear.app/)

![Image 10: Literal](https://ibelick.com/blog/bento-box-literal.jpg)

[Literal](https://literal.club/)

If you're looking for design inspiration you can check [bentogrids](https://bentogrids.com/). It's a curated collection showcasing the best bento grid layouts on the web.

Building a Bento Grid: Step-by-Step Code
----------------------------------------

There are countless ways to create bento grid layouts, and today, I'll show you some of them using Tailwind CSS and React.

_Note that the code examples provided are not responsive by default, as they are intended to be easily viewed on mobile devices too. If you want to make them responsive, you can simply add breakpoints to adjust the layout for different screen sizes._

### Using CSS Grid

One approach to building a bento grid is using CSS Grid, along with grid-template-columns, grid-auto-rows, and grid-row. Check out this example:

```
  

<div className="grid auto-rows-[192px] grid-cols-3 gap-4">

{[...Array(7)].map((_, i) => (

<div

key={i}

className={`row-span-1 rounded-xl border-2 border-slate-400/10 bg-neutral-100 p-4 dark:bg-neutral-900 ${

i === 3 || i === 6 ? "col-span-2" : ""

}`}

></div>

))}

</div>

  
```

We make the 3rd and 6th items span two columns on medium screens and up using the md:col-span-2 utility.

### Using CSS Columns

If the order of the items doesn't matter, and if you need it in columns you can opt for a multi-column layout using column-count, column-gap, and margin-bottom on the items.

```
  

<div className="columns-1 gap-4">

{[24, 32, 36, 32, 32, 32, 16, 16, 64].map((height, index) => (

<div

key={index}

className={`mb-4 h-${height} break-inside-avoid rounded-xl border-2 border-slate-400/10 bg-neutral-100 p-4 dark:bg-neutral-900`}

/>

))}

</div>

  
```

The array contains the height of each card component. Alternatively, you can use a full height and let the children components set the card height.

### Using CSS Flexbox

Just like with columns, flexbox is a great option too. You can use flex-wrap, flex-grow, and margin-bottom on the items.

```
  

<div className="flex gap-4">

{[

[24, 32, 32, 16, 16],

[32, 40, 56],

[64, 32, 32],

].map((card, index) => (

<div className="flex-1" key={index}>

{card.map((height, index) => (

<div

className={`mb-4 h-${height} rounded-xl border-2 border-slate-400/10 bg-neutral-100 p-4 dark:bg-neutral-900`}

key={index}

></div>

))}

</div>

))}

</div>

  
```

The code uses an array to store the heights of the cards in each column. The first element of the array is an array of the heights of the cards in the first column, the second element is an array of the heights of the cards in the second column, and so on. Again, you can use a full height and let the children components set the card height.

### More

We've covered some of the most common ways to create a bento grid, but there are loads of other methods depending on your needs.

If you're curisous to learn more, dive into [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) and [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) to discover even more possibilities.

\--

I'm looking forward to writing more articles covering a range of topics like design, front-end development, software, and more. So, stay tuned!

I'd love to hear your feedback, suggestions, or questions. If you found this article helpful, please consider sharing it with others who might enjoy it too. 🙌 Thanks for reading!

Published: 4/27/2023

Subscribe to my personal newsletter for project updates, great links, and some personal notes.

## Metadata

```json
{
  "title": "Creating Bento Grid Layouts",
  "description": "How to create Bento Grid Layouts with Tailwind CSS and React",
  "url": "https://www.julienthibeaut.xyz/blog/create-bento-grid-layouts",
  "content": "As you browse the web, you've likely come across this type of layout before. It can be called a bento grid layout, bento box layout, or bento box grid. This layout takes its inspiration from the traditional Japanese bento box. 🍱\n\nBento grids are super versatile, perfect for displaying all sorts of content like images, text, mixed media, and more. They showcase loads of content in a compact and organized way, making your website or app look clean and engaging.\n\nTrends and examples\n-------------------\n\nSome people say that it start with Windows 8 and the [metro design](https://en.wikipedia.org/wiki/Metro_(design_language)).\n\nHowever, the true trendsetter in recent times is Apple. They've been using bento grid layouts extensively in their video presentations and on their website, making it a popular design choice.\n\n![Image 8: Apple 14](https://ibelick.com/blog/bento-box-apple14.jpg)\n\n[Apple 14](https://www.apple.com/iphone-14/)\n\n![Image 9: Linear](https://ibelick.com/blog/bento-box-linear.jpg)\n\n[Linear](https://linear.app/)\n\n![Image 10: Literal](https://ibelick.com/blog/bento-box-literal.jpg)\n\n[Literal](https://literal.club/)\n\nIf you're looking for design inspiration you can check [bentogrids](https://bentogrids.com/). It's a curated collection showcasing the best bento grid layouts on the web.\n\nBuilding a Bento Grid: Step-by-Step Code\n----------------------------------------\n\nThere are countless ways to create bento grid layouts, and today, I'll show you some of them using Tailwind CSS and React.\n\n_Note that the code examples provided are not responsive by default, as they are intended to be easily viewed on mobile devices too. If you want to make them responsive, you can simply add breakpoints to adjust the layout for different screen sizes._\n\n### Using CSS Grid\n\nOne approach to building a bento grid is using CSS Grid, along with grid-template-columns, grid-auto-rows, and grid-row. Check out this example:\n\n```\n  \n\n<div className=\"grid auto-rows-[192px] grid-cols-3 gap-4\">\n\n{[...Array(7)].map((_, i) => (\n\n<div\n\nkey={i}\n\nclassName={`row-span-1 rounded-xl border-2 border-slate-400/10 bg-neutral-100 p-4 dark:bg-neutral-900 ${\n\ni === 3 || i === 6 ? \"col-span-2\" : \"\"\n\n}`}\n\n></div>\n\n))}\n\n</div>\n\n  \n```\n\nWe make the 3rd and 6th items span two columns on medium screens and up using the md:col-span-2 utility.\n\n### Using CSS Columns\n\nIf the order of the items doesn't matter, and if you need it in columns you can opt for a multi-column layout using column-count, column-gap, and margin-bottom on the items.\n\n```\n  \n\n<div className=\"columns-1 gap-4\">\n\n{[24, 32, 36, 32, 32, 32, 16, 16, 64].map((height, index) => (\n\n<div\n\nkey={index}\n\nclassName={`mb-4 h-${height} break-inside-avoid rounded-xl border-2 border-slate-400/10 bg-neutral-100 p-4 dark:bg-neutral-900`}\n\n/>\n\n))}\n\n</div>\n\n  \n```\n\nThe array contains the height of each card component. Alternatively, you can use a full height and let the children components set the card height.\n\n### Using CSS Flexbox\n\nJust like with columns, flexbox is a great option too. You can use flex-wrap, flex-grow, and margin-bottom on the items.\n\n```\n  \n\n<div className=\"flex gap-4\">\n\n{[\n\n[24, 32, 32, 16, 16],\n\n[32, 40, 56],\n\n[64, 32, 32],\n\n].map((card, index) => (\n\n<div className=\"flex-1\" key={index}>\n\n{card.map((height, index) => (\n\n<div\n\nclassName={`mb-4 h-${height} rounded-xl border-2 border-slate-400/10 bg-neutral-100 p-4 dark:bg-neutral-900`}\n\nkey={index}\n\n></div>\n\n))}\n\n</div>\n\n))}\n\n</div>\n\n  \n```\n\nThe code uses an array to store the heights of the cards in each column. The first element of the array is an array of the heights of the cards in the first column, the second element is an array of the heights of the cards in the second column, and so on. Again, you can use a full height and let the children components set the card height.\n\n### More\n\nWe've covered some of the most common ways to create a bento grid, but there are loads of other methods depending on your needs.\n\nIf you're curisous to learn more, dive into [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) and [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) to discover even more possibilities.\n\n\\--\n\nI'm looking forward to writing more articles covering a range of topics like design, front-end development, software, and more. So, stay tuned!\n\nI'd love to hear your feedback, suggestions, or questions. If you found this article helpful, please consider sharing it with others who might enjoy it too. 🙌 Thanks for reading!\n\nPublished: 4/27/2023\n\nSubscribe to my personal newsletter for project updates, great links, and some personal notes.",
  "publishedTime": "2023-04-27T00:00",
  "usage": {
    "tokens": 1197
  }
}
```
