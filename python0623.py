# pip install pywebview
from pathlib import Path
import webview
BASE_PATH = Path(__file__).parent
NOTE_PASS = BASE_PATH / "python" / "memo.txt"

class MemoApi:
    def __init__(self):
        pass

    def save_memo(self, text):
        NOTE_PASS.write_text(text,encoding="utf-8")
        return {"status": "save", "path": str(NOTE_PASS)}
    def load_memo(self):
        return {"text": NOTE_PASS.read_text(encoding="utf-8")}

    def set_memo(self, memo):
        self.memo = memo
        return "Memo updated successfully!"
    
from pathlib import Path

def main():
    webview.create_window(
        "simple text",
        url = Path("python/text.html").resolve().as_uri(),
        js_api=MemoApi(),
        width=640,
        height=520,
        resizable=True
        )
    webview.start()

if __name__ == "__main__":
    main()    