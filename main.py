from logging import root
import tkinter as tk
import tkinter.font as tkFont
import math as m

class App:
    
    def __init__(self, root):
        # title
        root.title("Ares")
        # window size
        width=650
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        ares_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        ares_label["font"] = ft
        ares_label["fg"] = "#333333"
        ares_label["justify"] = "center"
        ares_label["text"] = "ARES"
        ares_label.place(x=10,y=10,width=214,height=48)

        self.masa=tk.Entry(root)
        self.masa["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        self.masa["font"] = ft
        self.masa["fg"] = "#333333"
        self.masa["justify"] = "center"
        self.masa["text"] = ""
        self.masa.place(x=60,y=70,width=185,height=43)

        m_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        m_label["font"] = ft
        m_label["fg"] = "#333333"
        m_label["justify"] = "center"
        m_label["text"] = "m"
        m_label.place(x=10,y=80,width=49,height=30)

        self.gravedad=tk.Entry(root)
        self.gravedad["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        self.gravedad["font"] = ft
        self.gravedad["fg"] = "#333333"
        self.gravedad["justify"] = "center"
        self.gravedad["text"] = ""
        self.gravedad.place(x=60,y=140,width=184,height=41)

        g_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        g_label["font"] = ft
        g_label["fg"] = "#333333"
        g_label["justify"] = "center"
        g_label["text"] = "g"
        g_label.place(x=0,y=140,width=63,height=43)

        self.altura_final=tk.Entry(root)
        self.altura_final["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        self.altura_final["font"] = ft
        self.altura_final["fg"] = "#333333"
        self.altura_final["justify"] = "center"
        self.altura_final["text"] = ""
        self.altura_final.place(x=60,y=210,width=184,height=41)

        self.altura_inicial=tk.Entry(root)
        self.altura_inicial["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        self.altura_inicial["font"] = ft
        self.altura_inicial["fg"] = "#333333"
        self.altura_inicial["justify"] = "center"
        self.altura_inicial["text"] = ""
        self.altura_inicial.place(x=60,y=280,width=184,height=41)

        self.constante=tk.Entry(root)
        self.constante["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        self.constante["font"] = ft
        self.constante["fg"] = "#333333"
        self.constante["justify"] = "center"
        self.constante["text"] = ""
        self.constante.place(x=60,y=350,width=184,height=41)

        self.longitud=tk.Entry(root)
        self.longitud["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        self.longitud["font"] = ft
        self.longitud["fg"] = "#333333"
        self.longitud["justify"] = "center"
        self.longitud["text"] = ""
        self.longitud.place(x=60,y=420,width=184,height=41)


        teta=tk.Entry(root)
        teta["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        teta["font"] = ft
        teta["fg"] = "#333333"
        teta["justify"] = "center"
        teta["text"] = ""
        teta.place(x=330,y=70,width=111,height=41)

        compresion_resorte=tk.Entry(root)
        compresion_resorte["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        compresion_resorte["font"] = ft
        compresion_resorte["fg"] = "#333333"
        compresion_resorte["justify"] = "center"
        compresion_resorte["text"] = ""
        compresion_resorte.place(x=480,y=70,width=111,height=41)

        hf_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        hf_label["font"] = ft
        hf_label["fg"] = "#333333"
        hf_label["justify"] = "center"
        hf_label["text"] = "hf"
        hf_label.place(x=0,y=220,width=61,height=30)

        ho_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        ho_label["font"] = ft
        ho_label["fg"] = "#333333"
        ho_label["justify"] = "center"
        ho_label["text"] = "ho"
        ho_label.place(x=0,y=290,width=59,height=30)

        k_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        k_label["font"] = ft
        k_label["fg"] = "#333333"
        k_label["justify"] = "center"
        k_label["text"] = "k"
        k_label.place(x=0,y=360,width=59,height=30)

        L_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        L_label["font"] = ft
        L_label["fg"] = "#333333"
        L_label["justify"] = "center"
        L_label["text"] = "L"
        L_label.place(x=0,y=430,width=59,height=30)

        teta_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        teta_label["font"] = ft
        teta_label["fg"] = "#333333"
        teta_label["justify"] = "center"
        teta_label["text"] = "θ"
        teta_label.place(x=350,y=40,width=70,height=25)

        xc_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        xc_label["font"] = ft
        xc_label["fg"] = "#333333"
        xc_label["justify"] = "center"
        xc_label["text"] = "Xc"
        xc_label.place(x=500,y=40,width=70,height=25)

        start=tk.Button(root)
        start["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        start["font"] = ft
        start["fg"] = "#000000"
        start["justify"] = "center"
        start["text"] = "START"
        start.place(x=390,y=140,width=142,height=49)
        start["command"] = self.start_command(compresion_resorte)

        reset=tk.Button(root)
        reset["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        reset["font"] = ft
        reset["fg"] = "#000000"
        reset["justify"] = "center"
        reset["text"] = "RESET"
        reset.place(x=450,y=340,width=141,height=50)
        reset["command"] = self.reset_command

    def start_command(self,compresion_resorte):
        try:
            teta =(45)
            m = (self.masa.get())
            g = (self.gravedad.get())
            hf = (self.altura_final.get())
            ho = (self.altura_inicial.get())
            k = (self.constante.get())
            L = int((self.longitud.get()))
            velocidad =((L*L)*g) / (2*(m.cos(teta)*m.cos(teta))*(hf-ho-(L*m.tan(teta))))
            compresion = m.sqrt((m*(velocidad))/k)
            compresion_resorte.config(text=f"{compresion}")
        except ValueError:
            root=tk.Tk()
            root.title("Fallo")
            root.geometry("200x200")
            Label =tk.Label(root, text="esta calculadora se alimenta a base de numeros, cualquier caracter que no sea un numero no es parte de su dieta", bg="black", fg="white", font=("ft", 15))


    def reset_command(self):
        print("python")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()