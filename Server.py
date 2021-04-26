# import socket
# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 8888        # Port to listen on (non-privileged ports are > 1023)

# def morse(word):
#     global output
#     morze_alphabet = (
#     " .- ", " -... ", " -.-. ", " -.. ", " . ", " ..-. ", " --. ", " .... ", " .. ", " .--- ", " -.- ", " .-.. ",
#     " -- ",
#     " -. ",
#     " --- ", " .--. ", " --.- ", " .-. ", " ... ", " - ", " ..- ", " ...- ", " .-- ", " -..- ", " -.-- ", " --.. ", " / ")
#     alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
#             "w", "x", "y", "z", " ")
#     a = []
#     word = str(word, 'UTF-8')
#     splited = list(word.lower())
#     for letters in range(len(splited)):
#         a.append(morze_alphabet[alphabet.index(splited[letters])])
#         output = ''.join(a)
#     return output.encode()
#
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             conn.sendall(morse(data))


from flask import Flask, render_template, request
import winsound
import time

app = Flask(__name__)


def play_coded_message(message):
    for i in message:
        if i == '.':
            winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
            time.sleep(0.1)
        elif i == '-':
            winsound.Beep(1000, 600)  # Beep at 1000 Hz for 100 ms
            time.sleep(0.1)
        elif i == ' ':
            pass



def morse(message):
    global output
    morze_alphabet = (
        " .- ", " -... ", " -.-. ", " -.. ", " . ", " ..-. ", " --. ", " .... ", " .. ", " .--- ", " -.- ", " .-.. ",
        " -- ",
        " -. ",
        " --- ", " .--. ", " --.- ", " .-. ", " ... ", " - ", " ..- ", " ...- ", " .-- ", " -..- ", " -.-- ", " --.. ",
        " / ")
    alphabet = (
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", " ")
    a = []
    # message = str(message, 'UTF-8')
    splited = list(message.lower())
    for letters in range(len(splited)):
        a.append(morze_alphabet[alphabet.index(splited[letters])])
        output = ''.join(a)
    # return output.encode()
    # play_coded_message(output)
    return output


@app.route('/')
def index():
    return render_template('test.html')


@app.route('/coder', methods=['POST'])
def hello():
    message = request.form['message']
    return 'Your message %s <br/>Your translation %s <br/> Here is your sound <a href="/sound">Sound</a> <br/><a href="/">Back Home</a>' % (
        message, morse(message))


# @app.route('/sound')
# def play_coded_message(message):
#     message = request.form['message']
#     for i in message:
#         if i == '.':
#             winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
#             time.sleep(0.1)
#         elif i == '-':
#             winsound.Beep(1000, 600)  # Beep at 1000 Hz for 100 ms
#             time.sleep(0.1)
#         elif i == ' ':
#             pass
#         return 'Your Sound played<br/>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)
