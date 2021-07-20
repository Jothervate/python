import requests
import tkinter as tk
from tkinter.font import Font


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #取得網路上的資料
        res = requests.get('https://flask-robert.herokuapp.com/youbike')
        jsonObj = res.json()
        areas = jsonObj['areas']

        #介面
        self.title("台北市行政區")
        topFrame = tk.Frame(self,bd=2,relief=tk.GROOVE,padx=20,pady=10)
        buttonFont = Font(family='Helvetica', size=20)

        for index, area in enumerate(areas):
            if index % 6 == 0:
                parentframe = tk.Frame(topFrame)
                parentframe.pack()
            btn = tk.Button(parentframe, text=area, font=buttonFont, padx=5, pady=5)
            btn.bind('<Button-1>', self.userClick)
            btn.pack(side=tk.LEFT, padx=5)
        topFrame.pack(padx=20, pady=30)

        self.fixedWidthFrame = tk.Frame(self,width=500,bg='red')
        self.createdBottomFrame()
        self.fixedWidthFrame.pack(side=tk.LEFT,padx=20)

        #自動執行按鈕按一次的事件
        self.userClick()

    def userClick(self,event=None):
        self.bottomFrame.destroy()
        if(event == None):
            selectedArea = "中山區"
        else:
            selectedArea = event.widget['text']
        urlString = "https://flask-robert.herokuapp.com/youbike/%s" % selectedArea
        res = requests.get(urlString)
        jsonobj = res.json()
        self.areas = jsonobj['data']
        snaList = []
        for area in self.areas:
            snaList.append(area["sna"])
        self.createdBottomFrame(data=snaList)

    def createdBottomFrame(self,data=None):
        self.bottomFrame = tk.Frame(self.fixedWidthFrame, bd=2, relief=tk.GROOVE, padx=20, pady=10)
        if data == None:
            self.radioButtonData = ['仁愛林森路口', '捷運善導寺站(1號出口)', '南昌公園', '國家圖書館', '捷運臺大醫院(4號出口)', '信義連雲街口', '捷運西門站(3號出口)', '和平重慶路口',
                               '金山市民路口', '華山文創園區', '臺北市客家文化主題公園', '捷運小南門站(1號出口)', '臺北轉運站', '羅斯福寧波東街口', '河堤國小', '植物園',
                               '捷運古亭站(2號出口)', '臺北市立大學', '信義杭州路口(中華電信總公司)', '中山堂', '螢橋國小', '濟南紹興路口', '牯嶺公園', '自來水園區',
                               '捷運忠孝新生站(2號出口)', '光華商場', '莒光大埔街口', '重慶南海路口', '中正運動中心', '博愛寶慶路口', '中山青島路口', '紀州庵', '南門國中',
                               '聯合醫院和平院區']
        else:
            self.radioButtonData = data

        self.var = tk.IntVar()
        for index, data in enumerate(self.radioButtonData):
            if index % 10 == 0:
                parentframe = tk.Frame(self.bottomFrame)
                parentframe.pack(side=tk.LEFT,expand=True,fill=tk.Y)
            radioButton = tk.Radiobutton(parentframe, text=data, value=index, variable=self.var,command=self.userChoicedRadioButton).pack(anchor=tk.W)
        self.bottomFrame.pack()
        self.var.set(0)

    def userChoicedRadioButton(self):
        index = self.var.get()
        infomation = self.areas[index]
        print(infomation)

if __name__ == "__main__":
    window = Window()
    #window.title("台北市行政區")
    window.mainloop()
