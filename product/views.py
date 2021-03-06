from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import status
from .models import Product, Order,OrderItem,ShippingAddress
from .serializers import ProductSerializer,OrderSerializer
from datetime import datetime

# Create your views here.

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product,many=False)

    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data

    orderItems = data["orderItems"]

    if orderItems and len(orderItems) == 0:
        return Response({"detail":"No Order Item"},status=status.HTTP_400_BAD_REQUEST)
    else:
        # Create Order
        order = Order.objects.create(
            user = user,
            paymentMethod = data["paymentMethod"],
            taxPrice = data["taxPrice"],
            shippingPrice = data["shippingPrice"],
            totalPrice = data["totalPrice"],          
        )

        # Create Shipping
        shipping = ShippingAddress.objects.create(
            order = order,
            address = data["shippingAddress"]["address"],
            city = data["shippingAddress"]["city"],
            postalCode = data["shippingAddress"]["postalCode"],
            country = data["shippingAddress"]["country"]          
        )

        # Create Order Item
        for item in orderItems:
            product = Product.objects.get(_id=item['product'])

            orderItem = OrderItem.objects.create(
                product = product,
                order = order,
                name = product.name,
                quantity = item["qty"],
                price = item["price"],
                image = product.image.url            
            )

            product.countInStock -= orderItem.quantity
            product.save()

        serializer = OrderSerializer(order,many=False)
        return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getOrderById(request,pk):
    user = request.user
    order = Order.objects.get(_id=pk)

    try:

        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order,many=False)
            return Response(serializer.data)
        else:
            return Response({'detail':'Not Authorised to view this order'},status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"detail":"Order doesn't exist"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request,pk):
    user = request.user
    order = Order.objects.get(_id = pk)

    order.isPaid = True
    order.paidAt = datetime.now()

    order.save()
    
    return Response("Order is paid")
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orderList(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders,many=True)

    return Response(serializer.data)
