# import tomli_w
# import socket
# import time

# hostname = "titan.picoctf.net"
# port = 62026

# values = {}
# for i in range(1, 201):
#     # start netcat connection
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect((hostname, port))
#     print("Connected Successfully")

#     char = chr(i)
#     # send netcat message
#     sock.sendall(bytes(char, encoding="utf-8"))
#     time.sleep(0.5)
#     # sock.shutdown(socket.SHUT_WR)

#     # res = ""
#     while True:
#         data = sock.recv(1024)
#         if not data:
#             break
#         # res += data.decode()


#     values[i] = res
#     print(res)
#     print(f"{i}/{200} messages sent")

# with open("values.toml", 'wb') as f:
#     tomli_w.dump({"values": values}, f)
