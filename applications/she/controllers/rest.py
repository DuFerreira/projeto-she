@request.restful()
def api():
    table_name = request.args(2)
    response.view = 'generic.'+request.extension 
    def GET(*args,**vars):
        patterns = [
        "/disciplinas[disciplinas]",
        "/disciplina/{disciplinas.disciplina.startswith}",
        "/disciplina/{disciplinas.disciplina}/:field",
        "/disciplina/{disciplinas.disciplina}/turmas[turmas.turma]",
        "/disciplina/{disciplinas.disciplina}/semestre[turmas.turma]/{turmas.semestre}",
        "/disciplina/{disciplinas.disciplina}/semestre[turmas.turma]/{turmas.semestre}/:field",
        "/disciplina/{disciplinas.disciplina}/semestre[turmas.turma]/{turmas.semestre}/enturmacoes[enturmacoes.enturmacao]",
        "/disciplina/{disciplinas.disciplina}/semestre[turmas.turma]/{turmas.semestre}/enturmacoes[enturmacoes.enturmacao]/:field",
        "/disciplina/{disciplinas.disciplina}/semestre[turmas.turma]/{turmas.semestre}/enturmacao[enturmacoes.enturmacao]/{Enturmacoes.alunos}",
        "/disciplina/{disciplinas.disciplina}/semestre[turmas.turma]/{turmas.semestre}/enturmacao[enturmacoes.enturmacao]/{Enturmacoes.alunos}/:field"
        ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(table_name,**vars):
        retornar = (db[table_name].validate_and_insert(**vars))
        if(retornar['errors']==None):
            return dict(retornar='Frase número '+retornar['id']+' inserida com sucesso')
        elif request.is_local:
            response.toolbar()
    def PUT(table_name,record_id,**vars):
        return db(db[table_name]._id==record_id).update(**vars)
    def DELETE(table_name,record_id):
        return db(db[table_name]._id==record_id).delete()
    return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)
