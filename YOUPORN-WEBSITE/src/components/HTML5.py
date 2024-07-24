class HTML5:

    def style(self, css_text):
        data = ' style="'
        data += str(css_text)
        data += '" '
        return data
    
    def title(self, style = "", tagstring = ""):
        return '<title' + style + '>' + str(tagstring) + '</title>'
    
    def h(self, int_h, style = "", tagstring = ""):
        data = '<h' + str(int_h) + style + '>'
        data += tagstring + '</h' + str(int_h) + '>'
        return data
    
    def iframe(self, style = "", urlstring = ""):
        data = '<iframe'
        data += style + 'src="' + urlstring + '"'
        data += ' frameborder="0"'
        data += ' scrolling="no" allowfullscreen></iframe>'
        return  data

    def body(self, style = "", tagarray = []):
        data = '\n<body' + style
        data += '>'
        for tags in tagarray:
            data += '\n    ' + tags
        data += '\n</body>'
        return data

    def pack(self, style = "", tagtitle = "", tagbody = ""):
        data = '<!DOCTYPE html>\n<html'
        data += style + 'lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">'
        data += '\n    ' + tagtitle + '\n</head>'
        data += tagbody
        data += '\n</html>'
        return data