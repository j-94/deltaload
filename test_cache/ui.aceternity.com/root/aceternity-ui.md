---
title: Aceternity UI
description: Beautiful Tailwind CSS and Framer Motion Components, built with Next.js and TypeScript.
url: https://ui.aceternity.com/
timestamp: 2025-01-20T15:58:30.657Z
domain: ui.aceternity.com
path: root
---

# Aceternity UI


Beautiful Tailwind CSS and Framer Motion Components, built with Next.js and TypeScript.


## Content

As simple as copy and paste
---------------------------

Copy paste the code into your ui folder and use the components in your projects. It's that simple, really.

```
"use client";
  import { useEffect, useState } from "react";
  import { motion } from "framer-motion";
  
  let interval: any;
  
  type Card = {
    id: number;
    name: string;
    designation: string;
    content: React.ReactNode;
  };
  
  export const CardStack = ({
    items,
    offset,
    scaleFactor,
  }: {
    items: Card[];
    offset?: number;
    scaleFactor?: number;
  }) => {
    const CARD_OFFSET = offset || 10;
    const SCALE_FACTOR = scaleFactor || 0.06;
    const [cards, setCards] = useState<Card[]>(items);
  
    useEffect(() => {
      startFlipping();
  
      return () => clearInterval(interval);
    }, []);
    const startFlipping = () => {
      interval = setInterval(() => {
        setCards((prevCards: Card[]) => {
          const newArray = [...prevCards]; // create a copy of the array
          newArray.unshift(newArray.pop()!); // move the last element to the front
          return newArray;
        });
      }, 5000);
    };
  
    return (
      <div className="relative  h-60 w-60 md:h-60 md:w-96">
        {cards.map((card, index) => {
          return (
            <motion.div
              key={card.id}
              className="absolute dark:bg-black bg-white h-60 w-60 md:h-60 md:w-96 rounded-3xl p-4 shadow-xl border border-neutral-200 dark:border-white/[0.1]  shadow-black/[0.1] dark:shadow-white/[0.05] flex flex-col justify-between"
              style={{
                transformOrigin: "top center",
              }}
              animate={{
                top: index * -CARD_OFFSET,
                scale: 1 - index * SCALE_FACTOR, // decrease scale for cards that are behind
                zIndex: cards.length - index, //  decrease z-index for the cards that are behind
              }}
            >
              <div className="font-normal text-neutral-700 dark:text-neutral-200">
                {card.content}
              </div>
              <div>
                <p className="text-neutral-500 font-medium dark:text-white">
                  {card.name}
                </p>
                <p className="text-neutral-400 font-normal dark:text-neutral-200">
                  {card.designation}
                </p>
              </div>
            </motion.div>
          );
        })}
      </div>
    );
  };
  
```

These cards are amazing, I want to use them in my project. Framer motion is a godsend ngl tbh fam 🙏

Manu Arora

Senior Software Engineer

I dont like this Twitter thing, deleting it right away because yolo. Instead, I would like to call it X.com so that it can easily be confused with adult sites.

Elon Musk

Senior Shitposter

The first rule ofFight Club is that you do not talk about fight club. The second rule ofFight club is that you DO NOT TALK about fight club.

Tyler Durden

Manager Project Mayhem

## Metadata

```json
{
  "title": "Aceternity UI",
  "description": "Beautiful Tailwind CSS and Framer Motion Components, built with Next.js and TypeScript.",
  "url": "https://ui.aceternity.com/",
  "content": "As simple as copy and paste\n---------------------------\n\nCopy paste the code into your ui folder and use the components in your projects. It's that simple, really.\n\n```\n\"use client\";\n  import { useEffect, useState } from \"react\";\n  import { motion } from \"framer-motion\";\n  \n  let interval: any;\n  \n  type Card = {\n    id: number;\n    name: string;\n    designation: string;\n    content: React.ReactNode;\n  };\n  \n  export const CardStack = ({\n    items,\n    offset,\n    scaleFactor,\n  }: {\n    items: Card[];\n    offset?: number;\n    scaleFactor?: number;\n  }) => {\n    const CARD_OFFSET = offset || 10;\n    const SCALE_FACTOR = scaleFactor || 0.06;\n    const [cards, setCards] = useState<Card[]>(items);\n  \n    useEffect(() => {\n      startFlipping();\n  \n      return () => clearInterval(interval);\n    }, []);\n    const startFlipping = () => {\n      interval = setInterval(() => {\n        setCards((prevCards: Card[]) => {\n          const newArray = [...prevCards]; // create a copy of the array\n          newArray.unshift(newArray.pop()!); // move the last element to the front\n          return newArray;\n        });\n      }, 5000);\n    };\n  \n    return (\n      <div className=\"relative  h-60 w-60 md:h-60 md:w-96\">\n        {cards.map((card, index) => {\n          return (\n            <motion.div\n              key={card.id}\n              className=\"absolute dark:bg-black bg-white h-60 w-60 md:h-60 md:w-96 rounded-3xl p-4 shadow-xl border border-neutral-200 dark:border-white/[0.1]  shadow-black/[0.1] dark:shadow-white/[0.05] flex flex-col justify-between\"\n              style={{\n                transformOrigin: \"top center\",\n              }}\n              animate={{\n                top: index * -CARD_OFFSET,\n                scale: 1 - index * SCALE_FACTOR, // decrease scale for cards that are behind\n                zIndex: cards.length - index, //  decrease z-index for the cards that are behind\n              }}\n            >\n              <div className=\"font-normal text-neutral-700 dark:text-neutral-200\">\n                {card.content}\n              </div>\n              <div>\n                <p className=\"text-neutral-500 font-medium dark:text-white\">\n                  {card.name}\n                </p>\n                <p className=\"text-neutral-400 font-normal dark:text-neutral-200\">\n                  {card.designation}\n                </p>\n              </div>\n            </motion.div>\n          );\n        })}\n      </div>\n    );\n  };\n  \n```\n\nThese cards are amazing, I want to use them in my project. Framer motion is a godsend ngl tbh fam 🙏\n\nManu Arora\n\nSenior Software Engineer\n\nI dont like this Twitter thing, deleting it right away because yolo. Instead, I would like to call it X.com so that it can easily be confused with adult sites.\n\nElon Musk\n\nSenior Shitposter\n\nThe first rule ofFight Club is that you do not talk about fight club. The second rule ofFight club is that you DO NOT TALK about fight club.\n\nTyler Durden\n\nManager Project Mayhem",
  "usage": {
    "tokens": 685
  }
}
```
