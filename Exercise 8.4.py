def make_shirt(size='large', message='I love Python'):
    print(f"Shirt size: {size.title()}, Message: {message}")

# Large Shirt with default message
make_shirt()

# Medium Shirt with default message
make_shirt(size='medium')

# Custom Shirt with different message
make_shirt(size='small', message='Keep Calm and Code On')
