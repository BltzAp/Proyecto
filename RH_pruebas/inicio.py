from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
import preguntas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

#TODO:catalogos
#!area
@app.route('/area')
def area():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area order by idArea')
    datos = cursor.fetchall()
    return render_template("area.html", comentarios = datos)

@app.route('/area_editar/<string:id>')
def area_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area where idArea = %s', (id))
    dato  = cursor.fetchall()
    return render_template("area_edi.html", comentar=dato[0])

@app.route('/area_fedita/<string:id>',methods=['POST'])
def area_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update area set descripcion=%s where idArea=%s', (desc,id))
        conn.commit()
    return redirect(url_for('area'))

@app.route('/area_borrar/<string:id>')
def area_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from area where idArea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('area'))

@app.route('/area_agregar')
def area_agregar():
    return render_template("area_agr.html")

@app.route('/area_fagrega', methods=['POST'])
def area_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into area (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('area'))

#!carrera:
@app.route('/carrera')
def carrera():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera order by idCarrera')
    datos = cursor.fetchall()
    return render_template("carrera.html", comentarios = datos)

@app.route('/carrera_editar/<string:id>')
def carrera_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera where idCarrera = %s', (id))
    dato  = cursor.fetchall()
    return render_template("carrera_edi.html", comentar=dato[0])

@app.route('/carrera_fedita/<string:id>',methods=['POST'])
def carrera_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update carrera set descripcion=%s where idCarrera=%s', (desc,id))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route('/carrera_borrar/<string:id>')
def carrera_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from carrera where idCarrera = {0}'.format(id))
    conn.commit()
    return redirect(url_for('carrera'))

@app.route('/carrera_agregar')
def carrera_agregar():
    return render_template("carrera_agr.html")

@app.route('/carrera_fagrega', methods=['POST'])
def carrera_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into carrera (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('carrera'))

#!escolaridad
@app.route('/escolaridad')
def escolaridad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idEscolaridad, descripcion from escolaridad order by idEscolaridad')
    datos = cursor.fetchall()
    return render_template("escolaridad.html", comentarios = datos)

@app.route('/escolaridad_editar/<string:id>')
def escolaridad_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEscolaridad, descripcion from escolaridad where idEscolaridad = %s', (id))
    dato  = cursor.fetchall()
    return render_template("escolaridad_edi.html", comentar=dato[0])

@app.route('/escolaridad_fedita/<string:id>',methods=['POST'])
def escolaridad_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update escolaridad set descripcion=%s where idEscolaridad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('escolaridad'))

@app.route('/escolaridad_borrar/<string:id>')
def escolaridad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from escolaridad where idEscolaridad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('escolaridad'))

@app.route('/escolaridad_agregar')
def escolaridad_agregar():
    return render_template("escolaridad_agr.html")

@app.route('/escolaridad_fagrega', methods=['POST'])
def escolaridad_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into escolaridad (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('escolaridad'))

#!Estado civil
@app.route('/estado_civil')
def estado_civil():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idEstadoCivil, descripcion from estado_civil order by idEstadoCivil')
    datos = cursor.fetchall()
    return render_template("estado_civil.html", comentarios = datos)

@app.route('/estado_civil_editar/<string:id>')
def estado_civil_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEstadoCivil, descripcion from estado_civil where idEstadoCivil = %s', (id))
    dato  = cursor.fetchall()
    return render_template("estado_civil_edi.html", comentar=dato[0])

@app.route('/estado_civil_fedita/<string:id>',methods=['POST'])
def estado_civil_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update estado_civil set descripcion=%s where idEstadoCivil=%s', (desc,id))
        conn.commit()
    return redirect(url_for('estado_civil'))

@app.route('/estado_civil_borrar/<string:id>')
def estado_civil_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from estado_civil where idEstadoCivil = {0}'.format(id))
    conn.commit()
    return redirect(url_for('estado_civil'))

@app.route('/estado_civil_agregar')
def estado_civil_agregar():
    return render_template("estado_civil_agr.html")

@app.route('/estado_civil_fagrega', methods=['POST'])
def estado_civil_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into estado_civil (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('estado_civil'))

#!grado de avance
@app.route('/grado_avance')
def grado_avance():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance order by idGradoAvance')
    datos = cursor.fetchall()
    return render_template("grado_avance.html", comentarios = datos)

@app.route('/grado_avance_editar/<string:id>')
def grado_avance_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance where idGradoAvance = %s', (id))
    dato  = cursor.fetchall()
    return render_template("grado_avance_edi.html", comentar=dato[0])

@app.route('/grado_avance_fedita/<string:id>',methods=['POST'])
def grado_avance_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update grado_avance set descripcion=%s where idGradoAvance=%s', (desc,id))
        conn.commit()
    return redirect(url_for('grado_avance'))

@app.route('/grado_avance_borrar/<string:id>')
def grado_avance_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from grado_avance where idGradoAvance = {0}'.format(id))
    conn.commit()
    return redirect(url_for('grado_avance'))

