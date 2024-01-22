import React, {useState} from 'react';
import searchIcon from "../../assets/images/search-dark.svg"
import closeIcon from "../../assets/images/close.svg"

const SearchDesktop = () => {
  const [searchText, setSearchText] = useState('');
  const [isInputFocused, setIsInputFocused] = useState(false);
  const handleInputChange = (e) => {
    setSearchText(e.target.value);
  };

  const handleInputFocus = () => {
    setIsInputFocused(true);
  };

  const handleInputBlur = () => {
    setIsInputFocused(false);
  };
  return (
    <div className=' pl-10 pr-8 items-center flex gap-2 flex-auto hidden md:flex'>
      <form className=' flex px-3 py-[6px] border border-[#B2B2B2] hover:border-hover rounded-full w-full'>
        <input
          type='text'
          value={searchText}
          onChange={handleInputChange}
          onFocus={handleInputFocus}
          onBlur={handleInputBlur}
          className='  cursor-pointer border-none w-full outline-none'
          placeholder='Введіть ваш запит' />
        <img src={isInputFocused ? closeIcon : searchIcon}
          alt={isInputFocused ? 'Close' : 'Search'}
          className='search-icon' />
      </form>
      <button className=' px-4 py-2 rounded-full bg-primary text-[#fff] hover:bg-hover transition-all '>Знайти</button>
    </div>
  )
}

export default SearchDesktop