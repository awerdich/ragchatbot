from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version('ragchatbot')
except PackageNotFoundError:
    # package is not installed
    __version__ = 'unknown'

def main() -> None:
    print('Hello from the RAG Chatbot project!')
