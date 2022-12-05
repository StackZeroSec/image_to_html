from PIL import Image
import sys





if __name__ == "__main__":
    image_path="to_convert.jpg"
    image = Image.open(image_path)

   
    w, h = image.size
    
    out_html = "<html><head></head><body><table cellpadding=0 cellspacing=0>"
    for j in range(h):
        out_html+="<tr>"
        for i in range(w):
            pixel = image.getpixel((i, j))
            out_html+=f'<td style="background: rgb({pixel[0]}, {pixel[1]}, {pixel[2]}); height: 1px; width:1px;"></td>\n'
        out_html+="</tr>"
    
    out_html += "</table ></body></html>"
    with open("out_html.html", "w") as f:
        f.write(out_html)