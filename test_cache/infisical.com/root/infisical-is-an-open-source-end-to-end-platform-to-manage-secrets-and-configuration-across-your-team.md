---
title: Infisical is an open-source end-to-end platform to manage secrets and configuration across your team and infrastructure.
description: All-in-one platform to securely manage application configuration and secrets across your team and infrastructure. Used by Fortune 500 enterprises, international governments, and fastest-growing startups. Save time and boost security.
url: https://infisical.com
timestamp: 2025-01-20T15:43:24.544Z
domain: infisical.com
path: root
---

# Infisical is an open-source end-to-end platform to manage secrets and configuration across your team and infrastructure.


All-in-one platform to securely manage application configuration and secrets across your team and infrastructure. Used by Fortune 500 enterprises, international governments, and fastest-growing startups. Save time and boost security.


## Content

Everyone has secrets. We secure over  
every day.

Start quickly,  
scale effortlessly. Secure your applications without any hassle.

1import { InfisicalClient, LogLevel } from "@infisical/sdk";

2

3const client = new InfisicalClient({

4clientId: "YOUR\_CLIENT\_ID",

5clientSecret: "YOUR\_CLIENT\_SECRET"

6});

7

8const secret \= await client.getSecret({

9projectId: "PROJECT\_ID",

10environment: "prod",

11secretName: "POSTGRES\_TOKEN"

12});

