# djangorestframework-best-practices 


In this repo i will create new app for each best practices, and covering this that not available in the djangorestframewrok official documentations.And there is many ways to do this i found this method easy and effective. things we are gonna cover here in this env I am using 

django 1.8.13 
djangorestfrafmework 3.3.3

- 1. Writing a serializers without models. 
- 2. Writing a model serializer with non model fields 
- 3. Writing a Model method field and serializers method field 
- 4. Writing a nested write bull serializers 
- 5. Writing a read only seralizers and override create method etc... 
- 6. Writing a custom error handling  

# withoutmodelsapp

In this app I've created a serializer with models and it's has there files one of field is not require user input and i make that as read only. in the views file I've used two type of views one jest APIView and other one is generic views the advantage of using a generic view it's give helps on create documenations on browerbull API as well as swagger UI. if your want moke the the database we create a python class object here,we can fake the models by simpley writing python calls,useing this we can change our serializers to models serializers and use Person, object as models object.it's not a persistent data

# models_extra_fields_app

In this app I've create a simple model with three fileds , and added one extra field we can use this field make data base lookups and 
third party api calls and we jest over riding create methold on views And extra field can be simple string field or 
it can me model method or serializer method Note when your add extra field you have to over ride create method on serializer or in the view,

We added coustem error handling to serializers , And we added Person details view with all the method. in this example
I use user in request object if your app has authndication it will help.