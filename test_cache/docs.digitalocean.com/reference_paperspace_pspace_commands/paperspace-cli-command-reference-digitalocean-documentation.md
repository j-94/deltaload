---
title: Paperspace CLI Command Reference | DigitalOcean Documentation
description: Programmatically manage resources using the Paperspace Command Line Interface.
url: https://docs.digitalocean.com/reference/paperspace/pspace/commands/
timestamp: 2025-01-20T16:19:28.716Z
domain: docs.digitalocean.com
path: reference_paperspace_pspace_commands
---

# Paperspace CLI Command Reference | DigitalOcean Documentation


Programmatically manage resources using the Paperspace Command Line Interface.


## Content

Paperspace CLI Command Reference | DigitalOcean Documentation
===============

*   [](https://www.digitalocean.com/)
*   [](https://docs.digitalocean.com/)

*   [Platform](https://docs.digitalocean.com/platform)
*   [Products](https://docs.digitalocean.com/products)
*   [Reference](https://docs.digitalocean.com/reference)
*   [Support](https://docs.digitalocean.com/support)
*   Search Docs /
*   [Sign Up](https://cloud.digitalocean.com/registrations/new)
*   [](https://docs.digitalocean.com/reference/paperspace/pspace/commands/#)

*   [Platform](https://docs.digitalocean.com/platform)
*   [Products](https://docs.digitalocean.com/products)
*   [Reference](https://docs.digitalocean.com/reference)
*   [Support](https://docs.digitalocean.com/support)

*    [![Image 34](https://docs.digitalocean.com/images/icons/reference.svg) Reference](https://docs.digitalocean.com/reference/)
    
    *    [![Image 35](https://docs.digitalocean.com/images/icons/doctl.svg) doctl CLI](https://docs.digitalocean.com/reference/doctl/)
        
    *    [![Image 36](https://docs.digitalocean.com/images/icons/api.svg) DigitalOcean APIs](https://docs.digitalocean.com/reference/api/)
        
    *    [![Image 37](https://docs.digitalocean.com/images/icons/ml.svg) Paperspace](https://docs.digitalocean.com/reference/paperspace/)
        
        *   [API Keys](https://docs.digitalocean.com/reference/paperspace/api-keys/)
            
        *   [Paperspace API](https://docs.digitalocean.com/reference/paperspace/pspace/api-reference/)
            
        *   [Paperspace CLI Preview](https://docs.digitalocean.com/reference/paperspace/pspace/)
            
            *   [Install Paperspace CLI Preview](https://docs.digitalocean.com/reference/paperspace/pspace/install/)
                
            *   [Command Reference](https://docs.digitalocean.com/reference/paperspace/pspace/commands/)
                
                *   [autoscaling-group](https://docs.digitalocean.com/reference/paperspace/pspace/commands/autoscaling-group/)
                    
                *   [completion](https://docs.digitalocean.com/reference/paperspace/pspace/commands/completion/)
                    
                *   [config](https://docs.digitalocean.com/reference/paperspace/pspace/commands/config/)
                    
                *   [console](https://docs.digitalocean.com/reference/paperspace/pspace/commands/console/)
                    
                *   [deployment](https://docs.digitalocean.com/reference/paperspace/pspace/commands/deployment/)
                    
                *   [docs](https://docs.digitalocean.com/reference/paperspace/pspace/commands/docs/)
                    
                *   [help](https://docs.digitalocean.com/reference/paperspace/pspace/commands/help/)
                    
                *   [init](https://docs.digitalocean.com/reference/paperspace/pspace/commands/init/)
                    
                *   [login](https://docs.digitalocean.com/reference/paperspace/pspace/commands/login/)
                    
                *   [logout](https://docs.digitalocean.com/reference/paperspace/pspace/commands/logout/)
                    
                *   [machine](https://docs.digitalocean.com/reference/paperspace/pspace/commands/machine/)
                    
                *   [machine-event](https://docs.digitalocean.com/reference/paperspace/pspace/commands/machine-event/)
                    
                *   [private-network](https://docs.digitalocean.com/reference/paperspace/pspace/commands/private-network/)
                    
                *   [project](https://docs.digitalocean.com/reference/paperspace/pspace/commands/project/)
                    
                *   [public-ip](https://docs.digitalocean.com/reference/paperspace/pspace/commands/public-ip/)
                    
                *   [secret](https://docs.digitalocean.com/reference/paperspace/pspace/commands/secret/)
                    
                *   [shared-drive](https://docs.digitalocean.com/reference/paperspace/pspace/commands/shared-drive/)
                    
                *   [signup](https://docs.digitalocean.com/reference/paperspace/pspace/commands/signup/)
                    
                *   [snapshot](https://docs.digitalocean.com/reference/paperspace/pspace/commands/snapshot/)
                    
                *   [startup-script](https://docs.digitalocean.com/reference/paperspace/pspace/commands/startup-script/)
                    
                *   [template](https://docs.digitalocean.com/reference/paperspace/pspace/commands/template/)
                    
                *   [up](https://docs.digitalocean.com/reference/paperspace/pspace/commands/up/)
                    
                *   [upgrade](https://docs.digitalocean.com/reference/paperspace/pspace/commands/upgrade/)
                    
                *   [version](https://docs.digitalocean.com/reference/paperspace/pspace/commands/version/)
                    
        *   [Legacy Tools](https://docs.digitalocean.com/reference/paperspace/legacy/)
            
    *    [![Image 38](https://docs.digitalocean.com/images/icons/ansible.svg) Ansible](https://docs.digitalocean.com/reference/ansible/)
        
    *    [![Image 39](https://docs.digitalocean.com/images/icons/terraform.svg) Terraform](https://docs.digitalocean.com/reference/terraform/)
        
    *    [![Image 40](https://docs.digitalocean.com/images/icons/python.svg) PyDo](https://docs.digitalocean.com/reference/pydo/)
        
    *    [![Image 41](https://docs.digitalocean.com/images/icons/libraries.svg) Libraries](https://docs.digitalocean.com/reference/libraries/)
        
    *    [![Image 42](https://docs.digitalocean.com/images/icons/opensource.svg) Open Source](https://docs.digitalocean.com/reference/opensource/)
        

[Reference](https://docs.digitalocean.com/reference/)  \> [Paperspace](https://docs.digitalocean.com/reference/paperspace/)  \> [Paperspace CLI](https://docs.digitalocean.com/reference/paperspace/pspace/)  \> Command Reference 

Was this page helpful?

[Give Feedback](https://docs.digitalocean.com/feedback)

Paperspace CLI Command Reference Private Preview
================================================

Validated on 14 Dec 2023 • Last edited on 1 Aug 2024

![Image 43](https://docs.digitalocean.com/images/icons/default.svg)

[autoscaling-group](https://docs.digitalocean.com/reference/paperspace/pspace/commands/autoscaling-group/)

Interact programmatically with Paperspace using the Autoscaling group CLI.

![Image 44](https://docs.digitalocean.com/images/icons/default.svg)

[completion](https://docs.digitalocean.com/reference/paperspace/pspace/commands/completion/)

Interact programmatically with Paperspace using the Completion CLI.

![Image 45](https://docs.digitalocean.com/images/icons/default.svg)

[config](https://docs.digitalocean.com/reference/paperspace/pspace/commands/config/)

Interact programmatically with Paperspace using the Config CLI.

![Image 46](https://docs.digitalocean.com/images/icons/default.svg)

[console](https://docs.digitalocean.com/reference/paperspace/pspace/commands/console/)

Interact programmatically with Paperspace using the Console CLI.

![Image 47](https://docs.digitalocean.com/images/icons/default.svg)

[deployment](https://docs.digitalocean.com/reference/paperspace/pspace/commands/deployment/)

Interact programmatically with Paperspace using the Deployment CLI.

![Image 48](https://docs.digitalocean.com/images/icons/default.svg)

[docs](https://docs.digitalocean.com/reference/paperspace/pspace/commands/docs/)

Interact programmatically with Paperspace using the Docs CLI.

![Image 49](https://docs.digitalocean.com/images/icons/default.svg)

[help](https://docs.digitalocean.com/reference/paperspace/pspace/commands/help/)

Interact programmatically with Paperspace using the Help CLI.

![Image 50](https://docs.digitalocean.com/images/icons/default.svg)

[init](https://docs.digitalocean.com/reference/paperspace/pspace/commands/init/)

Interact programmatically with Paperspace using the Init CLI.

![Image 51](https://docs.digitalocean.com/images/icons/default.svg)

[login](https://docs.digitalocean.com/reference/paperspace/pspace/commands/login/)

Interact programmatically with Paperspace using the Login CLI.

![Image 52](https://docs.digitalocean.com/images/icons/default.svg)

[logout](https://docs.digitalocean.com/reference/paperspace/pspace/commands/logout/)

Interact programmatically with Paperspace using the Logout CLI.

![Image 53](https://docs.digitalocean.com/images/icons/default.svg)

[machine](https://docs.digitalocean.com/reference/paperspace/pspace/commands/machine/)

Interact programmatically with Paperspace using the Machine CLI.

![Image 54](https://docs.digitalocean.com/images/icons/default.svg)

[machine-event](https://docs.digitalocean.com/reference/paperspace/pspace/commands/machine-event/)

Interact programmatically with Paperspace using the Machine event CLI.

![Image 55](https://docs.digitalocean.com/images/icons/default.svg)

[private-network](https://docs.digitalocean.com/reference/paperspace/pspace/commands/private-network/)

Interact programmatically with Paperspace using the Private network CLI.

![Image 56](https://docs.digitalocean.com/images/icons/default.svg)

[project](https://docs.digitalocean.com/reference/paperspace/pspace/commands/project/)

Interact programmatically with Paperspace using the Project CLI.

![Image 57](https://docs.digitalocean.com/images/icons/default.svg)

[public-ip](https://docs.digitalocean.com/reference/paperspace/pspace/commands/public-ip/)

Interact programmatically with Paperspace using the Public IP CLI.

![Image 58](https://docs.digitalocean.com/images/icons/default.svg)

[secret](https://docs.digitalocean.com/reference/paperspace/pspace/commands/secret/)

Interact programmatically with Paperspace using the Secret CLI.

![Image 59](https://docs.digitalocean.com/images/icons/default.svg)

[shared-drive](https://docs.digitalocean.com/reference/paperspace/pspace/commands/shared-drive/)

Interact programmatically with Paperspace using the Shared Drive CLI.

![Image 60](https://docs.digitalocean.com/images/icons/default.svg)

[signup](https://docs.digitalocean.com/reference/paperspace/pspace/commands/signup/)

Interact programmatically with Paperspace using the Signup CLI.

![Image 61](https://docs.digitalocean.com/images/icons/default.svg)

[snapshot](https://docs.digitalocean.com/reference/paperspace/pspace/commands/snapshot/)

Interact programmatically with Paperspace using the Snapshot CLI.

![Image 62](https://docs.digitalocean.com/images/icons/default.svg)

[startup-script](https://docs.digitalocean.com/reference/paperspace/pspace/commands/startup-script/)

Interact programmatically with Paperspace using the Startup script CLI.

![Image 63](https://docs.digitalocean.com/images/icons/default.svg)

[template](https://docs.digitalocean.com/reference/paperspace/pspace/commands/template/)

Interact programmatically with Paperspace using the Template CLI.

![Image 64](https://docs.digitalocean.com/images/icons/default.svg)

[up](https://docs.digitalocean.com/reference/paperspace/pspace/commands/up/)

Interact programmatically with Paperspace using the Up CLI.

![Image 65](https://docs.digitalocean.com/images/icons/default.svg)

[upgrade](https://docs.digitalocean.com/reference/paperspace/pspace/commands/upgrade/)

Interact programmatically with Paperspace using the Upgrade CLI.

![Image 66](https://docs.digitalocean.com/images/icons/default.svg)

[version](https://docs.digitalocean.com/reference/paperspace/pspace/commands/version/)

Interact programmatically with Paperspace using the Version CLI.

Share this article!

[Control Panel](https://cloud.digitalocean.com/) [Blog](https://blog.digitalocean.com/) [Pricing](https://www.digitalocean.com/pricing) [Careers](https://www.digitalocean.com/company/careers) [Terms](https://www.digitalocean.com/legal/terms-of-service-agreement) [Privacy](https://www.digitalocean.com/legal/privacy-policy) [Status](https://status.digitalocean.com/) [API Docs](https://docs.digitalocean.com/reference/api/) [Tutorials](https://www.digitalocean.com/community) [Support](https://docs.digitalocean.com/support/)

 

### We can't find any results for your search.

Please try using alternative keywords or simplifying your search terms.

Loading...

Product Docs
------------

### We can't find any results for your search.

Please try using alternative keywords or simplifying your search terms.

Marketplace
-----------

DigitalOcean Blog
-----------------

Community
---------

navigate go exit

## Metadata

```json
{
  "title": "Paperspace CLI Command Reference | DigitalOcean Documentation",
  "description": "Programmatically manage resources using the Paperspace Command Line Interface.",
  "url": "https://docs.digitalocean.com/reference/paperspace/pspace/commands/",
  "content": "Paperspace CLI Command Reference | DigitalOcean Documentation\n===============\n\n*   [](https://www.digitalocean.com/)\n*   [](https://docs.digitalocean.com/)\n\n*   [Platform](https://docs.digitalocean.com/platform)\n*   [Products](https://docs.digitalocean.com/products)\n*   [Reference](https://docs.digitalocean.com/reference)\n*   [Support](https://docs.digitalocean.com/support)\n*   Search Docs /\n*   [Sign Up](https://cloud.digitalocean.com/registrations/new)\n*   [](https://docs.digitalocean.com/reference/paperspace/pspace/commands/#)\n\n*   [Platform](https://docs.digitalocean.com/platform)\n*   [Products](https://docs.digitalocean.com/products)\n*   [Reference](https://docs.digitalocean.com/reference)\n*   [Support](https://docs.digitalocean.com/support)\n\n*    [![Image 34](https://docs.digitalocean.com/images/icons/reference.svg) Reference](https://docs.digitalocean.com/reference/)\n    \n    *    [![Image 35](https://docs.digitalocean.com/images/icons/doctl.svg) doctl CLI](https://docs.digitalocean.com/reference/doctl/)\n        \n    *    [![Image 36](https://docs.digitalocean.com/images/icons/api.svg) DigitalOcean APIs](https://docs.digitalocean.com/reference/api/)\n        \n    *    [![Image 37](https://docs.digitalocean.com/images/icons/ml.svg) Paperspace](https://docs.digitalocean.com/reference/paperspace/)\n        \n        *   [API Keys](https://docs.digitalocean.com/reference/paperspace/api-keys/)\n            \n        *   [Paperspace API](https://docs.digitalocean.com/reference/paperspace/pspace/api-reference/)\n            \n        *   [Paperspace CLI Preview](https://docs.digitalocean.com/reference/paperspace/pspace/)\n            \n            *   [Install Paperspace CLI Preview](https://docs.digitalocean.com/reference/paperspace/pspace/install/)\n                \n            *   [Command Reference](https://docs.digitalocean.com/reference/paperspace/pspace/commands/)\n                \n                *   [autoscaling-group](https://docs.digitalocean.com/reference/paperspace/pspace/commands/autoscaling-group/)\n                    \n                *   [completion](https://docs.digitalocean.com/reference/paperspace/pspace/commands/completion/)\n                    \n                *   [config](https://docs.digitalocean.com/reference/paperspace/pspace/commands/config/)\n                    \n                *   [console](https://docs.digitalocean.com/reference/paperspace/pspace/commands/console/)\n                    \n                *   [deployment](https://docs.digitalocean.com/reference/paperspace/pspace/commands/deployment/)\n                    \n                *   [docs](https://docs.digitalocean.com/reference/paperspace/pspace/commands/docs/)\n                    \n                *   [help](https://docs.digitalocean.com/reference/paperspace/pspace/commands/help/)\n                    \n                *   [init](https://docs.digitalocean.com/reference/paperspace/pspace/commands/init/)\n                    \n                *   [login](https://docs.digitalocean.com/reference/paperspace/pspace/commands/login/)\n                    \n                *   [logout](https://docs.digitalocean.com/reference/paperspace/pspace/commands/logout/)\n                    \n                *   [machine](https://docs.digitalocean.com/reference/paperspace/pspace/commands/machine/)\n                    \n                *   [machine-event](https://docs.digitalocean.com/reference/paperspace/pspace/commands/machine-event/)\n                    \n                *   [private-network](https://docs.digitalocean.com/reference/paperspace/pspace/commands/private-network/)\n                    \n                *   [project](https://docs.digitalocean.com/reference/paperspace/pspace/commands/project/)\n                    \n                *   [public-ip](https://docs.digitalocean.com/reference/paperspace/pspace/commands/public-ip/)\n                    \n                *   [secret](https://docs.digitalocean.com/reference/paperspace/pspace/commands/secret/)\n                    \n                *   [shared-drive](https://docs.digitalocean.com/reference/paperspace/pspace/commands/shared-drive/)\n                    \n                *   [signup](https://docs.digitalocean.com/reference/paperspace/pspace/commands/signup/)\n                    \n                *   [snapshot](https://docs.digitalocean.com/reference/paperspace/pspace/commands/snapshot/)\n                    \n                *   [startup-script](https://docs.digitalocean.com/reference/paperspace/pspace/commands/startup-script/)\n                    \n                *   [template](https://docs.digitalocean.com/reference/paperspace/pspace/commands/template/)\n                    \n                *   [up](https://docs.digitalocean.com/reference/paperspace/pspace/commands/up/)\n                    \n                *   [upgrade](https://docs.digitalocean.com/reference/paperspace/pspace/commands/upgrade/)\n                    \n                *   [version](https://docs.digitalocean.com/reference/paperspace/pspace/commands/version/)\n                    \n        *   [Legacy Tools](https://docs.digitalocean.com/reference/paperspace/legacy/)\n            \n    *    [![Image 38](https://docs.digitalocean.com/images/icons/ansible.svg) Ansible](https://docs.digitalocean.com/reference/ansible/)\n        \n    *    [![Image 39](https://docs.digitalocean.com/images/icons/terraform.svg) Terraform](https://docs.digitalocean.com/reference/terraform/)\n        \n    *    [![Image 40](https://docs.digitalocean.com/images/icons/python.svg) PyDo](https://docs.digitalocean.com/reference/pydo/)\n        \n    *    [![Image 41](https://docs.digitalocean.com/images/icons/libraries.svg) Libraries](https://docs.digitalocean.com/reference/libraries/)\n        \n    *    [![Image 42](https://docs.digitalocean.com/images/icons/opensource.svg) Open Source](https://docs.digitalocean.com/reference/opensource/)\n        \n\n[Reference](https://docs.digitalocean.com/reference/)  \\> [Paperspace](https://docs.digitalocean.com/reference/paperspace/)  \\> [Paperspace CLI](https://docs.digitalocean.com/reference/paperspace/pspace/)  \\> Command Reference \n\nWas this page helpful?\n\n[Give Feedback](https://docs.digitalocean.com/feedback)\n\nPaperspace CLI Command Reference Private Preview\n================================================\n\nValidated on 14 Dec 2023 • Last edited on 1 Aug 2024\n\n![Image 43](https://docs.digitalocean.com/images/icons/default.svg)\n\n[autoscaling-group](https://docs.digitalocean.com/reference/paperspace/pspace/commands/autoscaling-group/)\n\nInteract programmatically with Paperspace using the Autoscaling group CLI.\n\n![Image 44](https://docs.digitalocean.com/images/icons/default.svg)\n\n[completion](https://docs.digitalocean.com/reference/paperspace/pspace/commands/completion/)\n\nInteract programmatically with Paperspace using the Completion CLI.\n\n![Image 45](https://docs.digitalocean.com/images/icons/default.svg)\n\n[config](https://docs.digitalocean.com/reference/paperspace/pspace/commands/config/)\n\nInteract programmatically with Paperspace using the Config CLI.\n\n![Image 46](https://docs.digitalocean.com/images/icons/default.svg)\n\n[console](https://docs.digitalocean.com/reference/paperspace/pspace/commands/console/)\n\nInteract programmatically with Paperspace using the Console CLI.\n\n![Image 47](https://docs.digitalocean.com/images/icons/default.svg)\n\n[deployment](https://docs.digitalocean.com/reference/paperspace/pspace/commands/deployment/)\n\nInteract programmatically with Paperspace using the Deployment CLI.\n\n![Image 48](https://docs.digitalocean.com/images/icons/default.svg)\n\n[docs](https://docs.digitalocean.com/reference/paperspace/pspace/commands/docs/)\n\nInteract programmatically with Paperspace using the Docs CLI.\n\n![Image 49](https://docs.digitalocean.com/images/icons/default.svg)\n\n[help](https://docs.digitalocean.com/reference/paperspace/pspace/commands/help/)\n\nInteract programmatically with Paperspace using the Help CLI.\n\n![Image 50](https://docs.digitalocean.com/images/icons/default.svg)\n\n[init](https://docs.digitalocean.com/reference/paperspace/pspace/commands/init/)\n\nInteract programmatically with Paperspace using the Init CLI.\n\n![Image 51](https://docs.digitalocean.com/images/icons/default.svg)\n\n[login](https://docs.digitalocean.com/reference/paperspace/pspace/commands/login/)\n\nInteract programmatically with Paperspace using the Login CLI.\n\n![Image 52](https://docs.digitalocean.com/images/icons/default.svg)\n\n[logout](https://docs.digitalocean.com/reference/paperspace/pspace/commands/logout/)\n\nInteract programmatically with Paperspace using the Logout CLI.\n\n![Image 53](https://docs.digitalocean.com/images/icons/default.svg)\n\n[machine](https://docs.digitalocean.com/reference/paperspace/pspace/commands/machine/)\n\nInteract programmatically with Paperspace using the Machine CLI.\n\n![Image 54](https://docs.digitalocean.com/images/icons/default.svg)\n\n[machine-event](https://docs.digitalocean.com/reference/paperspace/pspace/commands/machine-event/)\n\nInteract programmatically with Paperspace using the Machine event CLI.\n\n![Image 55](https://docs.digitalocean.com/images/icons/default.svg)\n\n[private-network](https://docs.digitalocean.com/reference/paperspace/pspace/commands/private-network/)\n\nInteract programmatically with Paperspace using the Private network CLI.\n\n![Image 56](https://docs.digitalocean.com/images/icons/default.svg)\n\n[project](https://docs.digitalocean.com/reference/paperspace/pspace/commands/project/)\n\nInteract programmatically with Paperspace using the Project CLI.\n\n![Image 57](https://docs.digitalocean.com/images/icons/default.svg)\n\n[public-ip](https://docs.digitalocean.com/reference/paperspace/pspace/commands/public-ip/)\n\nInteract programmatically with Paperspace using the Public IP CLI.\n\n![Image 58](https://docs.digitalocean.com/images/icons/default.svg)\n\n[secret](https://docs.digitalocean.com/reference/paperspace/pspace/commands/secret/)\n\nInteract programmatically with Paperspace using the Secret CLI.\n\n![Image 59](https://docs.digitalocean.com/images/icons/default.svg)\n\n[shared-drive](https://docs.digitalocean.com/reference/paperspace/pspace/commands/shared-drive/)\n\nInteract programmatically with Paperspace using the Shared Drive CLI.\n\n![Image 60](https://docs.digitalocean.com/images/icons/default.svg)\n\n[signup](https://docs.digitalocean.com/reference/paperspace/pspace/commands/signup/)\n\nInteract programmatically with Paperspace using the Signup CLI.\n\n![Image 61](https://docs.digitalocean.com/images/icons/default.svg)\n\n[snapshot](https://docs.digitalocean.com/reference/paperspace/pspace/commands/snapshot/)\n\nInteract programmatically with Paperspace using the Snapshot CLI.\n\n![Image 62](https://docs.digitalocean.com/images/icons/default.svg)\n\n[startup-script](https://docs.digitalocean.com/reference/paperspace/pspace/commands/startup-script/)\n\nInteract programmatically with Paperspace using the Startup script CLI.\n\n![Image 63](https://docs.digitalocean.com/images/icons/default.svg)\n\n[template](https://docs.digitalocean.com/reference/paperspace/pspace/commands/template/)\n\nInteract programmatically with Paperspace using the Template CLI.\n\n![Image 64](https://docs.digitalocean.com/images/icons/default.svg)\n\n[up](https://docs.digitalocean.com/reference/paperspace/pspace/commands/up/)\n\nInteract programmatically with Paperspace using the Up CLI.\n\n![Image 65](https://docs.digitalocean.com/images/icons/default.svg)\n\n[upgrade](https://docs.digitalocean.com/reference/paperspace/pspace/commands/upgrade/)\n\nInteract programmatically with Paperspace using the Upgrade CLI.\n\n![Image 66](https://docs.digitalocean.com/images/icons/default.svg)\n\n[version](https://docs.digitalocean.com/reference/paperspace/pspace/commands/version/)\n\nInteract programmatically with Paperspace using the Version CLI.\n\nShare this article!\n\n[Control Panel](https://cloud.digitalocean.com/) [Blog](https://blog.digitalocean.com/) [Pricing](https://www.digitalocean.com/pricing) [Careers](https://www.digitalocean.com/company/careers) [Terms](https://www.digitalocean.com/legal/terms-of-service-agreement) [Privacy](https://www.digitalocean.com/legal/privacy-policy) [Status](https://status.digitalocean.com/) [API Docs](https://docs.digitalocean.com/reference/api/) [Tutorials](https://www.digitalocean.com/community) [Support](https://docs.digitalocean.com/support/)\n\n \n\n### We can't find any results for your search.\n\nPlease try using alternative keywords or simplifying your search terms.\n\nLoading...\n\nProduct Docs\n------------\n\n### We can't find any results for your search.\n\nPlease try using alternative keywords or simplifying your search terms.\n\nMarketplace\n-----------\n\nDigitalOcean Blog\n-----------------\n\nCommunity\n---------\n\nnavigate go exit",
  "usage": {
    "tokens": 2866
  }
}
```
