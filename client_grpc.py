'''
Client script to send image bytes through gRPC stream.
'''
import argparse
import grpc
import cv2
import base64
import stream_pb2_grpc
import stream_pb2


def image2base64(frame):
    image = cv2.imencode('.jpg', frame)[1]
    image_code = str(base64.b64encode(image))[2:-1]
    return image_code


def generateImageBytes():
    '''
    Yields the images from picture, video or camera.
    '''

    n = 0
    cap = cv2.VideoCapture(args.input)
    ret, frame = cap.read()
    while ret:
        yield stream_pb2.imgReq(number=n, image_data=image2base64(frame))
        n += 1
        ret, frame = cap.read()
    cap.release()


def client_req(host, port):
    print(f"Request host: {host}, port :{port}")
    channel = grpc.insecure_channel(f'{host}:{port}')
    stub = stream_pb2_grpc.StreamImageStub(channel)
    response = stub.imageStreaming(generateImageBytes())
    print(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get the data info')
    parser.add_argument('-ip', '--host', help='IP address of server', default='192.168.130.57')
    parser.add_argument('-p', '--port', help='Port of server', default='24')
    parser.add_argument('-i', '--input', help='image source',
                        default='video.mp4')  # 'rtsp://192.168.130.11/stream0'
    args = parser.parse_args()
    client_req(host=args.host, port=args.port)
