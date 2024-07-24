from src.components.HTML5 import HTML5
from src.components.YOUPORN import YOUPORN
import sys
HTML = {
    "title" : 'YouPorn',
    "style" : '*{padding: 0;margin: 0;box-sizing: border-box;} body{width: 100vw;height: 100vh;background-color: #333;} iframe{margin: 0;padding: 0;}'
}
BODY = {
    "style" : 'background-color: #333;width:100vw;height:100vh;'
}

Html5 = HTML5()
def preview(data):
    return Html5.pack(

        style= Html5.style(HTML['style']),
        tagtitle= Html5.title(Html5.style("color:#000;"),HTML['title']),

        tagbody= Html5.body(
                style= Html5.style(BODY['style']),
                tagarray= [data]
        )
    )

def main():
    YouPorn = YOUPORN('src/')
    while True:
        search_all = []
        path_all = ""
        while True:
            print("print : '.Y' to Comfurm && '.exit' to exit programe")
            search = str(input(" Search : "))
            if search == ".exit":
                sys.exit()
            elif search == ".y" or search == ".Y":
                print("Loading")
                print(search_all)
                path_all += str(input(" set Path : "))
                break
            else:
                search_all.append(search)
        for search_leigth in search_all:
            output = ""
            for video in YouPorn.search(search_leigth):
                output += Html5.iframe(
                    Html5.style("width:100%;height:50%;"),
                    video['video']
                )
            open(YouPorn.setPath + "htmls/" + path_all + search_leigth + ".html", "w").write(preview(output))

if __name__ == "__main__":
    main()