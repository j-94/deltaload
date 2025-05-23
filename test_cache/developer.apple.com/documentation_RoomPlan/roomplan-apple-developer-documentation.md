---
title: RoomPlan | Apple Developer Documentation
description: Create a 3D model of a room by interactively guiding people to scan their physical environment using a device’s camera.
url: https://developer.apple.com/documentation/RoomPlan
timestamp: 2025-01-20T15:42:33.701Z
domain: developer.apple.com
path: documentation_RoomPlan
---

# RoomPlan | Apple Developer Documentation


Create a 3D model of a room by interactively guiding people to scan their physical environment using a device’s camera.


## Content

[Overview](https://developer.apple.com/documentation/RoomPlan#Overview)
-----------------------------------------------------------------------

Use RoomPlan to create a 3D model of an interior room. The framework uses a device’s sensors, trained ML models, and RealityKit’s rendering capabilities to capture the physical surroundings of an interior room. For example, the framework inspects a device’s camera feed and LiDAR readings to identify walls, windows, openings, and doors. RoomPlan also recognizes room features, furniture, and appliances, such as a fireplace, bed, or refrigerator, and provides that information to the app.

To begin a capture, the app presents a view ([`RoomCaptureView`](https://developer.apple.com/documentation/roomplan/roomcaptureview)) that the user looks through to see their room in AR. The view displays virtual cues as they move around the room:

*   Real-time graphic overlays display on top of physical structures in the room to convey scanning progress.
    
*   If the framework requires a specific kind of device movement or perspective to complete the capture, the UI displays instructions that explain how to position the device.
    

![Image 5: An illustration of a hand holding an iPhone in portrait mode in a kitchen. The device’s screen displays a camera feed of the kitchen with highlights around physical structures, such as the window and the sink. At the top of the screen is a banner that reads Move device to start. To the right of that banner is a callout that reads Instructional text. Another callout to the right of the device’s screen reads Structural highlights and points to the highlight around the window.](https://docs-assets.developer.apple.com/published/78ae1d75bc69bde0b0dee238d672cf6a/roomplan-hero-1@2x.png)

When the app determines that the current scan is complete, the view displays a small-scale version of the scanned room for the user to approve.

Alternatively, your app can display custom graphics during the scanning process by creating and using a scan session object ([`RoomCaptureSession`](https://developer.apple.com/documentation/roomplan/roomcapturesession)) directly.

### [Access the captured results](https://developer.apple.com/documentation/RoomPlan#Access-the-captured-results)

The framework outputs a scan as _parametric_ data, which makes it easy for your app to modify the scanned room’s individual components. RoomPlan also provides the results in various Universal Scene Description (USD) formats. With these assets, your app can implement custom features, such as the following:

*   Estimate the size of particular areas of a room.
    
*   Preview virtual furniture from a catalog in a variety of styles and positions.
    
*   Integrate a version of a scanned room or structure in a 3D game.
    

![Image 6: An illustration of a scanned room showing its data representations. From the left, the illustration shows a small scale 3D version of a scanned room. Three arrows flow to the right. The top arrow points to a house icon and four 2D images of floor plans with rulers that measure objects in the floor plans. The middle arrow points to an icon of a shopping cart and an iPhone in portrait mode that displays a furniture catalog with tables, a lamp, and chairs. Next to the phone is a copy of the small scale 3D version of a scanned room that includes a highlighted virtual table from the catalog. The bottom arrow points to an icon of a game controller and an iPhone in landscape mode that displays a 3D game version of the scanned room.](https://docs-assets.developer.apple.com/published/8909a2da99ac2c9fbb690113e0b340ed/roomplan-hero-2@2x.png)

### [Process scan results on macOS with Mac Catalyst](https://developer.apple.com/documentation/RoomPlan#Process-scan-results-on-macOS-with-Mac-Catalyst)

Mac apps built with Mac Catalyst can access [`CapturedRoom`](https://developer.apple.com/documentation/roomplan/capturedroom) and [`CapturedStructure`](https://developer.apple.com/documentation/roomplan/capturedstructure) and can perform encoding, decoding, and exporting. Environment scanning relies on a camera, LiDAR, and other sensors that support augmented reality on iOS and iPad OS devices. However, macOS apps built with Mac Catalyst can process the results of room-capture sessions performed on those devices. RoomPlan ignores all capture-session-related calls on macOS apps built with Mac Catalyst.

## Metadata

```json
{
  "title": "RoomPlan | Apple Developer Documentation",
  "description": "Create a 3D model of a room by interactively guiding people to scan their physical environment using a device’s camera.",
  "url": "https://developer.apple.com/documentation/RoomPlan",
  "content": "[Overview](https://developer.apple.com/documentation/RoomPlan#Overview)\n-----------------------------------------------------------------------\n\nUse RoomPlan to create a 3D model of an interior room. The framework uses a device’s sensors, trained ML models, and RealityKit’s rendering capabilities to capture the physical surroundings of an interior room. For example, the framework inspects a device’s camera feed and LiDAR readings to identify walls, windows, openings, and doors. RoomPlan also recognizes room features, furniture, and appliances, such as a fireplace, bed, or refrigerator, and provides that information to the app.\n\nTo begin a capture, the app presents a view ([`RoomCaptureView`](https://developer.apple.com/documentation/roomplan/roomcaptureview)) that the user looks through to see their room in AR. The view displays virtual cues as they move around the room:\n\n*   Real-time graphic overlays display on top of physical structures in the room to convey scanning progress.\n    \n*   If the framework requires a specific kind of device movement or perspective to complete the capture, the UI displays instructions that explain how to position the device.\n    \n\n![Image 5: An illustration of a hand holding an iPhone in portrait mode in a kitchen. The device’s screen displays a camera feed of the kitchen with highlights around physical structures, such as the window and the sink. At the top of the screen is a banner that reads Move device to start. To the right of that banner is a callout that reads Instructional text. Another callout to the right of the device’s screen reads Structural highlights and points to the highlight around the window.](https://docs-assets.developer.apple.com/published/78ae1d75bc69bde0b0dee238d672cf6a/roomplan-hero-1@2x.png)\n\nWhen the app determines that the current scan is complete, the view displays a small-scale version of the scanned room for the user to approve.\n\nAlternatively, your app can display custom graphics during the scanning process by creating and using a scan session object ([`RoomCaptureSession`](https://developer.apple.com/documentation/roomplan/roomcapturesession)) directly.\n\n### [Access the captured results](https://developer.apple.com/documentation/RoomPlan#Access-the-captured-results)\n\nThe framework outputs a scan as _parametric_ data, which makes it easy for your app to modify the scanned room’s individual components. RoomPlan also provides the results in various Universal Scene Description (USD) formats. With these assets, your app can implement custom features, such as the following:\n\n*   Estimate the size of particular areas of a room.\n    \n*   Preview virtual furniture from a catalog in a variety of styles and positions.\n    \n*   Integrate a version of a scanned room or structure in a 3D game.\n    \n\n![Image 6: An illustration of a scanned room showing its data representations. From the left, the illustration shows a small scale 3D version of a scanned room. Three arrows flow to the right. The top arrow points to a house icon and four 2D images of floor plans with rulers that measure objects in the floor plans. The middle arrow points to an icon of a shopping cart and an iPhone in portrait mode that displays a furniture catalog with tables, a lamp, and chairs. Next to the phone is a copy of the small scale 3D version of a scanned room that includes a highlighted virtual table from the catalog. The bottom arrow points to an icon of a game controller and an iPhone in landscape mode that displays a 3D game version of the scanned room.](https://docs-assets.developer.apple.com/published/8909a2da99ac2c9fbb690113e0b340ed/roomplan-hero-2@2x.png)\n\n### [Process scan results on macOS with Mac Catalyst](https://developer.apple.com/documentation/RoomPlan#Process-scan-results-on-macOS-with-Mac-Catalyst)\n\nMac apps built with Mac Catalyst can access [`CapturedRoom`](https://developer.apple.com/documentation/roomplan/capturedroom) and [`CapturedStructure`](https://developer.apple.com/documentation/roomplan/capturedstructure) and can perform encoding, decoding, and exporting. Environment scanning relies on a camera, LiDAR, and other sensors that support augmented reality on iOS and iPad OS devices. However, macOS apps built with Mac Catalyst can process the results of room-capture sessions performed on those devices. RoomPlan ignores all capture-session-related calls on macOS apps built with Mac Catalyst.",
  "usage": {
    "tokens": 925
  }
}
```
