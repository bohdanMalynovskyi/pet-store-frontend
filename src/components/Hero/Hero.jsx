import React from 'react';
import banner from '../../assets/images/banner.jpg';

const Hero = () => {
    return (
        <section className='mb-10'>
            <div className=' mb-3 md:mb-6'>
                <img className=' w-full object-cover h-[231px] md:h-[400px] xl:h-[600px]' src={banner} alt="banner" />
            </div>
            <div className=' xl:-mt-[450px] xl:mb-[300px] max-w-[1200px] mx-auto'>
                <div className='px-5 text-center xl:w-[458px]'>
                    <h3 className='uppercase text-2xl xl:text-[32px] font-bold mb-2'>Здорове харчування для домашніх тварин</h3>
                    <p className='text-sm xl:text-base'>У нас ви знайдете відбірні корми для ваших тварин, які враховують їхні унікальні потреби</p>
                </div>
            </div>
        </section>
    );
}

export default Hero;
