'use client'

import Image from "next/image";
import InputPanel from "./components/inputPanel";
export default function Home() {
  return (
    <>
    <br></br>
    <h1 className="title">Summarize your medical reports here!</h1>
    <br></br>
    <div style = {{alignItems: 'center'}}><InputPanel/></div>
    </>
  );
}
