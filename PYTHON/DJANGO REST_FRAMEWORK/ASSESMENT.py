"""                                                             *=*=*= Section A — Concept Application *=*=*=

Q1.Explain what statelessness means in the context of REST and describe how this principle affects the way your food delivery API handles user session data between requests.
~~> Statelessness Yani ki server har request ko independently handle karta hai, bina kisi purani request ya session ko yaad rakhe. har request apne aap mein complete honi chahiye.
statelessness Ka Rule Ye Kehta He Ki Request Ke Bich Me Wo Apne Pass Kisi Bhi Client Ka Session Data Apne Pass Store NAhi Karega.Matlab User Ne Login Request Bheji Aur Phir Next Request Bheji To USer Maan Ke NAhi Chalega Ki Ye Wahi User He User Ko Har Bar Request Ke Sath Authentication Bhi Dena Padega



Q2.why ModelSerializer is the better choice for this use case, and describe at least two specific field-level validations you would add to protect the data integrity of menu items.
~~> serialzer se zyada ModelSerializer Use Karna Bhaot Important He 
Restaurant management API me mobile app POST request ke through naye menu items add karegi. Is case me ModelSerializer use karna better hai kyunki ye directly Django model ke saath kaam karta hai. Wo Automatic Fields Genrate Karega Hume MAnuall Fields Define karne Ki jaroorat Nahi Jo Serializer Me Aa JAta He.Ye Hume create() aur upadarte() jesiMethod Provide Karta He Aur Sathosath Model Validation Bhi Automatically Ho Jata He.Jisse is feture Ki Vajah Se Jyada Secure Aur Fast Secure Hota he.

Q3.Explain how refactoring this to use a ModelViewSet with a DefaultRouter reduces URL management overhead, and identify which HTTP methods are automatically handled by ModelViewSet.
~~> Agra food Oredering API Me Resturant , Menu Aur Order Ke Liye Alag APIview classes Aur Alag URL Banane Padenge.Agar Sabke 5 URL Banege To tatal 15 jitne Url Aur Uske View Banane Padenge.
Aur ModelViewSet Me Har CRUD Opratin Ke liye Alag Se Banane Ki Jaroorat Nahi.Jisme ModelViewSet Me Sirf Ekbar Class Likhne Par Deafault Router Automaticaly URL Bana Deta He.

Q4.You are designing a dish search endpoint that returns all available dishes across 500+ restaurants. A QA engineer reports that
responses take over 8 seconds on a standard connection.
Question: Identify the most likely cause of this performance issue and justify which DRF pagination class you would choose to fix it. Compare the trade-offs between PageNumberPagination and CursorPagination for this scenario.
~~> Resturant Ke Sabhi dishes Eki Hi Response Me Return Kar Raha He.Jisme Sare Data Eksath Database Se Fetch Hona Phir JSON Me Convert , Internet Se Hokar Transfer , Client Side Response Me Time Lagega. Isme Pagination Most Usefull He.
from rest_framework.pagination import PageNumberPagination
class DishPagination(PageNumberPagination):
    page_size = 20 

    Ab Har Bar Sirf 20 Dish Ka Data Transfer Hoga

Q5.You are debugging a food delivery API where a logged-in customer can view anothercustomer's order history simply by changing the order ID in the URL. The IsAuthenticated permission is already applied.
Question: Identify the specific gap in the current permission setup and explain how you would implement object-level permission to ensure each customer can only access their own orders.
~~> Sirf Authenticated Se Ye Check Hoga Ki User login He Ya Nahi Ye Check Nahi Karta Ki Usi User Ne Order Kiya He Ya Nahi isiliye Custom order Class Banana Padega 
karta ki requested order usi customer ka hai ya nahi. Is security gap ko object-level permission se solve kiya ja sakta hai. Ek custom permission (BasePermission) me has_object_permission() method implement karke obj.customer == request.user check kiya jata hai. Agar logged-in user order ka owner hai to access milta hai, warna 403 Forbidden return hota hai. Security ko aur strong banane ke liye get_queryset() me bhi orders ko request.user ke basis par filter karna chahiye.

Q6.You are optimising a restaurant discovery feature that currently stores only static latitude and longitude values in the database. A product manager requests a 'findrestaurants near me' option that accepts a user's address string.
Question: Describe how you would integrate the Google Maps Geocoding API into a DRF view to
convert an address string into coordinates and use those coordinates to return nearbyrestaurant results.
~~>
                                                              *=*=*= Section B — Practical Coding Tasks *=*=*=
Task 1: Food Category Listing API
-Build a read-only DRF endpoint that returns a list of all food categories as a JSON response.Create a Category model with name (CharField, max 100) and description (TextField) fieldsand run migrations.
-Write a CategorySerializer using ModelSerializer that exposes id, name, and description.
-Create a ListAPIView endpoint mapped to /api/categories/ and register it in urls.py.
-Return all categories as a JSON array with HTTP 200; test the response in Postman or the DRF browsable API.
~~>
# url.py Me :
from django.urls import path
from .views import CategoryListView
urlpatterns = [
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
]

# view.py Me :
from rest_framework.generics import ListAPIView
from .models import Category
from .serializers import CategorySerializer
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

** ListAPIView Jo Sirf Sare Records Ko List Ke Form Me Return Karta He.Ye Data Read Karne Ke Liye Best He.
# model.py Me :
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# searealizer.py Me :
from rest_framework import serializers
from .models import Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


Task 2: Menu Item CRUD API
Build a full CRUD REST API for a MenuItem resource that includes price validation and appropriate status codes.
-Create a MenuItem model with name, price (DecimalField), category (ForeignKey to Category), and is_available (BooleanField) fields.
-Write a MenuItemSerializer using ModelSerializer that validates price is greater than 0 and raises a ValidationError if not.
-Implement list (GET), create (POST), retrieve (GET /id/), update (PUT /id/), and delete (DELETE/id/) endpoints using APIView or GenericAPIView.
-Return HTTP 201 for successful creation, 400 for validation failures, and 404 when the item is not found.
~~>
# model.py Me :
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    Uske Bad Makemigration Or Migrate Kare.
# Serializer.py Me :
from rest_framework import serializers
from .models import MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

    # Price Validation
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

# view.py :
class MenuItemListCreate(APIView):
    def get(self, request):
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# url.py :
from django.urls import path
from .views import MenuItemListCreate, MenuItemDetail

urlpatterns = [
    path("api/menuitems/",MenuItemListCreate.as_view(),name="menu-list"),
    path("api/menuitems/<int:pk>/",MenuItemDetail.as_view(),name="menu-detail") ]

Task 3: Order Listing with ViewSets, Router, and Pagination
Build a paginated and filterable order listing API by converting a plain APIView to a ModelViewSet registered with a DefaultRouter.
-Create an Order model with customer_name, item (CharField), quantity (IntegerField), andstatus (CharField with choices: pending, confirmed, delivered) fields.
-Convert the Order API to a ModelViewSet and register it with a DefaultRouter — the router mustauto-generate all CRUD URLs under /api/orders/.
-Configure PageNumberPagination in settings.py with PAGE_SIZE = 5 and apply it to the OrderViewSet.
-Support filtering orders by status using a query parameter (e.g. /api/orders/?status=pending) using the get_queryset method.
~~>
# models.py :
from django.db import models
class Order(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'),('confirmed', 'Confirmed'),('delivered', 'Delivered')]
    customer_name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.customer_name

Makemigration Or Migrate Command Run Karo.

# serializer.py :
from rest_framework import serializers
from .models import Order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

# seting.py Me :
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
}
* Mens Ek Page Me 5 Order Ayenge.

# urls.py :
from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    def get_queryset(self):
        queryset = Order.objects.all()
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)
        return queryset


# views.py :
from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    def get_queryset(self):
        queryset = Order.objects.all()
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)
        return queryset
 get_queryset Ye sirf Pending Order Dikhayega Or Agar query Perameter Na Ho To Sare Order Return Karega.

Task 4: Token-Authenticated Order Placement
-Build a protected endpoint that allows authenticated customers to place orders and retrieve only their own order history.
-Enable DRF TokenAuthentication in settings.py and generate auth tokens for test users via the Django shell or admin.
-Create a PlaceOrderAPIView (POST /api/my-orders/) that uses IsAuthenticated permission and saves the request.user as the order owner.
-Add a GET /api/my-orders/ view that returns only the orders belonging to the currently authenticated user, filtered by request.user.
-Return HTTP 401 Unauthorized (with a meaningful message) for any unauthenticated request to either endpoint.

# seting.py 
INSTALLED_APPS = [
    ...
    "rest_framework",
    "rest_framework.authtoken",
]
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],

    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ]
}

# model.py
from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    def __str__(self):
        return self.item

# serializer.py
from rest_framework import serializers
from .models import Order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["owner"]


# Apne CMD Ke Specific Location Me python manage.py shell Waha Token Create
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
user = User.objects.get(username="hiren")
token = Token.objects.create(user=user)
print(token.key)

# url.py :
from django.urls import path
from .views import PlaceOrderAPIView
urlpatterns = [
    path("api/my-orders/",PlaceOrderAPIView.as_view(),name="my-orders"),
]

# view :
class PlaceOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        orders = Order.objects.filter(owner=request.user)
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


                                                              *=*=*= Section C — Mini Capstone Project *=*=*=

# seting.py
INSTALLED_APPS=[
...
"rest_framework",
"rest_framework.authtoken",
"api"
]
REST_FRAMEWORK={
"DEFAULT_AUTHENTICATION_CLASSES":[
"rest_framework.authentication.TokenAuthentication"
],
"DEFAULT_PERMISSION_CLASSES":[
"rest_framework.permissions.AllowAny"
],

"DEFAULT_PAGINATION_CLASS":
"rest_framework.pagination.PageNumberPagination",
"PAGE_SIZE":5
}


# model.py
from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending","Pending"),
        ("confirmed","Confirmed"),
        ("delivered","Delivered")
    ]
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,
        default="pending")
    def __str__(self):
        return self.customer.username                                                   

# serializer.py
from rest_framework import serializers
from .models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def validate_name(self,value):
        if value.strip()=="":
            raise serializers.ValidationError("Name cannot be empty")
        return value


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields="__all__"

    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
        read_only_fields=["customer"]
    def validate_quantity(self,value):
        if value<1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

# url.py
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
router.register("categories",CategoryViewSet)
router.register("menu-items",MenuItemViewSet)
router.register("orders",OrderViewSet)
urlpatterns=[
    path("",include(router.urls))
]

# view.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class MenuItemViewSet(ModelViewSet):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer

class OrderViewSet(ModelViewSet):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        queryset=Order.objects.filter(customer=self.request.user)
        status=self.request.query_params.get("status")
        if status:
            queryset=queryset.filter(status=status)
        return queryset
    def perform_create(self,serializer):
        serializer.save(customer=self.request.user)

# Token Genarte :
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
user=User.objects.get(username="hiren")
token=Token.objects.create(user=user)
print(token.key)



                                                                *=*=*= Section D — AI-Augmented Learning *=*=*=
STEP 1 · BUILD WITH AI
Use an AI tool of your choice (ChatGPT, Claude, GitHub Copilot, etc.) to help you write a programthat:
Section D — AI-Augmented Learning
STEP 1 · BUILD WITH AI
Use an AI tool of your choice (ChatGPT, Claude, GitHub Copilot, etc.) to help you write a program that:
-Implements a POST /api/orders/place/ endpoint using DRF APIView that accepts customer_name, item, and quantity in the request body.
-Validates that quantity is a positive integer and returns a JSON error response with HTTP 400 if the validation fails.
-Saves the order to the database and returns the saved order details (including the auto-generated id) with HTTP 201 on success.
-Can be tested end-to-end using Postman — demonstrate at least one successful request and one validation-failure request in screenshots.
STEP 2 · TEST & DEBUG (WITHOUT AI)
-Then, working without AI, test the code and find at least one bug, limitation, or improvement in the AI's solution. Fix it yourself.
SUBMIT All 3 items required
    1 The exact prompt(s) you gave the AI tool.
    2 The AI's original code and your corrected version.
    3 A 3–4 line note explaining what you changed and why the AI's version needed it.

~~>
from django.db import models
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()

# serializer.py
from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()

# view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
class PlaceOrderAPIView(APView):
    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

# model.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
class PlaceOrderAPIView(APIView):
    def post(self,request):
        serializer=OrderSerializer(data=request.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

# url.py
from django.urls import path
from .views import PlaceOrderAPIView
urlpatterns=[
    path("api/orders/place/",PlaceOrderAPIView.as_view())
]

# correct :
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
class PlaceOrderAPIView(APIView):
    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

"""

