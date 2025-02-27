---
title: Terminal Setup - Make your Mac terminal awesome
description: How to configure your Mac terminal as Developer. Tagged with terminal, ohmyzsh, bash, dev.
url: https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc
timestamp: 2025-01-20T15:44:34.627Z
domain: dev.to
path: alagrede_terminal-setup-make-your-mac-terminal-awesome-4ecc
---

# Terminal Setup - Make your Mac terminal awesome


How to configure your Mac terminal as Developer. Tagged with terminal, ohmyzsh, bash, dev.


## Content

Terminal Setup - Make your Mac terminal awesome - DEV Community
===============                                         

  

[Skip to content](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#main-content)

 [![Image 60: DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)](https://dev.to/)

  [Powered by Algolia](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)

[](https://dev.to/search)

[Log in](https://dev.to/enter) [Create account](https://dev.to/enter?state=new-user)

DEV Community
-------------

 

 ![Image 61](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)Add reaction

 ![Image 62](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)Like ![Image 63](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)Unicorn  ![Image 64](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)Exploding Head  ![Image 65](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)Raised Hands  ![Image 66](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)Fire

Jump to Comments Save Boost

Copy link 

Copied to Clipboard

[Share to X](https://twitter.com/intent/tweet?text=%22Terminal%20Setup%20-%20Make%20your%20Mac%20terminal%20awesome%22%20by%20%40alagrede%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Falagrede%2Fterminal-setup-make-your-mac-terminal-awesome-4ecc) [Share to LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Falagrede%2Fterminal-setup-make-your-mac-terminal-awesome-4ecc&title=Terminal%20Setup%20-%20Make%20your%20Mac%20terminal%20awesome&summary=How%20to%20configure%20your%20Mac%20terminal%20as%20Developer&source=DEV%20Community) [Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Falagrede%2Fterminal-setup-make-your-mac-terminal-awesome-4ecc) [Share to Mastodon](https://toot.kytta.dev/?text=https%3A%2F%2Fdev.to%2Falagrede%2Fterminal-setup-make-your-mac-terminal-awesome-4ecc)

[Share Post via...](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#) [Report Abuse](https://dev.to/report-abuse)

[![Image 67: Cover image for Terminal Setup - Make your Mac terminal awesome](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq81bdk4ur4sfuij7ax45.png)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq81bdk4ur4sfuij7ax45.png)

[![Image 68: Anthony Lagrede](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)](https://dev.to/alagrede)

[Anthony Lagrede](https://dev.to/alagrede)Posted on Jan 7, 2022

   ![Image 69](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)  ![Image 70](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)  ![Image 71](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)  ![Image 72](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![Image 73](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

Terminal Setup - Make your Mac terminal awesome
===============================================

[#terminal](https://dev.to/t/terminal) [#ohmyzsh](https://dev.to/t/ohmyzsh) [#bash](https://dev.to/t/bash) [#dev](https://dev.to/t/dev)

I recently installed my new MacBook and set up my terminal. Here I'll show you how to do the same for your MacBook.

[](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#the-final-result)The final result
---------------------------------------------------------------------------------------------------------------

This is the end result based on the delicious **powerlevel10k**. Easy to configure and modify. Optimized to work as a developer.

> You will notice the toolbar at the top (Cpu, Ram, Network) to always have an overview of the hardware consumption.

[![Image 74: Mac terminal](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsoupov6aejxnjadtwzli.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsoupov6aejxnjadtwzli.png)

### [](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#prerequisites)Prerequisites

Install [Homebrew](https://brew.sh/index_fr)

```


/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


```

 

Install [iTerm2](https://iterm2.com/) and git

```


brew install --cask iterm2
brew install git


```

 

Install [Oh My Zsh](https://ohmyz.sh/#install)

```


$ sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"


```

 

### [](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#theme-installation)Theme installation

I choosed [powerlevel10k](https://github.com/romkatv/powerlevel10k) probably one of the best and most flexible theme you can choose.  
You can easily change your terminal layout simply by rerun the installation command.

Start to install [MesloLGS Fonts](https://github.com/romkatv/powerlevel10k#fonts)

```


MesloLGS NF Regular.ttf
MesloLGS NF Bold.ttf
MesloLGS NF Italic.ttf
MesloLGS NF Bold Italic.ttf


```

 

Then install **powerlevel10k** itself

```


git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k


```

 

In `~/.zshrc` set the ZSH theme to use:

```


ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc.


```

 

You will probably at least configure these two ZSH plugins:

**zsh-syntax-highlighting** - Fish shell like syntax highlighting for Zsh. This is what makes my aliases/commands green above. If it's green then it's installed!  
**zsh-autosuggestions** - Fish-like autosuggestions for zsh. Will show a preview of the last matching command while typing. Press right to use

In `~/.zshrc` set the ZSH plugins to use:

```


plugins=(
  git
  zsh-syntax-highlighting
  zsh-autosuggestions
)


```

 

**Restart your terminal** with Zsh

Now you can run

```


p10k configure


```

 

If you have issue with fonts, check MesloLGS font is selected.  
`Open iTerm2 → Preferences → Profiles → Text and set Font to MesloLGS NF`.

Finally, if you want to include your existing bash aliases and functions:  
In `~/.zshrc` source your bash\_profile just before the **export ZSH**

```


source ~/.bash_profile

```

 

###   
[](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#add-the-toolbar)  
Add the Toolbar  

[![Image 75: Toolbar](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpfk2ihzdvd4hx6oas6mo.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpfk2ihzdvd4hx6oas6mo.png)

Open your `iterm2 > Profile > Session > Status bar enabled`  
[![Image 76: iterm2 conf](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthnc8dsbdooisi2kr0m0.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthnc8dsbdooisi2kr0m0.png)

Select your widgets  
[![Image 77: iterm2 status bar widgets](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Frwxz05tbpydattvh1uhs.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Frwxz05tbpydattvh1uhs.png)

[](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#finished)Finished!
------------------------------------------------------------------------------------------------

I hope this small tutorial will help you to improve your setup. It is obviously not complete but easy enough to move on.

Top comments (12)
-----------------

Subscribe

    ![Image 78: pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Personal Trusted User

[Create template](https://dev.to/settings/response-templates)Templates let you quickly answer FAQs or store snippets for re-use.

Submit Preview [Dismiss](https://dev.to/404.html)

 

 

[![Image 79: zwacky profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F277593%2F29add9f7-4fe8-4608-8838-490dbeeb660c.jpg)](https://dev.to/zwacky)

[Simon Wicki](https://dev.to/zwacky)

Simon Wicki

 [![Image 80](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F277593%2F29add9f7-4fe8-4608-8838-490dbeeb660c.jpg)Simon Wicki](https://dev.to/zwacky)

Follow

💬 Frontend, webperf & non-fiction books 👨‍💻 Frontend at JustWatch 🔔 Creator of https://notyfy.co 🧙‍♂️ Freelancer

*   Location
    
    Berlin
    
*   Joined
    
    Nov 22, 2019
    

• [Jan 9 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5a6)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5a6)

*   Hide

First time I saw the toolbar feature in a CLI, sweet. Time to toy around with that one.

I can recommend these two tools to improve the Git experience on the CLI:

*   [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy): better visualisation of `git diff`
*   [git lg](http://garmoncheg.blogspot.com/2012/06/pretty-git-log.html): better visualisation than `git log`

3 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l5a6)

 

 

[![Image 81: thomasbredi profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F533935%2Ff5397200-9e46-4cca-8e20-017a11089281.png)](https://dev.to/thomasbredi)

[Thomas Bredillet](https://dev.to/thomasbredi)

Thomas Bredillet

 [![Image 82](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F533935%2Ff5397200-9e46-4cca-8e20-017a11089281.png)Thomas Bredillet](https://dev.to/thomasbredi)

Follow

*   Joined
    
    Dec 5, 2020
    

• [Jan 9 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5b6)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5b6)

*   Hide

For install this two plugins :

git clone [github.com/zsh-users/zsh-autosugge...](https://github.com/zsh-users/zsh-autosuggestions) ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions  
git clone [github.com/zsh-users/zsh-syntax-hi...](https://github.com/zsh-users/zsh-syntax-highlighting.git) ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting

3 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l5b6)

 

 

[![Image 83: sansk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)](https://dev.to/sansk)

[Sangy K](https://dev.to/sansk)

Sangy K

 [![Image 84](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)Sangy K](https://dev.to/sansk)

Follow

Full-Stack Developer • An Introvert Coder • Tech Blogger • A Proud Mom

*   Location
    
    Internet
    
*   Work
    
    Javascript Developer
    
*   Joined
    
    Sep 8, 2019
    

• [Jan 11 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l6h7)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l6h7)

*   Hide

Is there something like this for windows terminal/powershell?

2 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l6h7)

 

 

[![Image 85: zeeshan profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225799%2F83988eff-bb05-4461-b5a7-5398165ec0e1.jpeg)](https://dev.to/zeeshan)

[Mohammed Zeeshan](https://dev.to/zeeshan)

Mohammed Zeeshan

 [![Image 86](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225799%2F83988eff-bb05-4461-b5a7-5398165ec0e1.jpeg)Mohammed Zeeshan](https://dev.to/zeeshan)

Follow

Language Learner

*   Location
    
    Kerala, India
    
*   Work
    
    Frontend Engineer at Food Market Hub, Malaysia
    
*   Joined
    
    Sep 8, 2019
    

• [Jan 11 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l72g)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l72g)

*   Hide

ohmyposh. scott hanselman has some oretty good articles and videos on setting this up

3 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l72g)

 

 

[![Image 87: sansk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)](https://dev.to/sansk)

[Sangy K](https://dev.to/sansk)

Sangy K

 [![Image 88](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)Sangy K](https://dev.to/sansk)

Follow

Full-Stack Developer • An Introvert Coder • Tech Blogger • A Proud Mom

*   Location
    
    Internet
    
*   Work
    
    Javascript Developer
    
*   Joined
    
    Sep 8, 2019
    

• [Jan 14 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l98b)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l98b)

*   Hide

Thanks. I will check it out

2 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l98b)

 

 

[![Image 89: alagrede profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)](https://dev.to/alagrede)

[Anthony Lagrede](https://dev.to/alagrede)

Anthony Lagrede

 [![Image 90](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)Anthony Lagrede](https://dev.to/alagrede)

Follow

Passionate developer. Share skills and side projects. #web #DataScience stuff #freelance #Toulouse. Check out my last app: https://znote.io

*   Location
    
    Toulouse
    
*   Joined
    
    Nov 28, 2017
    

• [Jan 11 '22 • Edited on Jan 11 • Edited](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l6ji)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l6ji)

*   Hide

Hi Sangy,  
Yes, there is also ohmyposh. Take a look here for Windows 😊:  
[dev.to/alagrede/terminal-setup-mak...](https://dev.to/alagrede/terminal-setup-make-your-windows-terminal-awesome-569i)

2 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l6ji)

 

 

[![Image 91: sansk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)](https://dev.to/sansk)

[Sangy K](https://dev.to/sansk)

Sangy K

 [![Image 92](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)Sangy K](https://dev.to/sansk)

Follow

Full-Stack Developer • An Introvert Coder • Tech Blogger • A Proud Mom

*   Location
    
    Internet
    
*   Work
    
    Javascript Developer
    
*   Joined
    
    Sep 8, 2019
    

• [Jan 14 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l98a)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l98a)

*   Hide

Thanks. I will check it out

1 like Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l98a)

 

 

[![Image 93: gnsp profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F129205%2F21b17be8-1d7b-492e-aac7-7e73215b4266.jpeg)](https://dev.to/gnsp)

[Ganesh Prasad](https://dev.to/gnsp)

Ganesh Prasad

 [![Image 94](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F129205%2F21b17be8-1d7b-492e-aac7-7e73215b4266.jpeg)Ganesh Prasad](https://dev.to/gnsp)

Follow

Inventor of Ironscript

*   Location
    
    Odisha, India
    
*   Education
    
    National Institute of Technology, Rourkela
    
*   Work
    
    Software Engineer at Google
    
*   Joined
    
    Jan 16, 2019
    

• [Jan 10 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5ng)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5ng)

*   Hide

I have been using the same setup for last 5 years now. I use the font firacode though.

3 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l5ng)

 

 

[![Image 95: chideraike profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F523772%2F965eb653-cda8-4073-bd0d-8058e45241ce.png)](https://dev.to/chideraike)

[Chidera](https://dev.to/chideraike)

Chidera

 [![Image 96](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F523772%2F965eb653-cda8-4073-bd0d-8058e45241ce.png)Chidera](https://dev.to/chideraike)

Follow

I build Web & Mobile Applications

*   Location
    
    Lagos, Nigeria
    
*   Joined
    
    Dec 1, 2020
    

• [Jan 10 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l64p)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l64p)

*   Hide

Thanks for this, I found it helpful

2 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l64p)

 

 

[![Image 97: devphu profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F800864%2F1e510465-8d1f-4ba4-bd32-3e04243eb40f.jpeg)](https://dev.to/devphu)

[PhanPhú](https://dev.to/devphu)

PhanPhú

 [![Image 98](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F800864%2F1e510465-8d1f-4ba4-bd32-3e04243eb40f.jpeg)PhanPhú](https://dev.to/devphu)

Follow

*   Joined
    
    Jan 21, 2022
    

• [Jan 21 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1lei6)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1lei6)

*   Hide

it has work with mac chip m1?

1 like Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1lei6)

 

 

[![Image 99: alagrede profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)](https://dev.to/alagrede)

[Anthony Lagrede](https://dev.to/alagrede)

Anthony Lagrede

 [![Image 100](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)Anthony Lagrede](https://dev.to/alagrede)

Follow

Passionate developer. Share skills and side projects. #web #DataScience stuff #freelance #Toulouse. Check out my last app: https://znote.io

*   Location
    
    Toulouse
    
*   Joined
    
    Nov 28, 2017
    

• [Jan 24 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1lg9k)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1lg9k)

*   Hide

Hi [@devphu](https://dev.to/devphu), yes of course.

1 like Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1lg9k)

 

 

[![Image 101: rannn505 profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F791199%2F830fe8be-7090-4f15-9014-fa17e03e02ab.jpeg)](https://dev.to/rannn505)

[Ran Cohen](https://dev.to/rannn505)

Ran Cohen

 [![Image 102](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F791199%2F830fe8be-7090-4f15-9014-fa17e03e02ab.jpeg)Ran Cohen](https://dev.to/rannn505)

Follow

https://www.linkedin.com/in/rannn505/

*   Email
    
    [rannn505@outlook.com](mailto:rannn505@outlook.com)
    
*   Work
    
    CTO & Co-Founder at Configu
    
*   Joined
    
    Jan 12, 2022
    

• [Feb 9 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1m1f2)

*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1m1f2)

*   Hide

Check out [my post](https://dev.to/rannn505/macos-awesome-terminal-519n) for more awesome features 🦄

Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1m1f2)

[View full discussion (12 comments)](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments)

[Code of Conduct](https://dev.to/code-of-conduct) • [Report abuse](https://dev.to/report-abuse)

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#).

Hide child comments as well

Confirm

For further actions, you may consider blocking this person and/or [reporting abuse](https://dev.to/report-abuse)

Read next
---------

[![Image 103: desk_track profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F856539%2F0a7fac15-9810-4cd4-8ca9-05bd29eb6459.jpg) ### How work from home monitoring tools prevent distractions and increase focus DeskTrack - Jan 20](https://dev.to/desk_track/how-work-from-home-monitoring-tools-prevent-distractions-and-increase-focus-4fll)[![Image 104: asiaelbow2 profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2736881%2F61a08758-65a9-418f-9170-81b97a6092ad.png) ### Exploring the Power of Internet Marketing in Today’s Marketplace Seerup Carlson - Jan 20](https://dev.to/asiaelbow2/exploring-the-power-of-internet-marketing-in-todays-marketplace-93p)[![Image 105: heartgroup7 profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2727326%2F1f49fed7-96ae-46bd-8474-1582821ace0d.png) ### Sports training in Asia along with Italy: A comparison evaluation. Yang Thorsen - Jan 20](https://dev.to/heartgroup7/sports-training-in-asia-along-with-italy-a-comparison-evaluation-2f51)[![Image 106: veiledvirtue_042df28a9877 profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2713920%2Ff1aca135-eab8-4f3f-85a4-7ba16036499d.png) ### Boosting Your Business Online: Expert SEO Strategies for Maidenhead Companies VeiledVirtue - Jan 20](https://dev.to/veiledvirtue_042df28a9877/boosting-your-business-online-expert-seo-strategies-for-maidenhead-companies-555)

 [![Image 107](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)Anthony Lagrede](https://dev.to/alagrede)

Follow

Passionate developer. Share skills and side projects. #web #DataScience stuff #freelance #Toulouse. Check out my last app: https://znote.io

*   Location
    
    Toulouse
    
*   Joined
    
    Nov 28, 2017
    

### More from [Anthony Lagrede](https://dev.to/alagrede)

[Terminal Setup - Make your Windows terminal awesome #terminal #ohmyposh #bash #dev](https://dev.to/alagrede/terminal-setup-make-your-windows-terminal-awesome-569i)

Thank you to our Diamond Sponsor [Neon](https://neon.tech/) for supporting our community.

[DEV Community](https://dev.to/) — A constructive and inclusive social network for software developers. With you every step of your journey.

*   [Home](https://dev.to/)
*   [DEV++](https://dev.to/++)
*   [Podcasts](https://dev.to/pod)
*   [Videos](https://dev.to/videos)
*   [Tags](https://dev.to/tags)
*   [DEV Help](https://dev.to/help)
*   [Forem Shop](https://shop.forem.com/)
*   [Advertise on DEV](https://dev.to/advertise)
*   [DEV Challenges](https://dev.to/challenges)
*   [DEV Showcase](https://dev.to/showcase)
*   [About](https://dev.to/about)
*   [Contact](https://dev.to/contact)
*   [Free Postgres Database](https://dev.to/free-postgres-database-tier)
*   [Software comparisons](https://dev.to/software-comparisons)

*   [Code of Conduct](https://dev.to/code-of-conduct)
*   [Privacy Policy](https://dev.to/privacy)
*   [Terms of use](https://dev.to/terms)

Built on [Forem](https://www.forem.com/) — the [open source](https://dev.to/t/opensource) software that powers [DEV](https://dev.to/) and other inclusive communities.

Made with love and [Ruby on Rails](https://dev.to/t/rails). DEV Community © 2016 - 2025.

![Image 108: DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

We're a place where coders share, stay up-to-date and grow their careers.

[Log in](https://dev.to/enter) [Create account](https://dev.to/enter?state=new-user)

![Image 109](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![Image 110](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![Image 111](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![Image 112](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![Image 113](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

## Metadata

```json
{
  "title": "Terminal Setup - Make your Mac terminal awesome",
  "description": "How to configure your Mac terminal as Developer. Tagged with terminal, ohmyzsh, bash, dev.",
  "url": "https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc",
  "content": "Terminal Setup - Make your Mac terminal awesome - DEV Community\n===============                                         \n\n  \n\n[Skip to content](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#main-content)\n\n [![Image 60: DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)](https://dev.to/)\n\n  [Powered by Algolia](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)\n\n[](https://dev.to/search)\n\n[Log in](https://dev.to/enter) [Create account](https://dev.to/enter?state=new-user)\n\nDEV Community\n-------------\n\n \n\n ![Image 61](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)Add reaction\n\n ![Image 62](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)Like ![Image 63](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)Unicorn  ![Image 64](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)Exploding Head  ![Image 65](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)Raised Hands  ![Image 66](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)Fire\n\nJump to Comments Save Boost\n\nCopy link \n\nCopied to Clipboard\n\n[Share to X](https://twitter.com/intent/tweet?text=%22Terminal%20Setup%20-%20Make%20your%20Mac%20terminal%20awesome%22%20by%20%40alagrede%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Falagrede%2Fterminal-setup-make-your-mac-terminal-awesome-4ecc) [Share to LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Falagrede%2Fterminal-setup-make-your-mac-terminal-awesome-4ecc&title=Terminal%20Setup%20-%20Make%20your%20Mac%20terminal%20awesome&summary=How%20to%20configure%20your%20Mac%20terminal%20as%20Developer&source=DEV%20Community) [Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Falagrede%2Fterminal-setup-make-your-mac-terminal-awesome-4ecc) [Share to Mastodon](https://toot.kytta.dev/?text=https%3A%2F%2Fdev.to%2Falagrede%2Fterminal-setup-make-your-mac-terminal-awesome-4ecc)\n\n[Share Post via...](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#) [Report Abuse](https://dev.to/report-abuse)\n\n[![Image 67: Cover image for Terminal Setup - Make your Mac terminal awesome](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq81bdk4ur4sfuij7ax45.png)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq81bdk4ur4sfuij7ax45.png)\n\n[![Image 68: Anthony Lagrede](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)](https://dev.to/alagrede)\n\n[Anthony Lagrede](https://dev.to/alagrede)Posted on Jan 7, 2022\n\n   ![Image 69](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)  ![Image 70](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)  ![Image 71](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)  ![Image 72](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![Image 73](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)\n\nTerminal Setup - Make your Mac terminal awesome\n===============================================\n\n[#terminal](https://dev.to/t/terminal) [#ohmyzsh](https://dev.to/t/ohmyzsh) [#bash](https://dev.to/t/bash) [#dev](https://dev.to/t/dev)\n\nI recently installed my new MacBook and set up my terminal. Here I'll show you how to do the same for your MacBook.\n\n[](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#the-final-result)The final result\n---------------------------------------------------------------------------------------------------------------\n\nThis is the end result based on the delicious **powerlevel10k**. Easy to configure and modify. Optimized to work as a developer.\n\n> You will notice the toolbar at the top (Cpu, Ram, Network) to always have an overview of the hardware consumption.\n\n[![Image 74: Mac terminal](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsoupov6aejxnjadtwzli.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsoupov6aejxnjadtwzli.png)\n\n### [](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#prerequisites)Prerequisites\n\nInstall [Homebrew](https://brew.sh/index_fr)\n\n```\n\n\n/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"\n\n\n```\n\n \n\nInstall [iTerm2](https://iterm2.com/) and git\n\n```\n\n\nbrew install --cask iterm2\nbrew install git\n\n\n```\n\n \n\nInstall [Oh My Zsh](https://ohmyz.sh/#install)\n\n```\n\n\n$ sh -c \"$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\"\n\n\n```\n\n \n\n### [](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#theme-installation)Theme installation\n\nI choosed [powerlevel10k](https://github.com/romkatv/powerlevel10k) probably one of the best and most flexible theme you can choose.  \nYou can easily change your terminal layout simply by rerun the installation command.\n\nStart to install [MesloLGS Fonts](https://github.com/romkatv/powerlevel10k#fonts)\n\n```\n\n\nMesloLGS NF Regular.ttf\nMesloLGS NF Bold.ttf\nMesloLGS NF Italic.ttf\nMesloLGS NF Bold Italic.ttf\n\n\n```\n\n \n\nThen install **powerlevel10k** itself\n\n```\n\n\ngit clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k\n\n\n```\n\n \n\nIn `~/.zshrc` set the ZSH theme to use:\n\n```\n\n\nZSH_THEME=\"powerlevel10k/powerlevel10k\" in ~/.zshrc.\n\n\n```\n\n \n\nYou will probably at least configure these two ZSH plugins:\n\n**zsh-syntax-highlighting** - Fish shell like syntax highlighting for Zsh. This is what makes my aliases/commands green above. If it's green then it's installed!  \n**zsh-autosuggestions** - Fish-like autosuggestions for zsh. Will show a preview of the last matching command while typing. Press right to use\n\nIn `~/.zshrc` set the ZSH plugins to use:\n\n```\n\n\nplugins=(\n  git\n  zsh-syntax-highlighting\n  zsh-autosuggestions\n)\n\n\n```\n\n \n\n**Restart your terminal** with Zsh\n\nNow you can run\n\n```\n\n\np10k configure\n\n\n```\n\n \n\nIf you have issue with fonts, check MesloLGS font is selected.  \n`Open iTerm2 → Preferences → Profiles → Text and set Font to MesloLGS NF`.\n\nFinally, if you want to include your existing bash aliases and functions:  \nIn `~/.zshrc` source your bash\\_profile just before the **export ZSH**\n\n```\n\n\nsource ~/.bash_profile\n\n```\n\n \n\n###   \n[](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#add-the-toolbar)  \nAdd the Toolbar  \n\n[![Image 75: Toolbar](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpfk2ihzdvd4hx6oas6mo.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpfk2ihzdvd4hx6oas6mo.png)\n\nOpen your `iterm2 > Profile > Session > Status bar enabled`  \n[![Image 76: iterm2 conf](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthnc8dsbdooisi2kr0m0.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthnc8dsbdooisi2kr0m0.png)\n\nSelect your widgets  \n[![Image 77: iterm2 status bar widgets](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Frwxz05tbpydattvh1uhs.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Frwxz05tbpydattvh1uhs.png)\n\n[](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#finished)Finished!\n------------------------------------------------------------------------------------------------\n\nI hope this small tutorial will help you to improve your setup. It is obviously not complete but easy enough to move on.\n\nTop comments (12)\n-----------------\n\nSubscribe\n\n    ![Image 78: pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)\n\nPersonal Trusted User\n\n[Create template](https://dev.to/settings/response-templates)Templates let you quickly answer FAQs or store snippets for re-use.\n\nSubmit Preview [Dismiss](https://dev.to/404.html)\n\n \n\n \n\n[![Image 79: zwacky profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F277593%2F29add9f7-4fe8-4608-8838-490dbeeb660c.jpg)](https://dev.to/zwacky)\n\n[Simon Wicki](https://dev.to/zwacky)\n\nSimon Wicki\n\n [![Image 80](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F277593%2F29add9f7-4fe8-4608-8838-490dbeeb660c.jpg)Simon Wicki](https://dev.to/zwacky)\n\nFollow\n\n💬 Frontend, webperf & non-fiction books 👨‍💻 Frontend at JustWatch 🔔 Creator of https://notyfy.co 🧙‍♂️ Freelancer\n\n*   Location\n    \n    Berlin\n    \n*   Joined\n    \n    Nov 22, 2019\n    \n\n• [Jan 9 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5a6)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5a6)\n\n*   Hide\n\nFirst time I saw the toolbar feature in a CLI, sweet. Time to toy around with that one.\n\nI can recommend these two tools to improve the Git experience on the CLI:\n\n*   [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy): better visualisation of `git diff`\n*   [git lg](http://garmoncheg.blogspot.com/2012/06/pretty-git-log.html): better visualisation than `git log`\n\n3 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l5a6)\n\n \n\n \n\n[![Image 81: thomasbredi profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F533935%2Ff5397200-9e46-4cca-8e20-017a11089281.png)](https://dev.to/thomasbredi)\n\n[Thomas Bredillet](https://dev.to/thomasbredi)\n\nThomas Bredillet\n\n [![Image 82](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F533935%2Ff5397200-9e46-4cca-8e20-017a11089281.png)Thomas Bredillet](https://dev.to/thomasbredi)\n\nFollow\n\n*   Joined\n    \n    Dec 5, 2020\n    \n\n• [Jan 9 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5b6)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5b6)\n\n*   Hide\n\nFor install this two plugins :\n\ngit clone [github.com/zsh-users/zsh-autosugge...](https://github.com/zsh-users/zsh-autosuggestions) ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions  \ngit clone [github.com/zsh-users/zsh-syntax-hi...](https://github.com/zsh-users/zsh-syntax-highlighting.git) ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting\n\n3 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l5b6)\n\n \n\n \n\n[![Image 83: sansk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)](https://dev.to/sansk)\n\n[Sangy K](https://dev.to/sansk)\n\nSangy K\n\n [![Image 84](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)Sangy K](https://dev.to/sansk)\n\nFollow\n\nFull-Stack Developer • An Introvert Coder • Tech Blogger • A Proud Mom\n\n*   Location\n    \n    Internet\n    \n*   Work\n    \n    Javascript Developer\n    \n*   Joined\n    \n    Sep 8, 2019\n    \n\n• [Jan 11 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l6h7)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l6h7)\n\n*   Hide\n\nIs there something like this for windows terminal/powershell?\n\n2 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l6h7)\n\n \n\n \n\n[![Image 85: zeeshan profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225799%2F83988eff-bb05-4461-b5a7-5398165ec0e1.jpeg)](https://dev.to/zeeshan)\n\n[Mohammed Zeeshan](https://dev.to/zeeshan)\n\nMohammed Zeeshan\n\n [![Image 86](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225799%2F83988eff-bb05-4461-b5a7-5398165ec0e1.jpeg)Mohammed Zeeshan](https://dev.to/zeeshan)\n\nFollow\n\nLanguage Learner\n\n*   Location\n    \n    Kerala, India\n    \n*   Work\n    \n    Frontend Engineer at Food Market Hub, Malaysia\n    \n*   Joined\n    \n    Sep 8, 2019\n    \n\n• [Jan 11 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l72g)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l72g)\n\n*   Hide\n\nohmyposh. scott hanselman has some oretty good articles and videos on setting this up\n\n3 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l72g)\n\n \n\n \n\n[![Image 87: sansk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)](https://dev.to/sansk)\n\n[Sangy K](https://dev.to/sansk)\n\nSangy K\n\n [![Image 88](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)Sangy K](https://dev.to/sansk)\n\nFollow\n\nFull-Stack Developer • An Introvert Coder • Tech Blogger • A Proud Mom\n\n*   Location\n    \n    Internet\n    \n*   Work\n    \n    Javascript Developer\n    \n*   Joined\n    \n    Sep 8, 2019\n    \n\n• [Jan 14 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l98b)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l98b)\n\n*   Hide\n\nThanks. I will check it out\n\n2 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l98b)\n\n \n\n \n\n[![Image 89: alagrede profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)](https://dev.to/alagrede)\n\n[Anthony Lagrede](https://dev.to/alagrede)\n\nAnthony Lagrede\n\n [![Image 90](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)Anthony Lagrede](https://dev.to/alagrede)\n\nFollow\n\nPassionate developer. Share skills and side projects. #web #DataScience stuff #freelance #Toulouse. Check out my last app: https://znote.io\n\n*   Location\n    \n    Toulouse\n    \n*   Joined\n    \n    Nov 28, 2017\n    \n\n• [Jan 11 '22 • Edited on Jan 11 • Edited](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l6ji)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l6ji)\n\n*   Hide\n\nHi Sangy,  \nYes, there is also ohmyposh. Take a look here for Windows 😊:  \n[dev.to/alagrede/terminal-setup-mak...](https://dev.to/alagrede/terminal-setup-make-your-windows-terminal-awesome-569i)\n\n2 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l6ji)\n\n \n\n \n\n[![Image 91: sansk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)](https://dev.to/sansk)\n\n[Sangy K](https://dev.to/sansk)\n\nSangy K\n\n [![Image 92](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225772%2F78f31625-6031-4cfb-925d-365d96574036.jpg)Sangy K](https://dev.to/sansk)\n\nFollow\n\nFull-Stack Developer • An Introvert Coder • Tech Blogger • A Proud Mom\n\n*   Location\n    \n    Internet\n    \n*   Work\n    \n    Javascript Developer\n    \n*   Joined\n    \n    Sep 8, 2019\n    \n\n• [Jan 14 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l98a)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l98a)\n\n*   Hide\n\nThanks. I will check it out\n\n1 like Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l98a)\n\n \n\n \n\n[![Image 93: gnsp profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F129205%2F21b17be8-1d7b-492e-aac7-7e73215b4266.jpeg)](https://dev.to/gnsp)\n\n[Ganesh Prasad](https://dev.to/gnsp)\n\nGanesh Prasad\n\n [![Image 94](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F129205%2F21b17be8-1d7b-492e-aac7-7e73215b4266.jpeg)Ganesh Prasad](https://dev.to/gnsp)\n\nFollow\n\nInventor of Ironscript\n\n*   Location\n    \n    Odisha, India\n    \n*   Education\n    \n    National Institute of Technology, Rourkela\n    \n*   Work\n    \n    Software Engineer at Google\n    \n*   Joined\n    \n    Jan 16, 2019\n    \n\n• [Jan 10 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5ng)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l5ng)\n\n*   Hide\n\nI have been using the same setup for last 5 years now. I use the font firacode though.\n\n3 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l5ng)\n\n \n\n \n\n[![Image 95: chideraike profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F523772%2F965eb653-cda8-4073-bd0d-8058e45241ce.png)](https://dev.to/chideraike)\n\n[Chidera](https://dev.to/chideraike)\n\nChidera\n\n [![Image 96](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F523772%2F965eb653-cda8-4073-bd0d-8058e45241ce.png)Chidera](https://dev.to/chideraike)\n\nFollow\n\nI build Web & Mobile Applications\n\n*   Location\n    \n    Lagos, Nigeria\n    \n*   Joined\n    \n    Dec 1, 2020\n    \n\n• [Jan 10 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l64p)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1l64p)\n\n*   Hide\n\nThanks for this, I found it helpful\n\n2 likes Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1l64p)\n\n \n\n \n\n[![Image 97: devphu profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F800864%2F1e510465-8d1f-4ba4-bd32-3e04243eb40f.jpeg)](https://dev.to/devphu)\n\n[PhanPhú](https://dev.to/devphu)\n\nPhanPhú\n\n [![Image 98](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F800864%2F1e510465-8d1f-4ba4-bd32-3e04243eb40f.jpeg)PhanPhú](https://dev.to/devphu)\n\nFollow\n\n*   Joined\n    \n    Jan 21, 2022\n    \n\n• [Jan 21 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1lei6)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1lei6)\n\n*   Hide\n\nit has work with mac chip m1?\n\n1 like Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1lei6)\n\n \n\n \n\n[![Image 99: alagrede profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)](https://dev.to/alagrede)\n\n[Anthony Lagrede](https://dev.to/alagrede)\n\nAnthony Lagrede\n\n [![Image 100](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)Anthony Lagrede](https://dev.to/alagrede)\n\nFollow\n\nPassionate developer. Share skills and side projects. #web #DataScience stuff #freelance #Toulouse. Check out my last app: https://znote.io\n\n*   Location\n    \n    Toulouse\n    \n*   Joined\n    \n    Nov 28, 2017\n    \n\n• [Jan 24 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1lg9k)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1lg9k)\n\n*   Hide\n\nHi [@devphu](https://dev.to/devphu), yes of course.\n\n1 like Like [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1lg9k)\n\n \n\n \n\n[![Image 101: rannn505 profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F791199%2F830fe8be-7090-4f15-9014-fa17e03e02ab.jpeg)](https://dev.to/rannn505)\n\n[Ran Cohen](https://dev.to/rannn505)\n\nRan Cohen\n\n [![Image 102](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F791199%2F830fe8be-7090-4f15-9014-fa17e03e02ab.jpeg)Ran Cohen](https://dev.to/rannn505)\n\nFollow\n\nhttps://www.linkedin.com/in/rannn505/\n\n*   Email\n    \n    [rannn505@outlook.com](mailto:rannn505@outlook.com)\n    \n*   Work\n    \n    CTO & Co-Founder at Configu\n    \n*   Joined\n    \n    Jan 12, 2022\n    \n\n• [Feb 9 '22](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1m1f2)\n\n*   [Copy link](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#comment-1m1f2)\n\n*   Hide\n\nCheck out [my post](https://dev.to/rannn505/macos-awesome-terminal-519n) for more awesome features 🦄\n\nLike [Reply](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments/new/1m1f2)\n\n[View full discussion (12 comments)](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc/comments)\n\n[Code of Conduct](https://dev.to/code-of-conduct) • [Report abuse](https://dev.to/report-abuse)\n\nAre you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](https://dev.to/alagrede/terminal-setup-make-your-mac-terminal-awesome-4ecc#).\n\nHide child comments as well\n\nConfirm\n\nFor further actions, you may consider blocking this person and/or [reporting abuse](https://dev.to/report-abuse)\n\nRead next\n---------\n\n[![Image 103: desk_track profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F856539%2F0a7fac15-9810-4cd4-8ca9-05bd29eb6459.jpg) ### How work from home monitoring tools prevent distractions and increase focus DeskTrack - Jan 20](https://dev.to/desk_track/how-work-from-home-monitoring-tools-prevent-distractions-and-increase-focus-4fll)[![Image 104: asiaelbow2 profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2736881%2F61a08758-65a9-418f-9170-81b97a6092ad.png) ### Exploring the Power of Internet Marketing in Today’s Marketplace Seerup Carlson - Jan 20](https://dev.to/asiaelbow2/exploring-the-power-of-internet-marketing-in-todays-marketplace-93p)[![Image 105: heartgroup7 profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2727326%2F1f49fed7-96ae-46bd-8474-1582821ace0d.png) ### Sports training in Asia along with Italy: A comparison evaluation. Yang Thorsen - Jan 20](https://dev.to/heartgroup7/sports-training-in-asia-along-with-italy-a-comparison-evaluation-2f51)[![Image 106: veiledvirtue_042df28a9877 profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2713920%2Ff1aca135-eab8-4f3f-85a4-7ba16036499d.png) ### Boosting Your Business Online: Expert SEO Strategies for Maidenhead Companies VeiledVirtue - Jan 20](https://dev.to/veiledvirtue_042df28a9877/boosting-your-business-online-expert-seo-strategies-for-maidenhead-companies-555)\n\n [![Image 107](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F47181%2Fbd0719f9-6b9a-4729-ac61-f9e7379c609a.jpg)Anthony Lagrede](https://dev.to/alagrede)\n\nFollow\n\nPassionate developer. Share skills and side projects. #web #DataScience stuff #freelance #Toulouse. Check out my last app: https://znote.io\n\n*   Location\n    \n    Toulouse\n    \n*   Joined\n    \n    Nov 28, 2017\n    \n\n### More from [Anthony Lagrede](https://dev.to/alagrede)\n\n[Terminal Setup - Make your Windows terminal awesome #terminal #ohmyposh #bash #dev](https://dev.to/alagrede/terminal-setup-make-your-windows-terminal-awesome-569i)\n\nThank you to our Diamond Sponsor [Neon](https://neon.tech/) for supporting our community.\n\n[DEV Community](https://dev.to/) — A constructive and inclusive social network for software developers. With you every step of your journey.\n\n*   [Home](https://dev.to/)\n*   [DEV++](https://dev.to/++)\n*   [Podcasts](https://dev.to/pod)\n*   [Videos](https://dev.to/videos)\n*   [Tags](https://dev.to/tags)\n*   [DEV Help](https://dev.to/help)\n*   [Forem Shop](https://shop.forem.com/)\n*   [Advertise on DEV](https://dev.to/advertise)\n*   [DEV Challenges](https://dev.to/challenges)\n*   [DEV Showcase](https://dev.to/showcase)\n*   [About](https://dev.to/about)\n*   [Contact](https://dev.to/contact)\n*   [Free Postgres Database](https://dev.to/free-postgres-database-tier)\n*   [Software comparisons](https://dev.to/software-comparisons)\n\n*   [Code of Conduct](https://dev.to/code-of-conduct)\n*   [Privacy Policy](https://dev.to/privacy)\n*   [Terms of use](https://dev.to/terms)\n\nBuilt on [Forem](https://www.forem.com/) — the [open source](https://dev.to/t/opensource) software that powers [DEV](https://dev.to/) and other inclusive communities.\n\nMade with love and [Ruby on Rails](https://dev.to/t/rails). DEV Community © 2016 - 2025.\n\n![Image 108: DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)\n\nWe're a place where coders share, stay up-to-date and grow their careers.\n\n[Log in](https://dev.to/enter) [Create account](https://dev.to/enter?state=new-user)\n\n![Image 109](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![Image 110](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![Image 111](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![Image 112](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![Image 113](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)",
  "publishedTime": "2022-01-07T16:48:50Z",
  "usage": {
    "tokens": 10256
  }
}
```
