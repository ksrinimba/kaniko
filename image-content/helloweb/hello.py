import http.server
import socketserver

# Define the port number on which the server will listen
PORT = 8000

# Create a custom request handler by inheriting from SimpleHTTPRequestHandler
# This handler will dictate how the server responds to incoming requests.
class MyHandler(http.server.SimpleHTTPRequestHandler):
    """
    A custom HTTP request handler that always responds with "Hello, World!"
    for any GET request.
    """

    def do_GET(self):
        """
        Handle GET requests.
        This method is automatically called by the http.server when a GET request is received.
        """
        # Set the HTTP response status code to 200 (OK)
        self.send_response(200)

        # Set the HTTP header for Content-type to indicate that the response is plain text
        self.send_header("Content-type", "text/plain")

        # End the headers section of the HTTP response
        self.end_headers()

        # Define the message to send back
        message = "Hello, World!"

        # Encode the message to bytes (HTTP responses must be bytes)
        self.wfile.write(bytes(message, "utf-8"))

        print(f"[{self.date_time_string()}] Handled GET request from {self.client_address[0]}:{self.client_address[1]}")
        print(f"  Path: {self.path}")
        print(f"  Response: '{message}'")


# Create a TCP server that uses our custom handler
# socketserver.TCPServer creates a server instance.
# The `with` statement ensures the server is properly closed when done.
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    print(f"You can access the server at http://localhost:{PORT}/")
    print("Press Ctrl+C to stop the server.")

    # Activate the server; this will keep running until interrupted (e.g., Ctrl+C)
    # The server will handle requests forever.
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
        httpd.shutdown()  # Gracefully shut down the server
