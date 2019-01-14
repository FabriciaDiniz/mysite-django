from django import forms

#valida os dados adicionados ao formulário de cadastro de um novo tema
class AdicionaTemaForm(forms.Form):

    tema_text = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(AdicionaTemaForm, self).is_valid():
            self.adiciona_erro('O tema informado nao pode ser registrado')
            valid = False

        # if tema_exists:
        #     self.adiciona_erro('Tema ja registrado')
        #     valid = False

        return valid
    
    def adiciona_erro(self, message):
        erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        erros.append(message)

class TemaForm(forms.Form):

    tema_text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))