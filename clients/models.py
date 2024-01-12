from django.db import models


class Client(models.Model):
    GENDER = [
        ("F", "Feminino"),
        ("M", "Masculino"),
        (
            "N",
            "Não binário",
        ),
    ]
    STATUS = [
        ("G", "Em dia"),
        ("Y", "Mensal"),
        ("R", "Devedor"),
    ]
    name = models.CharField("nome", max_length=128)
    birth_date = models.DateField("data de nascimento")
    gender = models.CharField("gênero", max_length=1, choices=GENDER)
    address = models.CharField("endereço", max_length=128, null=True)
    email = models.EmailField(max_length=32, null=True)
    phone = models.CharField(max_length=16, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_purchase_date = models.DateField("data da última compra", null=True)
    status = models.CharField(max_length=1, choices=STATUS, null=True)
    occurrences = models.TextField("ocorrências", max_length=1024, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "cliente"
