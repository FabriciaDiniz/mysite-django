from django import forms
from .models import Perguntas


class AdicionaPerguntaForm(forms.Form):
    pergunta_text = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(AdicionaPerguntaForm, self).is_valid():
            self.adiciona_erro('A pergunta informada não pode ser registrada')
            valid = False

        # if pergunta_exists:
        #     self.adiciona_erro('Pergunta já registrada')
        #     valid = False

        return valid

    def adiciona_erro(self, message):
        erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        erros.append(message)


class PerguntaForm(forms.ModelForm):

    pergunta_text = forms.CharField(label='Pergunta', max_length=200)

    class Meta:
        model = Perguntas
        fields = '__all__'
