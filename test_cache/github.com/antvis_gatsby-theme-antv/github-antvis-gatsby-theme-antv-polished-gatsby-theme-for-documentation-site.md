---
title: GitHub - antvis/gatsby-theme-antv: ⚛️ Polished Gatsby theme for documentation site
description: ⚛️ Polished Gatsby theme for documentation site. Contribute to antvis/gatsby-theme-antv development by creating an account on GitHub.
url: https://github.com/antvis/gatsby-theme-antv
timestamp: 2025-01-20T15:31:24.670Z
domain: github.com
path: antvis_gatsby-theme-antv
---

# GitHub - antvis/gatsby-theme-antv: ⚛️ Polished Gatsby theme for documentation site


⚛️ Polished Gatsby theme for documentation site. Contribute to antvis/gatsby-theme-antv development by creating an account on GitHub.


## Content

[![Image 37: 图片](https://user-images.githubusercontent.com/507615/69481549-49b39d00-0e4d-11ea-87fd-1e7741f4bdf1.png)](https://user-images.githubusercontent.com/507615/69481549-49b39d00-0e4d-11ea-87fd-1e7741f4bdf1.png)

Gatsby Theme for AntV ⚛
-----------------------

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#gatsby-theme-for-antv-)

✨ Polished Gatsby theme for documentation site.

[![Image 38](https://camo.githubusercontent.com/daa59c27f8e3f221b0bb2e23f37ebb278267257120f7057cbde71230ccea0c61/68747470733a2f2f666c61742e62616467656e2e6e65742f6e706d2f762f40616e74762f6761747362792d7468656d652d616e74763f69636f6e3d6e706d)](https://www.npmjs.com/package/@antv/gatsby-theme-antv) [![Image 39: NPM downloads](https://camo.githubusercontent.com/f4e7ba9b2046178f9ab320cfb8331be292c302517a1cf76a2b5a9c0dc6da2ede/687474703a2f2f696d672e736869656c64732e696f2f6e706d2f646d2f40616e74762f6761747362792d7468656d652d616e74762e7376673f7374796c653d666c61742d737175617265)](http://npmjs.com/@antv/gatsby-theme-antv) [![Image 40: CI status](https://github.com/antvis/gatsby-theme-antv/workflows/Node%20CI/badge.svg)](https://github.com/antvis/gatsby-theme-antv/workflows/Node%20CI/badge.svg)

[![Image 41: Dependency Status](https://camo.githubusercontent.com/5575fbc83f7b1f2fde391a94dfca7ab4720cedba18c90503d11dacda2b73d2ef/68747470733a2f2f64617669642d646d2e6f72672f616e747669732f6761747362792d7468656d652d616e74762e7376673f7374796c653d666c61742d73717561726526706174683d40616e74762f6761747362792d7468656d652d616e7476)](https://david-dm.org/antvis/gatsby-theme-antv?path=@antv/gatsby-theme-antv)

Features
--------

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#features)

*   ⚛ Prerendered static site
*   🌎 Internationalization support by i18next
*   📝 Markdown-based documentation and menus
*   🎬 Examples with live playground
*   🏗 Unified Theme and Layout
*   🆙 Easy customized header nav
*   🧩 Built-in home page components

Websites using it
-----------------

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#websites-using-it)

*   ✨ [https://antv.vision](https://antv.vision/)
*   ✨ [https://g2plot.antv.vision](https://g2plot.antv.vision/)
*   ✨ [https://g2.antv.vision](https://g2.antv.vision/)
*   ✨ [https://g6.antv.vision](https://g6.antv.vision/)
*   ✨ [https://x6.antv.vision](https://x6.antv.vision/)
*   ✨ [https://f2.antv.vision](https://f2.antv.vision/)
*   ✨ [https://l7.antv.vision](https://l7.antv.vision/)
*   ✨ [https://graphin.antv.vision](https://graphin.antv.vision/)
*   ✨ [https://g.antv.vision](https://g.antv.vision/)
*   ✨ [https://gwebgpu.antv.vision](https://gwebgpu.antv.vision/)

Usage
-----

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#usage)

Create a Gatsby site from [gatsby-starter-theme-antv](https://github.com/antvis/gatsby-starter-theme-antv).

$ yarn global add gatsby-cli // or npm install gatsby-cli -g
$ gatsby new mysite https://github.com/antvis/gatsby-starter-theme-antv

Start developing.

> ✨ AntV 站点 [接入方式](https://github.com/antvis/antvis.github.io/issues/18#issuecomment-548754442) 和 [额外功能](https://github.com/antvis/antvis.github.io/issues/18#issuecomment-568692771)

### `gatsby-config.js`

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#gatsby-configjs)

// gatsby-config.js
const { repository } \= require('./package.json');

module.exports \= {
  plugins: \[
    {
      resolve: \`@antv/gatsby-theme-antv\`,
      options: {
        // pagesPath: './site/pages',
        GATrackingId: \`UA-XXXXXXXXX-X\`,
        pathPrefix: '/g2',
        // antd 主题：https://github.com/ant-design/ant-design/blob/master/components/style/themes/default.less
        theme: {
          'primary-color': '#873bf4',
        },
        pwa: true, // 是否开启 gatsby-plugin-offline
        cname: true, // 是否自动从 siteUrl 中提取 CNAME 文件
        codeSplit: true, // 是否开启 gatsby 按路由的代码分割，默认为 false
      },
    },
  \],
  siteMetadata: {
    title: \`AntV\`,
    description: \`Ant Visualization solution home page\`,
    githubUrl: repository.url,
    logoUrl: '', // 自定义 logo
    navs: \[\], // 用于定义顶部菜单
    docs: \[\], // 用于定义文档页面的二级分类菜单
    examples: \[\], // 用于定义演示页面的二级菜单，属性见下方
    isAntVSite: false, //是否是AntV官网，header样式footer和图表详情页均为定制
    galleryMenuCloseAll: false, // 是否默认收起 gallery 页面所有 menu
    showSearch: true, // 是否展示搜索框
    docsearchOptions: { // algolia 搜索配置
      versionV3: false, // 目前有两个版本的 docsearch.js，V2.x 和 V3.x，此开关决定用哪一个版本的搜索框，根据申请到的参数版本决定，二者互不兼容，详情见 https://docsearch.algolia.com/
      appId: 'xxxx', // V3.x 版本 docsearch 需要appId, V2.x 版不需要。
      apiKey: 'xxxxxx',
      indexName: 'xxx',

    }
    showChinaMirror: true, // 是否展示国内镜像链接
    showLanguageSwitcher: true, // 用于定义是否展示语言切换
    showAntVProductsCard: true, // 是否展示 AntV 系列产品的卡片链接
    showGithubStar: false, // 是否展示 Github Star
    showGithubCorner: true, // 是否展示角落的 GitHub 图标
    showChartResize: true, // 是否在demo页展示图表视图切换
    themeSwitcher: 'g2', // 是否在demo页展示主题切换, 取值为'g2' | 'g2plot' 如果不设置则不展示主题切换工具
    showAPIDoc: true, // 是否在demo页展示API文档
    showExampleDemoTitle: true, // 有截图的是否要展示 title 名称

    mdPlayground: {
      // markdown 文档中的 playground 若干设置
      splitPaneMainSize: '62%',
    },
    playground: {
      container: '<canvas id="container" /\>', // 定义演示的渲染节点，默认 <div id="container" /\>
      playgroundDidMount: 'console.log("playgroundDidMount");',
      playgroundWillUnmount: 'console.log("playgroundWillUnmount");',
      devDependencies: {
        // 如果 example 是 ts 文件，需要加上 ts 依赖，才能在 codesandbox 正确运行
        typescript: 'latest',
      },
    },
    versions: \[
      {
        '1.x': 'https://1x.ant.design',
        '2.x': 'https://2x.ant.design',
        '3.x': 'https://ant.design',
        '4.x': 'https://next.ant.design',
      },
    \],
    redirects: \[
      {
        from: /\\/old\-url/,
        to: '/new-url', // 不指定 to 时直接跳转到 https://antv-2018.alipay.com/\*\*\*
      },
    \],
    announcement: {
      zh: '站内公告，用于展示一些更新信息，如：文档更新、版本发布等',
      en:
        'The announcement in the website, used to display some updated information, such as document update, version release and etc',
    },
  },
};

*   `navs`: [props](https://github.com/antvis/gatsby-theme-antv/blob/aa8cdd7e24e965174cbe7173a841fd7d23537e52/%40antv/gatsby-theme-antv/gatsby-node.js#L242-L264)
*   `docs`: [props](https://github.com/antvis/gatsby-theme-antv/blob/aa8cdd7e24e965174cbe7173a841fd7d23537e52/%40antv/gatsby-theme-antv/gatsby-node.js#L242-L264)
*   `examples`: [props](https://github.com/antvis/gatsby-theme-antv/blob/aa8cdd7e24e965174cbe7173a841fd7d23537e52/%40antv/gatsby-theme-antv/gatsby-node.js#L242-L264)

### Components

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#components)

*   [Header Props](https://github.com/antvis/gatsby-theme-antv/blob/master/%40antv/gatsby-theme-antv/site/components/Header.tsx#L13-L39)
*   [Footer Props](https://github.com/antvis/gatsby-theme-antv/blob/046a9c4e32eea50b49347b114714425a9f99b4b7/%40antv/gatsby-theme-antv/site/components/Footer.tsx#L149-L159)
*   [SEO Props](https://github.com/antvis/gatsby-theme-antv/blob/046a9c4e32eea50b49347b114714425a9f99b4b7/%40antv/gatsby-theme-antv/site/components/Seo.tsx#L12-L17)
*   [Banner Props](https://github.com/antvis/gatsby-theme-antv/blob/c6178d1baeebce4ef4e31773a6b533020b662b27/%40antv/gatsby-theme-antv/site/components/Banner.tsx#L8-L31)
*   [Features Props](https://github.com/antvis/gatsby-theme-antv/blob/c6178d1baeebce4ef4e31773a6b533020b662b27/%40antv/gatsby-theme-antv/site/components/Features.tsx#L7-L17)
*   [Cases Props](https://github.com/antvis/gatsby-theme-antv/blob/c6178d1baeebce4ef4e31773a6b533020b662b27/%40antv/gatsby-theme-antv/site/components/Cases.tsx#L14-L25)
*   [Companies Props](https://github.com/antvis/gatsby-theme-antv/blob/c6178d1baeebce4ef4e31773a6b533020b662b27/%40antv/gatsby-theme-antv/site/components/Companies.tsx#L6-L16)

import SEO from '@antv/gatsby-theme-antv/site/components/Seo';
import Header from '@antv/gatsby-theme-antv/site/components/Header';
import Footer from '@antv/gatsby-theme-antv/site/components/Footer';
import Banner from '@antv/gatsby-theme-antv/site/components/Banner';
import Features from '@antv/gatsby-theme-antv/site/components/Features';
import Applications from '@antv/gatsby-theme-antv/site/components/Applications';
import Companies from '@antv/gatsby-theme-antv/site/components/Companies';

// @antv/gatsby-theme-antv/components/Header for commonjs version

const Layout \= () \=\> {
  const features \= \[
    {
      icon: 'https://gw.alipayobjects.com/zos/basement\_prod/5dbaf094-c064-4a0d-9968-76020b9f1510.svg',
      title: 'xxxxx',
      description: 'xxxxxxxxxxxxxxxxxxxxxxxxx',
    },
    {
      icon: 'https://gw.alipayobjects.com/zos/basement\_prod/0a0371ab-6bed-41ad-a99b-87a5044ba11b.svg',
      title: 'xxxxx',
      description: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    },
    {
      icon: 'https://gw.alipayobjects.com/zos/basement\_prod/716d0bc0-e311-4b28-b79f-afdd16e8148e.svg',
      title: 'xxxxx',
      description: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    },
  \];
  const cases \= \[
    {
      logo: 'https://gw.alipayobjects.com/mdn/rms\_23b644/afts/img/A\*2Ij9T76DyCcAAAAAAAAAAABkARQnAQ',
      title: '灯塔专业版',
      description:
        '深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金',
      link: '#',
      image:
        'https://gw.alipayobjects.com/mdn/rms\_23b644/afts/img/A\*oCd7Sq3N-QEAAAAAAAAAAABkARQnAQ',
    },
    // ...
  \];
  const companies \= \[
    {
      name: '公司1',
      image:
        'https://gw.alipayobjects.com/mdn/rms\_f8c6a0/afts/img/A\*Z1NnQ6L4xCIAAAAAAAAAAABkARQnAQ',
    },
    {
      name: '公司2',
      image:
        'https://gw.alipayobjects.com/mdn/rms\_f8c6a0/afts/img/A\*6u3hTpsd7h8AAAAAAAAAAABkARQnAQ',
    },
    // ...
  \];
  const notifications \= \[
    {
      type: '测试',
      title: 'G6 3.2 全新上线！',
      date: '2019.12.04',
      link: '#',
    },
  \];

  const downloadButton \= {
    text: '下载使用',
    link: 'https://antv.alipay.com/zh-cn/index.html',
  };

  return (
    <\>
      <SEO title\="蚂蚁数据可视化" lang\="zh" /\>
      <Header
        subTitle\="子产品名"
        logo\={{
          link: 'https://antv.alipay.com',
          img: <img src\="url" /\>,
        }}
        githubUrl\="https://github.com/antvis/g2"
        // docs={\[\]}
        showSearch\={false}
        showGithubCorner\={false}
        showLanguageSwitcher\={false}
        onLanguageChange\={(language) \=\> {
          console.log(language);
        }}
        defaultLanguage\="zh"
      /\>
      <Footer
      // columns={\[\]}
      // bottom={<div\>powered by antv</div\>}
      /\>

      <Banner
        coverImage\={<svg\></svg\>} // 右侧 banner svg 内容
        title\="主页标题"
        description\="主页描述内容描述内容描述内容描述内容"
        buttonText\="按钮文字"
        buttonHref\={'#按钮链接路径'}
        notifications\={notifications} // 可传 1-2 个内容，若不传则显示 2 个默认通知
        style\={{}}
        className\="Banner 的 className"
        video\="视频按钮点开后视频的链接，不传则不会出现视频按钮"
        githubStarLink\="Github Star 链接，不传则不会出现 GitHub Start 按钮"
        downloadButton\={downloadButton} // 不传则不会出现下载按钮
      /\>
      <Features
        title\="优势页面名称" // 可不传
        features\={features} // 必传
        style\={{}}
        className\="Features 的 className"
      /\>
      <Cases cases\={cases} style\={{}} className\="Cases 的 className" /\>
      <Companies
        title\="公司页面名称" // 必传
        companies\={companies} // 必传
        style\={{}}
        className\="Companies 的 className"
      /\>
    </\>
  );
};

### Custom Tag in Markdown

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#custom-tag-in-markdown)

We support three type of custom tags in markdown

*   **tag**

<tag color\="green" text\="分类图例"\>分类图例</tag\>

See [antd Tag components](https://ant.design/components/tag/) for more usage.

*   **swatch**

<swatch colors\="#F4664A,#30BF78,#FAAD14" colorNames\="Red,Green,Yellow"\></swatch\>

swatch props:

| name | description | isRequired | type | default |
| --- | --- | --- | --- | --- |
| title | \- | true | string | \- |
| darkmode | \- | false | boolean | \- |
| colors | \- | false | string | \- |
| colornames | \- | false | string | \- |
| grid | \- | false | 'sudoku' | 'sudoku' |

*   **playground**

Insert demos to markdown document as code playground.

将 demo 以代码预览效果插入到 markdown 文档中。

[![Image 42](https://camo.githubusercontent.com/cb9cc6a88e2f2a8659d8ceb77d175aa4debb9da61b52cdea16920765eae4fb7e/68747470733a2f2f67772e616c697061796f626a656374732e636f6d2f6d646e2f726d735f6433646434332f616674732f696d672f412a61586b6d544b6b5a343034414141414141414141414141414152516e4151)](https://camo.githubusercontent.com/cb9cc6a88e2f2a8659d8ceb77d175aa4debb9da61b52cdea16920765eae4fb7e/68747470733a2f2f67772e616c697061796f626a656374732e636f6d2f6d646e2f726d735f6433646434332f616674732f696d672f412a61586b6d544b6b5a343034414141414141414141414141414152516e4151)

<playground path\='category/basic/demo/ts-demo.ts' rid\='container'\></playground\>

playground props:

| name | description | isRequired | type | default |
| --- | --- | --- | --- | --- |
| path | demo relative path | true | string | \- |
| height | height of code playground | false | number | 400 |
| rid | specify the container ID when more than one demo in docs | false | string | 'container' |

Develop
-------

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#develop)

Visit [https://localhost:8000](https://localhost:8000/) to preview.

Publish to npm
--------------

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#publish-to-npm)

⚠️ If it is your first time for GitHub release, please read the following steps, otherwise, you can skip directly to the third step.

1.  Generate a [personal access token](https://github.com/settings/tokens): (release-it only needs "repo" access; no "admin" or other scopes).

[![Image 43: generate token](https://camo.githubusercontent.com/635d0e90649a315f59bd6af8a802f46db255d1f8abaccad4a3244407945c1b39/68747470733a2f2f67772e616c697061796f626a656374732e636f6d2f7a6f732f616e7466696e63646e2f6f72313835434a68544b2f32303230303831343135343835302e6a7067)](https://camo.githubusercontent.com/635d0e90649a315f59bd6af8a802f46db255d1f8abaccad4a3244407945c1b39/68747470733a2f2f67772e616c697061796f626a656374732e636f6d2f7a6f732f616e7466696e63646e2f6f72313835434a68544b2f32303230303831343135343835302e6a7067)

Click the button 'Generate token', then your token would be generated. Copy this token as soon as you get it since you won’t be able to see it again after refreshing the web page!

2.  Make sure the token is available as an environment variable.

Example:

export GITHUB\_TOKEN="YOUR TOKEN"

In macOS or Linux, this can be added to e.g. ~/.profile or ~/.zshrc, so it's available everytime the shell is used.

More details for the GitHub releases preperation: [GitHub Releases](https://github.com/release-it/release-it/blob/master/docs/github-releases.md)

3.  Run the following commands in your terminal.

cd @antv/gatsby-theme-antv
npm run release

Deploy
------

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#deploy)

> Set envoironment variable `GATSBY_PATH_PREFIX` to `/` in deploy service like netlify to preview pathPrefix site in root domain.

Add Dependency
--------------

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#add-dependency)

cd @antv/gatsby-theme-antv
yarn add shallowequal

or

yarn workspace @antv/gatsby-theme-antv add shallowequal

Q&A
---

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#qa)

### How to customise layout footer?

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#how-to-customise-layout-footer)

// gatsby-browser.js
exports.wrapPageElement \= ({ element, props }) \=\> {
  return React.cloneElement(element, {
    ...props,
    ...element.props,
    // https://github.com/react-component/footer#api
    footerProps: {
      bottom: 'xxx',
    },
  });
};

### How to embed other markdown document in a markdown document

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#how-to-embed-other-markdown-document-in-a-markdown-document)

\`markdown:docs/common/data-mapping.zh.md\`

_docs/common/data-mapping.zh.md_ is the path relative to the current project. It supports multiple levels of nested.

Related libraries
-----------------

[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#related-libraries)

*   [Gatsby](https://www.gatsbyjs.org/docs/)
*   [Ant Design](https://github.com/ant-design/ant-design)
*   [gatsby-transformer-remark](https://www.gatsbyjs.org/packages/gatsby-transformer-remark/)
*   [gatsby-remark-prismjs](https://www.gatsbyjs.org/packages/gatsby-remark-prismjs/?=highlight#line-highlighting)
*   [Jest](https://jestjs.io/)
*   [Testing Library](https://testing-library.com/)
*   [react-i18next](https://react.i18next.com/)

## Metadata

```json
{
  "title": "GitHub - antvis/gatsby-theme-antv: ⚛️ Polished Gatsby theme for documentation site",
  "description": "⚛️ Polished Gatsby theme for documentation site. Contribute to antvis/gatsby-theme-antv development by creating an account on GitHub.",
  "url": "https://github.com/antvis/gatsby-theme-antv?screenshot=true",
  "content": "[![Image 37: 图片](https://user-images.githubusercontent.com/507615/69481549-49b39d00-0e4d-11ea-87fd-1e7741f4bdf1.png)](https://user-images.githubusercontent.com/507615/69481549-49b39d00-0e4d-11ea-87fd-1e7741f4bdf1.png)\n\nGatsby Theme for AntV ⚛\n-----------------------\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#gatsby-theme-for-antv-)\n\n✨ Polished Gatsby theme for documentation site.\n\n[![Image 38](https://camo.githubusercontent.com/daa59c27f8e3f221b0bb2e23f37ebb278267257120f7057cbde71230ccea0c61/68747470733a2f2f666c61742e62616467656e2e6e65742f6e706d2f762f40616e74762f6761747362792d7468656d652d616e74763f69636f6e3d6e706d)](https://www.npmjs.com/package/@antv/gatsby-theme-antv) [![Image 39: NPM downloads](https://camo.githubusercontent.com/f4e7ba9b2046178f9ab320cfb8331be292c302517a1cf76a2b5a9c0dc6da2ede/687474703a2f2f696d672e736869656c64732e696f2f6e706d2f646d2f40616e74762f6761747362792d7468656d652d616e74762e7376673f7374796c653d666c61742d737175617265)](http://npmjs.com/@antv/gatsby-theme-antv) [![Image 40: CI status](https://github.com/antvis/gatsby-theme-antv/workflows/Node%20CI/badge.svg)](https://github.com/antvis/gatsby-theme-antv/workflows/Node%20CI/badge.svg)\n\n[![Image 41: Dependency Status](https://camo.githubusercontent.com/5575fbc83f7b1f2fde391a94dfca7ab4720cedba18c90503d11dacda2b73d2ef/68747470733a2f2f64617669642d646d2e6f72672f616e747669732f6761747362792d7468656d652d616e74762e7376673f7374796c653d666c61742d73717561726526706174683d40616e74762f6761747362792d7468656d652d616e7476)](https://david-dm.org/antvis/gatsby-theme-antv?path=@antv/gatsby-theme-antv)\n\nFeatures\n--------\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#features)\n\n*   ⚛ Prerendered static site\n*   🌎 Internationalization support by i18next\n*   📝 Markdown-based documentation and menus\n*   🎬 Examples with live playground\n*   🏗 Unified Theme and Layout\n*   🆙 Easy customized header nav\n*   🧩 Built-in home page components\n\nWebsites using it\n-----------------\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#websites-using-it)\n\n*   ✨ [https://antv.vision](https://antv.vision/)\n*   ✨ [https://g2plot.antv.vision](https://g2plot.antv.vision/)\n*   ✨ [https://g2.antv.vision](https://g2.antv.vision/)\n*   ✨ [https://g6.antv.vision](https://g6.antv.vision/)\n*   ✨ [https://x6.antv.vision](https://x6.antv.vision/)\n*   ✨ [https://f2.antv.vision](https://f2.antv.vision/)\n*   ✨ [https://l7.antv.vision](https://l7.antv.vision/)\n*   ✨ [https://graphin.antv.vision](https://graphin.antv.vision/)\n*   ✨ [https://g.antv.vision](https://g.antv.vision/)\n*   ✨ [https://gwebgpu.antv.vision](https://gwebgpu.antv.vision/)\n\nUsage\n-----\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#usage)\n\nCreate a Gatsby site from [gatsby-starter-theme-antv](https://github.com/antvis/gatsby-starter-theme-antv).\n\n$ yarn global add gatsby-cli // or npm install gatsby-cli -g\n$ gatsby new mysite https://github.com/antvis/gatsby-starter-theme-antv\n\nStart developing.\n\n> ✨ AntV 站点 [接入方式](https://github.com/antvis/antvis.github.io/issues/18#issuecomment-548754442) 和 [额外功能](https://github.com/antvis/antvis.github.io/issues/18#issuecomment-568692771)\n\n### `gatsby-config.js`\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#gatsby-configjs)\n\n// gatsby-config.js\nconst { repository } \\= require('./package.json');\n\nmodule.exports \\= {\n  plugins: \\[\n    {\n      resolve: \\`@antv/gatsby-theme-antv\\`,\n      options: {\n        // pagesPath: './site/pages',\n        GATrackingId: \\`UA-XXXXXXXXX-X\\`,\n        pathPrefix: '/g2',\n        // antd 主题：https://github.com/ant-design/ant-design/blob/master/components/style/themes/default.less\n        theme: {\n          'primary-color': '#873bf4',\n        },\n        pwa: true, // 是否开启 gatsby-plugin-offline\n        cname: true, // 是否自动从 siteUrl 中提取 CNAME 文件\n        codeSplit: true, // 是否开启 gatsby 按路由的代码分割，默认为 false\n      },\n    },\n  \\],\n  siteMetadata: {\n    title: \\`AntV\\`,\n    description: \\`Ant Visualization solution home page\\`,\n    githubUrl: repository.url,\n    logoUrl: '', // 自定义 logo\n    navs: \\[\\], // 用于定义顶部菜单\n    docs: \\[\\], // 用于定义文档页面的二级分类菜单\n    examples: \\[\\], // 用于定义演示页面的二级菜单，属性见下方\n    isAntVSite: false, //是否是AntV官网，header样式footer和图表详情页均为定制\n    galleryMenuCloseAll: false, // 是否默认收起 gallery 页面所有 menu\n    showSearch: true, // 是否展示搜索框\n    docsearchOptions: { // algolia 搜索配置\n      versionV3: false, // 目前有两个版本的 docsearch.js，V2.x 和 V3.x，此开关决定用哪一个版本的搜索框，根据申请到的参数版本决定，二者互不兼容，详情见 https://docsearch.algolia.com/\n      appId: 'xxxx', // V3.x 版本 docsearch 需要appId, V2.x 版不需要。\n      apiKey: 'xxxxxx',\n      indexName: 'xxx',\n\n    }\n    showChinaMirror: true, // 是否展示国内镜像链接\n    showLanguageSwitcher: true, // 用于定义是否展示语言切换\n    showAntVProductsCard: true, // 是否展示 AntV 系列产品的卡片链接\n    showGithubStar: false, // 是否展示 Github Star\n    showGithubCorner: true, // 是否展示角落的 GitHub 图标\n    showChartResize: true, // 是否在demo页展示图表视图切换\n    themeSwitcher: 'g2', // 是否在demo页展示主题切换, 取值为'g2' | 'g2plot' 如果不设置则不展示主题切换工具\n    showAPIDoc: true, // 是否在demo页展示API文档\n    showExampleDemoTitle: true, // 有截图的是否要展示 title 名称\n\n    mdPlayground: {\n      // markdown 文档中的 playground 若干设置\n      splitPaneMainSize: '62%',\n    },\n    playground: {\n      container: '<canvas id=\"container\" /\\>', // 定义演示的渲染节点，默认 <div id=\"container\" /\\>\n      playgroundDidMount: 'console.log(\"playgroundDidMount\");',\n      playgroundWillUnmount: 'console.log(\"playgroundWillUnmount\");',\n      devDependencies: {\n        // 如果 example 是 ts 文件，需要加上 ts 依赖，才能在 codesandbox 正确运行\n        typescript: 'latest',\n      },\n    },\n    versions: \\[\n      {\n        '1.x': 'https://1x.ant.design',\n        '2.x': 'https://2x.ant.design',\n        '3.x': 'https://ant.design',\n        '4.x': 'https://next.ant.design',\n      },\n    \\],\n    redirects: \\[\n      {\n        from: /\\\\/old\\-url/,\n        to: '/new-url', // 不指定 to 时直接跳转到 https://antv-2018.alipay.com/\\*\\*\\*\n      },\n    \\],\n    announcement: {\n      zh: '站内公告，用于展示一些更新信息，如：文档更新、版本发布等',\n      en:\n        'The announcement in the website, used to display some updated information, such as document update, version release and etc',\n    },\n  },\n};\n\n*   `navs`: [props](https://github.com/antvis/gatsby-theme-antv/blob/aa8cdd7e24e965174cbe7173a841fd7d23537e52/%40antv/gatsby-theme-antv/gatsby-node.js#L242-L264)\n*   `docs`: [props](https://github.com/antvis/gatsby-theme-antv/blob/aa8cdd7e24e965174cbe7173a841fd7d23537e52/%40antv/gatsby-theme-antv/gatsby-node.js#L242-L264)\n*   `examples`: [props](https://github.com/antvis/gatsby-theme-antv/blob/aa8cdd7e24e965174cbe7173a841fd7d23537e52/%40antv/gatsby-theme-antv/gatsby-node.js#L242-L264)\n\n### Components\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#components)\n\n*   [Header Props](https://github.com/antvis/gatsby-theme-antv/blob/master/%40antv/gatsby-theme-antv/site/components/Header.tsx#L13-L39)\n*   [Footer Props](https://github.com/antvis/gatsby-theme-antv/blob/046a9c4e32eea50b49347b114714425a9f99b4b7/%40antv/gatsby-theme-antv/site/components/Footer.tsx#L149-L159)\n*   [SEO Props](https://github.com/antvis/gatsby-theme-antv/blob/046a9c4e32eea50b49347b114714425a9f99b4b7/%40antv/gatsby-theme-antv/site/components/Seo.tsx#L12-L17)\n*   [Banner Props](https://github.com/antvis/gatsby-theme-antv/blob/c6178d1baeebce4ef4e31773a6b533020b662b27/%40antv/gatsby-theme-antv/site/components/Banner.tsx#L8-L31)\n*   [Features Props](https://github.com/antvis/gatsby-theme-antv/blob/c6178d1baeebce4ef4e31773a6b533020b662b27/%40antv/gatsby-theme-antv/site/components/Features.tsx#L7-L17)\n*   [Cases Props](https://github.com/antvis/gatsby-theme-antv/blob/c6178d1baeebce4ef4e31773a6b533020b662b27/%40antv/gatsby-theme-antv/site/components/Cases.tsx#L14-L25)\n*   [Companies Props](https://github.com/antvis/gatsby-theme-antv/blob/c6178d1baeebce4ef4e31773a6b533020b662b27/%40antv/gatsby-theme-antv/site/components/Companies.tsx#L6-L16)\n\nimport SEO from '@antv/gatsby-theme-antv/site/components/Seo';\nimport Header from '@antv/gatsby-theme-antv/site/components/Header';\nimport Footer from '@antv/gatsby-theme-antv/site/components/Footer';\nimport Banner from '@antv/gatsby-theme-antv/site/components/Banner';\nimport Features from '@antv/gatsby-theme-antv/site/components/Features';\nimport Applications from '@antv/gatsby-theme-antv/site/components/Applications';\nimport Companies from '@antv/gatsby-theme-antv/site/components/Companies';\n\n// @antv/gatsby-theme-antv/components/Header for commonjs version\n\nconst Layout \\= () \\=\\> {\n  const features \\= \\[\n    {\n      icon: 'https://gw.alipayobjects.com/zos/basement\\_prod/5dbaf094-c064-4a0d-9968-76020b9f1510.svg',\n      title: 'xxxxx',\n      description: 'xxxxxxxxxxxxxxxxxxxxxxxxx',\n    },\n    {\n      icon: 'https://gw.alipayobjects.com/zos/basement\\_prod/0a0371ab-6bed-41ad-a99b-87a5044ba11b.svg',\n      title: 'xxxxx',\n      description: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',\n    },\n    {\n      icon: 'https://gw.alipayobjects.com/zos/basement\\_prod/716d0bc0-e311-4b28-b79f-afdd16e8148e.svg',\n      title: 'xxxxx',\n      description: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',\n    },\n  \\];\n  const cases \\= \\[\n    {\n      logo: 'https://gw.alipayobjects.com/mdn/rms\\_23b644/afts/img/A\\*2Ij9T76DyCcAAAAAAAAAAABkARQnAQ',\n      title: '灯塔专业版',\n      description:\n        '深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金深入金融的基金',\n      link: '#',\n      image:\n        'https://gw.alipayobjects.com/mdn/rms\\_23b644/afts/img/A\\*oCd7Sq3N-QEAAAAAAAAAAABkARQnAQ',\n    },\n    // ...\n  \\];\n  const companies \\= \\[\n    {\n      name: '公司1',\n      image:\n        'https://gw.alipayobjects.com/mdn/rms\\_f8c6a0/afts/img/A\\*Z1NnQ6L4xCIAAAAAAAAAAABkARQnAQ',\n    },\n    {\n      name: '公司2',\n      image:\n        'https://gw.alipayobjects.com/mdn/rms\\_f8c6a0/afts/img/A\\*6u3hTpsd7h8AAAAAAAAAAABkARQnAQ',\n    },\n    // ...\n  \\];\n  const notifications \\= \\[\n    {\n      type: '测试',\n      title: 'G6 3.2 全新上线！',\n      date: '2019.12.04',\n      link: '#',\n    },\n  \\];\n\n  const downloadButton \\= {\n    text: '下载使用',\n    link: 'https://antv.alipay.com/zh-cn/index.html',\n  };\n\n  return (\n    <\\>\n      <SEO title\\=\"蚂蚁数据可视化\" lang\\=\"zh\" /\\>\n      <Header\n        subTitle\\=\"子产品名\"\n        logo\\={{\n          link: 'https://antv.alipay.com',\n          img: <img src\\=\"url\" /\\>,\n        }}\n        githubUrl\\=\"https://github.com/antvis/g2\"\n        // docs={\\[\\]}\n        showSearch\\={false}\n        showGithubCorner\\={false}\n        showLanguageSwitcher\\={false}\n        onLanguageChange\\={(language) \\=\\> {\n          console.log(language);\n        }}\n        defaultLanguage\\=\"zh\"\n      /\\>\n      <Footer\n      // columns={\\[\\]}\n      // bottom={<div\\>powered by antv</div\\>}\n      /\\>\n\n      <Banner\n        coverImage\\={<svg\\></svg\\>} // 右侧 banner svg 内容\n        title\\=\"主页标题\"\n        description\\=\"主页描述内容描述内容描述内容描述内容\"\n        buttonText\\=\"按钮文字\"\n        buttonHref\\={'#按钮链接路径'}\n        notifications\\={notifications} // 可传 1-2 个内容，若不传则显示 2 个默认通知\n        style\\={{}}\n        className\\=\"Banner 的 className\"\n        video\\=\"视频按钮点开后视频的链接，不传则不会出现视频按钮\"\n        githubStarLink\\=\"Github Star 链接，不传则不会出现 GitHub Start 按钮\"\n        downloadButton\\={downloadButton} // 不传则不会出现下载按钮\n      /\\>\n      <Features\n        title\\=\"优势页面名称\" // 可不传\n        features\\={features} // 必传\n        style\\={{}}\n        className\\=\"Features 的 className\"\n      /\\>\n      <Cases cases\\={cases} style\\={{}} className\\=\"Cases 的 className\" /\\>\n      <Companies\n        title\\=\"公司页面名称\" // 必传\n        companies\\={companies} // 必传\n        style\\={{}}\n        className\\=\"Companies 的 className\"\n      /\\>\n    </\\>\n  );\n};\n\n### Custom Tag in Markdown\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#custom-tag-in-markdown)\n\nWe support three type of custom tags in markdown\n\n*   **tag**\n\n<tag color\\=\"green\" text\\=\"分类图例\"\\>分类图例</tag\\>\n\nSee [antd Tag components](https://ant.design/components/tag/) for more usage.\n\n*   **swatch**\n\n<swatch colors\\=\"#F4664A,#30BF78,#FAAD14\" colorNames\\=\"Red,Green,Yellow\"\\></swatch\\>\n\nswatch props:\n\n| name | description | isRequired | type | default |\n| --- | --- | --- | --- | --- |\n| title | \\- | true | string | \\- |\n| darkmode | \\- | false | boolean | \\- |\n| colors | \\- | false | string | \\- |\n| colornames | \\- | false | string | \\- |\n| grid | \\- | false | 'sudoku' | 'sudoku' |\n\n*   **playground**\n\nInsert demos to markdown document as code playground.\n\n将 demo 以代码预览效果插入到 markdown 文档中。\n\n[![Image 42](https://camo.githubusercontent.com/cb9cc6a88e2f2a8659d8ceb77d175aa4debb9da61b52cdea16920765eae4fb7e/68747470733a2f2f67772e616c697061796f626a656374732e636f6d2f6d646e2f726d735f6433646434332f616674732f696d672f412a61586b6d544b6b5a343034414141414141414141414141414152516e4151)](https://camo.githubusercontent.com/cb9cc6a88e2f2a8659d8ceb77d175aa4debb9da61b52cdea16920765eae4fb7e/68747470733a2f2f67772e616c697061796f626a656374732e636f6d2f6d646e2f726d735f6433646434332f616674732f696d672f412a61586b6d544b6b5a343034414141414141414141414141414152516e4151)\n\n<playground path\\='category/basic/demo/ts-demo.ts' rid\\='container'\\></playground\\>\n\nplayground props:\n\n| name | description | isRequired | type | default |\n| --- | --- | --- | --- | --- |\n| path | demo relative path | true | string | \\- |\n| height | height of code playground | false | number | 400 |\n| rid | specify the container ID when more than one demo in docs | false | string | 'container' |\n\nDevelop\n-------\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#develop)\n\nVisit [https://localhost:8000](https://localhost:8000/) to preview.\n\nPublish to npm\n--------------\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#publish-to-npm)\n\n⚠️ If it is your first time for GitHub release, please read the following steps, otherwise, you can skip directly to the third step.\n\n1.  Generate a [personal access token](https://github.com/settings/tokens): (release-it only needs \"repo\" access; no \"admin\" or other scopes).\n\n[![Image 43: generate token](https://camo.githubusercontent.com/635d0e90649a315f59bd6af8a802f46db255d1f8abaccad4a3244407945c1b39/68747470733a2f2f67772e616c697061796f626a656374732e636f6d2f7a6f732f616e7466696e63646e2f6f72313835434a68544b2f32303230303831343135343835302e6a7067)](https://camo.githubusercontent.com/635d0e90649a315f59bd6af8a802f46db255d1f8abaccad4a3244407945c1b39/68747470733a2f2f67772e616c697061796f626a656374732e636f6d2f7a6f732f616e7466696e63646e2f6f72313835434a68544b2f32303230303831343135343835302e6a7067)\n\nClick the button 'Generate token', then your token would be generated. Copy this token as soon as you get it since you won’t be able to see it again after refreshing the web page!\n\n2.  Make sure the token is available as an environment variable.\n\nExample:\n\nexport GITHUB\\_TOKEN=\"YOUR TOKEN\"\n\nIn macOS or Linux, this can be added to e.g. ~/.profile or ~/.zshrc, so it's available everytime the shell is used.\n\nMore details for the GitHub releases preperation: [GitHub Releases](https://github.com/release-it/release-it/blob/master/docs/github-releases.md)\n\n3.  Run the following commands in your terminal.\n\ncd @antv/gatsby-theme-antv\nnpm run release\n\nDeploy\n------\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#deploy)\n\n> Set envoironment variable `GATSBY_PATH_PREFIX` to `/` in deploy service like netlify to preview pathPrefix site in root domain.\n\nAdd Dependency\n--------------\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#add-dependency)\n\ncd @antv/gatsby-theme-antv\nyarn add shallowequal\n\nor\n\nyarn workspace @antv/gatsby-theme-antv add shallowequal\n\nQ&A\n---\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#qa)\n\n### How to customise layout footer?\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#how-to-customise-layout-footer)\n\n// gatsby-browser.js\nexports.wrapPageElement \\= ({ element, props }) \\=\\> {\n  return React.cloneElement(element, {\n    ...props,\n    ...element.props,\n    // https://github.com/react-component/footer#api\n    footerProps: {\n      bottom: 'xxx',\n    },\n  });\n};\n\n### How to embed other markdown document in a markdown document\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#how-to-embed-other-markdown-document-in-a-markdown-document)\n\n\\`markdown:docs/common/data-mapping.zh.md\\`\n\n_docs/common/data-mapping.zh.md_ is the path relative to the current project. It supports multiple levels of nested.\n\nRelated libraries\n-----------------\n\n[](https://github.com/antvis/gatsby-theme-antv?screenshot=true#related-libraries)\n\n*   [Gatsby](https://www.gatsbyjs.org/docs/)\n*   [Ant Design](https://github.com/ant-design/ant-design)\n*   [gatsby-transformer-remark](https://www.gatsbyjs.org/packages/gatsby-transformer-remark/)\n*   [gatsby-remark-prismjs](https://www.gatsbyjs.org/packages/gatsby-remark-prismjs/?=highlight#line-highlighting)\n*   [Jest](https://jestjs.io/)\n*   [Testing Library](https://testing-library.com/)\n*   [react-i18next](https://react.i18next.com/)",
  "usage": {
    "tokens": 5842
  }
}
```
