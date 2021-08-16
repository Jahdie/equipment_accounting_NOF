from locations.models import *


def workshop_by_production(production_id):
    locations = {'production_id': [], 'production_name': [], 'workshop_id': [], 'workshop_name': [],
                 'compartment_id': [], 'compartment_name': []}
    for item_prod in Locations.objects.filter(production_id=production_id):
        locations['workshop_id'].append(item_prod.workshop.id)
        locations['workshop_name'].append(item_prod.workshop.name)
    return locations

