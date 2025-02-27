---
title: GitHub - plaid/react-native-plaid-link-sdk: Plaid Link for React Native
description: Plaid Link for React Native. Contribute to plaid/react-native-plaid-link-sdk development by creating an account on GitHub.
url: https://github.com/plaid/react-native-plaid-link-sdk
timestamp: 2025-01-20T15:31:27.622Z
domain: github.com
path: plaid_react-native-plaid-link-sdk
---

# GitHub - plaid/react-native-plaid-link-sdk: Plaid Link for React Native


Plaid Link for React Native. Contribute to plaid/react-native-plaid-link-sdk development by creating an account on GitHub.


## Content

Plaid React Native SDK
----------------------

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#plaid-react-native-sdk)

[![Image 7: version](https://camo.githubusercontent.com/b4ecf6bf722c19dc28d272dc5425c65aea072495336df6285f5dff35599987e7/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d6e61746976652d706c6169642d6c696e6b2d73646b)](https://camo.githubusercontent.com/b4ecf6bf722c19dc28d272dc5425c65aea072495336df6285f5dff35599987e7/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d6e61746976652d706c6169642d6c696e6b2d73646b) [![Image 8: License](https://camo.githubusercontent.com/3cbe83010f22100dad9f8bdee796b672c02d34459ac1e3d9b1fec1ed98bbce51/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f706c6169642f72656163742d6e61746976652d706c6169642d6c696e6b2d73646b)](https://github.com/plaid/react-native-plaid-link-sdk/blob/master/LICENSE)

The Plaid React Native SDK provides the client-side component that your users will interact with in order to link their accounts to Plaid and allow you access to their accounts via the Plaid API.

For more information about Plaid Link check out our [introduction documentation](https://plaid.com/docs/link/#introduction-to-link).

Plaid currently supports two versions of the Plaid React Native SDK v10.x and v11.x. You can find v10 on the [master-v10](https://github.com/plaid/react-native-plaid-link-sdk/tree/master-v10) branch.

Features
--------

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#features)

The SDK provides:

*   A PlaidLink functional component.
*   A function to open Link.
*   A hook to handle [onEvent](https://plaid.com/docs/link/react-native/#onevent) callbacks.
*   A function to dismiss link on iOS.

Getting Started
---------------

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#getting-started)

Get started with our 📝 [documentation](https://plaid.com/docs/link/react-native/) and the 📱[example project](https://github.com/plaid/react-native-plaid-link-sdk/blob/master/example/README.md), or ↔️ [Tiny Quickstart (React Native)](https://github.com/plaid/tiny-quickstart/tree/main/react_native) which is an end to end example demonstrating a minimal integration with this SDK.

If you're unfamiliar with React Native we recommend starting with the [environment setup instructions](https://reactnative.dev/docs/environment-setup).

In your React Native project directory:

npm install --save react-native-plaid-link-sdk

### iOS Setup

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#ios-setup)

Add `Plaid` to your project’s Podfile as follows (likely located at `ios/Podfile`). The latest version is [![Image 9: version](https://camo.githubusercontent.com/a121bb31ee0eedc363b4ea5d38b7b47daa92e5e853c01b87e0da1167a6e24f12/68747470733a2f2f696d672e736869656c64732e696f2f636f636f61706f64732f762f506c616964)](https://camo.githubusercontent.com/a121bb31ee0eedc363b4ea5d38b7b47daa92e5e853c01b87e0da1167a6e24f12/68747470733a2f2f696d672e736869656c64732e696f2f636f636f61706f64732f762f506c616964).

pod 'Plaid', '~\> <insert latest version\>'

Autolinking should install the CocoaPods dependencies for iOS project. If it fails you can run

cd ios && bundle install && bundle exec pod install

### Android Setup

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#android-setup)

*   Android 5.0 (API level 21) and above.
    *   Your `compileSdkVersion` must be `33`.
*   Android gradle plugin `4.x` and above.

AutoLinking should handle all of the Android setup.

Remember to register your Android package name in the [Dashboard](https://dashboard.plaid.com/developers/api). This is required in order to connect to OAuth institutions (which includes most major banks).

### React Native Setup

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#react-native-setup)

*   To initialize `PlaidLink`, you will need to first create a `link_token` at [/link/token/create](https://plaid.com/docs/api/link/#linktokencreate). Check out our [QuickStart guide](https://plaid.com/docs/quickstart/#introduction) for additional API information.

#### Version \>\= 11.6.0

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#version--1160)

Starting from version `11.6.0`, we introduced the ability to preload part of the Link experience. You can initiate the preloading process by invoking the `create` function.

function createLinkTokenConfiguration(
  token: string,
  noLoadingState: boolean \= false,
): LinkTokenConfiguration {
  return {
    token: token,
    // Hides native activity indicator if true.
    noLoadingState: noLoadingState,
  };
}

const tokenConfiguration \= createLinkTokenConfiguration("#GENERATED\_LINK\_TOKEN#");
create(tokenConfiguration);

After calling `create`, you can subsequently invoke the `open` function. Note that maximizing the delay between these two calls will reduce latency for your users by allowing Link more time to load.

function createLinkOpenProps(): LinkOpenProps {
  return {
    onSuccess: (success: LinkSuccess) \=\> {
      // User was able to successfully link their account.
      console.log('Success: ', success);
    },
    onExit: (linkExit: LinkExit) \=\> {
      // User exited Link session. There may or may not be an error depending on what occured.
      console.log('Exit: ', linkExit);
      dismissLink();
    },
    // MODAL or FULL\_SCREEEN presentation on iOS. Defaults to MODAL.
    iOSPresentationStyle: LinkIOSPresentationStyle.MODAL,
    logLevel: LinkLogLevel.ERROR,
  };
}

const openProps \= createLinkOpenProps();
open(openProps);

#### Version < 11.6.0

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#version--1160-1)

In versions prior to `11.6.0`, you can open a link by calling the `openLink` function.

// Create PlaidLinkProps from the provided token string.
function makeLinkTokenProps(token: string): PlaidLinkProps {
  return {
    tokenConfig: {
      token: token,
      logLevel: LinkLogLevel.ERROR,
      // Hides native activity indicator if true.
      noLoadingState: false, 
    },
    onSuccess: (success: LinkSuccess) \=\> {
      // User was able to successfully link their account.
      console.log('Success: ', success); 
      success.metadata.accounts.forEach(it \=\> console.log('accounts', it));
    },
    onExit: (linkExit: LinkExit) \=\> {
      // User exited Link session. There may or may not be an error depending on what occured.
      console.log('Exit: ', linkExit);
      dismissLink();
    },
    // MODAL or FULL\_SCREEEN presentation on iOS. Defaults to MODAL.
    iOSPresentationStyle: LinkIOSPresentationStyle.MODAL,
  };
}

const linkTokenProps \= makeLinkTokenProps("#GENERATED\_LINK\_TOKEN#");
openLink(linkTokenProps);

#### OAuth requirements

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#oauth-requirements)

⚠️ All integrations must use version 9.0.0 or later of the React Native SDK (requires version 4.1.0 or later of the iOS LinkKit SDK) to maintain support for Chase OAuth on iOS.

##### Android OAuth Requirements

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#android-oauth-requirements)

###### Register your app package name

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#register-your-app-package-name)

1.  Log into your [Plaid Dashboard](https://dashboard.plaid.com/developers/api) and navigate to the API page under the Developers tab.
2.  Next to Allowed Android package names click "Configure" then "Add New Android Package Name".
3.  Enter your package name, for example `com.plaid.example`.
4.  Click "Save Changes", you may be prompted to re-enter your password.

##### iOS OAuth Requirements

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#ios-oauth-requirements)

For iOS OAuth to work, specific requirements must be met.

1.  Redirect URIs must be [registered](https://plaid.com/docs/link/ios/#register-your-redirect-uri), and set up as [universal links](https://developer.apple.com/documentation/xcode/supporting-associated-domains).
2.  Your native iOS application, must be configured with your associated domain. See your iOS [set up universal links](https://plaid.com/docs/link/ios/#set-up-universal-links) for more information.

##### Link Token OAuth Requirements

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#link-token-oauth-requirements)

*   On iOS you must configure your `link_token` with a [redirect\_uri](https://plaid.com/docs/api/tokens/#link-token-create-request-redirect-uri) to support OAuth. When creating a `link_token` for initializing Link on Android, `android_package_name` must be specified and `redirect_uri` must be left blank.
    
*   On Android you must configure your `link_token` with an [android\_package\_name](https://plaid.com/docs/api/tokens/#link-token-create-request-android-package-name) to support OAuth. When creating a `link_token` for initializing Link on iOS, `android_package_name` must be left blank and `redirect_uri` should be used instead.
    

#### To receive onEvent callbacks:

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#to-receive-onevent-callbacks)

The React Native Plaid module emits `onEvent` events throughout the account linking process — see [details here](https://plaid.com/docs/link/react-native/#onevent). To receive these events in your React Native app, use the `usePlaidEmitter` hook in react functional components:

  usePlaidEmitter((event: LinkEvent) \=\> {
    console.log(event)
  })

Upgrading
---------

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#upgrading)

Plaid releases updates to the SDK approximately every few months. For the best user experience, we recommend using the latest version of the SDK.

Major SDK versions are released annually. SDK versions are supported for two years; with each major SDK release, Plaid will stop officially supporting any previous SDK versions that are more than two years old.

While these older versions are expected to continue to work without disruption, Plaid will not provide assistance with unsupported SDK versions.

Version compatibility
---------------------

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#version-compatibility)

| Plaid SDK Version | Min React Native Version | Android SDK | Android Min Version | Android Compile Version | iOS SDK | iOS Min Version | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12.0.0 | \* | \[5.0.0+\] | 21 | 34 | \>\=6.0.0 | 14.0 | Active, supports Xcode 16.1.0 |
| 12.0.0-beta.3 | \* | \[4.4.0+\] | 21 | 34 | \>\=6.0.0 | 14.0 | Active, supports Xcode 15.3.0 |
| 12.0.0-beta.2 | \* | \[4.4.0+\] | 21 | 34 | \>\=6.0.0 | 14.0 | Active, supports Xcode 15.3.0 |
| 12.0.0-beta.1 | \* | \[4.4.0+\] | 21 | 34 | \>\=6.0.0 | 14.0 | **Deprecated** |
| 11.13.3 | \* | \[4.6.1+\] | 21 | 34 | \>\=5.6.1 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.13.2 | \* | \[4.6.1+\] | 21 | 34 | \>\=5.6.1 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.13.1 | \* | \[4.6.1+\] | 21 | 34 | \>\=5.6.1 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.13.0 | \* | \[4.6.1+\] | 21 | 34 | \>\=5.6.1 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.12.1 | \* | \[4.6.0+\] | 21 | 34 | \>\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.12.0 | \* | \[4.6.0+\] | 21 | 34 | \>\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.11.2 | \* | \[4.5.1+\] | 21 | 34 | \>\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.11.1 | \* | \[4.5.1+\] | 21 | 34 | \>\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.11.0 | \* | \[4.5.0+\] | 21 | 34 | \>\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.10.3 | \* | \[4.4.2+\] | 21 | 34 | \>\=5.5.1 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.10.2 | \* | \[4.3.1+\] | 21 | 34 | \>\=5.5.1 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.10.1 | \* | \[4.3.1+\] | 21 | 34 | \>\=5.5.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.10.0 | \* | \[4.3.1+\] | 21 | 34 | \>\=5.5.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.9.0 | \* | \[4.3.1+\] | 21 | 34 | \>\=5.5.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.8.2 | \* | \[4.3.1+\] | 21 | 34 | \>\=5.4.2 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.8.1 | \* | \[4.3.1+\] | 21 | 34 | \>\=5.4.2 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.8.0 | \* | \[4.3.1+\] | 21 | 34 | \>\=5.4.2 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.7.1 | \* | \[4.3.0+\] | 21 | 34 | \>\=5.4.1 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.7.0 | \* | \[4.3.0+\] | 21 | 34 | \>\=5.4.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.6.0 | \* | \[4.2.0+\] | 21 | 34 | \>\=5.3.1 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.5.2 | \* | \[4.1.1+\] | 21 | 34 | \>\=5.2.1 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.5.1 | \* | \[4.1.1+\] | 21 | 34 | \>\=5.2.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.5.0 | \* | \[4.1.1+\] | 21 | 34 | \>\=5.2.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.4.0 | \* | \[4.1.1+\] | 21 | 34 | \>\=5.1.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.3.0 | \* | \[4.0.0+\] | 21 | 34 | \>\=5.1.0 | 14.0 | Active, supports Xcode 15.0.1 |
| ~11.2.0~ | \* | \[4.1.0+\] | 21 | 34 | \>\=5.1.0 | 14.0 | **Deprecated** |
| 11.1.0 | \* | \[4.0.0+\] | 21 | 34 | \>\=5.1.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.0.3 | \* | \[4.0.0+\] | 21 | 34 | \>\=5.0.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.0.2 | \* | \[4.0.0+\] | 21 | 34 | \>\=5.0.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.0.1 | \* | \[4.0.0+\] | 21 | 34 | \>\=5.0.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 11.0.0 | \* | \[4.0.0+\] | 21 | 34 | \>\=5.0.0 | 14.0 | Active, supports Xcode 15.0.1 |
| 10.13.0 | \>\= 0.66.0 | \[3.14.3+\] | 21 | 33 | \>\=4.7.2 | 11.0 | Active, supports Xcode 14 |
| 10.12.0 | \>\= 0.66.0 | \[3.14.3+\] | 21 | 33 | \>\=4.7.1 | 11.0 | Active, supports Xcode 14 |
| 10.11.0 | \>\= 0.66.0 | \[3.14.1+\] | 21 | 33 | \>\=4.7.1 | 11.0 | Active, supports Xcode 14 |
| ~10.10.0~ | \>\= 0.66.0 | \[3.14.2+\] | 21 | 33 | \>\=4.7.1 | 11.0 | **Deprecated** |
| 10.9.1 | \>\= 0.66.0 | \[3.14.1+\] | 21 | 33 | \>\=4.7.0 | 11.0 | Active, supports Xcode 14 |
| 10.9.0 | \>\= 0.66.0 | \[3.14.1+\] | 21 | 33 | \>\=4.7.0 | 11.0 | Active, supports Xcode 14 |
| 10.8.0 | \>\= 0.66.0 | \[3.14.0+\] | 21 | 33 | \>\=4.7.0 | 11.0 | Active, supports Xcode 14 |
| 10.7.0 | \>\= 0.66.0 | \[3.14.0+\] | 21 | 33 | \>\=4.6.4 | 11.0 | Active, supports Xcode 14 |
| 10.6.4 | \>\= 0.66.0 | \[3.14.0+\] | 21 | 33 | \>\=4.6.4 | 11.0 | Active, supports Xcode 14 |
| 10.6.3 | \>\= 0.66.0 | \[3.14.0+\] | 21 | 33 | \>\=4.6.4 | 11.0 | Active, supports Xcode 14 |
| 10.6.2 | \>\= 0.66.0 | \[3.14.0+\] | 21 | 33 | \>\=4.6.4 | 11.0 | Deprecated, supports Xcode 14 |
| 10.6.0 | \>\= 0.66.0 | \[3.14.0+\] | 21 | 33 | \>\=4.6.4 | 11.0 | Deprecated, supports Xcode 14 |
| 10.5.0 | \>\= 0.66.0 | \[3.13.2+\] | 21 | 33 | \>\=4.5.1 | 11.0 | Deprecated, supports Xcode 14 |
| 10.4.0 | \>\= 0.66.0 | \[3.13.2+\] | 21 | 33 | \>\=4.4.0 | 11.0 | Deprecated, supports Xcode 14 |
| 10.3.0 | \>\= 0.66.0 | \[3.12.1+\] | 21 | 33 | \>\=4.3.0 | 11.0 | Deprecated, supports Xcode 14 |
| 10.2.0 | \>\= 0.66.0 | \[3.12.0+\] | 21 | 33 | \>\=4.3.0 | 11.0 | Deprecated, supports Xcode 14 |
| 10.1.0 | \>\= 0.66.0 | \[3.11.0+\] | 21 | 33 | \>\=4.2.0 | 11.0 | Deprecated, supports Xcode 14 |
| 10.0.0 | \>\= 0.66.0 | \[3.10.1+\] | 21 | 33 | \>\=4.1.0 | 11.0 | Deprecated, supports Xcode 14 |
| 9.1.0 | \>\= 0.65.3 | \[3.13.2+\] | 21 | 33 | \>\=4.4.0 | 11.0 | Deprecated, supports Xcode 14 |
| 9.0.1 | \>\= 0.65.3 | \[3.10.1+\] | 21 | 33 | \>\=4.1.0 | 11.0 | Deprecated, supports Xcode 14 |
| 9.0.0 | \>\= 0.65.3 | \[3.10.1+\] | 21 | 33 | \>\=4.1.0 | 11.0 | Deprecated, supports Xcode 14 |

Contributing
------------

[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#contributing)

See the [contributor guidelines](https://github.com/plaid/react-native-plaid-link-sdk/blob/master/CONTRIBUTING.md) to learn how to contribute to the repository.

## Metadata

```json
{
  "title": "GitHub - plaid/react-native-plaid-link-sdk: Plaid Link for React Native",
  "description": "Plaid Link for React Native. Contribute to plaid/react-native-plaid-link-sdk development by creating an account on GitHub.",
  "url": "https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true",
  "content": "Plaid React Native SDK\n----------------------\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#plaid-react-native-sdk)\n\n[![Image 7: version](https://camo.githubusercontent.com/b4ecf6bf722c19dc28d272dc5425c65aea072495336df6285f5dff35599987e7/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d6e61746976652d706c6169642d6c696e6b2d73646b)](https://camo.githubusercontent.com/b4ecf6bf722c19dc28d272dc5425c65aea072495336df6285f5dff35599987e7/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d6e61746976652d706c6169642d6c696e6b2d73646b) [![Image 8: License](https://camo.githubusercontent.com/3cbe83010f22100dad9f8bdee796b672c02d34459ac1e3d9b1fec1ed98bbce51/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f706c6169642f72656163742d6e61746976652d706c6169642d6c696e6b2d73646b)](https://github.com/plaid/react-native-plaid-link-sdk/blob/master/LICENSE)\n\nThe Plaid React Native SDK provides the client-side component that your users will interact with in order to link their accounts to Plaid and allow you access to their accounts via the Plaid API.\n\nFor more information about Plaid Link check out our [introduction documentation](https://plaid.com/docs/link/#introduction-to-link).\n\nPlaid currently supports two versions of the Plaid React Native SDK v10.x and v11.x. You can find v10 on the [master-v10](https://github.com/plaid/react-native-plaid-link-sdk/tree/master-v10) branch.\n\nFeatures\n--------\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#features)\n\nThe SDK provides:\n\n*   A PlaidLink functional component.\n*   A function to open Link.\n*   A hook to handle [onEvent](https://plaid.com/docs/link/react-native/#onevent) callbacks.\n*   A function to dismiss link on iOS.\n\nGetting Started\n---------------\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#getting-started)\n\nGet started with our 📝 [documentation](https://plaid.com/docs/link/react-native/) and the 📱[example project](https://github.com/plaid/react-native-plaid-link-sdk/blob/master/example/README.md), or ↔️ [Tiny Quickstart (React Native)](https://github.com/plaid/tiny-quickstart/tree/main/react_native) which is an end to end example demonstrating a minimal integration with this SDK.\n\nIf you're unfamiliar with React Native we recommend starting with the [environment setup instructions](https://reactnative.dev/docs/environment-setup).\n\nIn your React Native project directory:\n\nnpm install --save react-native-plaid-link-sdk\n\n### iOS Setup\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#ios-setup)\n\nAdd `Plaid` to your project’s Podfile as follows (likely located at `ios/Podfile`). The latest version is [![Image 9: version](https://camo.githubusercontent.com/a121bb31ee0eedc363b4ea5d38b7b47daa92e5e853c01b87e0da1167a6e24f12/68747470733a2f2f696d672e736869656c64732e696f2f636f636f61706f64732f762f506c616964)](https://camo.githubusercontent.com/a121bb31ee0eedc363b4ea5d38b7b47daa92e5e853c01b87e0da1167a6e24f12/68747470733a2f2f696d672e736869656c64732e696f2f636f636f61706f64732f762f506c616964).\n\npod 'Plaid', '~\\> <insert latest version\\>'\n\nAutolinking should install the CocoaPods dependencies for iOS project. If it fails you can run\n\ncd ios && bundle install && bundle exec pod install\n\n### Android Setup\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#android-setup)\n\n*   Android 5.0 (API level 21) and above.\n    *   Your `compileSdkVersion` must be `33`.\n*   Android gradle plugin `4.x` and above.\n\nAutoLinking should handle all of the Android setup.\n\nRemember to register your Android package name in the [Dashboard](https://dashboard.plaid.com/developers/api). This is required in order to connect to OAuth institutions (which includes most major banks).\n\n### React Native Setup\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#react-native-setup)\n\n*   To initialize `PlaidLink`, you will need to first create a `link_token` at [/link/token/create](https://plaid.com/docs/api/link/#linktokencreate). Check out our [QuickStart guide](https://plaid.com/docs/quickstart/#introduction) for additional API information.\n\n#### Version \\>\\= 11.6.0\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#version--1160)\n\nStarting from version `11.6.0`, we introduced the ability to preload part of the Link experience. You can initiate the preloading process by invoking the `create` function.\n\nfunction createLinkTokenConfiguration(\n  token: string,\n  noLoadingState: boolean \\= false,\n): LinkTokenConfiguration {\n  return {\n    token: token,\n    // Hides native activity indicator if true.\n    noLoadingState: noLoadingState,\n  };\n}\n\nconst tokenConfiguration \\= createLinkTokenConfiguration(\"#GENERATED\\_LINK\\_TOKEN#\");\ncreate(tokenConfiguration);\n\nAfter calling `create`, you can subsequently invoke the `open` function. Note that maximizing the delay between these two calls will reduce latency for your users by allowing Link more time to load.\n\nfunction createLinkOpenProps(): LinkOpenProps {\n  return {\n    onSuccess: (success: LinkSuccess) \\=\\> {\n      // User was able to successfully link their account.\n      console.log('Success: ', success);\n    },\n    onExit: (linkExit: LinkExit) \\=\\> {\n      // User exited Link session. There may or may not be an error depending on what occured.\n      console.log('Exit: ', linkExit);\n      dismissLink();\n    },\n    // MODAL or FULL\\_SCREEEN presentation on iOS. Defaults to MODAL.\n    iOSPresentationStyle: LinkIOSPresentationStyle.MODAL,\n    logLevel: LinkLogLevel.ERROR,\n  };\n}\n\nconst openProps \\= createLinkOpenProps();\nopen(openProps);\n\n#### Version < 11.6.0\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#version--1160-1)\n\nIn versions prior to `11.6.0`, you can open a link by calling the `openLink` function.\n\n// Create PlaidLinkProps from the provided token string.\nfunction makeLinkTokenProps(token: string): PlaidLinkProps {\n  return {\n    tokenConfig: {\n      token: token,\n      logLevel: LinkLogLevel.ERROR,\n      // Hides native activity indicator if true.\n      noLoadingState: false, \n    },\n    onSuccess: (success: LinkSuccess) \\=\\> {\n      // User was able to successfully link their account.\n      console.log('Success: ', success); \n      success.metadata.accounts.forEach(it \\=\\> console.log('accounts', it));\n    },\n    onExit: (linkExit: LinkExit) \\=\\> {\n      // User exited Link session. There may or may not be an error depending on what occured.\n      console.log('Exit: ', linkExit);\n      dismissLink();\n    },\n    // MODAL or FULL\\_SCREEEN presentation on iOS. Defaults to MODAL.\n    iOSPresentationStyle: LinkIOSPresentationStyle.MODAL,\n  };\n}\n\nconst linkTokenProps \\= makeLinkTokenProps(\"#GENERATED\\_LINK\\_TOKEN#\");\nopenLink(linkTokenProps);\n\n#### OAuth requirements\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#oauth-requirements)\n\n⚠️ All integrations must use version 9.0.0 or later of the React Native SDK (requires version 4.1.0 or later of the iOS LinkKit SDK) to maintain support for Chase OAuth on iOS.\n\n##### Android OAuth Requirements\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#android-oauth-requirements)\n\n###### Register your app package name\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#register-your-app-package-name)\n\n1.  Log into your [Plaid Dashboard](https://dashboard.plaid.com/developers/api) and navigate to the API page under the Developers tab.\n2.  Next to Allowed Android package names click \"Configure\" then \"Add New Android Package Name\".\n3.  Enter your package name, for example `com.plaid.example`.\n4.  Click \"Save Changes\", you may be prompted to re-enter your password.\n\n##### iOS OAuth Requirements\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#ios-oauth-requirements)\n\nFor iOS OAuth to work, specific requirements must be met.\n\n1.  Redirect URIs must be [registered](https://plaid.com/docs/link/ios/#register-your-redirect-uri), and set up as [universal links](https://developer.apple.com/documentation/xcode/supporting-associated-domains).\n2.  Your native iOS application, must be configured with your associated domain. See your iOS [set up universal links](https://plaid.com/docs/link/ios/#set-up-universal-links) for more information.\n\n##### Link Token OAuth Requirements\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#link-token-oauth-requirements)\n\n*   On iOS you must configure your `link_token` with a [redirect\\_uri](https://plaid.com/docs/api/tokens/#link-token-create-request-redirect-uri) to support OAuth. When creating a `link_token` for initializing Link on Android, `android_package_name` must be specified and `redirect_uri` must be left blank.\n    \n*   On Android you must configure your `link_token` with an [android\\_package\\_name](https://plaid.com/docs/api/tokens/#link-token-create-request-android-package-name) to support OAuth. When creating a `link_token` for initializing Link on iOS, `android_package_name` must be left blank and `redirect_uri` should be used instead.\n    \n\n#### To receive onEvent callbacks:\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#to-receive-onevent-callbacks)\n\nThe React Native Plaid module emits `onEvent` events throughout the account linking process — see [details here](https://plaid.com/docs/link/react-native/#onevent). To receive these events in your React Native app, use the `usePlaidEmitter` hook in react functional components:\n\n  usePlaidEmitter((event: LinkEvent) \\=\\> {\n    console.log(event)\n  })\n\nUpgrading\n---------\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#upgrading)\n\nPlaid releases updates to the SDK approximately every few months. For the best user experience, we recommend using the latest version of the SDK.\n\nMajor SDK versions are released annually. SDK versions are supported for two years; with each major SDK release, Plaid will stop officially supporting any previous SDK versions that are more than two years old.\n\nWhile these older versions are expected to continue to work without disruption, Plaid will not provide assistance with unsupported SDK versions.\n\nVersion compatibility\n---------------------\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#version-compatibility)\n\n| Plaid SDK Version | Min React Native Version | Android SDK | Android Min Version | Android Compile Version | iOS SDK | iOS Min Version | Status |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n| 12.0.0 | \\* | \\[5.0.0+\\] | 21 | 34 | \\>\\=6.0.0 | 14.0 | Active, supports Xcode 16.1.0 |\n| 12.0.0-beta.3 | \\* | \\[4.4.0+\\] | 21 | 34 | \\>\\=6.0.0 | 14.0 | Active, supports Xcode 15.3.0 |\n| 12.0.0-beta.2 | \\* | \\[4.4.0+\\] | 21 | 34 | \\>\\=6.0.0 | 14.0 | Active, supports Xcode 15.3.0 |\n| 12.0.0-beta.1 | \\* | \\[4.4.0+\\] | 21 | 34 | \\>\\=6.0.0 | 14.0 | **Deprecated** |\n| 11.13.3 | \\* | \\[4.6.1+\\] | 21 | 34 | \\>\\=5.6.1 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.13.2 | \\* | \\[4.6.1+\\] | 21 | 34 | \\>\\=5.6.1 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.13.1 | \\* | \\[4.6.1+\\] | 21 | 34 | \\>\\=5.6.1 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.13.0 | \\* | \\[4.6.1+\\] | 21 | 34 | \\>\\=5.6.1 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.12.1 | \\* | \\[4.6.0+\\] | 21 | 34 | \\>\\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.12.0 | \\* | \\[4.6.0+\\] | 21 | 34 | \\>\\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.11.2 | \\* | \\[4.5.1+\\] | 21 | 34 | \\>\\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.11.1 | \\* | \\[4.5.1+\\] | 21 | 34 | \\>\\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.11.0 | \\* | \\[4.5.0+\\] | 21 | 34 | \\>\\=5.6.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.10.3 | \\* | \\[4.4.2+\\] | 21 | 34 | \\>\\=5.5.1 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.10.2 | \\* | \\[4.3.1+\\] | 21 | 34 | \\>\\=5.5.1 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.10.1 | \\* | \\[4.3.1+\\] | 21 | 34 | \\>\\=5.5.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.10.0 | \\* | \\[4.3.1+\\] | 21 | 34 | \\>\\=5.5.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.9.0 | \\* | \\[4.3.1+\\] | 21 | 34 | \\>\\=5.5.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.8.2 | \\* | \\[4.3.1+\\] | 21 | 34 | \\>\\=5.4.2 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.8.1 | \\* | \\[4.3.1+\\] | 21 | 34 | \\>\\=5.4.2 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.8.0 | \\* | \\[4.3.1+\\] | 21 | 34 | \\>\\=5.4.2 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.7.1 | \\* | \\[4.3.0+\\] | 21 | 34 | \\>\\=5.4.1 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.7.0 | \\* | \\[4.3.0+\\] | 21 | 34 | \\>\\=5.4.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.6.0 | \\* | \\[4.2.0+\\] | 21 | 34 | \\>\\=5.3.1 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.5.2 | \\* | \\[4.1.1+\\] | 21 | 34 | \\>\\=5.2.1 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.5.1 | \\* | \\[4.1.1+\\] | 21 | 34 | \\>\\=5.2.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.5.0 | \\* | \\[4.1.1+\\] | 21 | 34 | \\>\\=5.2.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.4.0 | \\* | \\[4.1.1+\\] | 21 | 34 | \\>\\=5.1.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.3.0 | \\* | \\[4.0.0+\\] | 21 | 34 | \\>\\=5.1.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| ~11.2.0~ | \\* | \\[4.1.0+\\] | 21 | 34 | \\>\\=5.1.0 | 14.0 | **Deprecated** |\n| 11.1.0 | \\* | \\[4.0.0+\\] | 21 | 34 | \\>\\=5.1.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.0.3 | \\* | \\[4.0.0+\\] | 21 | 34 | \\>\\=5.0.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.0.2 | \\* | \\[4.0.0+\\] | 21 | 34 | \\>\\=5.0.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.0.1 | \\* | \\[4.0.0+\\] | 21 | 34 | \\>\\=5.0.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 11.0.0 | \\* | \\[4.0.0+\\] | 21 | 34 | \\>\\=5.0.0 | 14.0 | Active, supports Xcode 15.0.1 |\n| 10.13.0 | \\>\\= 0.66.0 | \\[3.14.3+\\] | 21 | 33 | \\>\\=4.7.2 | 11.0 | Active, supports Xcode 14 |\n| 10.12.0 | \\>\\= 0.66.0 | \\[3.14.3+\\] | 21 | 33 | \\>\\=4.7.1 | 11.0 | Active, supports Xcode 14 |\n| 10.11.0 | \\>\\= 0.66.0 | \\[3.14.1+\\] | 21 | 33 | \\>\\=4.7.1 | 11.0 | Active, supports Xcode 14 |\n| ~10.10.0~ | \\>\\= 0.66.0 | \\[3.14.2+\\] | 21 | 33 | \\>\\=4.7.1 | 11.0 | **Deprecated** |\n| 10.9.1 | \\>\\= 0.66.0 | \\[3.14.1+\\] | 21 | 33 | \\>\\=4.7.0 | 11.0 | Active, supports Xcode 14 |\n| 10.9.0 | \\>\\= 0.66.0 | \\[3.14.1+\\] | 21 | 33 | \\>\\=4.7.0 | 11.0 | Active, supports Xcode 14 |\n| 10.8.0 | \\>\\= 0.66.0 | \\[3.14.0+\\] | 21 | 33 | \\>\\=4.7.0 | 11.0 | Active, supports Xcode 14 |\n| 10.7.0 | \\>\\= 0.66.0 | \\[3.14.0+\\] | 21 | 33 | \\>\\=4.6.4 | 11.0 | Active, supports Xcode 14 |\n| 10.6.4 | \\>\\= 0.66.0 | \\[3.14.0+\\] | 21 | 33 | \\>\\=4.6.4 | 11.0 | Active, supports Xcode 14 |\n| 10.6.3 | \\>\\= 0.66.0 | \\[3.14.0+\\] | 21 | 33 | \\>\\=4.6.4 | 11.0 | Active, supports Xcode 14 |\n| 10.6.2 | \\>\\= 0.66.0 | \\[3.14.0+\\] | 21 | 33 | \\>\\=4.6.4 | 11.0 | Deprecated, supports Xcode 14 |\n| 10.6.0 | \\>\\= 0.66.0 | \\[3.14.0+\\] | 21 | 33 | \\>\\=4.6.4 | 11.0 | Deprecated, supports Xcode 14 |\n| 10.5.0 | \\>\\= 0.66.0 | \\[3.13.2+\\] | 21 | 33 | \\>\\=4.5.1 | 11.0 | Deprecated, supports Xcode 14 |\n| 10.4.0 | \\>\\= 0.66.0 | \\[3.13.2+\\] | 21 | 33 | \\>\\=4.4.0 | 11.0 | Deprecated, supports Xcode 14 |\n| 10.3.0 | \\>\\= 0.66.0 | \\[3.12.1+\\] | 21 | 33 | \\>\\=4.3.0 | 11.0 | Deprecated, supports Xcode 14 |\n| 10.2.0 | \\>\\= 0.66.0 | \\[3.12.0+\\] | 21 | 33 | \\>\\=4.3.0 | 11.0 | Deprecated, supports Xcode 14 |\n| 10.1.0 | \\>\\= 0.66.0 | \\[3.11.0+\\] | 21 | 33 | \\>\\=4.2.0 | 11.0 | Deprecated, supports Xcode 14 |\n| 10.0.0 | \\>\\= 0.66.0 | \\[3.10.1+\\] | 21 | 33 | \\>\\=4.1.0 | 11.0 | Deprecated, supports Xcode 14 |\n| 9.1.0 | \\>\\= 0.65.3 | \\[3.13.2+\\] | 21 | 33 | \\>\\=4.4.0 | 11.0 | Deprecated, supports Xcode 14 |\n| 9.0.1 | \\>\\= 0.65.3 | \\[3.10.1+\\] | 21 | 33 | \\>\\=4.1.0 | 11.0 | Deprecated, supports Xcode 14 |\n| 9.0.0 | \\>\\= 0.65.3 | \\[3.10.1+\\] | 21 | 33 | \\>\\=4.1.0 | 11.0 | Deprecated, supports Xcode 14 |\n\nContributing\n------------\n\n[](https://github.com/plaid/react-native-plaid-link-sdk?screenshot=true#contributing)\n\nSee the [contributor guidelines](https://github.com/plaid/react-native-plaid-link-sdk/blob/master/CONTRIBUTING.md) to learn how to contribute to the repository.",
  "usage": {
    "tokens": 5790
  }
}
```
