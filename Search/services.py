def model_filter(model, query):
    return model.objects.filter(search_vector=query)


def queryset_filter(queryset, query):
    return queryset.filter(search_vector=query)
