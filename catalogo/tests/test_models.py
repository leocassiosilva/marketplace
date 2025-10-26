from decimal import Decimal
from django.forms import ValidationError
from django.test import TestCase

from catalogo.models.peca import Peca


class PecaModelTest(TestCase):

    def setUp(self):
        self.peca = Peca.objects.create(
            nome="Peça Teste",
            descricao="Descrição de teste",
            preco=Decimal("49.90"),
            quantidade=10
        )

    def test_criacao_peca(self):
        """Testa se a peça foi criada corretamente."""
        self.assertEqual(self.peca.nome, "Peça Teste")
        self.assertEqual(self.peca.descricao, "Descrição de teste")
        self.assertEqual(self.peca.preco, Decimal("49.90"))
        self.assertEqual(self.peca.quantidade, 10)

    def test_nome_obrigatorio(self):
        """Deve falhar ao tentar criar sem nome."""
        peca = Peca(
            nome="",
            descricao="Teste",
            preco=Decimal("10.00"),
            quantidade=1
        )

        with self.assertRaises(ValidationError):
            peca.full_clean()  # Valida o modelo