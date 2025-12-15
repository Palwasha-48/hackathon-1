/// <reference types="@docusaurus/module-type-aliases" />

declare module "@theme/Heading" {
  import type { HTMLAttributes, ReactNode } from "react";

  export interface HeadingProps extends HTMLAttributes<HTMLHeadingElement> {
    as?: "h1" | "h2" | "h3" | "h4" | "h5" | "h6";
    children?: ReactNode;
  }

  export default function Heading(props: HeadingProps): JSX.Element;
}
