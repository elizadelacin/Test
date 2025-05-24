from modeltranslation.translator import register, TranslationOptions
from .models import AllNews

@register(AllNews)
class AllNewsTranslationOptions(TranslationOptions):
    fields = ('title',)