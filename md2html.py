import markdown

head = open("head","r",encoding="utf-8").read()

def gen_html(md_file_path):
    md_file = open(md_file_path,"r",encoding="utf-8").read()
    html = markdown.markdown(md_file)

    html="""
    <!doctype html>
    <html>
    """+head+"""
    <body class='typora-export os-windows'>
    <div class='typora-export-content'>
    <div id='write'  class=''>
    """+html+"""
    <p>&nbsp;</p>
    </div>
    </div>
    </body>
    </html>
    """
    return html

html = gen_html("profile/README.md")
open("index.html", "w", encoding='utf-8').write(html)

html = gen_html("profile/README-cn.md")
open("index-cn.html", "w", encoding='utf-8').write(html)