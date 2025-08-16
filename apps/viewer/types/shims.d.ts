declare module "react" {
  export const useEffect: any;
  export const useMemo: any;
  export const useState: any;
  export type ReactNode = any;
  const React: any;
  export default React;
}
declare module "next" {
  export type Metadata = any;
}
declare module "convex/react" {
  export class ConvexReactClient {
    constructor(url: string);
    query(name: string, args?: any): Promise<any>;
  }
}
declare namespace JSX {
  interface IntrinsicElements {
    [elemName: string]: any;
  }
}
