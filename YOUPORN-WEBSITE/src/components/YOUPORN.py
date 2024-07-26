import requests, os, json

class YOUPORN:

    def __init__(self, setPath = "src/"):
        self.webdata = []
        self.API = "https://lust.scathach.id/youporn/"
        self.setPath = setPath
        self.numname = 1
    
    def push(self, commandName = "", link = "", id = "", video = ""):
        return {
            'command' : commandName,
            'link' : link,
            'id' : id,
            'video' : video
        }
    
    def addAPI(self, urldata = ""):
        response = requests.get(urldata)
        print(response.status_code)
        return response.json()
    
    def search(self, keyEntry = ""):
        group = []
        command = "searchs/"
        url = str(self.API) + "search?key=" + keyEntry + "&page=" + str(self.numname)
        file = self.setPath + command + keyEntry + str(self.numname)
        datas = self.addAPI(url)
        data_leigth = 0
        if datas['success']:

            for data in datas['data']:
                data_leigth += 1

            for leigth in range(int(data_leigth / 2)):
                tep2 = int(leigth * 2)
                link = datas['data'][tep2]['link']
                id = datas['data'][tep2]['id']
                video = datas['data'][tep2]['video']
                group.append(self.push(
                    command + keyEntry,
                    link,
                    id,
                    video
                ))

            for i in group:
                self.webdata.append(i)
            
        return group