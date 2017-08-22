export_classes = dict(csv=False	, json=False, html=False,
	tsv=False, xml=False, csv_with_hidden_cols=False,
	tsv_with_hidden_cols=False)
def index():
	msg = T('Sistema Hibrido de Ensino')
	perfil = crud.read(db.auth_user, auth.user.id)
	if auth.has_membership('aluno'):
		query = ((Enturmacoes.alunos == auth.user.id)
			&(Turmas.professor == db.auth_user.id)
			&(Enturmacoes.enturmacao == Turmas.id)
			&(Turmas.turma == Disciplinas.id))
	elif auth.has_membership('professor'):
		query = ((Turmas.professor == auth.user.id)
			&(Turmas.turma == Disciplinas.id))
	disciplina = crud.select(Disciplinas, query, fields=[Disciplinas.disciplina])
	semestre = crud.select(Turmas, query, fields=[Turmas.semestre], exportclasses=export_classes)
	
	#professor = crud.select(Enturmacoes, query, fields=[Turmas.professor], exportclasses=export_classes)
	
	#turma = SQLFORM.grid(query, searchable=False, deletable=False, editable=False, create=False,paginate=5,  exportclasses=export_classes)



	return dict(perfil=perfil, disciplina=disciplina, semestre=semestre)

@auth.requires_membership('administrador')
def usuarios():
	form = SQLFORM.grid(db.auth_user)
	return dict(form=form)

@auth.requires_membership('administrador')
def grupos():
	form = SQLFORM.grid(db.auth_group)
	return dict(form=form)

@auth.requires_membership('administrador')
def membros():
	form = SQLFORM.grid(db.auth_membership)
	return dict(form=form)
