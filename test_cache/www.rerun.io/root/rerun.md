---
title: Rerun
description: Multimodal log handling and visualization for spatial and embodied AI. Managed infrastructure to ingest, store, analyze, and stream data at scale with built-in visual debugging. Fast, flexible, and easy to use.
url: https://www.rerun.io/
timestamp: 2025-01-20T15:46:09.321Z
domain: www.rerun.io
path: root
---

# Rerun


Multimodal log handling and visualization for spatial and embodied AI. Managed infrastructure to ingest, store, analyze, and stream data at scale with built-in visual debugging. Fast, flexible, and easy to use.


## Content

The multimodal data stack
-------------------------

Open source log handling and visualization for spatial and embodied AI. Managed infrastructure to ingest, store, analyze, and stream data at scale with built-in visual debugging. Fast, flexible, and easy to use.

[Rerun is open source ![Image 25](blob:https://www.rerun.io/f1f2a9eb0cf2bdc7a47625bb8b2820c4) 6,200](https://github.com/rerun-io/rerun)

![Image 26](https://rerun.io/_app/immutable/assets/hero-illustration.CUteR0Ty.svg)

![Image 27](https://rerun.io/_app/immutable/assets/hero-illustration-mobile.BX62HIjd.svg)

Start visualizing in seconds
----------------------------

Powerful and flexible visualization for spatial and embodied AI that's shockingly easy to get started with. Simple no sign-up installation and minimal code to get up and running.

```
pip install rerun-sdk
rerun
```

Infrastructure to simplify your data engine
-------------------------------------------

![Image 28](https://rerun.io/_app/immutable/assets/icon-infra-run-and-record.ecUFW5Gi.svg)

#### Run & record

Run your systems and record data for analysis and training. Use the Rerun SDK to log data or interpret existing log files.

![Image 29](https://rerun.io/_app/immutable/assets/icon-infra-find-issues.BfY0Tri-.svg)

#### Find issues

Use the Rerun viewer to understand behavior and pinpoint issues. Extract signals from logs for further analysis.

![Image 30](https://rerun.io/_app/immutable/assets/icon-infra-improve-and-debug.ReamtZz3.svg)

#### Improve & deploy

Visualize training and eval, debug prototypes, and extract time aligned training samples from messy logs.

How it works
------------

1

### Model

Use the SDK to model your data and write it to storage or a live viewer. Rerun's data model, a time aware Entity Component System, makes common scenarios simple but is flexible enough to handle custom data.

```
import rerun as rr
rr.init("my_data_generating_application")
rr.connect()  # Connect to a remote viewer
…
rr.log("points", rr.Points3D(positions))
rr.log("camera", rr.Transform3D(pos, rot))
rr.log("camera/image", rr.Pinhole(intrinsics))
rr.log("camera/image", rr.Image(tensor))
rr.log("reprojection_error", rr.Scalar(err))
```

2

### View

Get powerful interactive visualizations of live and recorded data. Time travel through your data, with the industry's fastest multimodal viewer. It's open source and runs both natively and in the browser.

3

### Build

Build layouts and customize visualizations directly through code or interactively in the UI. Build visualization into your tools by embedding the viewer in your Rust, JS, or Gradio apps.

4

### Query

Use Rerun's query APIs to extract time-aligned datasets from messy robotics recordings. Rerun returns Apache Arrow data that plugs in to your favorite dataframe library for further analysis.

```
import rerun as rr
…
# Create an aligned dataframe based on time-points where an Image was logged
aligned_samples = rr.dataframe
    .load_recording("raw.rrd")
    .view(index="sensor_time", contents="/**")
    .filter_is_not_null("/camera/image:ImageBuffer")
    .fill_latest_at()
    .select()

# Write aligned samples to a parquet file for later training
with pq.ParquetWriter("train.parquet", aligned_samples.schema()) as writer:
    for chunk in aligned_samples:
        writer.write_batch(chunk)
```

[Read the documentation](https://rerun.io/docs/getting-started/what-is-rerun)

Open source vs commercial
-------------------------

#### Open source

Visualization and simple log handling

Dual licensed under MIT and Apache 2

[Join on GitHub](https://github.com/rerun-io/rerun)

*   The fastest & easiest to use multimodal visualizer out there
*   Visualizer runs native, on the web and is embeddable in notebooks and web apps
*   An SDK for modeling and handling multimodal logs

#### Commercial

Data management at scale

Under development with select design partners

[Sign up for waitlist](https://5li7zhj98k8.typeform.com/to/sLD8QaHJ)

*   Data platform for embodied AI where all data is instantly visualizable and debuggable
*   Ingestion, storage engine and index management for large scale data
*   Dataset management for both recordings and structured tables

Our blog
--------

## Metadata

```json
{
  "title": "Rerun",
  "description": "Multimodal log handling and visualization for spatial and embodied AI. Managed infrastructure to ingest, store, analyze, and stream data at scale with built-in visual debugging. Fast, flexible, and easy to use.",
  "url": "https://www.rerun.io/",
  "content": "The multimodal data stack\n-------------------------\n\nOpen source log handling and visualization for spatial and embodied AI. Managed infrastructure to ingest, store, analyze, and stream data at scale with built-in visual debugging. Fast, flexible, and easy to use.\n\n[Rerun is open source ![Image 25](blob:https://www.rerun.io/f1f2a9eb0cf2bdc7a47625bb8b2820c4) 6,200](https://github.com/rerun-io/rerun)\n\n![Image 26](https://rerun.io/_app/immutable/assets/hero-illustration.CUteR0Ty.svg)\n\n![Image 27](https://rerun.io/_app/immutable/assets/hero-illustration-mobile.BX62HIjd.svg)\n\nStart visualizing in seconds\n----------------------------\n\nPowerful and flexible visualization for spatial and embodied AI that's shockingly easy to get started with. Simple no sign-up installation and minimal code to get up and running.\n\n```\npip install rerun-sdk\nrerun\n```\n\nInfrastructure to simplify your data engine\n-------------------------------------------\n\n![Image 28](https://rerun.io/_app/immutable/assets/icon-infra-run-and-record.ecUFW5Gi.svg)\n\n#### Run & record\n\nRun your systems and record data for analysis and training. Use the Rerun SDK to log data or interpret existing log files.\n\n![Image 29](https://rerun.io/_app/immutable/assets/icon-infra-find-issues.BfY0Tri-.svg)\n\n#### Find issues\n\nUse the Rerun viewer to understand behavior and pinpoint issues. Extract signals from logs for further analysis.\n\n![Image 30](https://rerun.io/_app/immutable/assets/icon-infra-improve-and-debug.ReamtZz3.svg)\n\n#### Improve & deploy\n\nVisualize training and eval, debug prototypes, and extract time aligned training samples from messy logs.\n\nHow it works\n------------\n\n1\n\n### Model\n\nUse the SDK to model your data and write it to storage or a live viewer. Rerun's data model, a time aware Entity Component System, makes common scenarios simple but is flexible enough to handle custom data.\n\n```\nimport rerun as rr\nrr.init(\"my_data_generating_application\")\nrr.connect()  # Connect to a remote viewer\n…\nrr.log(\"points\", rr.Points3D(positions))\nrr.log(\"camera\", rr.Transform3D(pos, rot))\nrr.log(\"camera/image\", rr.Pinhole(intrinsics))\nrr.log(\"camera/image\", rr.Image(tensor))\nrr.log(\"reprojection_error\", rr.Scalar(err))\n```\n\n2\n\n### View\n\nGet powerful interactive visualizations of live and recorded data. Time travel through your data, with the industry's fastest multimodal viewer. It's open source and runs both natively and in the browser.\n\n3\n\n### Build\n\nBuild layouts and customize visualizations directly through code or interactively in the UI. Build visualization into your tools by embedding the viewer in your Rust, JS, or Gradio apps.\n\n4\n\n### Query\n\nUse Rerun's query APIs to extract time-aligned datasets from messy robotics recordings. Rerun returns Apache Arrow data that plugs in to your favorite dataframe library for further analysis.\n\n```\nimport rerun as rr\n…\n# Create an aligned dataframe based on time-points where an Image was logged\naligned_samples = rr.dataframe\n    .load_recording(\"raw.rrd\")\n    .view(index=\"sensor_time\", contents=\"/**\")\n    .filter_is_not_null(\"/camera/image:ImageBuffer\")\n    .fill_latest_at()\n    .select()\n\n# Write aligned samples to a parquet file for later training\nwith pq.ParquetWriter(\"train.parquet\", aligned_samples.schema()) as writer:\n    for chunk in aligned_samples:\n        writer.write_batch(chunk)\n```\n\n[Read the documentation](https://rerun.io/docs/getting-started/what-is-rerun)\n\nOpen source vs commercial\n-------------------------\n\n#### Open source\n\nVisualization and simple log handling\n\nDual licensed under MIT and Apache 2\n\n[Join on GitHub](https://github.com/rerun-io/rerun)\n\n*   The fastest & easiest to use multimodal visualizer out there\n*   Visualizer runs native, on the web and is embeddable in notebooks and web apps\n*   An SDK for modeling and handling multimodal logs\n\n#### Commercial\n\nData management at scale\n\nUnder development with select design partners\n\n[Sign up for waitlist](https://5li7zhj98k8.typeform.com/to/sLD8QaHJ)\n\n*   Data platform for embodied AI where all data is instantly visualizable and debuggable\n*   Ingestion, storage engine and index management for large scale data\n*   Dataset management for both recordings and structured tables\n\nOur blog\n--------",
  "usage": {
    "tokens": 998
  }
}
```
