from .test_recipe_base import RecipeTestBase


class RecipeModelTeste(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_the_test(self):
        recipe = self.recipe
        ...