@app.route('/grado_avance_agregar')
def grado_avance_agregar():
    return render_template("grado_avance_agr.html")

@app.route('/grado_avance_fagrega', methods=['POST'])
def grado_avance_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into grado_avance (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('grado_avance'))

#!habilidades
@app.route('/habilidad')
def habilidad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad order by idHabilidad')
    datos = cursor.fetchall()
    return render_template("habilidad.html", comentarios = datos)

@app.route('/habilidad_editar/<string:id>')
def habilidad_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad where idHabilidad = %s', (id))
    dato  = cursor.fetchall()
    return render_template("habilidad_edi.html", comentar=dato[0])

@app.route('/habilidad_fedita/<string:id>',methods=['POST'])
def habilidad_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update habilidad set descripcion=%s where idHabilidad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('habilidad'))

@app.route('/habilidad_borrar/<string:id>')
def habilidad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from habilidad where idHabilidad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('habilidad'))

@app.route('/habilidad_agregar')
def habilidad_agregar():
    return render_template("habilidad_agr.html")

@app.route('/habilidad_fagrega', methods=['POST'])
def habilidad_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into habilidad (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('habilidad'))

#!idiomas
@app.route('/idioma')
def idioma():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma order by idIdioma')
    datos = cursor.fetchall()
    return render_template("idioma.html", comentarios = datos)

@app.route('/idioma_editar/<string:id>')
def idioma_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma where idIdioma = %s', (id))
    dato  = cursor.fetchall()
    return render_template("idioma_edi.html", comentar=dato[0])

@app.route('/idioma_fedita/<string:id>',methods=['POST'])
def idioma_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update idioma set descripcion=%s where idIdioma=%s', (desc,id))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_borrar/<string:id>')
def idioma_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from idioma where idIdioma = {0}'.format(id))
    conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_agregar')
def idioma_agregar():
    return render_template("idioma_agr.html")

@app.route('/idioma_fagrega', methods=['POST'])
def idioma_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into idioma (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('idioma'))

#TODO:contratación
#!puesto
@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    return render_template("puesto.html", pue = datos, dat='   ', catArea = '   ', catEdoCivil = '   ', catEscolaridad = '   ',
                           catGradoAvance = '    ', catCarrera = '    ', catIdioma = ' ', catHabilidad = ' ')


@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
            'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
            'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s', (idP))
    datos2 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s', (idP))
    datos4 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos7 = cursor.fetchall()
    return render_template("puesto.html", pue = datos, dat=dato[0], catArea=datos1[0], catEdoCivil=datos2[0], catEscolaridad=datos3[0],
                           catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()
    return redirect(url_for('puesto'))


@app.route('/puesto_agrOp2')
def puesto_agrOp2():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    return render_template("puesto_agrOp2.html", catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7)


@app.route('/puesto_fagrega2', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':

        if  'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'
        if 'idEstadoCivil' in request.form:
            idEC = request.form['idEstadoCivil']
        else:
            idEC = '1'
        if 'idEscolaridad' in request.form:
            idEs = request.form['idEscolaridad']
        else:
            idEs = '1'
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        if 'sexo' in request.form:
            sex = request.form['sexo']
        else:
            sex = '1'
        codP = request.form['codPuesto']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute(
    'insert into puesto (codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
    'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
    'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF,
     reqP, resp, conT))
    conn.commit()

    cursor.execute('select idPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato = cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh =nhab[0]+1

    for i in range(1,nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP,i))
            conn.commit()

    return redirect(url_for('puesto'))


@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos11 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s',(idP))
    datos12 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s',(idP))
    datos13 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s',(idP))
    datos14 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos17 = cursor.fetchall()

    return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7,
                           Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0],
                           Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        codP = request.form['codPuesto']
        idAr = request.form['idArea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idEstadoCivil']
        idEs = request.form['idEscolaridad']
        idGA = request.form['idGradoAvance']
        idCa = request.form['idCarrera']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('update puesto set codPuesto = %s, idArea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, '
                   'remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, '
                   'idEstadoCivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, experiencia = %s, '
                   'conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                   'condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                   sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
    conn.commit()

    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh = nhab[0] + 1

    for i in range(1, nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP, i))
            conn.commit()
    return redirect(url_for('puesto'))



#TODO: Examenes psicometricos