Start quickly,  
scale effortlessly. Secure your applications without any hassle. [Quickstart Guide for Node](https://infisical.com/docs/sdks/languages/node)

Building secure applications can be Infisical provides a set of tools to automate your security in a “security shift left” way.

[](https://infisical.com/docs/cli/usage)Switch from .env files to Infisical CLI. Keep secrets always in sync with your teammates. Works with any platform and framework.

(base) user@MacBook % infisical run \--env=dev \-- npm run devInjecting 13 Infisical secrets into your application process...

[](https://infisical.com/docs/documentation/getting-started/platform)A simple interface to manage your secrets, environments, and applications.

[](https://infisical.com/docs/cli/scanning-overview#scanning)Automatically identify and prevent secret leaks to git using Infisical's continuous monitoring and precommit checks. Supports 150+ secret types.

(base) user@MacBook % git commit -m "Code Update"Warning: Hardcoded secret detected – commit blocked by Infisical.File: backend/src/json/integrations.json Line: 5

[](https://infisical.com/docs/documentation/platform/pit-recovery)Track every change of your secrets and rollback to any point in time.

1

Value: 2B7E151628AED2A6ABF7158809CF4F3CTimestamp: March 1st at 12:03amBy: user@example.com

2

Value: 8E73B0F7DA0E6452C810F32B809079E56Timestamp: March 3rd at 7:45amBy: machine@example.com

3

Value: 603DEB1015CA71BE2B73AEF0857D77811Timestamp: March 7th at 4:23pmBy: user2@example.com

[Secret Rotation and Dynamic Secrets](https://infisical.com/docs/documentation/platform/secret-rotation/overview)Eliminate long-lasting credentials to reduce risk of breach and credential leaks. Generate secrets dynamically on-demand in a way that is unique to every client.

Set up Automatic Secret Rotation

Secret Path: /Secret Key: POSTGRES\_TOKENEnvironment: ProductionInterval: 1 day

We’ve got your back, Use Infisical to manage secrets in your favorite cloud providers, Infrastructure tools, frameworks, and more.

[Explore Integrations](https://infisical.com/docs/documentation/getting-started/introduction)

![Image 105: Hugging Face Logo](blob:https://infisical.com/b9a31d3949b1882a09ed2f8508d538f3)

![Image 106: Hugging Face Logo](blob:https://infisical.com/b9a31d3949b1882a09ed2f8508d538f3)

Securing the future of AI with **Infisical**

[](https://infisical.com/customers/hugging-face)"Infisical provided all the functionality and security settings we needed to boost our security posture and save engineering time. Whether you're working locally, running kubernetes clusters in production, or operating secrets within CI/CD pipelines, Infisical has a seamless prebuilt workflow."Adrien Carreira, Head of Infrastructure, Hugging Face

[](https://infisical.com/customers/hugging-face)

Enterprise-level Infisical lets you set up tight authorization policies, and provides access control tools to embrace "security shift left".

[](https://infisical.com/docs/documentation/platform/audit-logs)Track everything. Be aware of every action that is happening to your secrets and other sensitive data.

[](https://infisical.com/docs/documentation/platform/role-based-access-controls)Stay in control. Set up tight granular permissions for human and machine identities.

Review sensitive changes. Just like in git, assign reviewers to approve secret changes before propagating to apps.

1 Secret Addedvm@acme.com submitted a change request to production environment.

[](https://infisical.com/docs/documentation/platform/pr-workflows)Trust minimally. Give access to sensitive resources only temporarily. Revoke automatically upon expiration.

User: vm@acme.comEnvironment: Pre-productionPeriod: 90 minutes

Automatically rotate secrets upon access revocation

Reliability you can count on.Infisical leads the industry with its reliability and security inititatives.

Infisical is SOC 2 compliant and is constantly undergoing continuous penetration testing.

Powering mission-critical infrastructures of all sizes, with support SLAs and observability.

Infisical encrypts secrets with AES-GCM-256, enforces tight authentication policies, and more.

Deploy Infisical on your own infrastructure or use Infisical Cloud with no maintenance overhead.

[Explore Security](https://infisical.com/docs/internals/security)

Starting with Infisical is simple, fast, and free.

## Metadata

```json
{
  "title": "Infisical is an open-source end-to-end platform to manage secrets and configuration across your team and infrastructure.",
  "description": "All-in-one platform to securely manage application configuration and secrets across your team and infrastructure. Used by Fortune 500 enterprises, international governments, and fastest-growing startups. Save time and boost security.",
  "url": "https://infisical.com/",
  "content": "Everyone has secrets. We secure over  \nevery day.\n\nStart quickly,  \nscale effortlessly. Secure your applications without any hassle.\n\n1import { InfisicalClient, LogLevel } from \"@infisical/sdk\";\n\n2\n\n3const client = new InfisicalClient({\n\n4clientId: \"YOUR\\_CLIENT\\_ID\",\n\n5clientSecret: \"YOUR\\_CLIENT\\_SECRET\"\n\n6});\n\n7\n\n8const secret \\= await client.getSecret({\n\n9projectId: \"PROJECT\\_ID\",\n\n10environment: \"prod\",\n\n11secretName: \"POSTGRES\\_TOKEN\"\n\n12});\n\nStart quickly,  \nscale effortlessly. Secure your applications without any hassle. [Quickstart Guide for Node](https://infisical.com/docs/sdks/languages/node)\n\nBuilding secure applications can be Infisical provides a set of tools to automate your security in a “security shift left” way.\n\n[](https://infisical.com/docs/cli/usage)Switch from .env files to Infisical CLI. Keep secrets always in sync with your teammates. Works with any platform and framework.\n\n(base) user@MacBook % infisical run \\--env=dev \\-- npm run devInjecting 13 Infisical secrets into your application process...\n\n[](https://infisical.com/docs/documentation/getting-started/platform)A simple interface to manage your secrets, environments, and applications.\n\n[](https://infisical.com/docs/cli/scanning-overview#scanning)Automatically identify and prevent secret leaks to git using Infisical's continuous monitoring and precommit checks. Supports 150+ secret types.\n\n(base) user@MacBook % git commit -m \"Code Update\"Warning: Hardcoded secret detected – commit blocked by Infisical.File: backend/src/json/integrations.json Line: 5\n\n[](https://infisical.com/docs/documentation/platform/pit-recovery)Track every change of your secrets and rollback to any point in time.\n\n1\n\nValue: 2B7E151628AED2A6ABF7158809CF4F3CTimestamp: March 1st at 12:03amBy: user@example.com\n\n2\n\nValue: 8E73B0F7DA0E6452C810F32B809079E56Timestamp: March 3rd at 7:45amBy: machine@example.com\n\n3\n\nValue: 603DEB1015CA71BE2B73AEF0857D77811Timestamp: March 7th at 4:23pmBy: user2@example.com\n\n[Secret Rotation and Dynamic Secrets](https://infisical.com/docs/documentation/platform/secret-rotation/overview)Eliminate long-lasting credentials to reduce risk of breach and credential leaks. Generate secrets dynamically on-demand in a way that is unique to every client.\n\nSet up Automatic Secret Rotation\n\nSecret Path: /Secret Key: POSTGRES\\_TOKENEnvironment: ProductionInterval: 1 day\n\nWe’ve got your back, Use Infisical to manage secrets in your favorite cloud providers, Infrastructure tools, frameworks, and more.\n\n[Explore Integrations](https://infisical.com/docs/documentation/getting-started/introduction)\n\n![Image 105: Hugging Face Logo](blob:https://infisical.com/b9a31d3949b1882a09ed2f8508d538f3)\n\n![Image 106: Hugging Face Logo](blob:https://infisical.com/b9a31d3949b1882a09ed2f8508d538f3)\n\nSecuring the future of AI with **Infisical**\n\n[](https://infisical.com/customers/hugging-face)\"Infisical provided all the functionality and security settings we needed to boost our security posture and save engineering time. Whether you're working locally, running kubernetes clusters in production, or operating secrets within CI/CD pipelines, Infisical has a seamless prebuilt workflow.\"Adrien Carreira, Head of Infrastructure, Hugging Face\n\n[](https://infisical.com/customers/hugging-face)\n\nEnterprise-level Infisical lets you set up tight authorization policies, and provides access control tools to embrace \"security shift left\".\n\n[](https://infisical.com/docs/documentation/platform/audit-logs)Track everything. Be aware of every action that is happening to your secrets and other sensitive data.\n\n[](https://infisical.com/docs/documentation/platform/role-based-access-controls)Stay in control. Set up tight granular permissions for human and machine identities.\n\nReview sensitive changes. Just like in git, assign reviewers to approve secret changes before propagating to apps.\n\n1 Secret Addedvm@acme.com submitted a change request to production environment.\n\n[](https://infisical.com/docs/documentation/platform/pr-workflows)Trust minimally. Give access to sensitive resources only temporarily. Revoke automatically upon expiration.\n\nUser: vm@acme.comEnvironment: Pre-productionPeriod: 90 minutes\n\nAutomatically rotate secrets upon access revocation\n\nReliability you can count on.Infisical leads the industry with its reliability and security inititatives.\n\nInfisical is SOC 2 compliant and is constantly undergoing continuous penetration testing.\n\nPowering mission-critical infrastructures of all sizes, with support SLAs and observability.\n\nInfisical encrypts secrets with AES-GCM-256, enforces tight authentication policies, and more.\n\nDeploy Infisical on your own infrastructure or use Infisical Cloud with no maintenance overhead.\n\n[Explore Security](https://infisical.com/docs/internals/security)\n\nStarting with Infisical is simple, fast, and free.",
  "usage": {
    "tokens": 1144
  }
}
```
