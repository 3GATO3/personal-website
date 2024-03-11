from django.core.management.base import BaseCommand
from explorer_app.models import Country, Indicator, DebtData
from explorer_app.data_utils import reshape_debt_data

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']
        transformed_data = reshape_debt_data(file_path)
        for index, row in transformed_data.iterrows():
            country, _ = Country.objects.get_or_create(name=row['country_name'])
            indicator, _ = Indicator.objects.get_or_create(name=row['indicator_name'])
            debt_type = self._get_debt_type_from_filename(file_path) 
            debt_data = DebtData(country=country, indicator=indicator, year=row['year'], value=row['value'], debt_type=debt_type)
            debt_data.save()
        self.stdout.write(self.style.SUCCESS('Data loaded successfully')) 


    def _get_debt_type_from_filename(self, filename):
        if 'central_government_debt' in filename.lower():
            return 'central_government'
        elif 'general_government_debt' in filename.lower():
            return 'general_government'
        elif 'household_debt' in filename.lower():
            return 'household'
        elif 'non-financial_corporate_debt' in filename.lower():
            return 'non_financial_corporate'
        elif 'private_debt' in filename.lower():
            return 'private'


