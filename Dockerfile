FROM ubuntu:latest
RUN echo "Hello from Docker!" > /hello.txt
CMD ["cat", "/hello.txt"] 