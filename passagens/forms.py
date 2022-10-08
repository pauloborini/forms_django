from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from passagens.models import Passagem, Pessoa
from passagens.validation import *


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(
        label='Data da pesquisa', disabled=True, initial=datetime.today)

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'data_ida': 'Data de ida', 'data_volta': 'Data de volta', 'data_pesquisa': 'Data de Hoje',
                  'informacoes': 'Informações Adicionais', 'classe_viagem': 'Classe de vôo'}
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()}

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}
        campo_tem_numero(destino, 'destino', lista_de_erros)
        campo_tem_numero(origem, 'origem', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_volta_anterior_data_ida(data_ida, data_volta, lista_de_erros)
        data_ida_anterior_hoje(data_ida, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['email', 'nome']
