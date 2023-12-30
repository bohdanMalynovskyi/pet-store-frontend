import React from 'react';
import search from "../../assets/images/search-dark.svg"

const SearchDesktop = () => {
  return (
    <div className=' pl-10 pr-8 items-center flex gap-2 flex-auto hidden md:flex'>
      <div className=' flex px-3 py-[6px] border border-[#B2B2B2] hover:border-cyan rounded-full w-full'>
        <input
          type='text'
          className='  cursor-pointer border-none w-full outline-none'
          placeholder='Введіть ваш запит' />
        <img src={search} alt="" />
      </div>
      <button className=' px-4 py-2 rounded-full bg-primary text-[#fff] hover:bg-cyan transition-all '>Знайти</button>
    </div>
  )
}

export default SearchDesktop