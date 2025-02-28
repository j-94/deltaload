---
title: Embed in Iframe - Chainlit
description: 
url: https://docs.chainlit.io/guides/iframe
timestamp: 2025-01-20T15:56:20.002Z
domain: docs.chainlit.io
path: guides_iframe
---

# Embed in Iframe - Chainlit



## Content

This section outlines the steps and specifications for embedding the external Chatbot UI, provided by Chainlit, into an existing frontend service. This integration is achieved using an HTML `<iframe>`. Below we detail the properties and considerations that need attention.

Overview
--------

The `<iframe>` tag specifies an inline frame. It is used to embed another document within the current HTML document. In this scenario, we’re embedding the Chainlit Chatbot interface that resides at a different URL.

Code Snippet
------------

Here is the basic setup of the `<iframe>` used to embed the Chatbot UI:

Attributes and Style
--------------------

*   `src`: The URL of the page to embed. This should be the URL of the Chainlit chatbot interface.
*   `width` & `height`: These attributes define the size of the iframe. The width is set to 100% of the parent container, and the height is a fixed 600px. Adjust according to your layout requirements.
*   `frameBorder`: This attribute specifies whether or not to display a border around the iframe. It’s set to “0” to avoid any border, making the embedded page blend seamlessly with your content.
*   `title`: A text description of the frame’s contents, providing essential information for assistive technologies, such as screen readers.
*   `style`: Inline CSS for the iframe. Here, it’s used to ensure there’s no border around the iframe, but it can include other styles as necessary.

Security Considerations
-----------------------

When embedding iframes, consider the following security implications:

*   **Mixed Content**: Ensure that the embedded content is served over HTTPS to prevent mixed content issues, where secure pages (served over HTTPS) also contain elements using the insecure HTTP protocol.
*   **Sandboxing**: If additional security is required, especially when embedding content from untrusted sources, consider using the `sandbox` attribute to impose restrictions on the content.
*   **Content Security Policy (CSP)**: If your website uses CSP, ensure that the policy allows for the embedding of external content from the specified URL.

Accessibility
-------------

Ensure the embedded interface adheres to accessibility guidelines:

*   The `title` attribute should accurately describe the embedded content for screen readers.
*   Ensure that the chatbot interface within the iframe itself is built according to accessibility standards, with features such as keyboard navigation and ARIA roles and properties.

Responsive Design
-----------------

To maintain a responsive design:

*   Test the iframe in multiple viewports to see how it responds to different screen sizes. The width is set to 100%, so it should adjust to the parent container’s width, but other aspects might not adjust as cleanly.
*   Consider using CSS and JavaScript to adjust the iframe’s dimensions dynamically based on the viewport size.

Troubleshooting
---------------

*   **Blocked Content**: If the iframe content doesn’t load, ensure it’s not being blocked by browser policies or extensions.
*   **Cross-Origin Issues**: Check for console errors related to CORS. The server where the chatbot UI is hosted must set appropriate headers allowing the content to be embedded on your domain.
*   **Layout Shifts**: If the layout shifts unexpectedly, verify the fixed height of the iframe isn’t causing visual issues, especially on smaller screens.

Conclusion
----------

Embedding the Chainlit chatbot interface within an iframe allows users to interact with the chatbot directly on our platform. However, it requires careful attention to security, accessibility, and responsive design. Regular testing and updates are necessary to maintain the integrity and user-friendliness of the integration.

## Metadata

```json
{
  "title": "Embed in Iframe - Chainlit",
  "description": "",
  "url": "https://docs.chainlit.io/guides/iframe",
  "content": "This section outlines the steps and specifications for embedding the external Chatbot UI, provided by Chainlit, into an existing frontend service. This integration is achieved using an HTML `<iframe>`. Below we detail the properties and considerations that need attention.\n\nOverview\n--------\n\nThe `<iframe>` tag specifies an inline frame. It is used to embed another document within the current HTML document. In this scenario, we’re embedding the Chainlit Chatbot interface that resides at a different URL.\n\nCode Snippet\n------------\n\nHere is the basic setup of the `<iframe>` used to embed the Chatbot UI:\n\nAttributes and Style\n--------------------\n\n*   `src`: The URL of the page to embed. This should be the URL of the Chainlit chatbot interface.\n*   `width` & `height`: These attributes define the size of the iframe. The width is set to 100% of the parent container, and the height is a fixed 600px. Adjust according to your layout requirements.\n*   `frameBorder`: This attribute specifies whether or not to display a border around the iframe. It’s set to “0” to avoid any border, making the embedded page blend seamlessly with your content.\n*   `title`: A text description of the frame’s contents, providing essential information for assistive technologies, such as screen readers.\n*   `style`: Inline CSS for the iframe. Here, it’s used to ensure there’s no border around the iframe, but it can include other styles as necessary.\n\nSecurity Considerations\n-----------------------\n\nWhen embedding iframes, consider the following security implications:\n\n*   **Mixed Content**: Ensure that the embedded content is served over HTTPS to prevent mixed content issues, where secure pages (served over HTTPS) also contain elements using the insecure HTTP protocol.\n*   **Sandboxing**: If additional security is required, especially when embedding content from untrusted sources, consider using the `sandbox` attribute to impose restrictions on the content.\n*   **Content Security Policy (CSP)**: If your website uses CSP, ensure that the policy allows for the embedding of external content from the specified URL.\n\nAccessibility\n-------------\n\nEnsure the embedded interface adheres to accessibility guidelines:\n\n*   The `title` attribute should accurately describe the embedded content for screen readers.\n*   Ensure that the chatbot interface within the iframe itself is built according to accessibility standards, with features such as keyboard navigation and ARIA roles and properties.\n\nResponsive Design\n-----------------\n\nTo maintain a responsive design:\n\n*   Test the iframe in multiple viewports to see how it responds to different screen sizes. The width is set to 100%, so it should adjust to the parent container’s width, but other aspects might not adjust as cleanly.\n*   Consider using CSS and JavaScript to adjust the iframe’s dimensions dynamically based on the viewport size.\n\nTroubleshooting\n---------------\n\n*   **Blocked Content**: If the iframe content doesn’t load, ensure it’s not being blocked by browser policies or extensions.\n*   **Cross-Origin Issues**: Check for console errors related to CORS. The server where the chatbot UI is hosted must set appropriate headers allowing the content to be embedded on your domain.\n*   **Layout Shifts**: If the layout shifts unexpectedly, verify the fixed height of the iframe isn’t causing visual issues, especially on smaller screens.\n\nConclusion\n----------\n\nEmbedding the Chainlit chatbot interface within an iframe allows users to interact with the chatbot directly on our platform. However, it requires careful attention to security, accessibility, and responsive design. Regular testing and updates are necessary to maintain the integrity and user-friendliness of the integration.",
  "usage": {
    "tokens": 730
  }
}
```
