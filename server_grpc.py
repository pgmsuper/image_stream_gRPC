'''
Server script to receive image bytes in stream.
'''
from concurrent import futures
import cv2
import grpc
import numpy
import base64
import argparse
import stream_pb2
import stream_pb2_grpc


class StreamImage(stream_pb2_grpc.StreamImageServicer):

    def imageStreaming(self, image_iterator, context):
        '''
        Receive image streams.
        Args:
            image_iterator : iterator object containing base64 image data.
        base64 image data convert to image.
        '''
        print("play start")
        for data in image_iterator:
            print(data.number)
            image = self.base642image(data.image_data)
            cv2.imshow("image show window", image)
            cv2.waitKey(1)
        cv2.destroyAllWindows()
        print("play done")
        return stream_pb2.imgResponse(response="play done")

    def base642image(self, base64_data):
        image_data = base64.b64decode(base64_data)
        image_array = numpy.frombuffer(image_data, numpy.uint8)
        img = cv2.imdecode(image_array, cv2.COLOR_RGB2BGR)
        return img


def serve(host, port):
    print(f'server host: {host}, port: {port}')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stream_pb2_grpc.add_StreamImageServicer_to_server(StreamImage(), server)
    server.add_insecure_port(f'{host}:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the data info')
    parser.add_argument('-ip', '--host', help='IP address of server', default='192.168.130.57')
    parser.add_argument('-p', '--port', help='Port', default='24')
    args = parser.parse_args()

    serve(host=args.host, port=args.port)
