import React, { type ComponentProps } from "react";
import OriginalLayout from "@theme-original/Layout";
import Chatbot from "@site/src/components/Chatbot";

type Props = ComponentProps<typeof OriginalLayout> & {
  title?: string;
  description?: string;
};

export default function Layout(props: Props): JSX.Element {
  return (
    <>
      <OriginalLayout {...props}>
        {props.children}
        <Chatbot />
      </OriginalLayout>
    </>
  );
}
