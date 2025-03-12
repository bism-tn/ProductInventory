from django.shortcuts import render,redirect

from django.views.generic import View

from productapp.forms import AddproductForm

from productapp.models import ProductModel

class AddproductView(View):

    def get(self,request):

        form = AddproductForm
        
        return render(request,"addproduct.html",{"form":form})

    def post(self,request):

        data =  AddproductForm(request.POST)

        if data.is_valid():

            ProductModel.objects.create(**data.cleaned_data)
        
        form = AddproductForm

        return render(request,"addproduct.html",{"form":form})


class ReadAllProductView(View):

    def get(self,request):
         
         data = ProductModel.objects.all()

         return render(request,"showproducts.html",{"form":data})
    

class UpdateProductView(View):

    def get(self,request,**kwargs):

        id= kwargs.get("pk")

        data= ProductModel.objects.get(id=id)

        form= AddproductForm(instance=data)

        return render(request,"updateproduct.html",{"form":form})
    
    def post(self,request,**kwargs):

        id=kwargs.get("pk")

        data= ProductModel.objects.get(id=id)

        form= AddproductForm(request.POST,instance=data)

        if form.is_valid():
            print("done")

            form.save()

        return render(request,"updateproduct.html",{"form":form})


class DeleteProductView(View):
    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        data = ProductModel.objects.get(id=id)

        return render(request,"deleteproduct.html",{"form":data})
    
    def post(self,request,**kwargs):

        id = kwargs.get("pk")

        data = ProductModel.objects.get(id=id)

        data.delete()
        return redirect("allproducts")






        # data.delete()

        # return redirect("allproducts")

