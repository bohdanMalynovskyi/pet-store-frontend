const nav__links = [
    {
        id: "1",
        display: "Собакам",
        path: "/dogs",
        dropdown: [
            {
                id:'1.1',
                display: "Корм для собак",
                path: "/korm-dlya-sobak",
                subcategory:[
                    {
                        id:'1.1.1',
                        display: "Сухий корм",
                    },
                    {
                        id:'1.1.2',
                        display: "Вологий корм",
                    },
                    {
                        id:'1.1.3',
                        display: "Паштет",
                    },
                ]
            },
            {
                id:'1.2',
                display: "Одяг для собак",
                path: "/odyag-dlya-sobak",
                subcategory:[
                    {
                        id:'1.1.1',
                        display: "Сухий корм",
                    },
                    {
                        id:'1.1.2',
                        display: "Вологий корм",
                    },
                    {
                        id:'1.1.3',
                        display: "Паштет",
                    },
                ]
            },
            {
                id:'1.3',
                display: "Іграшки для собак",
                path: "/igrashki-dlya-sobak",
            },
            {
                id:'1.4',
                display: "Ласощі для собак",
                path: "/lasoshhi-dlya-sobak",
            },
            {
                id:'1.5',
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
                id:'1.1',
                display: "Корм для котів",
                path: "/korm-dlya-kotiv",
            },
            {
                id:'1.2',
                display: "Одяг для котів",
                path: "/odyag-dlya-kotiv",
            },
            {
                id:'1.3',
                display: "Іграшки для котів",
                path: "/igrashki-dlya-kotiv",
            },
            {
                id:'1.4',
                display: "Ласощі для котів",
                path: "/lasoshhi-dlya-kotiv",
            },
            {
                id:'1.5',
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
                id:"3.1",
                display:"Корм для гризунів",
                path:"/korm-dlya-grizuniv",
            },
            {
                id:"3.2",
                display:"Клітки для гризунів",
                path:"/klitki-dlya-grizuniv",
            },
            {
                id:"3.3",
                display:"Ласощі для гризунів",
                path:"/lasoshhi-dlya-grizuniv",
            },
            {
                id:"3.4",
                display:"Вітаміни для гризунів",
                path:"/vitamini-dlya-grizuniv",
            },
            {
                id:"3.5",
                display:"Іграшки для гризунів",
                path:"/igrashki-dlya-grizunv",
            },

        ]

    },
    {
        display: "Птахам",
        path: "/birds",

    },
    {
        display: "Рибам",
        path: "/fish",

    },
    {
        display: "Рептиліям",
        path: "/reptiles",

    },
]

export default nav__links
