---
title: Theming
description: Add styles to your site using Theme UI and Style props.
url: https://sbs-www.vercel.app/docs/theming#create-a-theme
timestamp: 2025-01-20T16:09:02.644Z
domain: sbs-www.vercel.app
path: docs_theming
---

# Theming


Add styles to your site using Theme UI and Style props.


## Content

Note: Reflex is still in **development** and we are actively working on the documentation.

Add styles to your site using Theme UI and Style props.

[Theme UI](https://sbs-www.vercel.app/docs/theming#theme-ui)
------------------------------------------------------------

Reflex uses [Theme UI](https://theme-ui.com/) for styling. Theme UI is a CSS-in-JS library for creating constraint-based designs.

What this means is you create a shared set of values such as colors, font sizes, and spacing and then reference these values to build your site.

Here's a simple theme:

src/gatsby-theme-base/theme.js

export default {

colors: {

text: "#000",

background: "#fff"

primary: "#82aaff",

},

fontSizes: \[14, 16, 18, 20, 22, 36, 56, 72\],

}

You can then use values from this theme in your components.

<Button bg\="primary" color\="text" fontSize\="2"\>

Styled button

</Button\>

This will create a `button` with the following CSS styles:

{

background-color: "#82aaff", // --\> colors.primary

color: "#000", // --\> colors.text

font-size: "18px" // --\> fontSizes\[2\]

}

[Style props](https://sbs-www.vercel.app/docs/theming#style-props)
------------------------------------------------------------------

Style props is using CSS attributes as props. All [components](https://sbs-www.vercel.app/docs/components) and [blocks](https://sbs-www.vercel.app/docs/blocks) can use style props.

<Button bg\="primary" color\="text" px\="3" py\="2"\>

Button

</Button\>

<P fontSize\="2" fontWeight\="semi"\>

This is a paragraph

</P\>

<Grid col\="1fr 1fr" gap\="2"\>

<Div\>First column</Div\>

<Div\>Second column</Div\>

</Grid\>

[Create a theme](https://sbs-www.vercel.app/docs/theming#create-a-theme)
------------------------------------------------------------------------

Let's start by creating a simple theme.

Create the following file in your site: `src/@reflexjs/gatsby-theme-base/theme.js`. This is where you are going to define your theme values.

Let's add some `colors`, `fontSizes` and `lineHeights`.

src/gatsby-theme-base/theme.js

export default {

colors: {

text: "#000",

background: "#fff",

primary: "#07c",

},

fonts: {

body: '"Segoe UI", Roboto, "Helvetica Neue", sans-serif',

heading: "Georgia, serif",

monospace: "Menlo, monospace",

},

fontSizes: \[12, 14, 16, 20, 24, 32, 48, 64\],

fontWeights: {

body: 400,

heading: 700,

bold: 700,

},

lineHeights: {

body: 1.5,

heading: 1.125,

},

letterSpacings: {

body: "normal",

caps: "0.2em",

},

}

[Styling](https://sbs-www.vercel.app/docs/theming#styling)
----------------------------------------------------------

Once you have created your theme, you can now use the theme values in any `.mdx` or `React` component.

<H1 fontFamily\="heading" fontSize\="5" lineHeight\="heading" color\="text"\>

This is heading

</H1\>

[Responsive](https://sbs-www.vercel.app/docs/theming#responsive)
----------------------------------------------------------------

Theme UI includes a shorthand syntax for writing mobile-first responsive styles.

Define your breakpoints in your theme file:

src/gatsby-theme-base/theme.js

export default {

...

breakpoints: \[\`768px\`, \`1024px\`, \`1280px\`\],

...

}

Then use an array-like syntax to style components.

<Grid col\="1fr|1fr 1fr"\>

<Div\>First</Div\>

<Div\>Second</Div\>

</Grid\>

<Button fontSize\="2|4|6" colors\="primary|secondary"\>

Button

</Button\>

**Tip**: You can also use an array-like syntax for responsive values.

<Button fontSize\={\[2, 4, 6\]} colors\={\["primary", "secondary"\]}\>

Button

</Button\>

[Hover and focus](https://sbs-www.vercel.app/docs/theming#hover-and-focus)
--------------------------------------------------------------------------

Hover, focus and other CSS pseudo-classes have equivalent style props by using a prefix. Examples: `hoverBg`, `hoverColor`, and `hoverBorderColor`.

<Button bg\="primary" hoverBg\="secondary" focusBorderWidth\="1px"\>

Button

</Button\>

[Variants](https://sbs-www.vercel.app/docs/theming#variants)
------------------------------------------------------------

If you find yourself repeating common styles for the same components, you can abstract the styles into a variant.

Every component has support for variants. See example below:

src/gatsby-theme-base/theme.js

export default {

...

colors: {

text: "#000",

background: "#fff",

primary: "#07c",

},

fontSizes: \[12, 14, 16, 20, 24, 32, 48, 64\],

radii: {

xs: ".1rem",

sm: ".2rem",

md: ".25rem",

lg: ".5rem",

},

...

button: {

border: "1px solid",

borderRadius: "sm",

fontSize: 2,

primary: {

bg: "primary",

},

secondary: {

bg: "secondary",

},

lg: {

fontSize: 4,

}

}

}

To use variant, simply pass in values to the `variant` prop.

<Button variant\="primary"\>Primary button</Button\>

You can also use multiple variants.

<Button variant\="primary lg"\>Large Primary button</Button\>

## Metadata

```json
{
  "title": "Theming",
  "description": "Add styles to your site using Theme UI and Style props.",
  "url": "https://sbs-www.vercel.app/docs/theming#create-a-theme",
  "content": "Note: Reflex is still in **development** and we are actively working on the documentation.\n\nAdd styles to your site using Theme UI and Style props.\n\n[Theme UI](https://sbs-www.vercel.app/docs/theming#theme-ui)\n------------------------------------------------------------\n\nReflex uses [Theme UI](https://theme-ui.com/) for styling. Theme UI is a CSS-in-JS library for creating constraint-based designs.\n\nWhat this means is you create a shared set of values such as colors, font sizes, and spacing and then reference these values to build your site.\n\nHere's a simple theme:\n\nsrc/gatsby-theme-base/theme.js\n\nexport default {\n\ncolors: {\n\ntext: \"#000\",\n\nbackground: \"#fff\"\n\nprimary: \"#82aaff\",\n\n},\n\nfontSizes: \\[14, 16, 18, 20, 22, 36, 56, 72\\],\n\n}\n\nYou can then use values from this theme in your components.\n\n<Button bg\\=\"primary\" color\\=\"text\" fontSize\\=\"2\"\\>\n\nStyled button\n\n</Button\\>\n\nThis will create a `button` with the following CSS styles:\n\n{\n\nbackground-color: \"#82aaff\", // --\\> colors.primary\n\ncolor: \"#000\", // --\\> colors.text\n\nfont-size: \"18px\" // --\\> fontSizes\\[2\\]\n\n}\n\n[Style props](https://sbs-www.vercel.app/docs/theming#style-props)\n------------------------------------------------------------------\n\nStyle props is using CSS attributes as props. All [components](https://sbs-www.vercel.app/docs/components) and [blocks](https://sbs-www.vercel.app/docs/blocks) can use style props.\n\n<Button bg\\=\"primary\" color\\=\"text\" px\\=\"3\" py\\=\"2\"\\>\n\nButton\n\n</Button\\>\n\n<P fontSize\\=\"2\" fontWeight\\=\"semi\"\\>\n\nThis is a paragraph\n\n</P\\>\n\n<Grid col\\=\"1fr 1fr\" gap\\=\"2\"\\>\n\n<Div\\>First column</Div\\>\n\n<Div\\>Second column</Div\\>\n\n</Grid\\>\n\n[Create a theme](https://sbs-www.vercel.app/docs/theming#create-a-theme)\n------------------------------------------------------------------------\n\nLet's start by creating a simple theme.\n\nCreate the following file in your site: `src/@reflexjs/gatsby-theme-base/theme.js`. This is where you are going to define your theme values.\n\nLet's add some `colors`, `fontSizes` and `lineHeights`.\n\nsrc/gatsby-theme-base/theme.js\n\nexport default {\n\ncolors: {\n\ntext: \"#000\",\n\nbackground: \"#fff\",\n\nprimary: \"#07c\",\n\n},\n\nfonts: {\n\nbody: '\"Segoe UI\", Roboto, \"Helvetica Neue\", sans-serif',\n\nheading: \"Georgia, serif\",\n\nmonospace: \"Menlo, monospace\",\n\n},\n\nfontSizes: \\[12, 14, 16, 20, 24, 32, 48, 64\\],\n\nfontWeights: {\n\nbody: 400,\n\nheading: 700,\n\nbold: 700,\n\n},\n\nlineHeights: {\n\nbody: 1.5,\n\nheading: 1.125,\n\n},\n\nletterSpacings: {\n\nbody: \"normal\",\n\ncaps: \"0.2em\",\n\n},\n\n}\n\n[Styling](https://sbs-www.vercel.app/docs/theming#styling)\n----------------------------------------------------------\n\nOnce you have created your theme, you can now use the theme values in any `.mdx` or `React` component.\n\n<H1 fontFamily\\=\"heading\" fontSize\\=\"5\" lineHeight\\=\"heading\" color\\=\"text\"\\>\n\nThis is heading\n\n</H1\\>\n\n[Responsive](https://sbs-www.vercel.app/docs/theming#responsive)\n----------------------------------------------------------------\n\nTheme UI includes a shorthand syntax for writing mobile-first responsive styles.\n\nDefine your breakpoints in your theme file:\n\nsrc/gatsby-theme-base/theme.js\n\nexport default {\n\n...\n\nbreakpoints: \\[\\`768px\\`, \\`1024px\\`, \\`1280px\\`\\],\n\n...\n\n}\n\nThen use an array-like syntax to style components.\n\n<Grid col\\=\"1fr|1fr 1fr\"\\>\n\n<Div\\>First</Div\\>\n\n<Div\\>Second</Div\\>\n\n</Grid\\>\n\n<Button fontSize\\=\"2|4|6\" colors\\=\"primary|secondary\"\\>\n\nButton\n\n</Button\\>\n\n**Tip**: You can also use an array-like syntax for responsive values.\n\n<Button fontSize\\={\\[2, 4, 6\\]} colors\\={\\[\"primary\", \"secondary\"\\]}\\>\n\nButton\n\n</Button\\>\n\n[Hover and focus](https://sbs-www.vercel.app/docs/theming#hover-and-focus)\n--------------------------------------------------------------------------\n\nHover, focus and other CSS pseudo-classes have equivalent style props by using a prefix. Examples: `hoverBg`, `hoverColor`, and `hoverBorderColor`.\n\n<Button bg\\=\"primary\" hoverBg\\=\"secondary\" focusBorderWidth\\=\"1px\"\\>\n\nButton\n\n</Button\\>\n\n[Variants](https://sbs-www.vercel.app/docs/theming#variants)\n------------------------------------------------------------\n\nIf you find yourself repeating common styles for the same components, you can abstract the styles into a variant.\n\nEvery component has support for variants. See example below:\n\nsrc/gatsby-theme-base/theme.js\n\nexport default {\n\n...\n\ncolors: {\n\ntext: \"#000\",\n\nbackground: \"#fff\",\n\nprimary: \"#07c\",\n\n},\n\nfontSizes: \\[12, 14, 16, 20, 24, 32, 48, 64\\],\n\nradii: {\n\nxs: \".1rem\",\n\nsm: \".2rem\",\n\nmd: \".25rem\",\n\nlg: \".5rem\",\n\n},\n\n...\n\nbutton: {\n\nborder: \"1px solid\",\n\nborderRadius: \"sm\",\n\nfontSize: 2,\n\nprimary: {\n\nbg: \"primary\",\n\n},\n\nsecondary: {\n\nbg: \"secondary\",\n\n},\n\nlg: {\n\nfontSize: 4,\n\n}\n\n}\n\n}\n\nTo use variant, simply pass in values to the `variant` prop.\n\n<Button variant\\=\"primary\"\\>Primary button</Button\\>\n\nYou can also use multiple variants.\n\n<Button variant\\=\"primary lg\"\\>Large Primary button</Button\\>",
  "usage": {
    "tokens": 1274
  }
}
```
