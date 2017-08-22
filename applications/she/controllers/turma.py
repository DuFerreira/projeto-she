from gluon.tools import *
import requests, json
def index():
	query=(Turmas)
	total = db(query).count()
	#link = URL('list_records', args='db')
	
	#form = crud.select(db.chamadas == auth.user_id, fields=['data_acionamento', 'sistema', 'email', 'estado'])
	query =(
		(Enturmacoes.alunos.contains(auth.user.id))&
		(Turmas.id == Enturmacoes.enturmacao)&
		(Turmas.turma == Disciplinas.id)
		)

	alunos=db(query).select(db.auth_user.first_name)
	grid = SQLFORM.grid(query,
	fields=[
	Disciplinas.disciplina,
	Disciplinas.descricao,
	Turmas.semestre,
	Turmas.professor],deletable=False, create=False, editable=False, paginate=10)
	resposta = requests.get("http://127.0.0.1:8000/she/rest/api/disciplina/.json")
	saida = json.loads(resposta.content)
	return dict(grid=grid)


@auth.requires_membership('professor')
def inserir():
	#request.env.request_method = 'POST'
	'''curl -d "disciplina=Tim" http://127.0.0.1:8000/she/rest/api/disciplinas'''
	form = FORM(
		LABEL('Disciplina'), INPUT(_name='disciplina'),
		LABEL('Descrição'), INPUT(_name='descricao'),
		INPUT(_type='submit'),
		_action=URL('rest', 'api/disciplinas.json'),
		_method = 'POST'
		)
	return dict(form=form,vars=form.vars)



