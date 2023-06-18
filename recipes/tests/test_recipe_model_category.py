from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeCategoryModelTeste(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category Testing'
        )
        return super().setUp()

    def test_recipe_category_model_string_representation_is_name_field(self):
        needed = 'Category Testing'
        self.category.title = needed
        self.category.full_clean()
        self.category.save()
        self.assertEqual(str(self.category), needed,
                         msg=f'Category string representation must be '
                         f'"{needed}" but "{str(self.category)}" was received.')

    def test_recipe_category_model_name_max_length_is_65_chars(self):
        self.category.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
            self.category.save()
