from GUI import Initialize


def show():
    x = Initialize.initialize()
    x.top.geometry('300x550')

    x.top.title("星巴克店铺分布及统计")

    x.button.place(x=50, y=50)

    x.button1.place(x=150, y=50)

    x.button5.place(x=250, y=50)

    x.button2.place(x=50, y=100)

    x.button2.place(x=150, y=100)

    x.latidude.place(x=50, y=150)

    x.enter_latidtude.place(x=100, y=150)

    x.longitude.place(x=50, y=180)

    x.enter_longitude.place(x=100, y=180)

    x.radius.place(x=50, y=210)

    x.radius_value.place(x=100, y=210)

    x.k.place(x=50, y=240)

    x.k_value.place(x=100, y=240)

    x.key_word.place(x=50, y=270)

    x.key_word_enter.place(x=100, y=270)

    x.button3.place(x=100, y=300)

    x.button4.place(x=100, y=340)

    x.button6.place(x=100, y=380)

    x.button7.place(x=100, y=430)

    x.button8.place(x=100, y=480)

    x.button9.place(x=200, y=480)

    x.top.mainloop()
