from django.db import models


class MeetupManager(models.Manager):
    def get_meetups_from_context(self, context: dict):
        obj_to_return = self.filter(is_visible=True)
        name = context.get('name')
        category = context.get('category')
        from_date = context.get('from_date')
        to_date = context.get('to_date')

        if name:
            obj_to_return = obj_to_return.filter(name__icontains=name)

        if category:
            obj_to_return = obj_to_return.filter(tags__name__iexact=category)

        if from_date:
            obj_to_return = obj_to_return.filter(date__gte=from_date)

        if to_date:
            obj_to_return = obj_to_return.filter(date__lte=to_date)

        return obj_to_return
