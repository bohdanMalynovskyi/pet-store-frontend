const nav__links = [
    {
        id: "1",
        display: "Собакам",
        path: "/dogs",
        dropdown: [
            {
                id:'11',
                display: "Корм для собак",
                path: "/dogs/korm-dlya-sobak",
                children:[
                    {id:'111', display: "Сухий корм", path:"/dogs/korm-dlya-sobak/111"},
                    {id:'112',display: "Вологий корм",path:"/dogs/korm-dlya-sobak/112"},
                    {id:'113',display: "Паштет",path:"/dogs/korm-dlya-sobak/113"},
                ]
            },
            {
                id:'12',
                display: "Одяг для собак",
                path: "/odyag-dlya-sobak",
            },
            {
                id:'13',
                display: "Іграшки для собак",
                path: "/igrashki-dlya-sobak",
            },
            {
                id:'14',
                display: "Ласощі для собак",
                path: "/lasoshhi-dlya-sobak",
            },
            {
                id:'15',
                display: "Вітаміни для собак",
                path: "/vitamini-dlya-sobak",
            },
        ]
    },
    {   
        id: "2",
        display: "Котам",
        path: "/cats",
        dropdown: [
            {
                id:'21',
                display: "Корм для котів",
                path: "/korm-dlya-kotiv",
            },
            {
                id:'22',
                display: "Одяг для котів",
                path: "/odyag-dlya-kotiv",
            },
            {
                id:'23',
                display: "Іграшки для котів",
                path: "/igrashki-dlya-kotiv",
            },
            {
                id:'24',
                display: "Ласощі для котів",
                path: "/lasoshhi-dlya-kotiv",
            },
            {
                id:'25',
                display: "Вітаміни для котів",
                path: "/vitamini-dlya-kotiv",
            },
        ]

    },
    {
        id:"3",
        display: "Гризунам",
        path: "/smallpets",
        dropdown:[
            {
                id:"31",
                display:"Корм для гризунів",
                path:"/korm-dlya-grizuniv",
            },
            {
                id:"32",
                display:"Клітки для гризунів",
                path:"/klitki-dlya-grizuniv",
            },
            {
                id:"33",
                display:"Ласощі для гризунів",
                path:"/lasoshhi-dlya-grizuniv",
            },
            {
                id:"34",
                display:"Вітаміни для гризунів",
                path:"/vitamini-dlya-grizuniv",
            },
            {
                id:"35",
                display:"Іграшки для гризунів",
                path:"/igrashki-dlya-grizunv",
            },
        ]

    },
    {
        id:"4",
        display: "Птахам",
        path: "/birds",

    },
    {
        id:"5",
        display: "Рибам",
        path: "/fish",

    },
    {
        id:"6",
        display: "Рептиліям",
        path: "/reptiles",

    },
]

export default nav__links



