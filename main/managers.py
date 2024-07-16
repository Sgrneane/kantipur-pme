from django.db import models

from fpn.exceptions import RecordAlreadyExists
from account.models import CustomUser
from fpn import commons
import nepali_datetime

class ObjectManager(models.Manager):
    "Model to manage aayat niryat object"
    def record_for_type_and_month_exists(self,created_by,broad_type,month,date):
        """Method to check existing record for user's office exists for certain month of the year

        Args:
           created_by (CustomUser): User whose office record is to be checked.
             broad_type: Import Export and Bhansar chori Nikasi
             month:related month

         Returns:
            bool: Record Exists for Month or Not.
         """
        return self.filter(
            created_by__office=created_by.office,
            broad_type=broad_type,
            related_month=month,
            created_on_np_date__startswith=date[:4]  #this returns year with month (2080)
         ).exists()

    def create(self, **kwargs):
        """Create  override to add custom need based logic"""
        created_on_np_date = nepali_datetime.date.today().strftime("%Y-%m-%d")

        if self.record_for_type_and_month_exists(
            created_by=kwargs.get("created_by"),
            broad_type=kwargs.get('broad_type'),
            month=kwargs.get('related_month'),
            date=created_on_np_date,
        ):
            raise RecordAlreadyExists
        kwargs.update({
            "created_on_np_date": created_on_np_date,
        })
        return super().create(**kwargs)
    
    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False, *args, **kwargs):
        """Bulk create override to add custom need based logic"""
        # validating user passes at least one object to bulk create
        assert objs, "Objects to bulk create cannot be None or Empty."
        created_on_np_date = nepali_datetime.date.today().strftime("%Y-%m-%d")


        # assuming all objs are created by same user in bulk create
        # performing this check outside of for loop to reduce db hit
        first_record = next(iter(objs))
        if self.record_for_type_and_month_exists(
            created_by=first_record.created_by,
            broad_type=first_record.broad_type,
            month=first_record.related_month,
            date=created_on_np_date
        ):
            raise RecordAlreadyExists

        # inserting created_on_np_date to each obj manually 
        # since save or create method is not called in bulk create
        for obj in objs:
             obj.created_on_np_date = created_on_np_date
        return super().bulk_create(objs, batch_size, ignore_conflicts, *args, **kwargs)


class YearlyBudgetObjectManager(models.Manager):
    def record_for_year_exists(self,created_by,date):
        return self.filter(
            created_by__office=created_by.office,
            created_on_np_date__startswith=date[:4]  #this returns year with month (2080)
         ).exists()
    def create(self, **kwargs):
        """Create  override to add custom need based logic"""
        created_on_np_date = nepali_datetime.date.today().strftime("%Y-%m-%d")

        if self.record_for_year_exists(
            created_by=kwargs.get("created_by"),
            date=created_on_np_date,
        ):
            raise RecordAlreadyExists
        kwargs.update({
            "created_on_np_date": created_on_np_date,
        })
        return super().create(**kwargs)
    
class QuarterelyMonthlyBudgetObjectManager(models.Manager):
    def record_for_year_exists(self,created_by,month_or_quarter,date):
        return self.filter(
            created_by__office=created_by.office,
            month_or_quarter=month_or_quarter,
            created_on_np_date__startswith=date[:4]  #this returns year with month (2080)
         ).exists()
    def create(self, **kwargs):
        """Create  override to add custom need based logic"""
        created_on_np_date = nepali_datetime.date.today().strftime("%Y-%m-%d")

        if self.record_for_year_exists(
            created_by=kwargs.get("created_by"),
            month_or_quarter = kwargs.get('month_or_quarter'),
            date=created_on_np_date,
        ):
            raise RecordAlreadyExists
        kwargs.update({
            "created_on_np_date": created_on_np_date,
        })
        return super().create(**kwargs)
