from app import app_instance,  sio

if __name__ == "__main__":
    sio.run(app_instance, debug=True )