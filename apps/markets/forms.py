from django import forms
from .models import Market


class QueryChoiceMixin(object):
    """
    Mixin for a choice field, that takes a model and an attribute of that model, and gets all distinct values for that
    attribute from the database, and uses that to generate the choices of the field
    """

    def __init__(self, model, attr, *args, **kwargs):
        choices = model.objects.all().values_list(attr, attr).distinct().order_by(attr)
        return super().__init__(choices=choices, *args, **kwargs)


class QueryChoiceField(QueryChoiceMixin, forms.ChoiceField):
    """
    A convinience model using QueryChoiceMixin and ChoiceField, that provide a ChoiceField that set it's own choices
    """

    pass


class QueryMultipleChoiceField(QueryChoiceMixin, forms.MultipleChoiceField):
    """
    A convinience model using QueryChoiceMixin and MultipleChoiceField, that provide a MultipleChoiceField that set
    it's own choices
    """

    pass


class QueryMultipleCheckboxField(QueryMultipleChoiceField):
    """
    A convinience model identical to the QueryMultipleChoiceField, but that uses a default mutliple checkbox as it's
    widget, rather than a multi-select box
    """

    def __init__(self, *args, **kwargs):
        return super().__init__(widget=forms.CheckboxSelectMultiple(), *args, **kwargs)


class ModelFilterForm(forms.ModelForm):
    """
    A Model form that can have a specified list of query_fields, and it will automatically convert these into
    QueryMultipleCheckboxFields
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.Meta.query_fields:
            self.fields[field_name] = QueryMultipleCheckboxField(self.Meta.model, field_name)


class MarketFilterForm(ModelFilterForm):

    class Meta:
        model = Market
        fields = ['company_name', ]
        query_fields = ['company_name', ]