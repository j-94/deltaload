---
title: WWDC23 — Explore enhancements to RoomPlan - ganeshrajugalla - Medium
description: RoomPlan uses ARKit, which uses sophisticated machine learning algorithms, to recognize walls, windows, doors, empty spaces and objects. The RoomCaptureView API allows you to experience the…
url: https://medium.com/@ganeshrajugalla/wwdc23-explore-enhancements-to-roomplan-7ecbb8f68328
timestamp: 2025-01-20T15:42:35.358Z
domain: medium.com
path: @ganeshrajugalla_wwdc23-explore-enhancements-to-roomplan-7ecbb8f68328
---

# WWDC23 — Explore enhancements to RoomPlan - ganeshrajugalla - Medium


RoomPlan uses ARKit, which uses sophisticated machine learning algorithms, to recognize walls, windows, doors, empty spaces and objects. The RoomCaptureView API allows you to experience the…


## Content

[![Image 51: ganeshrajugalla](https://miro.medium.com/v2/resize:fill:88:88/1*CWsSKCqvldt0tHppsYTiSw.jpeg)](https://medium.com/@ganeshrajugalla?source=post_page---byline--7ecbb8f68328--------------------------------)

![Image 52](https://miro.medium.com/v2/resize:fit:700/1*B9nEEoM8FoPmoi978QSerQ.jpeg)

> Obviously, the main theme of this WWDC is AR/VR. In fact, the reason I’m watching this WWDC is because I’m thinking of an app with AR features.

RoomPlan uses ARKit, which uses sophisticated machine learning algorithms, to recognize walls, windows, doors, empty spaces and objects. The RoomCaptureView API allows you to experience the experience of scanning a room directly through an app. The result can be confirmed as a 3D model or extracted as a USDZ file.

This presentation covers four items.

*   Custom ARSession support
*   MultiRoom (combining multiple rooms into one space) support
*   Accessibility (Voice Over)
*   RoomPlan representations
*   Enhanced export function

> caution! : The above are APIs applied at least from iOS 16. And the improved features of RoomPlan will be applied from iOS 17.

Custom ARSession support
------------------------

Originally, only the given ARSession was used, but now ARSession using ARWorldTrackingConfiguration can be created and used.

/// Create previous RoomCaptureSession  
public class RoomCaptureSession {  
    public init() {  
       ...  
    }public func stop() {  
       ...  
    }  
}

/// Create a new RoomCaptureSession  
public class RoomCaptureSession {  
    // Init: ARSession is an optional input for RoomCaptureSession  
    public init(arSession: ARSession? = nil) {  
       ...  
  }// Stop: pauseARSession is used for whether to continue ARSession experience  
    public func stop(pauseARSession: Bool = true) {  
       ...  
  }  
}

Add photos and videos to RoomPlan scan

MultiRoom support
-----------------

Let’s say you scanned the living room, my room, and the kitchen. What do I need to consider to put this together?

First of all, all scan results have respective coordinate planes. Since they are not all scanned in the same space, they cannot be said to be the same coordinate plane. If you ignore this and simply attach rooms facing each other based on the wall, the objects will be duplicated.

Therefore, we have to merge several same scan results into one coordinate plane system. To do this, Apple offers two methods.

1.  Scan using the same ARSession.
2.  Use ARSession relocalization.

Use Continuous ARSession
------------------------

When the original RoomCaptureSession ended, the ARSession also stopped. However, due to the change in the stop function seen above, the same ARSession can be used repeatedly

![Image 53](https://miro.medium.com/v2/resize:fit:700/1*7iBzU3k8-FCu6Ay9gQsXLg.png)

`stop()`Based on , ARSession stops.

![Image 54](https://miro.medium.com/v2/resize:fit:700/1*r2RCRpNihBgA4Q_fSeVK9g.png)

`stop(pauseARSession: false)`causes the ARSession to persist. It will use the same coordinate plane system.

// Continuous ARSession// start 1st scan  
roomCaptureSession.run(configuration: captureSessionConfig)

// stop 1st scan with continuing ARSession  
roomCaptureSession.stop(pauseARSession: false)

// start 2nd scan  
roomCaptureSession.run(configuration: captureSessionConfig)

// stop 2nd scan(pauseARSession = true by default)  
roomCaptureSession.stop()

ARSession relocalization
------------------------

The above method can be used to repeat multiple scans at the same time, but relocalization can be used if you want to shoot at a different time (tomorrow or next week, etc.).

First, we need to save the ARWorldMap when the ARSession stops.

![Image 55](https://miro.medium.com/v2/resize:fit:700/1*jc7Wvs7QG0gJjHLiSZM_ug.png)

When scanning is repeated next time, a new scan can be started by calling the ARWorldMap stored in the stopped ARSession.

![Image 56](https://miro.medium.com/v2/resize:fit:700/1*A_dgXFMyTEVHQY0quhq3rQ.png)

The code below shows the process of saving an ARWorldMap after performing the initial scan. For reference, since ARWorldMap is an NSObject, it can be saved as NSData using NSKeyedArchiver.

// Capture with saving ARWorldMap// start 1st scan  
roomCaptureSession.run(configuration: captureSessionConfig)

// stop 1st scan (pauseARSession = true by default)  
roomCaptureSession.stop()

// save ARWorldMap  
roomCaptureSession.arSession.getCurrentWorldMap(completionHandler:{worldMap, error in ...})

And the code below shows the process of loading the saved ARWorldMap and scanning it again.

// Capture with loading ARWorldMap// load ARWorldMap  
let arWorldMap = try NSKeyedUnarchiver.unarchivedObject(ofClass: ARWorldMap.self, from: data)

// run ARKit relocalization  
let arWorldTrackingConfig = ARWorldTrackingConfiguration()  
arWorldTrackingConfig.initialWorldMap=arWorldMap  
roomCaptureSession.init()  
roomCaptureSession.arSession.ru(arWorldTrackingConfig, options: \[\])

// Wait for relocalization to complete  
// start 2nd scan  
roomCaptureSession.run(configuration: captureSessionConfig)  
// stop 2nd scan  
roomCaptureSession.stop ()

Thus, the first and second scans have the same results as scanning in the same coordinate plane system.

MultiRoom API
-------------

If you have scanned multiple rooms using the above two methods, you need to merge them into one. Each scan can obtain a CapturedRoom object by using the RoomBuilder API.

![Image 57](https://miro.medium.com/v2/resize:fit:700/1*bB87mrEdmbpjsYeRk0i8Eg.png)

And what to do? Combine the CapturedRoom objects into one using StructureBuilder. The combined spatial data becomes a CapturedStructure object.

![Image 58](https://miro.medium.com/v2/resize:fit:700/1*hAkz-4oT5k8HBzb4GYqbgA.png)

A code example using the StructureBuilder API is shown below.

// StructureBuilder// create structureBuilder instance  
let structureBuilder = StructureBuilder (option: \[.beautifyObjects\])

// load multiple capturedRoom results to capturedRoomArray  
var capturedRoomArray: \[CapturedRoom\] = \[\]

// run structureBuilder API to get capturedStructure  
let capturedStructure = try await structureBuilder.capturedStructure(from: capturedRoomArray)

// export capturedStructure to usdz  
try capturedStructure.export (to: destinationURL)

Let’s briefly point out the difference between CapturedRoom and CapturedStructure here.

*   CapturedRoom = The result of scanning a single room.
*   CapturedStructure = This is a structure that combines multiple CapturedRooms into one.

Regarding the MultiRoom API, we plan to provide a sample app. I’ve tried to find the official documentation, but I can’t seem to find a page yet.

The USDZ file is a file format that can be viewed directly on iOS and macOS. USDZ files can also be run in digital content creation tools such as Blender.

Considerations
--------------

Considering the space available for MultiRoom, the most suitable options were also provided.

1.  One-story residential house with 4 beds, living room, kitchen and dining area
2.  The size of all spaces to be merged is 2,000 ft square or 186 m square
3.  Mining more than 50 lux

Accessibility
-------------

Voice feedback using VoiceOver is provided for those who have visual difficulties in apps that use RoomPlan APIs.

In the demonstration video, a person who seemed to have zero emotion read ‘Point camera at bottom edge of wall’, ‘A fireplace’, ‘A wall’, ‘A window’ as they recognized them.

RoomPlan representations
------------------------

So far, RoomPlan’s scan results have only covered limited objects. This time, RoomPlan is said to be able to scan slanted walls, circular walls, and concave spaces such as ovens.

It also provides more detailed results for items that can be scanned, and a sofa was cited as an example. It is to collect single-seater sofas, L-shaped sofas, and straight sofas in a new way.

The reason this is possible is because the type of data collected by scanning has increased. Most of the categories that CapturedRoom can scan as mentioned above are expressed as internal structures called Surface and Object.

Here’s some additional data.

*   Section = represents the space inside the room.
*   Surface -\> Polygon = Now, walls can be expressed using Polygon, which is not a regular shape. (Curved walls, walls with beams attached, etc.)
*   It is one of the categories that can be expressed as Surface -\> Category -\> floor = Polygon.
*   Object -\> Attribute = Added for more accurate object scanning.

![Image 59](https://miro.medium.com/v2/resize:fit:700/1*fcrXOVNJDWvo5LryrKBSfA.png)

Also, Surfaces and Objects have a Parent added that references their parent (e.g. a window’s parent is a wall, a chair’s parent is a table).

![Image 60](https://miro.medium.com/v2/resize:fit:700/1*fGovurxSkA-lTH-OrZxGZA.png)

Let’s take a closer look at the code.

As you can see, all the spaces are divided, and each section has one label attached. Living Room, Dining Room, and Undefined are one space, but they are divided into Sections.

public struct CapturedStructure: Codable, Sendable {  
 public struct Section: Codable, Sendable {  
  public enum Label: String, Codable, Sendable {  
   case livingRoom  
   case bedroom   
            case bathroom   
            case kitchen   
            case diningRoom   
            case unidentified  
  }public var label: Label { get }

// The center position of the section  
  public var center: simd\_float3 { get }

// Indicator for which story, level, or floor  
  public var story: Int { get }  
 }  
}

![Image 61](https://miro.medium.com/v2/resize:fit:638/1*U4Qfd3G-uF2GgbYRZAmLvQ.png)

Polygons allow us to recognize non-planar structures as well. In addition, the scanned floor is changed into a more elegant form through floor added to the category.

// Floors for Surfaces in CapturedRoompublic struct CapturedRoom: Codable, Sendable {

// A 2D area in a room identified as a surface  
 public struct Surface: Codable, Sendable {

// A 2D polygon to represent walls and floors  
  // in local plan coordinates  
  public var polygonCorners: \[sim\_float3\] { get }

// classifications of a surface in a captured room  
  public enum Category: Codable, Sendable {  
   case floor  
  }  
 }  
}

![Image 62](https://miro.medium.com/v2/resize:fit:632/1*WkJAqSbz7RbgE3W0MiMJdw.png)

Polygon using wall

![Image 63](https://miro.medium.com/v2/resize:fit:572/1*fM_QKWwJcn0MlCs6UmQaWw.png)

Polygon using floor

This is the most exciting part for me personally. Thanks to the ability to recognize the parent of the object mentioned above, it is possible to recognize kitchen utensils as shown below.

// Parent identifiers for surfaces and objects in CapturedRoom  
public struct CapturedRoom: Codable, Sendable {  
 // A 2D area in a room identified as a surface  
 public struct Surface: Codable, Sendable {// A unique UUID to indicate surface's parent  
        public var parentIdentifier: UUID? { get }  
 }

// A 3D area in a room identified as an obiect  
 public struct Object: Codable, Sendable {

// A unique UUID to indicate object's parent  
  public var parentIdentifier: UUID? { get }  
 }  
}

![Image 64](https://miro.medium.com/v2/resize:fit:528/1*YhLreSR8v8S9Vfst1gyMpg.png)

I looked up to this point and explained one limitation, and he explained it with a chair. A chair may have four legs, or it may have one. It can be an office chair or a rocking chair. Object’s Attribute helps to recognize these objects. This is said to be dealt with in more detail in the next presentation.

Enhanced export function
------------------------

When exporting, it became necessary to reflect the above additions.

A newly added method is a method of mapping each object using a UUID string value.

![Image 65](https://miro.medium.com/v2/resize:fit:700/1*oIFv__Mf5rnLXx_u3ArpXw.png)

In the past, when exporting CapturedRoom, only USDZ files were provided and JSON files could also be provided, but now it is possible to obtain a file containing mapping information in USDZ files.

![Image 66](https://miro.medium.com/v2/resize:fit:700/1*608eLw1IekNyNCN4tQFzOA.png)

This mapping information is useful. Since each element is mapped with an object, change it to the Model URL that embodies the object through the Model Provider added this time.

![Image 67](https://miro.medium.com/v2/resize:fit:700/1*pWzsu1zvD6u37X24_dwleg.png)

Detailed scan information can be obtained through the mapping information of the USDZ file for the entire space, not just one object above.

![Image 68](https://miro.medium.com/v2/resize:fit:700/1*fQHmN1XIuQIK4mVTjXch8A.png)

3D Model Catalog can be created using these Model URLs.

First of all, create a file structure using the category and attribute of the model.

![Image 69](https://miro.medium.com/v2/resize:fit:700/1*mznMWgIvrEePxUtVVKo6MQ.png)

Now create the index file. Below is the index file structure (RoomPlanCatalogCategoryAttribute). It includes Category and Attribute, and the model name below is also shown.

![Image 70](https://miro.medium.com/v2/resize:fit:700/1*nH7rpSlIMQSooajwlTfL6Q.png)

Create a catalog to store models.

![Image 71](https://miro.medium.com/v2/resize:fit:700/1*GmOQZKv17cdQ0h21OWfiSQ.png)

Create a Model Provider using the created Catalog.

![Image 72](https://miro.medium.com/v2/resize:fit:700/1*Ngu7YXeIUYYcmWXBKx3t-Q.png)

Now run export. The actual space and the space represented by the USDZ file look very similar.

![Image 73](https://miro.medium.com/v2/resize:fit:700/1*12-8H71AOSp2fB0sMN2V3g.png)

I felt that
-----------

First of all, I think it is a framework that is unreasonable to use in the field. iOS 17 also means that many users will have to give up.

Still, I thought that I could make a very strange app. Unlike when iOS 16 came out, it is now a framework that is being outlined, so it would be fun to create an actual app.

My iphone is 13 pro max. I think I bought this phone and finally used it properly.

Reference
---------

**By Ganesh |** [**LinkedIn**](https://www.linkedin.com/in/ganeshrajugalla/) **|** [**Medium**](https://medium.com/@ganeshrajugalla) **|** [**GitHub**](https://github.com/GaneshRajuGalla)

## Metadata

```json
{
  "title": "WWDC23 — Explore enhancements to RoomPlan - ganeshrajugalla - Medium",
  "description": "RoomPlan uses ARKit, which uses sophisticated machine learning algorithms, to recognize walls, windows, doors, empty spaces and objects. The RoomCaptureView API allows you to experience the…",
  "url": "https://medium.com/@ganeshrajugalla/wwdc23-explore-enhancements-to-roomplan-7ecbb8f68328",
  "content": "[![Image 51: ganeshrajugalla](https://miro.medium.com/v2/resize:fill:88:88/1*CWsSKCqvldt0tHppsYTiSw.jpeg)](https://medium.com/@ganeshrajugalla?source=post_page---byline--7ecbb8f68328--------------------------------)\n\n![Image 52](https://miro.medium.com/v2/resize:fit:700/1*B9nEEoM8FoPmoi978QSerQ.jpeg)\n\n> Obviously, the main theme of this WWDC is AR/VR. In fact, the reason I’m watching this WWDC is because I’m thinking of an app with AR features.\n\nRoomPlan uses ARKit, which uses sophisticated machine learning algorithms, to recognize walls, windows, doors, empty spaces and objects. The RoomCaptureView API allows you to experience the experience of scanning a room directly through an app. The result can be confirmed as a 3D model or extracted as a USDZ file.\n\nThis presentation covers four items.\n\n*   Custom ARSession support\n*   MultiRoom (combining multiple rooms into one space) support\n*   Accessibility (Voice Over)\n*   RoomPlan representations\n*   Enhanced export function\n\n> caution! : The above are APIs applied at least from iOS 16. And the improved features of RoomPlan will be applied from iOS 17.\n\nCustom ARSession support\n------------------------\n\nOriginally, only the given ARSession was used, but now ARSession using ARWorldTrackingConfiguration can be created and used.\n\n/// Create previous RoomCaptureSession  \npublic class RoomCaptureSession {  \n    public init() {  \n       ...  \n    }public func stop() {  \n       ...  \n    }  \n}\n\n/// Create a new RoomCaptureSession  \npublic class RoomCaptureSession {  \n    // Init: ARSession is an optional input for RoomCaptureSession  \n    public init(arSession: ARSession? = nil) {  \n       ...  \n  }// Stop: pauseARSession is used for whether to continue ARSession experience  \n    public func stop(pauseARSession: Bool = true) {  \n       ...  \n  }  \n}\n\nAdd photos and videos to RoomPlan scan\n\nMultiRoom support\n-----------------\n\nLet’s say you scanned the living room, my room, and the kitchen. What do I need to consider to put this together?\n\nFirst of all, all scan results have respective coordinate planes. Since they are not all scanned in the same space, they cannot be said to be the same coordinate plane. If you ignore this and simply attach rooms facing each other based on the wall, the objects will be duplicated.\n\nTherefore, we have to merge several same scan results into one coordinate plane system. To do this, Apple offers two methods.\n\n1.  Scan using the same ARSession.\n2.  Use ARSession relocalization.\n\nUse Continuous ARSession\n------------------------\n\nWhen the original RoomCaptureSession ended, the ARSession also stopped. However, due to the change in the stop function seen above, the same ARSession can be used repeatedly\n\n![Image 53](https://miro.medium.com/v2/resize:fit:700/1*7iBzU3k8-FCu6Ay9gQsXLg.png)\n\n`stop()`Based on , ARSession stops.\n\n![Image 54](https://miro.medium.com/v2/resize:fit:700/1*r2RCRpNihBgA4Q_fSeVK9g.png)\n\n`stop(pauseARSession: false)`causes the ARSession to persist. It will use the same coordinate plane system.\n\n// Continuous ARSession// start 1st scan  \nroomCaptureSession.run(configuration: captureSessionConfig)\n\n// stop 1st scan with continuing ARSession  \nroomCaptureSession.stop(pauseARSession: false)\n\n// start 2nd scan  \nroomCaptureSession.run(configuration: captureSessionConfig)\n\n// stop 2nd scan(pauseARSession = true by default)  \nroomCaptureSession.stop()\n\nARSession relocalization\n------------------------\n\nThe above method can be used to repeat multiple scans at the same time, but relocalization can be used if you want to shoot at a different time (tomorrow or next week, etc.).\n\nFirst, we need to save the ARWorldMap when the ARSession stops.\n\n![Image 55](https://miro.medium.com/v2/resize:fit:700/1*jc7Wvs7QG0gJjHLiSZM_ug.png)\n\nWhen scanning is repeated next time, a new scan can be started by calling the ARWorldMap stored in the stopped ARSession.\n\n![Image 56](https://miro.medium.com/v2/resize:fit:700/1*A_dgXFMyTEVHQY0quhq3rQ.png)\n\nThe code below shows the process of saving an ARWorldMap after performing the initial scan. For reference, since ARWorldMap is an NSObject, it can be saved as NSData using NSKeyedArchiver.\n\n// Capture with saving ARWorldMap// start 1st scan  \nroomCaptureSession.run(configuration: captureSessionConfig)\n\n// stop 1st scan (pauseARSession = true by default)  \nroomCaptureSession.stop()\n\n// save ARWorldMap  \nroomCaptureSession.arSession.getCurrentWorldMap(completionHandler:{worldMap, error in ...})\n\nAnd the code below shows the process of loading the saved ARWorldMap and scanning it again.\n\n// Capture with loading ARWorldMap// load ARWorldMap  \nlet arWorldMap = try NSKeyedUnarchiver.unarchivedObject(ofClass: ARWorldMap.self, from: data)\n\n// run ARKit relocalization  \nlet arWorldTrackingConfig = ARWorldTrackingConfiguration()  \narWorldTrackingConfig.initialWorldMap=arWorldMap  \nroomCaptureSession.init()  \nroomCaptureSession.arSession.ru(arWorldTrackingConfig, options: \\[\\])\n\n// Wait for relocalization to complete  \n// start 2nd scan  \nroomCaptureSession.run(configuration: captureSessionConfig)  \n// stop 2nd scan  \nroomCaptureSession.stop ()\n\nThus, the first and second scans have the same results as scanning in the same coordinate plane system.\n\nMultiRoom API\n-------------\n\nIf you have scanned multiple rooms using the above two methods, you need to merge them into one. Each scan can obtain a CapturedRoom object by using the RoomBuilder API.\n\n![Image 57](https://miro.medium.com/v2/resize:fit:700/1*bB87mrEdmbpjsYeRk0i8Eg.png)\n\nAnd what to do? Combine the CapturedRoom objects into one using StructureBuilder. The combined spatial data becomes a CapturedStructure object.\n\n![Image 58](https://miro.medium.com/v2/resize:fit:700/1*hAkz-4oT5k8HBzb4GYqbgA.png)\n\nA code example using the StructureBuilder API is shown below.\n\n// StructureBuilder// create structureBuilder instance  \nlet structureBuilder = StructureBuilder (option: \\[.beautifyObjects\\])\n\n// load multiple capturedRoom results to capturedRoomArray  \nvar capturedRoomArray: \\[CapturedRoom\\] = \\[\\]\n\n// run structureBuilder API to get capturedStructure  \nlet capturedStructure = try await structureBuilder.capturedStructure(from: capturedRoomArray)\n\n// export capturedStructure to usdz  \ntry capturedStructure.export (to: destinationURL)\n\nLet’s briefly point out the difference between CapturedRoom and CapturedStructure here.\n\n*   CapturedRoom = The result of scanning a single room.\n*   CapturedStructure = This is a structure that combines multiple CapturedRooms into one.\n\nRegarding the MultiRoom API, we plan to provide a sample app. I’ve tried to find the official documentation, but I can’t seem to find a page yet.\n\nThe USDZ file is a file format that can be viewed directly on iOS and macOS. USDZ files can also be run in digital content creation tools such as Blender.\n\nConsiderations\n--------------\n\nConsidering the space available for MultiRoom, the most suitable options were also provided.\n\n1.  One-story residential house with 4 beds, living room, kitchen and dining area\n2.  The size of all spaces to be merged is 2,000 ft square or 186 m square\n3.  Mining more than 50 lux\n\nAccessibility\n-------------\n\nVoice feedback using VoiceOver is provided for those who have visual difficulties in apps that use RoomPlan APIs.\n\nIn the demonstration video, a person who seemed to have zero emotion read ‘Point camera at bottom edge of wall’, ‘A fireplace’, ‘A wall’, ‘A window’ as they recognized them.\n\nRoomPlan representations\n------------------------\n\nSo far, RoomPlan’s scan results have only covered limited objects. This time, RoomPlan is said to be able to scan slanted walls, circular walls, and concave spaces such as ovens.\n\nIt also provides more detailed results for items that can be scanned, and a sofa was cited as an example. It is to collect single-seater sofas, L-shaped sofas, and straight sofas in a new way.\n\nThe reason this is possible is because the type of data collected by scanning has increased. Most of the categories that CapturedRoom can scan as mentioned above are expressed as internal structures called Surface and Object.\n\nHere’s some additional data.\n\n*   Section = represents the space inside the room.\n*   Surface -\\> Polygon = Now, walls can be expressed using Polygon, which is not a regular shape. (Curved walls, walls with beams attached, etc.)\n*   It is one of the categories that can be expressed as Surface -\\> Category -\\> floor = Polygon.\n*   Object -\\> Attribute = Added for more accurate object scanning.\n\n![Image 59](https://miro.medium.com/v2/resize:fit:700/1*fcrXOVNJDWvo5LryrKBSfA.png)\n\nAlso, Surfaces and Objects have a Parent added that references their parent (e.g. a window’s parent is a wall, a chair’s parent is a table).\n\n![Image 60](https://miro.medium.com/v2/resize:fit:700/1*fGovurxSkA-lTH-OrZxGZA.png)\n\nLet’s take a closer look at the code.\n\nAs you can see, all the spaces are divided, and each section has one label attached. Living Room, Dining Room, and Undefined are one space, but they are divided into Sections.\n\npublic struct CapturedStructure: Codable, Sendable {  \n public struct Section: Codable, Sendable {  \n  public enum Label: String, Codable, Sendable {  \n   case livingRoom  \n   case bedroom   \n            case bathroom   \n            case kitchen   \n            case diningRoom   \n            case unidentified  \n  }public var label: Label { get }\n\n// The center position of the section  \n  public var center: simd\\_float3 { get }\n\n// Indicator for which story, level, or floor  \n  public var story: Int { get }  \n }  \n}\n\n![Image 61](https://miro.medium.com/v2/resize:fit:638/1*U4Qfd3G-uF2GgbYRZAmLvQ.png)\n\nPolygons allow us to recognize non-planar structures as well. In addition, the scanned floor is changed into a more elegant form through floor added to the category.\n\n// Floors for Surfaces in CapturedRoompublic struct CapturedRoom: Codable, Sendable {\n\n// A 2D area in a room identified as a surface  \n public struct Surface: Codable, Sendable {\n\n// A 2D polygon to represent walls and floors  \n  // in local plan coordinates  \n  public var polygonCorners: \\[sim\\_float3\\] { get }\n\n// classifications of a surface in a captured room  \n  public enum Category: Codable, Sendable {  \n   case floor  \n  }  \n }  \n}\n\n![Image 62](https://miro.medium.com/v2/resize:fit:632/1*WkJAqSbz7RbgE3W0MiMJdw.png)\n\nPolygon using wall\n\n![Image 63](https://miro.medium.com/v2/resize:fit:572/1*fM_QKWwJcn0MlCs6UmQaWw.png)\n\nPolygon using floor\n\nThis is the most exciting part for me personally. Thanks to the ability to recognize the parent of the object mentioned above, it is possible to recognize kitchen utensils as shown below.\n\n// Parent identifiers for surfaces and objects in CapturedRoom  \npublic struct CapturedRoom: Codable, Sendable {  \n // A 2D area in a room identified as a surface  \n public struct Surface: Codable, Sendable {// A unique UUID to indicate surface's parent  \n        public var parentIdentifier: UUID? { get }  \n }\n\n// A 3D area in a room identified as an obiect  \n public struct Object: Codable, Sendable {\n\n// A unique UUID to indicate object's parent  \n  public var parentIdentifier: UUID? { get }  \n }  \n}\n\n![Image 64](https://miro.medium.com/v2/resize:fit:528/1*YhLreSR8v8S9Vfst1gyMpg.png)\n\nI looked up to this point and explained one limitation, and he explained it with a chair. A chair may have four legs, or it may have one. It can be an office chair or a rocking chair. Object’s Attribute helps to recognize these objects. This is said to be dealt with in more detail in the next presentation.\n\nEnhanced export function\n------------------------\n\nWhen exporting, it became necessary to reflect the above additions.\n\nA newly added method is a method of mapping each object using a UUID string value.\n\n![Image 65](https://miro.medium.com/v2/resize:fit:700/1*oIFv__Mf5rnLXx_u3ArpXw.png)\n\nIn the past, when exporting CapturedRoom, only USDZ files were provided and JSON files could also be provided, but now it is possible to obtain a file containing mapping information in USDZ files.\n\n![Image 66](https://miro.medium.com/v2/resize:fit:700/1*608eLw1IekNyNCN4tQFzOA.png)\n\nThis mapping information is useful. Since each element is mapped with an object, change it to the Model URL that embodies the object through the Model Provider added this time.\n\n![Image 67](https://miro.medium.com/v2/resize:fit:700/1*pWzsu1zvD6u37X24_dwleg.png)\n\nDetailed scan information can be obtained through the mapping information of the USDZ file for the entire space, not just one object above.\n\n![Image 68](https://miro.medium.com/v2/resize:fit:700/1*fQHmN1XIuQIK4mVTjXch8A.png)\n\n3D Model Catalog can be created using these Model URLs.\n\nFirst of all, create a file structure using the category and attribute of the model.\n\n![Image 69](https://miro.medium.com/v2/resize:fit:700/1*mznMWgIvrEePxUtVVKo6MQ.png)\n\nNow create the index file. Below is the index file structure (RoomPlanCatalogCategoryAttribute). It includes Category and Attribute, and the model name below is also shown.\n\n![Image 70](https://miro.medium.com/v2/resize:fit:700/1*nH7rpSlIMQSooajwlTfL6Q.png)\n\nCreate a catalog to store models.\n\n![Image 71](https://miro.medium.com/v2/resize:fit:700/1*GmOQZKv17cdQ0h21OWfiSQ.png)\n\nCreate a Model Provider using the created Catalog.\n\n![Image 72](https://miro.medium.com/v2/resize:fit:700/1*Ngu7YXeIUYYcmWXBKx3t-Q.png)\n\nNow run export. The actual space and the space represented by the USDZ file look very similar.\n\n![Image 73](https://miro.medium.com/v2/resize:fit:700/1*12-8H71AOSp2fB0sMN2V3g.png)\n\nI felt that\n-----------\n\nFirst of all, I think it is a framework that is unreasonable to use in the field. iOS 17 also means that many users will have to give up.\n\nStill, I thought that I could make a very strange app. Unlike when iOS 16 came out, it is now a framework that is being outlined, so it would be fun to create an actual app.\n\nMy iphone is 13 pro max. I think I bought this phone and finally used it properly.\n\nReference\n---------\n\n**By Ganesh |** [**LinkedIn**](https://www.linkedin.com/in/ganeshrajugalla/) **|** [**Medium**](https://medium.com/@ganeshrajugalla) **|** [**GitHub**](https://github.com/GaneshRajuGalla)",
  "publishedTime": "2023-06-12T15:54:56.441Z",
  "usage": {
    "tokens": 3594
  }
}
```
