import web
from web import form
import data_file


data = data_file.Data_file()
data.data_readClientes()
data.data_readPelis()

#Codigo creado por herick024


db = web.database(dbn='mysql', db='hko7hg2s5g6po4he', user='qwy4jn8jtn5eqhxb', pw='ers2akf9foqgd8p6', host='o61qijqeuqnj9chh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com')
render = web.template.render('templates/', base = 'base')

urls = (
    '/','index',    
)

myForm = form.Form(
    form.Dropdown('Cliente',data.data_campoName('Nom_cliente')),
    form.Dropdown('Pelicula', data.data_campoMovie('Nom_peli')),
    form.Dropdown('Formato', ['Blueray','DVD']),
    form.Textbox("Tiempo",size="1",maxlength="21")
      
)

class index:        
    def GET(self):
        myF = myForm 

        return render.index(myF,None,None,None,None,None)

    def POST(self):
        myF = myForm
        if not myF.validates():
            return render.index(myF,None,None,None,None,None)
        else:
            print myF.d.Cliente , myF.d.Pelicula, myF['Formato'].value, myF.d.Tiempo
            if  myF['Formato'].value == 'Blueray':    
                result = db.insert('detalle_renta', pelicula= myF['Pelicula'].value, formato= myF['Formato'].value, tiempo= myF.d.Tiempo, total= int(myF.d.Tiempo) * 20)    
                return render.index(myF, int(myF.d.Tiempo) * 20 ,myF['Pelicula'].value, myF['Formato'].value ,myF.d.Tiempo,result)
            else:
                result = db.insert('detalle_renta', pelicula= myF['Pelicula'].value, formato= myF['Formato'].value, tiempo= myF.d.Tiempo, total= int(myF.d.Tiempo) * 10)
                return render.index(myF,int(myF.d.Tiempo) * 10,myF['Pelicula'].value,myF['Formato'].value ,myF.d.Tiempo,result)
                 
                  
            
        



if __name__ == "__main__":
    app = web.application(urls, globals())
    web.internalerror = web.debugerror
    app.run()
