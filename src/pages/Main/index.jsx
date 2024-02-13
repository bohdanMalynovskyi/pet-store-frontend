import React from "react";

import Slider from "../../components/Slider/Slider";

import data from "../../db/data";

const Main = () => {
  return (
    <>
      <section className="section">
        <Slider title="Акції та знижки" data={data} />
        <Slider title="Новинки" data={data} />
      </section>
    </>
  );
};

export default Main;
