from src.components.HTML5 import HTML5
from src.components.YOUPORN import YOUPORN
import sys

HTML = {
    "title" : 'YouPorn',
    "style" : '* {padding: 0;margin: 0;box-sizing: border-box;} body {width: 100vw;height: 100vh;background-color: #333;} iframe {width: 100vw;height: 50vh;margin: 0;padding: 0;}'
}

STYLE = HTML['style']

Html5 = HTML5()
def preview(data):
    return Html5.pack(

        style= "",
        tagtitle= Html5.title(Html5.style("color:#000;"),HTML['title']) + '\n    <style>' + STYLE + '</style>',

        tagbody= Html5.body(
                style= "",
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
                path = str(input(" set Path : "))
                if path == "":
                    path_all = YouPorn.setPath + "htmls"
                elif path == True:
                    path_all = path
                break
            else:
                search_all.append(search)
        for search_leigth in search_all:
            output = ""
            for video in YouPorn.search(search_leigth):
                output += "\n    " + Html5.iframe(
                    " ",
                    video['video']
                )
            open(path_all + "/" + search_leigth + ".html", "w").write(preview(output))

if __name__ == "__main__":
    main()