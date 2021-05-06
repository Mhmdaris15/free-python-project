#Belajar keyword argument list 

def create_html(tag, text, href=""):
    html = f"<{tag} href='{href}'>{text}</{tag}>"
    return html

html = create_html("p", "Hello Python")
print(html)
html = create_html("a", "Ini Link", href="www.amazon.com")
print(html)

# <a href:"">Ini Link</a>
#seharusnya href hanya untuk "a" saja, untuk "p" tidak 
#oleh karena itu kita gunakan keyword ini (**)
#Jadi kita bisa memasukkan custom sesuai yg kita inginkan

def create_html(tag, text,**attributes):
    html = f"<{tag}>{text}</{tag}>"
    print(attributes) #ini akan diprint terlebih dahulu
    return html #baru print variabel html

html = create_html("p", "Hello Python", style="paragraf") #style masuknya ke keyword attributes
print(html)
html = create_html("a", "Ini Link", href="www.amazon.com", style="Link")
print(html)

#hasil di atas akan terdapat spasi antara hmtl dengan attributes
#oleh karena itu dijadikan method sebagai berikut

#INI YANG BENAR !!!
print("=============================")


def create_html(tag, text,**attributes):
    html = f"<{tag}"
    
    for key, value in attributes.items():
        html = html + f" {key}='{value}'"
    
    html = html + f">{text}</{tag}>"
    return html #baru print variabel html

html = create_html("p", "Hello Python", style="paragraf") #style masuknya ke keyword attributes
print(html)
html = create_html("a", "Ini Link", href="www.amazon.com", style="Link")
print(html)
html = create_html("div", "Ini Div", style="Contoh")
print(html)
