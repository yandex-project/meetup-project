from djeym.models import Map


# return the global map of meetups (the active one)
def get_global_map():
    return Map.objects.get(active=True)
