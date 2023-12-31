import React from 'react'

const MegaMenu = () => {
    return (
        <div className=' z-50 flex gap-5 ' >
            <ul>
           
                    <div className=' group'>
                        <button>product</button>
                        <div className=' hidden group-hover:flex flex-col absolute left-0 p-10 w-full bg-purple-200 z-20 text-black duration-300'>
                        <div className=' grid grid-cols-2 md:grid-cols-4 gap-5'>
                            <h3>category</h3>
                        </div>
                        </div>
                    </div>

            </ul>
            <ul>
            </ul>
        </div>
    )
}

export default MegaMenu