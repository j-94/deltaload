---
title: Utils - Adala Docs
description: 
url: https://humansignal.github.io/Adala/utils/
timestamp: 2025-01-20T16:14:55.010Z
domain: humansignal.github.io
path: Adala_utils
---

# Utils - Adala Docs



## Content

Skip to content
Adala Docs
Utils
Initializing search
 humansignal/Adala
Adala Docs
Home
Agents
Environments
Memories
Runtimes
Skills
Utils
Table of contents
internal_data
InternalDataFrameConcat
logs
print_dataframe
print_error
print_series
print_text
matching
fuzzy_match
Utils
InternalDataFrameConcat(dfs, **kwargs)

Concatenate dataframes.

Parameters:

Name	Type	Description	Default
dfs	Iterable[InternalDataFrame]	

The dataframes to concatenate.

	required

Returns:

Name	Type	Description
InternalDataFrame	InternalDataFrame	

The concatenated dataframe.

Source code in adala/utils/internal_data.py
print_dataframe(dataframe)

Print dataframe to console.

Source code in adala/utils/logs.py
print_error(text)

Print error message to console.

Source code in adala/utils/logs.py
print_series(data)

Print series to console.

Source code in adala/utils/logs.py
print_text(text, style=None, streaming_style=False)

Print text to console with optional style and streaming style.

Source code in adala/utils/logs.py
fuzzy_match(x, y, threshold=0.8)

Fuzzy match string values in two series.

Parameters:

Name	Type	Description	Default
x	InternalSeries	

The first series.

	required
y	InternalSeries	

The second series.

	required
threshold	float	

The threshold to use for fuzzy matching. Defaults to 0.8.

	0.8

Returns:

Name	Type	Description
InternalSeries	InternalSeries	

The series with fuzzy match results.

Source code in adala/utils/matching.py
 Back to top
Previous
Skills
Made with Material for MkDocs

## Metadata

```json
{
  "title": "Utils - Adala Docs",
  "description": "",
  "url": "https://humansignal.github.io/Adala/utils/",
  "content": "Skip to content\nAdala Docs\nUtils\nInitializing search\n humansignal/Adala\nAdala Docs\nHome\nAgents\nEnvironments\nMemories\nRuntimes\nSkills\nUtils\nTable of contents\ninternal_data\nInternalDataFrameConcat\nlogs\nprint_dataframe\nprint_error\nprint_series\nprint_text\nmatching\nfuzzy_match\nUtils\nInternalDataFrameConcat(dfs, **kwargs)\n\nConcatenate dataframes.\n\nParameters:\n\nName\tType\tDescription\tDefault\ndfs\tIterable[InternalDataFrame]\t\n\nThe dataframes to concatenate.\n\n\trequired\n\nReturns:\n\nName\tType\tDescription\nInternalDataFrame\tInternalDataFrame\t\n\nThe concatenated dataframe.\n\nSource code in adala/utils/internal_data.py\nprint_dataframe(dataframe)\n\nPrint dataframe to console.\n\nSource code in adala/utils/logs.py\nprint_error(text)\n\nPrint error message to console.\n\nSource code in adala/utils/logs.py\nprint_series(data)\n\nPrint series to console.\n\nSource code in adala/utils/logs.py\nprint_text(text, style=None, streaming_style=False)\n\nPrint text to console with optional style and streaming style.\n\nSource code in adala/utils/logs.py\nfuzzy_match(x, y, threshold=0.8)\n\nFuzzy match string values in two series.\n\nParameters:\n\nName\tType\tDescription\tDefault\nx\tInternalSeries\t\n\nThe first series.\n\n\trequired\ny\tInternalSeries\t\n\nThe second series.\n\n\trequired\nthreshold\tfloat\t\n\nThe threshold to use for fuzzy matching. Defaults to 0.8.\n\n\t0.8\n\nReturns:\n\nName\tType\tDescription\nInternalSeries\tInternalSeries\t\n\nThe series with fuzzy match results.\n\nSource code in adala/utils/matching.py\n Back to top\nPrevious\nSkills\nMade with Material for MkDocs",
  "usage": {
    "tokens": 341
  }
}
```
