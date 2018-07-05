from copy import deepcopy
def track_changed(copied_obj,new_obj,i_dont_need):
       changed={}
       for i in new_obj._meta.get_fields():
           if i.name in i_dont_need:
               continue
           try:
               old=eval("copied_obj."+i.name)
               new=eval("new_obj."+i.name)
               
               if old!=new:
                   changed[i.name]=str(old)+"=>"+str(new)

           except Exception as ex:
               pass
       return changed

