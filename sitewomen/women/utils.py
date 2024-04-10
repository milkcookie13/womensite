menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'addpage'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context

