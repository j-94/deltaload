---
title: Scan to BIM, for real - with IFC?
description: I do scanning of heritage buildings and it is painful to see how a millimetre precision scan gets modeled with decimeter errors into a flat, right angled, perfectly plumb and even thickness wall in BIM software.
url: https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc
timestamp: 2025-01-20T15:42:48.045Z
domain: community.osarch.org
path: discussion_1163_scan-to-bim-for-real-with-ifc
---

# Scan to BIM, for real - with IFC?


I do scanning of heritage buildings and it is painful to see how a millimetre precision scan gets modeled with decimeter errors into a flat, right angled, perfectly plumb and even thickness wall in BIM software.


## Content

Scan to BIM, for real - with IFC? — OSArch
=============== 

toggle menu

 [![Image 71: OSArch](https://community.osarch.org/uploads/de6adc1b2433bca292f0fdec02c9da1e.png)](https://community.osarch.org/)[![Image 72: OSArch](https://community.osarch.org/uploads/a8113bffcd015452fcb76db9f6a332bb.png)](https://community.osarch.org/)

[Categories](https://community.osarch.org/categories)

[Discussions](https://community.osarch.org/discussions)

[Wiki](https://wiki.osarch.org/)

[Live Chat](https://osarch.org/chat)

[Back to OSArch.org](https://osarch.org/)

[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc) · [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc)

[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc) · [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc)

[Categories](https://community.osarch.org/categories)

[Discussions](https://community.osarch.org/discussions)

[Activity](https://community.osarch.org/activity)

[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc) · [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc)

×

[Home](https://community.osarch.org/) › [General](https://community.osarch.org/categories/general)

Scan to BIM, for real - with IFC?
=================================

[![Image 73: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")[Hagaeus](https://community.osarch.org/profile/Hagaeus)

[October 2022](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc) edited October 2022 in [General](https://community.osarch.org/categories/general)

I do scanning of heritage buildings and it is painful to see how a millimetre precision scan gets modeled with decimeter errors into a flat, right angled, perfectly plumb and even thickness wall in BIM software. That is not how they look.

I have tried to cut up a mesh and assign IFC classes to the parts, but it really struggles with big meshes. In vanilla Blender I can handle 100 million polys with acceptable lag, but converting to IFC crashes already at 10 million.  
I can simplify them a lot of course but then I also loose detail.

How to approach this? Is the IFC inherently bad at mesh, or is there a way to fix that? Should I detach the mesh from the IFC in some way instead? Other suggestions?

![Image 74](https://community.osarch.org/uploads/editor/sj/ukbfrc5h1s91.jpg)

[![Image 75: carlopav](https://community.osarch.org/uploads/userpics/381/nRXYZUZ2ZBIM4.jpg)](https://community.osarch.org/profile/carlopav "carlopav")[![Image 76: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace "Ace")[![Image 77: RaphaëlVouilloz](https://community.osarch.org/uploads/userpics/673/n8RKIQD0RTEYI.jpg)](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz "RaphaëlVouilloz")[![Image 78: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious "Gorgious")[![Image 79: CadGiru](https://community.osarch.org/uploads/userpics/771/n9EA1SGIY3DD7.JPG)](https://community.osarch.org/profile/CadGiru "CadGiru")[![Image 80: PavlosDem9](https://secure.gravatar.com/avatar/d9861123fcbf2053d09b017023b72dec/?default=https%3A%2F%2Fvanillicon.com%2F39de0a7c0668b7658cd5215a87e16f55_200.png&rating=g&size=200)](https://community.osarch.org/profile/PavlosDem9 "PavlosDem9")

«[1](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc)[2](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc/p2)[»](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc/p2)

Comments
--------

*   [![Image 81: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace "Ace")[Ace](https://community.osarch.org/profile/Ace)
    
    [October 2022](https://community.osarch.org/discussion/comment/12843/#Comment_12843)
    
    Could I ask what you process is for the scan to mesh?  
    A point cloud from a laser scan, then you import as an obj into Blender? and then begin converting to Ifc?  
    Would it not be possible to use IfcOpenShell directly to make an IFC without first going into Blender?  
    I haven't used IfcOpenShell myself but taking out the Obj process might speed things up
    
*   [![Image 82: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious "Gorgious")[Gorgious](https://community.osarch.org/profile/Gorgious)
    
    [October 2022](https://community.osarch.org/discussion/comment/12844/#Comment_12844)
    
    From my experience IFC and more broadly, AEC programs are not tailored for defining existing building with precision. AFAIK in REVIT, Archicad and Blender's Archipack addon you can't define a regular wall with varying width. I think your desired workflow here if you want to preserve data integrity is not to define the geometry inside the IFC file but to use a link to a model you'll share alongside with it, and open with a dedicated 3D modeling program, not a CAD authoring tool. Until we get quantum computers I don't think architects and engineers will accept to work with millions of polygons for a simple beam. :)
    
    I've been scratching my head at this problem for a while, too so I'd really like any workflow improvement exploration :)
    
*   [![Image 83: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult "Moult")[Moult](https://community.osarch.org/profile/Moult)
    
    [October 2022](https://community.osarch.org/discussion/comment/12845/#Comment_12845)
    
    In theory what you're doing could work, but in practice there are some problems:
    
    1.  The IFC STEP serialisation (.ifc file) is ASCII and very, very inefficient at storing high poly objects. Expect very large filesizes and slow reading. There is a way to bypass this by using HDF5 serialisation which has experimental support in IfcOpenShell, which was used for point clouds in IFC [https://github.com/IfcOpenShell/IfcOpenShell/issues/760](https://github.com/IfcOpenShell/IfcOpenShell/issues/760) - but it is highly experimental.
    2.  IfcOpenShell uses OpenCASCADE out of the box to process tessellations, which means that its converting your mesh into a geometrically perfect BRep (and thus very, very inefficient), so expect load times to be so slow it's basically impractical. Note there is a way to bypass this and use "Native Meshes" in advanced mode when loading, but that's for things like 20-40k polys, definitely not 10 million. And of course that's assuming you solve problem 1 first.
    
    In my opinion, this is not IFC's problem to solve. IFC should focus on what it does best - semantics for the AEC industry... where semantics overlap with geometry, IFC may get involved (e.g. parametric I-beams, profile cardinality, parametric layered materials and extrusions), but high poly meshes is definitely _not_ semantic and sounds very much like the domain of the CG / scanning world. I would propose merely recording simple forms (perhaps highly decimated) and then referencing an external file for the high-res mesh.
    
    However, these "low res proxies linking to high res external sources" is merely my own theory, and is not officially part of the schema (though maybe in the future it may be?). It's what I did for things like Radiance support which had similar issues, and for things like CG viz and grass blade instances. If you go this route, use an external library reference relationship.
    
    For my Radiance examples, I stored the meshes as OBJ, but since it's an unofficial convention, do what you want ;)
    
    [![Image 84: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious "Gorgious")[![Image 85: Martin156131](https://community.osarch.org/uploads/userpics/398/nJUZMRIKZD54F.png)](https://community.osarch.org/profile/Martin156131 "Martin156131")[![Image 86: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")[![Image 87: cvillagrasa](https://community.osarch.org/uploads/userpics/137/nXVSWS33CR6PC.jpg)](https://community.osarch.org/profile/cvillagrasa "cvillagrasa")[![Image 88: fusionBIM](https://secure.gravatar.com/avatar/0671699a79c4971923c31577b62d18ec/?default=https%3A%2F%2Fvanillicon.com%2Fd7147ad1c37004dde05245a3b621b0c6_200.png&rating=g&size=200)](https://community.osarch.org/profile/fusionBIM "fusionBIM")
    
*   [![Image 89: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")[Hagaeus](https://community.osarch.org/profile/Hagaeus)
    
    [October 2022](https://community.osarch.org/discussion/comment/12867/#Comment_12867) edited October 2022
    
    First my process: I combine laser scans and photogrammetry in RealityCapture to produce a textured mesh. I then import it to Blender to cut it up. I usually just separate the rooms to give the customer the possibility to open one room at a time. That way they don't need a beefy computer and it's easier to look at that room with backface culling and nothing else in the way.  
    For me pointclouds are just a step in the process and not useful for anything but some calculations. They are horrible to navigate as they have no real surface, update as you go, and no backface culling.
    
    My goal is to segment all the parts. Walls, floors. beams etc. and also be able to add information like salt problems in masonry, sensor readings, rot and so on as separate geometry. As well as all the usual maintanance intervall and so on.
    
    I thought .ifc was more agnostic to geometry and able to handle meshes without transforming them to Brep. And I am unfortunately not the guy to write code to get it to work with workarounds. What I may be able to do is get funding so one of you guys can do it, if you think it's worth. I can imagine also architects could enjoy not being limited to Brep.
    
    [![Image 90: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace "Ace")[![Image 91: cvillagrasa](https://community.osarch.org/uploads/userpics/137/nXVSWS33CR6PC.jpg)](https://community.osarch.org/profile/cvillagrasa "cvillagrasa")[![Image 92: fusionBIM](https://secure.gravatar.com/avatar/0671699a79c4971923c31577b62d18ec/?default=https%3A%2F%2Fvanillicon.com%2Fd7147ad1c37004dde05245a3b621b0c6_200.png&rating=g&size=200)](https://community.osarch.org/profile/fusionBIM "fusionBIM")
    
*   [![Image 93: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")[Hagaeus](https://community.osarch.org/profile/Hagaeus)
    
    [October 2022](https://community.osarch.org/discussion/comment/12888/#Comment_12888)
    
    Just saw the interview with Thomas Krijnen on BIMvoice and he mentioned he had actually worked on integrating mesh, and was almost there. Is he on here under some pseodonym?
    
    [![Image 94: condur](https://community.osarch.org/uploads/userpics/385/nBG6153YR211L.jpg)](https://community.osarch.org/profile/condur "condur")
    
*   [![Image 95: theoryshaw](https://community.osarch.org/uploads/userpics/399/n1LFZQA87XEVG.png)](https://community.osarch.org/profile/theoryshaw "theoryshaw")[theoryshaw](https://community.osarch.org/profile/theoryshaw)
    
    [October 2022](https://community.osarch.org/discussion/comment/12889/#Comment_12889)
    
    [@aothms](https://community.osarch.org/profile/aothms) , sorry Thomas. ;) Great interview, btw. :)
    
    [![Image 96: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")[![Image 97: CadGiru](https://community.osarch.org/uploads/userpics/771/n9EA1SGIY3DD7.JPG)](https://community.osarch.org/profile/CadGiru "CadGiru")
    
*   [![Image 98: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace "Ace")[Ace](https://community.osarch.org/profile/Ace)
    
    [October 2022](https://community.osarch.org/discussion/comment/12890/#Comment_12890)
    
    I think that's [@aothms](https://community.osarch.org/profile/aothms) ?
    
    [![Image 99: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")
    
*   [![Image 100: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult "Moult")[Moult](https://community.osarch.org/profile/Moult)
    
    [October 2022](https://community.osarch.org/discussion/comment/12904/#Comment_12904)
    
    > I thought .ifc was more agnostic to geometry and able to handle meshes
    
    It is, it can handle tessellations, yet still runs into the two issues I described above. I guess one option is to try and overcome the two issues via HDF5 and a dedicated mesh parser, and the second option is to only use IFC for semantics and develop a convention for referencing externally defined high-res meshes (e.g. via OBJ, glB, or other open data standard) which can be proposed to buildingSMART for IFC5 (but backwards compatible).
    
    The latter sounds easier to me :)
    
    [![Image 101: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace "Ace")
    
*   [![Image 102: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms "aothms")[aothms](https://community.osarch.org/profile/aothms)
    
    [October 2022](https://community.osarch.org/discussion/comment/12919/#Comment_12919)
    
    Hey guys, immensely interesting subject. The IFC-HDF5 work we did was also for cultural heritage documentation. We opted for the approach of a regular bim model and then storing the point cloud segments as offsets to those surfaces. We focussed only on the semantic storage and retrieval efficiency. We just assumed a handmodelled IFC model exist that corresponds to the point cloud. What was nice about this was that the compression we got from storing the points as offsets also made the combination of these two so semantically interesting.
    
    Yes, in the talk with Petru from Bimvoice I indeed mentioned the work I have been doing for a couple of years already on being able to select alternative geometry libraries. That would indeed eliminate the BRep reconstruction as highlighted by [@Moult](https://community.osarch.org/profile/Moult). HDF5 could indeed eliminate the difficulties with storing large arrays as textual formats. But even if both were production ready it's still not really realistic to efficiently perform realtime modifications on them. Isolating mesh or point cloud segments into new representations for elements still means move ridiculous amounts of data around that neither HDF5 nor IFC schema is intended for.
    
    Most efficient would be to store the mesh as a monolithic array and rather use something like vertex groups or a separate channel of data to store the association to building element ids. So that you edit by changing _values_ and not _structure_. And then indeed a way to reference that from IFC or periodically bake this into an IFC file. In HDF5 something like this would be possible by using _Region references_ so that entity instance attribute values would actually be subsets of this monolithic array. Blender and HDF5 both have good interfaces with numpy, so there might be something possible.
    
    [![Image 103: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace "Ace")[![Image 104: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious "Gorgious")[![Image 105: carlopav](https://community.osarch.org/uploads/userpics/381/nRXYZUZ2ZBIM4.jpg)](https://community.osarch.org/profile/carlopav "carlopav")[![Image 106: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")[![Image 107: cvillagrasa](https://community.osarch.org/uploads/userpics/137/nXVSWS33CR6PC.jpg)](https://community.osarch.org/profile/cvillagrasa "cvillagrasa")[![Image 108: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult "Moult")
    
*   [![Image 109: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")[Hagaeus](https://community.osarch.org/profile/Hagaeus)
    
    [October 2022](https://community.osarch.org/discussion/comment/12926/#Comment_12926)
    
    So if we use vertex groups for example and link that to the IFC schema, Would that be readable (in a longer perspective) in other software, or never leave BlenderBIM? And what happens if you make a door in this vertexgroup?
    
    For me to be able to get funding it needs to work outside BlenderBIM. Perhaps not immediately, but eventually, and have a chance of becoming a standard.
    
    How much time and money (very, very roughly) are we talking about?
    
*   [![Image 110: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult "Moult")[Moult](https://community.osarch.org/profile/Moult)
    
    [October 2022](https://community.osarch.org/discussion/comment/12929/#Comment_12929)
    
    To make this work in other software, it would need to be a project supported by buildingSMART. It would definitely not be immediate. Maybe [@berlotti](https://community.osarch.org/profile/berlotti) might know if it's of interest?
    
*   [![Image 111: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms "aothms")[aothms](https://community.osarch.org/profile/aothms)
    
    [October 2022](https://community.osarch.org/discussion/comment/12930/#Comment_12930)
    
    Ok, also note that I was talking solely about efficiency. My approach collides with BlenderBIM's native IFC editing because of the non-standard way of relating mesh segments to elements. And also it might not be what you want from a usability perspective, because when you hide all this information in mesh channels there's a lot of Blender navigation functionality that doesn't work anymore (e.g conveniently hiding objects by type or sth).
    
    It was just a thought I had that even if you do HDF5, moving around large mesh subsets from one instance to the other is going to be painful because HDF5 statically arranges the datasets and doesn't "vacuum" empty space. Hence my thoughts on creating region references into a monolithic array and trying to see if there is an equivalent for that in Blender. So again, solely thinking from performance, I was hoping for some refinement on this idea in the thread maybe with ideas thinking more from the viewpoint of UX.
    
    To me this sounds more like a EU-funded project or sth. Heritage and digitalization are always topics on the agenda. The RWTH design computation group has done some could heritage and ifc related things and they know blenderbim and I know Duncan has brought up EU-funded projects earlier. This might be the thing.
    
    [![Image 112: theoryshaw](https://community.osarch.org/uploads/userpics/399/n1LFZQA87XEVG.png)](https://community.osarch.org/profile/theoryshaw "theoryshaw")[![Image 113: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace "Ace")
    
*   [![Image 114: berlotti](https://community.osarch.org/uploads/userpics/304/n8A1A9L2VAXWY.jpeg)](https://community.osarch.org/profile/berlotti "berlotti")[berlotti](https://community.osarch.org/profile/berlotti)
    
    [October 2022](https://community.osarch.org/discussion/comment/12956/#Comment_12956)
    
    There would definitely be interest. Biggest challenge will probably be to define a clear objective, scope, intended outcome, etc. Happy to help!
    
    [![Image 115: theoryshaw](https://community.osarch.org/uploads/userpics/399/n1LFZQA87XEVG.png)](https://community.osarch.org/profile/theoryshaw "theoryshaw")[![Image 116: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace "Ace")
    
*   [![Image 117: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult "Moult")[Moult](https://community.osarch.org/profile/Moult)
    
    [October 2022](https://community.osarch.org/discussion/comment/12960/#Comment_12960) edited October 2022
    
    Just speculating here, what if a "perfect" geometry was stored (i.e. the typical parametric extruded beam prism) but alongside it was referenced raw textures which represented offset from the base surface of the perfect geometry. No need to load 2 billion points, can in theory scale very, very easily (just zoom into interested area, inspect texture as displacement map where necessary. Algorithms that were mixed between human intervention and AABB/OBB generation could be used to rapidly create this proxy perfect surface.
    
    We could probably cook up a prototype in Blender within a week or so, reusing Blender's XYZ map baking abilities.
    
*   [![Image 118: RaphaëlVouilloz](https://community.osarch.org/uploads/userpics/673/n8RKIQD0RTEYI.jpg)](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz "RaphaëlVouilloz")[RaphaëlVouilloz](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz)
    
    [October 2022](https://community.osarch.org/discussion/comment/12962/#Comment_12962)
    
    At CNPA EPFL we are also really interested in this topic for HBIM ; we could do some tests if you develop prototypes.  
    I would point that :  
    \-To produce high quality photomesh models becomes more and more easy and accessible.  
    \-As Blender is perfect to work on the mesh, it would be a great process to classify the photomesh in IFC with BlenderBIM.  
    \-It also becomes easy to share such a work with three.js and IFC.js
    
    I am also interested to see how we could classify a Pointcloud in IFC.
    
*   [![Image 119: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms "aothms")[aothms](https://community.osarch.org/profile/aothms)
    
    [October 2022](https://community.osarch.org/discussion/comment/12964/#Comment_12964)
    
    In our work we proposed three methods:
    
    ![Image 120](https://community.osarch.org/uploads/editor/p7/p08pfuhc7vhy.png)
    
    [https://pure.tue.nl/ws/files/119667686/20190402\_Krijnen.pdf](https://pure.tue.nl/ws/files/119667686/20190402_Krijnen.pdf)
    
    What [@Moult](https://community.osarch.org/profile/Moult) describes is basically the third level. Maybe indeed using textures is a nice middle ground between semantics and ease of use in Blender. You'd obviously need to use some psets or sth to map the \[0,255\] range onto the physical range of deviations. But essentially this is exactly what we did, we also quantized the point cloud deviations for compression. In the end we just had a little semantic structure to store the deviations, but you could easily opt for storing them as textures.
    
    You'd run in to the limitations of IFC and textures though, especially for extrusions there is very little control over the UV coords, so you'd likely end up with extremely non-uniform texture resolution. So maybe you'd make different choices there, e.g probably not to use extrusions. Or use the schema extension when writing IFC and keep the textures solely as a way to represent them in Blender.
    
    What we were also interested in is seeing the progression of deviation over time, e.g structural health monitoring. So I think that would also be something to account for that you might have multiple scans associated to the same model. Analyse the deviations as a 2d function and then compute the differences in parameters for these function to assess the rate of change.
    
    > To produce high quality photomesh models becomes more and more easy and accessible.
    
    Are you suggesting not to use point clouds, but rather photogrammetry? Or what is a photomesh precisely?
    
    [![Image 121: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")
    
*   [![Image 122: RaphaëlVouilloz](https://community.osarch.org/uploads/userpics/673/n8RKIQD0RTEYI.jpg)](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz "RaphaëlVouilloz")[RaphaëlVouilloz](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz)
    
    [October 2022](https://community.osarch.org/discussion/comment/12965/#Comment_12965) edited October 2022
    
    Really interesting aothms, thanks.  
    A photomesh is built on pointclouds, it triangles the points to create surfaces and if you have done your capture through photogrammetry, you can texture these surfaces.  
    You can have really precise pointclouds through lasergammetry (3d scans), you can then convert it in meshes but not texturize it. Although some scanners as Faro do take also photos to allow you to do it. Or you can mix both techniques with a laser and your own camera, as we did on the first project here : [https://enac-cnpa.github.io/IFCjs-Stereotomie/](https://enac-cnpa.github.io/IFCjs-Stereotomie/)  
    The fact is softwares like Revit and Archicad let you work really easily on pointclouds, but are really not good at importing huge photomesh to model on it. Blender is, and so BlenderBIM would be really a unique tool, if we beginn to scan to bim from photomesh and not anymore from pointclouds. On photomesh you have more comprehensive infos, think for example to a fresco or joints on a stone assembly.  
    I say photomesh become accessible because of tools as Scaniverse. An architect now just needs an Ipad, whitout understanding anything of all these process, to create a photomesh and start to work on in Blender.
    
    [![Image 123: PavlosDem9](https://secure.gravatar.com/avatar/d9861123fcbf2053d09b017023b72dec/?default=https%3A%2F%2Fvanillicon.com%2F39de0a7c0668b7658cd5215a87e16f55_200.png&rating=g&size=200)](https://community.osarch.org/profile/PavlosDem9 "PavlosDem9")
    
*   [![Image 124: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms "aothms")[aothms](https://community.osarch.org/profile/aothms)
    
    [October 2022](https://community.osarch.org/discussion/comment/12967/#Comment_12967)
    
    Thanks for explaining, it's been a while since I worked on this. We indeed had these Faro scanners that give an additional colour channel by internally pairing the point cloud with regular photographs. On the one hand, indeed a mesh is much easier to consume visually, on the other hand, it's also quite a destructive process (not sure how much smoothing is involved) but I guess quite a few points are discarded in order to get a reasonable manifold surface. I don't think Blender is even able to actually display the colour channel on points though so there are definitely quite a few arguments to use mesh. I guess it depends on personal preference, required accuracy, documentation requirements and completeness of scan vs amount of geometric detail.
    
    Circling back to the original questions:
    
    > For me to be able to get funding it needs to work outside BlenderBIM
    
    What are we exploring here: multi-year funded project or trying to make some quick progress on the great foss tools that are currently already available. Or both? Maybe we should setup a quick online get together to quickly outline everybody's interests in this topic?
    
*   [![Image 125: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult "Moult")[Moult](https://community.osarch.org/profile/Moult)
    
    [October 2022](https://community.osarch.org/discussion/comment/12968/#Comment_12968)
    
    > to map the \[0,255\] range
    
    EXR :)
    
*   [![Image 126: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms "aothms")[aothms](https://community.osarch.org/profile/aothms)
    
    [October 2022](https://community.osarch.org/discussion/comment/12969/#Comment_12969)
    
    Yes, I actually thought of that, but do you get reasonable colour values when you look at that in the 3d view? That would be even cooler though, maybe there is a live colour map you can slap onto it.
    
*   [![Image 127: tobenz](https://secure.gravatar.com/avatar/30f5473760f285c39fc2a2b9817d812a/?default=https%3A%2F%2Fvanillicon.com%2F5c8ff3934561922ee76c36279eef0caa_200.png&rating=g&size=200)](https://community.osarch.org/profile/tobenz "tobenz")[tobenz](https://community.osarch.org/profile/tobenz)
    
    [October 2022](https://community.osarch.org/discussion/comment/12977/#Comment_12977)
    
    I'm not really sure if point cloud data should make it into an IFC model at all. 3D scans are made several times during construction and operation of a building. What is the geometry of an object then?  
    I would find it much more helpful if all those scans would be geo referenced and I could grab the relevant portion of the point cloud using my element bounding box. The goal should be clean and efficient geometry to not bloat the ifc file size. Abstraction is king.
    
    [![Image 128: carlopav](https://community.osarch.org/uploads/userpics/381/nRXYZUZ2ZBIM4.jpg)](https://community.osarch.org/profile/carlopav "carlopav")
    
*   [![Image 129: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms "aothms")[aothms](https://community.osarch.org/profile/aothms)
    
    [October 2022](https://community.osarch.org/discussion/comment/12978/#Comment_12978)
    
    [@tobenz](https://community.osarch.org/profile/tobenz) this depends on the use case though. First of all, what I was saying with HDF5 isn't too far off of what you say, one big dataset with point clouds, and instead of doing a lookup by bounding box, you directly associate point cloud segments to the elements (as the primary representation or supplementary with a timestamp).
    
    More generally (you see this also with IfcTunnel now for example and geotechnical datasets) there is the need to make meaningful semantic connections for documentation purposes, so then you either need to:
    
    1.  internalize the dataset in IFC and use relationships,
    2.  use a container format like ICDD to keep both files separate and include a third file that makes links between subsets) or
    3.  somehow use external references from one dataset into the other.
    
    The pros and cons of these are fairly obvious, but how you weigh them depends on the use case.
    
*   [![Image 130: Bimlooser](https://secure.gravatar.com/avatar/07d3eb90596bac5de9bf8047142ccb99/?default=https%3A%2F%2Fvanillicon.com%2F1c993d5d8ad44364df420074422fc059_200.png&rating=g&size=200)](https://community.osarch.org/profile/Bimlooser "Bimlooser")[Bimlooser](https://community.osarch.org/profile/Bimlooser)
    
    [October 2022](https://community.osarch.org/discussion/comment/12980/#Comment_12980)
    
    Maybe this guy [https://github.com/florentPoux](https://github.com/florentPoux) can be useful
    
*   [![Image 131: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")[Hagaeus](https://community.osarch.org/profile/Hagaeus)
    
    [October 2022](https://community.osarch.org/discussion/comment/12984/#Comment_12984)
    
    Gigantic meshes are a problem of course. Can be solved with LOD (Level of Detail, as in game engine, not the architectural version). I usually make a web version of the mesh with low polycount and Normal maps, and one high poly version for measures, 3d-print and calculations. Clipping box is useful of course as even a low poly royal palace has millions of triangles. We can also hope for Unreal engines Nanite goes open-source and implemented in all 3d sofware (yeah, right).
    
    I am doing a prestudy right now for the National Heritage Board about the implementation of the EU recommendations from 2011, updated 2021, stating that:  
    "The digital strategy should set clear digitisation and digital preservation goals. Those goals should be based on objective and clear criteria, including:  
    (a) cultural heritage at risk,  
    (b) the most physically visited cultural and heritage monuments, buildings and sites and  
    (c) the low level of digitisation for specific categories of cultural heritage assets.  
    By 2030, Member States should digitise in 3D all monuments and sites falling under (a) and 50% of those falling under (b).  
    By 2025, Member States should digitise 40% of the overall 2030 targets.  
    Member States should take the necessary measures to ensure that all digitised cultural assets referred to in point 6 (a), (b) and (c) are also digitally preserved."  
    This will hopefully lead to a lot of heritage being scanned. It would be a pity if those scans just rotted away on a harddrive somewhere and only were used in case of destruction of the monument. They should be used for visualisations for the public and also BIM models for the administration. But seeing all these wonderful buildings as Revit cardboard boxes will break my heart.
    
    So there is potential for big money, but I can only affect little Sweden and would need help from you others. If we can set a goal, a way there, an estimated budget and timeschedule, it will be a lot easier to get funding. Do you think it is possible in a few years perspective?
    
*   [![Image 132: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult "Moult")[Moult](https://community.osarch.org/profile/Moult)
    
    [October 2022](https://community.osarch.org/discussion/comment/12985/#Comment_12985)
    
    I am also aware of an Australian NSW initiative to scan every single heritage sandstone building here (though I heard they had funding heavily cut) but perhaps I can help reach out to some Australian contacts here and make a connection if you'd like to take the lead?
    
*   [![Image 133: duncan](https://community.osarch.org/uploads/userpics/126/n73IZIYE779NH.png)](https://community.osarch.org/profile/duncan "duncan")[duncan](https://community.osarch.org/profile/duncan)
    
    [October 2022](https://community.osarch.org/discussion/comment/12990/#Comment_12990)
    
    [@Hagaeus](https://community.osarch.org/profile/Hagaeus) here in Denmark we have Molio which might be well suited to taking the lead on an initiative like this. Is there anything similar in Sweden?
    
*   [![Image 134: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus "Hagaeus")[Hagaeus](https://community.osarch.org/profile/Hagaeus)
    
    [October 2022](https://community.osarch.org/discussion/comment/12993/#Comment_12993)
    
    [@duncan](https://community.osarch.org/profile/duncan) I think that would be the equivalent of Boverket. I actually talked to a guy there this week who was interested in a co-operation regarding other stuff. That is a great idea as they are under the finance department and therefore have money, unlike the Heritage board that is under the Culture department.
    
    [@Moult](https://community.osarch.org/profile/Moult) I could do that next year if I get some support from others. I am a one man company with the workload for two, plus admin, right now. Getting support from Australia would show that it is of international interest as well. I guess you are the one for lobbying towards BuildingSmart? Or does anyone else have good connections there?
    
*   [![Image 135: paireks](https://community.osarch.org/uploads/userpics/745/nQIDJTUDZ7T10.png)](https://community.osarch.org/profile/paireks "paireks")[paireks](https://community.osarch.org/profile/paireks)
    
    [October 2022](https://community.osarch.org/discussion/comment/12994/#Comment_12994)
    
    Hey [@Hagaeus](https://community.osarch.org/profile/Hagaeus)  
    it would be interesting if you could try out using .bim file format for that ([https://dotbim.net/](https://dotbim.net/)), and let me know the results.  
    For tests I created a mesh with 12 500 000 triangles in Grasshopper. I attached some custom data to it and exported it as .bim. It took as you can see below 52 seconds to save that file, and it is 1.13 GB big. After simple ZIP it reduced the size to 140 MB. There is still room for improvement there (removing white spaces, removing unnecessary decimal numbers, quality of mesh).  
    ![Image 136](https://community.osarch.org/uploads/editor/l3/8tbbaihj7mc5.png)  
    Then I imported it to Blender and it works fine:  
    ![Image 137](https://community.osarch.org/uploads/editor/cx/wudp1dvwow7b.png)
    
    Regarding having a giant meshes in a model and LOD, one of the ideas was to actually store different LODs in separate models and link them together, rather than having it all in one giantic model / file. Not sure if such concept would be interesting for scans, but you can also check it out there and let me know what you think: [https://github.com/paireks/dotbim/blob/master/LinkingData.md](https://github.com/paireks/dotbim/blob/master/LinkingData.md)
    
*   [![Image 138: mattsharon](https://community.osarch.org/uploads/userpics/306/nH8GYDBXGHUJ2.jpg)](https://community.osarch.org/profile/mattsharon "mattsharon")[mattsharon](https://community.osarch.org/profile/mattsharon)
    
    [February 2024](https://community.osarch.org/discussion/comment/19344/#Comment_19344) edited February 2024
    
    I completely understand your frustration! Losing precious detail from high-precision scans due to limitations in BIM software is definitely painful. Here are some thoughts and potential approaches.
    
    **Understanding the Challenge:**
    
    **IFC limitations** While IFC supports meshes, large and complex ones can indeed cause issues. Some software might have better handling than others, so investigating alternatives could be worthwhile.  
    **Software optimization** Check if your BIM software offers any settings or plugins specifically designed for handling large meshes efficiently. Sometimes tweaking mesh decimation algorithms or using lower-precision representations for less critical details can help.  
    **Data reduction strategies** Explore options like simplifying specific areas while preserving high detail in crucial parts. Consider using LOD (Level of Detail) techniques to manage complexity depending on the viewing distance and purpose of the model.
    
*   [![Image 139: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious "Gorgious")[Gorgious](https://community.osarch.org/profile/Gorgious)
    
    [February 2024](https://community.osarch.org/discussion/comment/19348/#Comment_19348)
    
    This looks like something spat out of chatGPT, did you mean to add something specific to the conversation ? :)
    

«[1](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc)[2](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc/p2)[»](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc/p2)

[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc%3F) or [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc%3F) to comment.

#### Howdy, Stranger!

It looks like you're new here. If you want to get involved, click one of these buttons!

[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc) [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc)

Quick Links
-----------

*   [Categories](https://community.osarch.org/categories)
*   [Recent Discussions](https://community.osarch.org/discussions)
*   [Activity](https://community.osarch.org/activity)
*   [All Tags](https://community.osarch.org/vanilla/alltags)
*   [Best Of...](https://community.osarch.org/best)

#### Categories

*   [2.5K All Categories](https://community.osarch.org/categories)
*   [2.3K General](https://community.osarch.org/categories/general)
*   [95 Español / Spanish](https://community.osarch.org/categories/espa%C3%B1ol-spanish)

#### In this Discussion

*   [February 2024 Gorgious](https://community.osarch.org/profile/Gorgious)
*   [February 2024 mattsharon](https://community.osarch.org/profile/mattsharon)
*   [October 2022 paireks](https://community.osarch.org/profile/paireks)
*   [October 2022 Hagaeus](https://community.osarch.org/profile/Hagaeus)
*   [October 2022 duncan](https://community.osarch.org/profile/duncan)
*   [October 2022 Moult](https://community.osarch.org/profile/Moult)
*   [October 2022 Bimlooser](https://community.osarch.org/profile/Bimlooser)
*   [October 2022 aothms](https://community.osarch.org/profile/aothms)
*   [October 2022 tobenz](https://community.osarch.org/profile/tobenz)
*   [October 2022 RaphaëlVouilloz](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz)
*   [October 2022 berlotti](https://community.osarch.org/profile/berlotti)
*   [October 2022 Ace](https://community.osarch.org/profile/Ace)
*   [October 2022 theoryshaw](https://community.osarch.org/profile/theoryshaw)

Except where otherwise noted, content on this site added after June 2021 is licensed under a [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/) .

## Metadata

```json
{
  "title": "Scan to BIM, for real - with IFC?",
  "description": "I do scanning of heritage buildings and it is painful to see how a millimetre precision scan gets modeled with decimeter errors into a flat, right angled, perfectly plumb and even thickness wall in BIM software.",
  "url": "https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc",
  "content": "Scan to BIM, for real - with IFC? — OSArch\n=============== \n\ntoggle menu\n\n [![Image 71: OSArch](https://community.osarch.org/uploads/de6adc1b2433bca292f0fdec02c9da1e.png)](https://community.osarch.org/)[![Image 72: OSArch](https://community.osarch.org/uploads/a8113bffcd015452fcb76db9f6a332bb.png)](https://community.osarch.org/)\n\n[Categories](https://community.osarch.org/categories)\n\n[Discussions](https://community.osarch.org/discussions)\n\n[Wiki](https://wiki.osarch.org/)\n\n[Live Chat](https://osarch.org/chat)\n\n[Back to OSArch.org](https://osarch.org/)\n\n[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc) · [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc)\n\n[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc) · [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc)\n\n[Categories](https://community.osarch.org/categories)\n\n[Discussions](https://community.osarch.org/discussions)\n\n[Activity](https://community.osarch.org/activity)\n\n[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc) · [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc)\n\n×\n\n[Home](https://community.osarch.org/) › [General](https://community.osarch.org/categories/general)\n\nScan to BIM, for real - with IFC?\n=================================\n\n[![Image 73: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")[Hagaeus](https://community.osarch.org/profile/Hagaeus)\n\n[October 2022](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc) edited October 2022 in [General](https://community.osarch.org/categories/general)\n\nI do scanning of heritage buildings and it is painful to see how a millimetre precision scan gets modeled with decimeter errors into a flat, right angled, perfectly plumb and even thickness wall in BIM software. That is not how they look.\n\nI have tried to cut up a mesh and assign IFC classes to the parts, but it really struggles with big meshes. In vanilla Blender I can handle 100 million polys with acceptable lag, but converting to IFC crashes already at 10 million.  \nI can simplify them a lot of course but then I also loose detail.\n\nHow to approach this? Is the IFC inherently bad at mesh, or is there a way to fix that? Should I detach the mesh from the IFC in some way instead? Other suggestions?\n\n![Image 74](https://community.osarch.org/uploads/editor/sj/ukbfrc5h1s91.jpg)\n\n[![Image 75: carlopav](https://community.osarch.org/uploads/userpics/381/nRXYZUZ2ZBIM4.jpg)](https://community.osarch.org/profile/carlopav \"carlopav\")[![Image 76: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace \"Ace\")[![Image 77: RaphaëlVouilloz](https://community.osarch.org/uploads/userpics/673/n8RKIQD0RTEYI.jpg)](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz \"RaphaëlVouilloz\")[![Image 78: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious \"Gorgious\")[![Image 79: CadGiru](https://community.osarch.org/uploads/userpics/771/n9EA1SGIY3DD7.JPG)](https://community.osarch.org/profile/CadGiru \"CadGiru\")[![Image 80: PavlosDem9](https://secure.gravatar.com/avatar/d9861123fcbf2053d09b017023b72dec/?default=https%3A%2F%2Fvanillicon.com%2F39de0a7c0668b7658cd5215a87e16f55_200.png&rating=g&size=200)](https://community.osarch.org/profile/PavlosDem9 \"PavlosDem9\")\n\n«[1](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc)[2](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc/p2)[»](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc/p2)\n\nComments\n--------\n\n*   [![Image 81: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace \"Ace\")[Ace](https://community.osarch.org/profile/Ace)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12843/#Comment_12843)\n    \n    Could I ask what you process is for the scan to mesh?  \n    A point cloud from a laser scan, then you import as an obj into Blender? and then begin converting to Ifc?  \n    Would it not be possible to use IfcOpenShell directly to make an IFC without first going into Blender?  \n    I haven't used IfcOpenShell myself but taking out the Obj process might speed things up\n    \n*   [![Image 82: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious \"Gorgious\")[Gorgious](https://community.osarch.org/profile/Gorgious)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12844/#Comment_12844)\n    \n    From my experience IFC and more broadly, AEC programs are not tailored for defining existing building with precision. AFAIK in REVIT, Archicad and Blender's Archipack addon you can't define a regular wall with varying width. I think your desired workflow here if you want to preserve data integrity is not to define the geometry inside the IFC file but to use a link to a model you'll share alongside with it, and open with a dedicated 3D modeling program, not a CAD authoring tool. Until we get quantum computers I don't think architects and engineers will accept to work with millions of polygons for a simple beam. :)\n    \n    I've been scratching my head at this problem for a while, too so I'd really like any workflow improvement exploration :)\n    \n*   [![Image 83: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult \"Moult\")[Moult](https://community.osarch.org/profile/Moult)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12845/#Comment_12845)\n    \n    In theory what you're doing could work, but in practice there are some problems:\n    \n    1.  The IFC STEP serialisation (.ifc file) is ASCII and very, very inefficient at storing high poly objects. Expect very large filesizes and slow reading. There is a way to bypass this by using HDF5 serialisation which has experimental support in IfcOpenShell, which was used for point clouds in IFC [https://github.com/IfcOpenShell/IfcOpenShell/issues/760](https://github.com/IfcOpenShell/IfcOpenShell/issues/760) - but it is highly experimental.\n    2.  IfcOpenShell uses OpenCASCADE out of the box to process tessellations, which means that its converting your mesh into a geometrically perfect BRep (and thus very, very inefficient), so expect load times to be so slow it's basically impractical. Note there is a way to bypass this and use \"Native Meshes\" in advanced mode when loading, but that's for things like 20-40k polys, definitely not 10 million. And of course that's assuming you solve problem 1 first.\n    \n    In my opinion, this is not IFC's problem to solve. IFC should focus on what it does best - semantics for the AEC industry... where semantics overlap with geometry, IFC may get involved (e.g. parametric I-beams, profile cardinality, parametric layered materials and extrusions), but high poly meshes is definitely _not_ semantic and sounds very much like the domain of the CG / scanning world. I would propose merely recording simple forms (perhaps highly decimated) and then referencing an external file for the high-res mesh.\n    \n    However, these \"low res proxies linking to high res external sources\" is merely my own theory, and is not officially part of the schema (though maybe in the future it may be?). It's what I did for things like Radiance support which had similar issues, and for things like CG viz and grass blade instances. If you go this route, use an external library reference relationship.\n    \n    For my Radiance examples, I stored the meshes as OBJ, but since it's an unofficial convention, do what you want ;)\n    \n    [![Image 84: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious \"Gorgious\")[![Image 85: Martin156131](https://community.osarch.org/uploads/userpics/398/nJUZMRIKZD54F.png)](https://community.osarch.org/profile/Martin156131 \"Martin156131\")[![Image 86: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")[![Image 87: cvillagrasa](https://community.osarch.org/uploads/userpics/137/nXVSWS33CR6PC.jpg)](https://community.osarch.org/profile/cvillagrasa \"cvillagrasa\")[![Image 88: fusionBIM](https://secure.gravatar.com/avatar/0671699a79c4971923c31577b62d18ec/?default=https%3A%2F%2Fvanillicon.com%2Fd7147ad1c37004dde05245a3b621b0c6_200.png&rating=g&size=200)](https://community.osarch.org/profile/fusionBIM \"fusionBIM\")\n    \n*   [![Image 89: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")[Hagaeus](https://community.osarch.org/profile/Hagaeus)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12867/#Comment_12867) edited October 2022\n    \n    First my process: I combine laser scans and photogrammetry in RealityCapture to produce a textured mesh. I then import it to Blender to cut it up. I usually just separate the rooms to give the customer the possibility to open one room at a time. That way they don't need a beefy computer and it's easier to look at that room with backface culling and nothing else in the way.  \n    For me pointclouds are just a step in the process and not useful for anything but some calculations. They are horrible to navigate as they have no real surface, update as you go, and no backface culling.\n    \n    My goal is to segment all the parts. Walls, floors. beams etc. and also be able to add information like salt problems in masonry, sensor readings, rot and so on as separate geometry. As well as all the usual maintanance intervall and so on.\n    \n    I thought .ifc was more agnostic to geometry and able to handle meshes without transforming them to Brep. And I am unfortunately not the guy to write code to get it to work with workarounds. What I may be able to do is get funding so one of you guys can do it, if you think it's worth. I can imagine also architects could enjoy not being limited to Brep.\n    \n    [![Image 90: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace \"Ace\")[![Image 91: cvillagrasa](https://community.osarch.org/uploads/userpics/137/nXVSWS33CR6PC.jpg)](https://community.osarch.org/profile/cvillagrasa \"cvillagrasa\")[![Image 92: fusionBIM](https://secure.gravatar.com/avatar/0671699a79c4971923c31577b62d18ec/?default=https%3A%2F%2Fvanillicon.com%2Fd7147ad1c37004dde05245a3b621b0c6_200.png&rating=g&size=200)](https://community.osarch.org/profile/fusionBIM \"fusionBIM\")\n    \n*   [![Image 93: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")[Hagaeus](https://community.osarch.org/profile/Hagaeus)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12888/#Comment_12888)\n    \n    Just saw the interview with Thomas Krijnen on BIMvoice and he mentioned he had actually worked on integrating mesh, and was almost there. Is he on here under some pseodonym?\n    \n    [![Image 94: condur](https://community.osarch.org/uploads/userpics/385/nBG6153YR211L.jpg)](https://community.osarch.org/profile/condur \"condur\")\n    \n*   [![Image 95: theoryshaw](https://community.osarch.org/uploads/userpics/399/n1LFZQA87XEVG.png)](https://community.osarch.org/profile/theoryshaw \"theoryshaw\")[theoryshaw](https://community.osarch.org/profile/theoryshaw)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12889/#Comment_12889)\n    \n    [@aothms](https://community.osarch.org/profile/aothms) , sorry Thomas. ;) Great interview, btw. :)\n    \n    [![Image 96: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")[![Image 97: CadGiru](https://community.osarch.org/uploads/userpics/771/n9EA1SGIY3DD7.JPG)](https://community.osarch.org/profile/CadGiru \"CadGiru\")\n    \n*   [![Image 98: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace \"Ace\")[Ace](https://community.osarch.org/profile/Ace)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12890/#Comment_12890)\n    \n    I think that's [@aothms](https://community.osarch.org/profile/aothms) ?\n    \n    [![Image 99: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")\n    \n*   [![Image 100: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult \"Moult\")[Moult](https://community.osarch.org/profile/Moult)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12904/#Comment_12904)\n    \n    > I thought .ifc was more agnostic to geometry and able to handle meshes\n    \n    It is, it can handle tessellations, yet still runs into the two issues I described above. I guess one option is to try and overcome the two issues via HDF5 and a dedicated mesh parser, and the second option is to only use IFC for semantics and develop a convention for referencing externally defined high-res meshes (e.g. via OBJ, glB, or other open data standard) which can be proposed to buildingSMART for IFC5 (but backwards compatible).\n    \n    The latter sounds easier to me :)\n    \n    [![Image 101: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace \"Ace\")\n    \n*   [![Image 102: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms \"aothms\")[aothms](https://community.osarch.org/profile/aothms)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12919/#Comment_12919)\n    \n    Hey guys, immensely interesting subject. The IFC-HDF5 work we did was also for cultural heritage documentation. We opted for the approach of a regular bim model and then storing the point cloud segments as offsets to those surfaces. We focussed only on the semantic storage and retrieval efficiency. We just assumed a handmodelled IFC model exist that corresponds to the point cloud. What was nice about this was that the compression we got from storing the points as offsets also made the combination of these two so semantically interesting.\n    \n    Yes, in the talk with Petru from Bimvoice I indeed mentioned the work I have been doing for a couple of years already on being able to select alternative geometry libraries. That would indeed eliminate the BRep reconstruction as highlighted by [@Moult](https://community.osarch.org/profile/Moult). HDF5 could indeed eliminate the difficulties with storing large arrays as textual formats. But even if both were production ready it's still not really realistic to efficiently perform realtime modifications on them. Isolating mesh or point cloud segments into new representations for elements still means move ridiculous amounts of data around that neither HDF5 nor IFC schema is intended for.\n    \n    Most efficient would be to store the mesh as a monolithic array and rather use something like vertex groups or a separate channel of data to store the association to building element ids. So that you edit by changing _values_ and not _structure_. And then indeed a way to reference that from IFC or periodically bake this into an IFC file. In HDF5 something like this would be possible by using _Region references_ so that entity instance attribute values would actually be subsets of this monolithic array. Blender and HDF5 both have good interfaces with numpy, so there might be something possible.\n    \n    [![Image 103: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace \"Ace\")[![Image 104: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious \"Gorgious\")[![Image 105: carlopav](https://community.osarch.org/uploads/userpics/381/nRXYZUZ2ZBIM4.jpg)](https://community.osarch.org/profile/carlopav \"carlopav\")[![Image 106: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")[![Image 107: cvillagrasa](https://community.osarch.org/uploads/userpics/137/nXVSWS33CR6PC.jpg)](https://community.osarch.org/profile/cvillagrasa \"cvillagrasa\")[![Image 108: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult \"Moult\")\n    \n*   [![Image 109: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")[Hagaeus](https://community.osarch.org/profile/Hagaeus)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12926/#Comment_12926)\n    \n    So if we use vertex groups for example and link that to the IFC schema, Would that be readable (in a longer perspective) in other software, or never leave BlenderBIM? And what happens if you make a door in this vertexgroup?\n    \n    For me to be able to get funding it needs to work outside BlenderBIM. Perhaps not immediately, but eventually, and have a chance of becoming a standard.\n    \n    How much time and money (very, very roughly) are we talking about?\n    \n*   [![Image 110: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult \"Moult\")[Moult](https://community.osarch.org/profile/Moult)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12929/#Comment_12929)\n    \n    To make this work in other software, it would need to be a project supported by buildingSMART. It would definitely not be immediate. Maybe [@berlotti](https://community.osarch.org/profile/berlotti) might know if it's of interest?\n    \n*   [![Image 111: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms \"aothms\")[aothms](https://community.osarch.org/profile/aothms)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12930/#Comment_12930)\n    \n    Ok, also note that I was talking solely about efficiency. My approach collides with BlenderBIM's native IFC editing because of the non-standard way of relating mesh segments to elements. And also it might not be what you want from a usability perspective, because when you hide all this information in mesh channels there's a lot of Blender navigation functionality that doesn't work anymore (e.g conveniently hiding objects by type or sth).\n    \n    It was just a thought I had that even if you do HDF5, moving around large mesh subsets from one instance to the other is going to be painful because HDF5 statically arranges the datasets and doesn't \"vacuum\" empty space. Hence my thoughts on creating region references into a monolithic array and trying to see if there is an equivalent for that in Blender. So again, solely thinking from performance, I was hoping for some refinement on this idea in the thread maybe with ideas thinking more from the viewpoint of UX.\n    \n    To me this sounds more like a EU-funded project or sth. Heritage and digitalization are always topics on the agenda. The RWTH design computation group has done some could heritage and ifc related things and they know blenderbim and I know Duncan has brought up EU-funded projects earlier. This might be the thing.\n    \n    [![Image 112: theoryshaw](https://community.osarch.org/uploads/userpics/399/n1LFZQA87XEVG.png)](https://community.osarch.org/profile/theoryshaw \"theoryshaw\")[![Image 113: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace \"Ace\")\n    \n*   [![Image 114: berlotti](https://community.osarch.org/uploads/userpics/304/n8A1A9L2VAXWY.jpeg)](https://community.osarch.org/profile/berlotti \"berlotti\")[berlotti](https://community.osarch.org/profile/berlotti)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12956/#Comment_12956)\n    \n    There would definitely be interest. Biggest challenge will probably be to define a clear objective, scope, intended outcome, etc. Happy to help!\n    \n    [![Image 115: theoryshaw](https://community.osarch.org/uploads/userpics/399/n1LFZQA87XEVG.png)](https://community.osarch.org/profile/theoryshaw \"theoryshaw\")[![Image 116: Ace](https://community.osarch.org/uploads/userpics/799/nX85JOI81KLYF.jpg)](https://community.osarch.org/profile/Ace \"Ace\")\n    \n*   [![Image 117: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult \"Moult\")[Moult](https://community.osarch.org/profile/Moult)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12960/#Comment_12960) edited October 2022\n    \n    Just speculating here, what if a \"perfect\" geometry was stored (i.e. the typical parametric extruded beam prism) but alongside it was referenced raw textures which represented offset from the base surface of the perfect geometry. No need to load 2 billion points, can in theory scale very, very easily (just zoom into interested area, inspect texture as displacement map where necessary. Algorithms that were mixed between human intervention and AABB/OBB generation could be used to rapidly create this proxy perfect surface.\n    \n    We could probably cook up a prototype in Blender within a week or so, reusing Blender's XYZ map baking abilities.\n    \n*   [![Image 118: RaphaëlVouilloz](https://community.osarch.org/uploads/userpics/673/n8RKIQD0RTEYI.jpg)](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz \"RaphaëlVouilloz\")[RaphaëlVouilloz](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12962/#Comment_12962)\n    \n    At CNPA EPFL we are also really interested in this topic for HBIM ; we could do some tests if you develop prototypes.  \n    I would point that :  \n    \\-To produce high quality photomesh models becomes more and more easy and accessible.  \n    \\-As Blender is perfect to work on the mesh, it would be a great process to classify the photomesh in IFC with BlenderBIM.  \n    \\-It also becomes easy to share such a work with three.js and IFC.js\n    \n    I am also interested to see how we could classify a Pointcloud in IFC.\n    \n*   [![Image 119: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms \"aothms\")[aothms](https://community.osarch.org/profile/aothms)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12964/#Comment_12964)\n    \n    In our work we proposed three methods:\n    \n    ![Image 120](https://community.osarch.org/uploads/editor/p7/p08pfuhc7vhy.png)\n    \n    [https://pure.tue.nl/ws/files/119667686/20190402\\_Krijnen.pdf](https://pure.tue.nl/ws/files/119667686/20190402_Krijnen.pdf)\n    \n    What [@Moult](https://community.osarch.org/profile/Moult) describes is basically the third level. Maybe indeed using textures is a nice middle ground between semantics and ease of use in Blender. You'd obviously need to use some psets or sth to map the \\[0,255\\] range onto the physical range of deviations. But essentially this is exactly what we did, we also quantized the point cloud deviations for compression. In the end we just had a little semantic structure to store the deviations, but you could easily opt for storing them as textures.\n    \n    You'd run in to the limitations of IFC and textures though, especially for extrusions there is very little control over the UV coords, so you'd likely end up with extremely non-uniform texture resolution. So maybe you'd make different choices there, e.g probably not to use extrusions. Or use the schema extension when writing IFC and keep the textures solely as a way to represent them in Blender.\n    \n    What we were also interested in is seeing the progression of deviation over time, e.g structural health monitoring. So I think that would also be something to account for that you might have multiple scans associated to the same model. Analyse the deviations as a 2d function and then compute the differences in parameters for these function to assess the rate of change.\n    \n    > To produce high quality photomesh models becomes more and more easy and accessible.\n    \n    Are you suggesting not to use point clouds, but rather photogrammetry? Or what is a photomesh precisely?\n    \n    [![Image 121: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")\n    \n*   [![Image 122: RaphaëlVouilloz](https://community.osarch.org/uploads/userpics/673/n8RKIQD0RTEYI.jpg)](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz \"RaphaëlVouilloz\")[RaphaëlVouilloz](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12965/#Comment_12965) edited October 2022\n    \n    Really interesting aothms, thanks.  \n    A photomesh is built on pointclouds, it triangles the points to create surfaces and if you have done your capture through photogrammetry, you can texture these surfaces.  \n    You can have really precise pointclouds through lasergammetry (3d scans), you can then convert it in meshes but not texturize it. Although some scanners as Faro do take also photos to allow you to do it. Or you can mix both techniques with a laser and your own camera, as we did on the first project here : [https://enac-cnpa.github.io/IFCjs-Stereotomie/](https://enac-cnpa.github.io/IFCjs-Stereotomie/)  \n    The fact is softwares like Revit and Archicad let you work really easily on pointclouds, but are really not good at importing huge photomesh to model on it. Blender is, and so BlenderBIM would be really a unique tool, if we beginn to scan to bim from photomesh and not anymore from pointclouds. On photomesh you have more comprehensive infos, think for example to a fresco or joints on a stone assembly.  \n    I say photomesh become accessible because of tools as Scaniverse. An architect now just needs an Ipad, whitout understanding anything of all these process, to create a photomesh and start to work on in Blender.\n    \n    [![Image 123: PavlosDem9](https://secure.gravatar.com/avatar/d9861123fcbf2053d09b017023b72dec/?default=https%3A%2F%2Fvanillicon.com%2F39de0a7c0668b7658cd5215a87e16f55_200.png&rating=g&size=200)](https://community.osarch.org/profile/PavlosDem9 \"PavlosDem9\")\n    \n*   [![Image 124: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms \"aothms\")[aothms](https://community.osarch.org/profile/aothms)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12967/#Comment_12967)\n    \n    Thanks for explaining, it's been a while since I worked on this. We indeed had these Faro scanners that give an additional colour channel by internally pairing the point cloud with regular photographs. On the one hand, indeed a mesh is much easier to consume visually, on the other hand, it's also quite a destructive process (not sure how much smoothing is involved) but I guess quite a few points are discarded in order to get a reasonable manifold surface. I don't think Blender is even able to actually display the colour channel on points though so there are definitely quite a few arguments to use mesh. I guess it depends on personal preference, required accuracy, documentation requirements and completeness of scan vs amount of geometric detail.\n    \n    Circling back to the original questions:\n    \n    > For me to be able to get funding it needs to work outside BlenderBIM\n    \n    What are we exploring here: multi-year funded project or trying to make some quick progress on the great foss tools that are currently already available. Or both? Maybe we should setup a quick online get together to quickly outline everybody's interests in this topic?\n    \n*   [![Image 125: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult \"Moult\")[Moult](https://community.osarch.org/profile/Moult)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12968/#Comment_12968)\n    \n    > to map the \\[0,255\\] range\n    \n    EXR :)\n    \n*   [![Image 126: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms \"aothms\")[aothms](https://community.osarch.org/profile/aothms)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12969/#Comment_12969)\n    \n    Yes, I actually thought of that, but do you get reasonable colour values when you look at that in the 3d view? That would be even cooler though, maybe there is a live colour map you can slap onto it.\n    \n*   [![Image 127: tobenz](https://secure.gravatar.com/avatar/30f5473760f285c39fc2a2b9817d812a/?default=https%3A%2F%2Fvanillicon.com%2F5c8ff3934561922ee76c36279eef0caa_200.png&rating=g&size=200)](https://community.osarch.org/profile/tobenz \"tobenz\")[tobenz](https://community.osarch.org/profile/tobenz)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12977/#Comment_12977)\n    \n    I'm not really sure if point cloud data should make it into an IFC model at all. 3D scans are made several times during construction and operation of a building. What is the geometry of an object then?  \n    I would find it much more helpful if all those scans would be geo referenced and I could grab the relevant portion of the point cloud using my element bounding box. The goal should be clean and efficient geometry to not bloat the ifc file size. Abstraction is king.\n    \n    [![Image 128: carlopav](https://community.osarch.org/uploads/userpics/381/nRXYZUZ2ZBIM4.jpg)](https://community.osarch.org/profile/carlopav \"carlopav\")\n    \n*   [![Image 129: aothms](https://community.osarch.org/uploads/userpics/727/nD93CA00SCD13.png)](https://community.osarch.org/profile/aothms \"aothms\")[aothms](https://community.osarch.org/profile/aothms)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12978/#Comment_12978)\n    \n    [@tobenz](https://community.osarch.org/profile/tobenz) this depends on the use case though. First of all, what I was saying with HDF5 isn't too far off of what you say, one big dataset with point clouds, and instead of doing a lookup by bounding box, you directly associate point cloud segments to the elements (as the primary representation or supplementary with a timestamp).\n    \n    More generally (you see this also with IfcTunnel now for example and geotechnical datasets) there is the need to make meaningful semantic connections for documentation purposes, so then you either need to:\n    \n    1.  internalize the dataset in IFC and use relationships,\n    2.  use a container format like ICDD to keep both files separate and include a third file that makes links between subsets) or\n    3.  somehow use external references from one dataset into the other.\n    \n    The pros and cons of these are fairly obvious, but how you weigh them depends on the use case.\n    \n*   [![Image 130: Bimlooser](https://secure.gravatar.com/avatar/07d3eb90596bac5de9bf8047142ccb99/?default=https%3A%2F%2Fvanillicon.com%2F1c993d5d8ad44364df420074422fc059_200.png&rating=g&size=200)](https://community.osarch.org/profile/Bimlooser \"Bimlooser\")[Bimlooser](https://community.osarch.org/profile/Bimlooser)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12980/#Comment_12980)\n    \n    Maybe this guy [https://github.com/florentPoux](https://github.com/florentPoux) can be useful\n    \n*   [![Image 131: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")[Hagaeus](https://community.osarch.org/profile/Hagaeus)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12984/#Comment_12984)\n    \n    Gigantic meshes are a problem of course. Can be solved with LOD (Level of Detail, as in game engine, not the architectural version). I usually make a web version of the mesh with low polycount and Normal maps, and one high poly version for measures, 3d-print and calculations. Clipping box is useful of course as even a low poly royal palace has millions of triangles. We can also hope for Unreal engines Nanite goes open-source and implemented in all 3d sofware (yeah, right).\n    \n    I am doing a prestudy right now for the National Heritage Board about the implementation of the EU recommendations from 2011, updated 2021, stating that:  \n    \"The digital strategy should set clear digitisation and digital preservation goals. Those goals should be based on objective and clear criteria, including:  \n    (a) cultural heritage at risk,  \n    (b) the most physically visited cultural and heritage monuments, buildings and sites and  \n    (c) the low level of digitisation for specific categories of cultural heritage assets.  \n    By 2030, Member States should digitise in 3D all monuments and sites falling under (a) and 50% of those falling under (b).  \n    By 2025, Member States should digitise 40% of the overall 2030 targets.  \n    Member States should take the necessary measures to ensure that all digitised cultural assets referred to in point 6 (a), (b) and (c) are also digitally preserved.\"  \n    This will hopefully lead to a lot of heritage being scanned. It would be a pity if those scans just rotted away on a harddrive somewhere and only were used in case of destruction of the monument. They should be used for visualisations for the public and also BIM models for the administration. But seeing all these wonderful buildings as Revit cardboard boxes will break my heart.\n    \n    So there is potential for big money, but I can only affect little Sweden and would need help from you others. If we can set a goal, a way there, an estimated budget and timeschedule, it will be a lot easier to get funding. Do you think it is possible in a few years perspective?\n    \n*   [![Image 132: Moult](https://community.osarch.org/uploads/userpics/423/nNVZKBY01IS1C.png)](https://community.osarch.org/profile/Moult \"Moult\")[Moult](https://community.osarch.org/profile/Moult)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12985/#Comment_12985)\n    \n    I am also aware of an Australian NSW initiative to scan every single heritage sandstone building here (though I heard they had funding heavily cut) but perhaps I can help reach out to some Australian contacts here and make a connection if you'd like to take the lead?\n    \n*   [![Image 133: duncan](https://community.osarch.org/uploads/userpics/126/n73IZIYE779NH.png)](https://community.osarch.org/profile/duncan \"duncan\")[duncan](https://community.osarch.org/profile/duncan)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12990/#Comment_12990)\n    \n    [@Hagaeus](https://community.osarch.org/profile/Hagaeus) here in Denmark we have Molio which might be well suited to taking the lead on an initiative like this. Is there anything similar in Sweden?\n    \n*   [![Image 134: Hagaeus](https://community.osarch.org/uploads/userpics/518/nY0QO5O2NPIJ8.jpg)](https://community.osarch.org/profile/Hagaeus \"Hagaeus\")[Hagaeus](https://community.osarch.org/profile/Hagaeus)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12993/#Comment_12993)\n    \n    [@duncan](https://community.osarch.org/profile/duncan) I think that would be the equivalent of Boverket. I actually talked to a guy there this week who was interested in a co-operation regarding other stuff. That is a great idea as they are under the finance department and therefore have money, unlike the Heritage board that is under the Culture department.\n    \n    [@Moult](https://community.osarch.org/profile/Moult) I could do that next year if I get some support from others. I am a one man company with the workload for two, plus admin, right now. Getting support from Australia would show that it is of international interest as well. I guess you are the one for lobbying towards BuildingSmart? Or does anyone else have good connections there?\n    \n*   [![Image 135: paireks](https://community.osarch.org/uploads/userpics/745/nQIDJTUDZ7T10.png)](https://community.osarch.org/profile/paireks \"paireks\")[paireks](https://community.osarch.org/profile/paireks)\n    \n    [October 2022](https://community.osarch.org/discussion/comment/12994/#Comment_12994)\n    \n    Hey [@Hagaeus](https://community.osarch.org/profile/Hagaeus)  \n    it would be interesting if you could try out using .bim file format for that ([https://dotbim.net/](https://dotbim.net/)), and let me know the results.  \n    For tests I created a mesh with 12 500 000 triangles in Grasshopper. I attached some custom data to it and exported it as .bim. It took as you can see below 52 seconds to save that file, and it is 1.13 GB big. After simple ZIP it reduced the size to 140 MB. There is still room for improvement there (removing white spaces, removing unnecessary decimal numbers, quality of mesh).  \n    ![Image 136](https://community.osarch.org/uploads/editor/l3/8tbbaihj7mc5.png)  \n    Then I imported it to Blender and it works fine:  \n    ![Image 137](https://community.osarch.org/uploads/editor/cx/wudp1dvwow7b.png)\n    \n    Regarding having a giant meshes in a model and LOD, one of the ideas was to actually store different LODs in separate models and link them together, rather than having it all in one giantic model / file. Not sure if such concept would be interesting for scans, but you can also check it out there and let me know what you think: [https://github.com/paireks/dotbim/blob/master/LinkingData.md](https://github.com/paireks/dotbim/blob/master/LinkingData.md)\n    \n*   [![Image 138: mattsharon](https://community.osarch.org/uploads/userpics/306/nH8GYDBXGHUJ2.jpg)](https://community.osarch.org/profile/mattsharon \"mattsharon\")[mattsharon](https://community.osarch.org/profile/mattsharon)\n    \n    [February 2024](https://community.osarch.org/discussion/comment/19344/#Comment_19344) edited February 2024\n    \n    I completely understand your frustration! Losing precious detail from high-precision scans due to limitations in BIM software is definitely painful. Here are some thoughts and potential approaches.\n    \n    **Understanding the Challenge:**\n    \n    **IFC limitations** While IFC supports meshes, large and complex ones can indeed cause issues. Some software might have better handling than others, so investigating alternatives could be worthwhile.  \n    **Software optimization** Check if your BIM software offers any settings or plugins specifically designed for handling large meshes efficiently. Sometimes tweaking mesh decimation algorithms or using lower-precision representations for less critical details can help.  \n    **Data reduction strategies** Explore options like simplifying specific areas while preserving high detail in crucial parts. Consider using LOD (Level of Detail) techniques to manage complexity depending on the viewing distance and purpose of the model.\n    \n*   [![Image 139: Gorgious](https://community.osarch.org/uploads/userpics/961/nLQUS81VILV2M.jpg)](https://community.osarch.org/profile/Gorgious \"Gorgious\")[Gorgious](https://community.osarch.org/profile/Gorgious)\n    \n    [February 2024](https://community.osarch.org/discussion/comment/19348/#Comment_19348)\n    \n    This looks like something spat out of chatGPT, did you mean to add something specific to the conversation ? :)\n    \n\n«[1](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc)[2](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc/p2)[»](https://community.osarch.org/discussion/1163/scan-to-bim-for-real-with-ifc/p2)\n\n[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc%3F) or [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc%3F) to comment.\n\n#### Howdy, Stranger!\n\nIt looks like you're new here. If you want to get involved, click one of these buttons!\n\n[Sign In](https://community.osarch.org/entry/signin?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc) [Register](https://community.osarch.org/entry/register?Target=discussion%2F1163%2Fscan-to-bim-for-real-with-ifc)\n\nQuick Links\n-----------\n\n*   [Categories](https://community.osarch.org/categories)\n*   [Recent Discussions](https://community.osarch.org/discussions)\n*   [Activity](https://community.osarch.org/activity)\n*   [All Tags](https://community.osarch.org/vanilla/alltags)\n*   [Best Of...](https://community.osarch.org/best)\n\n#### Categories\n\n*   [2.5K All Categories](https://community.osarch.org/categories)\n*   [2.3K General](https://community.osarch.org/categories/general)\n*   [95 Español / Spanish](https://community.osarch.org/categories/espa%C3%B1ol-spanish)\n\n#### In this Discussion\n\n*   [February 2024 Gorgious](https://community.osarch.org/profile/Gorgious)\n*   [February 2024 mattsharon](https://community.osarch.org/profile/mattsharon)\n*   [October 2022 paireks](https://community.osarch.org/profile/paireks)\n*   [October 2022 Hagaeus](https://community.osarch.org/profile/Hagaeus)\n*   [October 2022 duncan](https://community.osarch.org/profile/duncan)\n*   [October 2022 Moult](https://community.osarch.org/profile/Moult)\n*   [October 2022 Bimlooser](https://community.osarch.org/profile/Bimlooser)\n*   [October 2022 aothms](https://community.osarch.org/profile/aothms)\n*   [October 2022 tobenz](https://community.osarch.org/profile/tobenz)\n*   [October 2022 RaphaëlVouilloz](https://community.osarch.org/profile/Rapha%C3%ABlVouilloz)\n*   [October 2022 berlotti](https://community.osarch.org/profile/berlotti)\n*   [October 2022 Ace](https://community.osarch.org/profile/Ace)\n*   [October 2022 theoryshaw](https://community.osarch.org/profile/theoryshaw)\n\nExcept where otherwise noted, content on this site added after June 2021 is licensed under a [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/) .",
  "usage": {
    "tokens": 11274
  }
}
```
