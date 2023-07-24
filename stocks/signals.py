from django.db.models.signals import post_save
from .models import Stock_in,Stock_out,Stock,User,Person
from django.shortcuts import reverse

def main_stock_update_in_signal(sender,instance , created, **kwargs):

    if Stock.objects.filter(company_name=instance.company_name,tile_code=instance.tile_code,tile_size=instance.tile_size):
        
        st =Stock.objects.get(company_name=instance.company_name,tile_code=instance.tile_code,tile_size=instance.tile_size)
        # print(st.values())
        st.box_quantity+=instance.box_quantity_in
        st.save()
    else:
        Stock.objects.create(
            company_name = instance.company_name,
            tile_code = instance.tile_code,
            tile_size = instance.tile_size,
            tile_picture = instance.tile_picture,
            box_quantity = instance.box_quantity_in,
            box_capacity = instance.box_capacity
            
        )
        
    

def main_stock_update_out_signal(sender,instance , created, **kwargs):

    if Stock.objects.filter(company_name=instance.company_name,tile_code=instance.tile_code,tile_size=instance.tile_size):
        
        st =Stock.objects.get(company_name=instance.company_name,tile_code=instance.tile_code,tile_size=instance.tile_size)
        # print(st.values())
        st.box_quantity-=instance.box_quantity_out
        st.save()
    else:   
        print("no stock")
        return  reverse ('stocks:out-list')
  
        
        
        
        
def user_creation_signal(sender,instance , created, **kwargs):
    
    

    if  created:
        Person.objects.create(
            person  = instance,

            
        )
        


post_save.connect(main_stock_update_in_signal,sender=Stock_in)
post_save.connect(main_stock_update_out_signal,sender=Stock_out)
post_save.connect(user_creation_signal,sender=User)
