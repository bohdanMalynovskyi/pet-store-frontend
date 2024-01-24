export const Bone = ({ onClick }) => {
  return (
    <svg
      onClick={onClick}
      className="cursor-pointer"
      xmlns="http://www.w3.org/2000/svg"
      width="25"
      height="24"
      viewBox="0 0 25 24"
      fill="none"
    >
      <path
        d="M21.9584 5.70853C21.3984 5.03423 20.597 4.60559 19.7253 4.51416C19.67 4.01054 19.5019 3.52585 19.2337 3.09603C18.9655 2.66621 18.6039 2.30229 18.1759 2.03127C17.7478 1.76025 17.2642 1.58909 16.7609 1.53048C16.2577 1.47186 15.7477 1.5273 15.2688 1.69268C14.7899 1.85806 14.3544 2.12914 13.9946 2.48581C13.6347 2.84247 13.3598 3.27558 13.1902 3.753C13.0206 4.23041 12.9607 4.73989 13.0148 5.24363C13.069 5.74738 13.2359 6.23246 13.5031 6.66291C13.5035 6.66539 13.5035 6.66793 13.5031 6.67041L6.91154 13.2667C6.91154 13.2667 6.91154 13.2667 6.90217 13.2667C6.47172 12.9994 5.98664 12.8326 5.48289 12.7784C4.97915 12.7242 4.46967 12.7842 3.99225 12.9538C3.51484 13.1234 3.08173 13.3983 2.72506 13.7581C2.3684 14.118 2.09732 14.5535 1.93194 15.0324C1.76656 15.5113 1.71112 16.0213 1.76973 16.5245C1.82835 17.0277 1.99951 17.5113 2.27053 17.9394C2.54155 18.3675 2.90546 18.729 3.33529 18.9973C3.76511 19.2655 4.2498 19.4335 4.75342 19.4888C4.80876 19.9925 4.97678 20.4772 5.245 20.907C5.51323 21.3368 5.87479 21.7007 6.30286 21.9717C6.73093 22.2428 7.21452 22.4139 7.71776 22.4725C8.22101 22.5311 8.731 22.4757 9.20989 22.3103C9.68879 22.1449 10.1243 21.8739 10.4841 21.5172C10.844 21.1605 11.1189 20.7274 11.2885 20.25C11.4581 19.7726 11.518 19.2631 11.4639 18.7594C11.4097 18.2556 11.2428 17.7705 10.9756 17.3401C10.9754 17.3376 10.9754 17.3351 10.9756 17.3326L17.5709 10.7363C17.5709 10.7363 17.5709 10.7363 17.5803 10.7363C18.2614 11.1653 19.0734 11.3368 19.8698 11.2197C20.6661 11.1027 21.3945 10.7049 21.9233 10.098C22.4522 9.49123 22.7467 8.71537 22.7539 7.91047C22.761 7.10557 22.4802 6.32462 21.9622 5.70853H21.9584ZM20.78 9.10885C20.4867 9.44465 20.0834 9.66497 19.6423 9.73025C19.2013 9.79554 18.7514 9.70153 18.3734 9.4651C18.0856 9.2825 17.7443 9.20334 17.4055 9.24066C17.0667 9.27798 16.7508 9.42955 16.5097 9.67041L9.90967 16.2704C9.66939 16.512 9.51852 16.8282 9.48188 17.1669C9.44525 17.5057 9.52503 17.8468 9.70811 18.1342C9.86773 18.3909 9.9629 18.6825 9.98549 18.984C10.0081 19.2855 9.95742 19.588 9.83783 19.8657C9.71825 20.1434 9.53328 20.388 9.2987 20.5788C9.06412 20.7696 8.7869 20.9008 8.49065 20.9612C8.19441 21.0217 7.88794 21.0096 7.59738 20.926C7.30681 20.8424 7.04077 20.6898 6.82193 20.4812C6.6031 20.2726 6.43796 20.0141 6.3406 19.7279C6.24324 19.4416 6.21654 19.1361 6.26279 18.8373C6.27959 18.7302 6.27299 18.6208 6.24343 18.5165C6.21388 18.4123 6.16208 18.3156 6.0916 18.2333C6.02113 18.151 5.93364 18.0849 5.83518 18.0396C5.73671 17.9943 5.62961 17.9709 5.52123 17.971C5.48262 17.9714 5.44408 17.9745 5.40592 17.9804C5.10743 18.0263 4.80228 17.9994 4.51642 17.9021C4.23055 17.8047 3.97244 17.6397 3.76403 17.4212C3.55562 17.2026 3.40308 16.937 3.31939 16.6468C3.23571 16.3566 3.22334 16.0505 3.28336 15.7546C3.34337 15.4586 3.47399 15.1815 3.66409 14.9469C3.8542 14.7122 4.09817 14.527 4.37525 14.4069C4.65233 14.2868 4.95432 14.2354 5.25553 14.257C5.55674 14.2787 5.84826 14.3728 6.10529 14.5313C6.39306 14.7139 6.73444 14.7931 7.0732 14.7558C7.41196 14.7185 7.72792 14.5669 7.96904 14.326L14.569 7.72604C14.8084 7.48471 14.9587 7.16924 14.9953 6.83131C15.032 6.49338 14.9527 6.15304 14.7706 5.86603C14.611 5.60926 14.5158 5.31769 14.4932 5.01619C14.4706 4.71468 14.5213 4.41219 14.6409 4.1345C14.7605 3.8568 14.9454 3.61215 15.18 3.42139C15.4146 3.23063 15.6918 3.09943 15.9881 3.03897C16.2843 2.97852 16.5908 2.99059 16.8813 3.07418C17.1719 3.15777 17.4379 3.31038 17.6568 3.51901C17.8756 3.72763 18.0408 3.98609 18.1381 4.27233C18.2355 4.55858 18.2622 4.86412 18.2159 5.16291C18.1977 5.2796 18.2072 5.39896 18.2438 5.51125C18.2805 5.62354 18.3431 5.7256 18.4266 5.80912C18.5101 5.89264 18.6122 5.95525 18.7245 5.99186C18.8367 6.02846 18.9561 6.03803 19.0728 6.01978C19.4546 5.958 19.8462 6.0158 20.1938 6.18526C20.5415 6.35472 20.8282 6.62754 21.0148 6.96635C21.2013 7.30515 21.2785 7.69335 21.2358 8.07775C21.1931 8.46215 21.0326 8.82394 20.7762 9.11353L20.78 9.10885Z"
        fill="#011240"
      />
    </svg>
  );
};
