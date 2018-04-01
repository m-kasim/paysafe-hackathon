# Team NEXT
Paysafe Hackathon 2018

# Architecture
- Backend:    Python (Django) + Postgre
- AI module:  TensorFlow and ImageNET
- Server:     AWS GPU instance (16 x CPU, 32 GB RAM)

# Product splash:
![Multiple products image recognition](https://raw.githubusercontent.com/PaysafeHackathon2018/next/master/presentation/product_splash.png)

# Product description:
NEXT is a white-label mobile POS product for small and medium businesses in developing countries.

Using our web API merchants are able to integrate in their products instant image recognition.

Using image recognition we are able to instantly recognize items in the user basket, calculate their price
and eliminate the process of marking products one by one by cashiers.

The final result appears on the screen of the cashier's mobile app and he/she is able to correct any items (only if needed).

# Benefits
NEXT eliminates the need to mark retail products one by one.
It also serves as a total replacement for the POS hardware, by replacing it with a client and server application.
This reduces the initial investment cost (of purchasing a POS hardware) for small merchants and provides them the
opportunity to carry out their business only via the NEXT mobile API and their mobile phones.

# Dataset:
I am using a data set of the popular snack "KitKat" which has a classic and white cholocate variations.
- KitKat Classic (30 training examples, manually created and optimized)
- KitKat White   (30 training examples, manually created and optimized)

# Training:
The training takes about 5-10 minutes on a machine with no GPU.
Using this trained model we are able to recognize the product's subbrand variations correctly with our trained Neural Network.

![TensorFlow results](
https://github.com/PaysafeHackathon2018/next/raw/master/presentation/product_detect.png)


# Author
Murad Kasim

mkasim@uni-sofia.bg

FMI, Sofia University