@app.route('/examen')
def preguntass():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    examen_id = None
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO examenes (nombre) VALUES (%s)"
            cursor.execute(sql, ('Examen de ejemplo',))
            examen_id = cursor.lastrowid
            print(f"Nuevo examen creado con ID: {examen_id}")
        conn.commit()
    finally:
        conn.close()
    (pregunta1, p1_resp1, p1_resp2, p1_resp3, pregunta2, p2_resp1, p2_resp2, p2_resp3, pregunta3, p3_resp1, p3_resp2, p3_resp3, pregunta4, p4_resp1, p4_resp2, p4_resp3, pregunta5, p5_resp1, p5_resp2, p5_resp3, pregunta6, p6_resp1, p6_resp2, p6_resp3, pregunta7, p7_resp1, p7_resp2, p7_resp3, pregunta8, p8_resp1, p8_resp2, p8_resp3, pregunta9, p9_resp1, p9_resp2, p9_resp3, pregunta10, p10_resp1, p10_resp2, p10_resp3) = preguntas.test()
    return render_template("exam.html", examen_id=examen_id, pregunta1=pregunta1, p1_resp1=p1_resp1, p1_resp2=p1_resp2, p1_resp3=p1_resp3, pregunta2=pregunta2, p2_resp1=p2_resp1, p2_resp2=p2_resp2, p2_resp3=p2_resp3, pregunta3=pregunta3, p3_resp1=p3_resp1, p3_resp2=p3_resp2, p3_resp3=p3_resp3, pregunta4=pregunta4, p4_resp1=p4_resp1, p4_resp2=p4_resp2, p4_resp3=p4_resp3, pregunta5=pregunta5, p5_resp1=p5_resp1, p5_resp2=p5_resp2, p5_resp3=p5_resp3, pregunta6=pregunta6, p6_resp1=p6_resp1, p6_resp2=p6_resp2, p6_resp3=p6_resp3, pregunta7=pregunta7, p7_resp1=p7_resp1, p7_resp2=p7_resp2, p7_resp3=p7_resp3, pregunta8=pregunta8, p8_resp1=p8_resp1, p8_resp2=p8_resp2, p8_resp3=p8_resp3, pregunta9=pregunta9, p9_resp1=p9_resp1, p9_resp2=p9_resp2, p9_resp3=p9_resp3, pregunta10=pregunta10, p10_resp1=p10_resp1, p10_resp2=p10_resp2, p10_resp3=p10_resp3)


@app.route('/guardar', methods=['POST'])
def guardar():
    examen_id = request.form['examen_id']
    respuestas = []
    for i in range(1, 11):
        respuesta = request.form.get(f'p{i}')
        if respuesta:
            respuestas.append((examen_id, i, respuesta))
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO respuestas (examen_id, pregunta_id, respuesta_seleccionada) VALUES (%s, %s, %s)"
            cursor.executemany(sql, respuestas)
        conn.commit()
    finally:
        conn.close()
    return render_template("home.html")

@app.route('/revisar')
def revisar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    examenes = []
    try: 
        with conn.cursor() as cursor:
            # Obtener todos los exámenes
            cursor.execute("SELECT * FROM examenes ORDER BY id")
            examenes_db = cursor.fetchall()
            # Convertir las tuplas a listas y agregar un campo vacío para las respuestas
            for examen in examenes_db:
                examenes.append(list(examen) + [[]])
            # Obtener las respuestas para cada examen
            for examen in examenes:
                cursor.execute("SELECT * FROM respuestas WHERE examen_id = %s ORDER BY pregunta_id", (examen[0],))
                examen_respuestas = cursor.fetchall()
                examen[2].extend(examen_respuestas)
    finally:
        conn.close()
    return render_template("revisa.html", examenes=examenes)

@app.route('/calificar', methods=['POST'])
def calificar():
    examen_id = request.form['examen_id']
    pregunta_id = request.form['pregunta_id']
    calificacion = request.form['calificacion']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    try:
        with conn.cursor() as cursor:
            # Guardar la calificación en la base de datos
            sql = "UPDATE respuestas SET calificacion = %s WHERE examen_id = %s AND pregunta_id = %s"
            cursor.execute(sql, (calificacion, examen_id, pregunta_id))
        conn.commit()
    finally:
        conn.close()
    return redirect('/revisar')

@app.route('/calificados')
def examenes_revisados():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    try:
        with conn.cursor() as cursor:
            # Obtener los exámenes calificados y sus respuestas
            sql = "SELECT e.id, e.nombre, r.pregunta_id, r.respuesta_seleccionada, r.calificacion \
                   FROM examenes e \
                   INNER JOIN respuestas r ON e.id = r.examen_id \
                   WHERE r.calificacion IS NOT NULL \
                   ORDER BY e.id, r.pregunta_id"
            cursor.execute(sql)
            resultados = cursor.fetchall()
    finally:
        conn.close()

    # Procesar los resultados para agrupar las respuestas por examen
    examenes = {}
    for fila in resultados:
        examen_id, nombre_examen, pregunta_id, respuesta, calificacion = fila
        if examen_id not in examenes:
            examenes[examen_id] = {'nombre': nombre_examen, 'respuestas': []}
        examenes[examen_id]['respuestas'].append({'pregunta_id': pregunta_id, 'respuesta': respuesta, 'calificacion': calificacion})

    # Calcular el promedio de calificaciones para cada examen
    for examen_id, datos_examen in examenes.items():
        calificaciones = [respuesta['calificacion'] for respuesta in datos_examen['respuestas']]
        promedio_calificaciones = sum(calificaciones) / len(calificaciones)
        examenes[examen_id]['promedio_calificaciones'] = round(promedio_calificaciones, 2)

    return render_template("califica.html", examenes=examenes)


if __name__ == "__main__":
    app.run(debug=True)
