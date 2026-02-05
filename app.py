from flask import Flask, render_template, request, send_file, redirect, url_for
from count_name import count_names_from_content
import io
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        names_text = ""
        # Handle file upload
        if "file" in request.files and request.files["file"].filename != "":
            file = request.files["file"]
            names_text = file.read().decode("utf-8")
        # Handle text area input
        elif "names_text" in request.form:
            names_text = request.form["names_text"]

        if names_text.strip():
            result = count_names_from_content(names_text)

    return render_template("index.html", result=result)


@app.route("/download", methods=["POST"])
def download():
    unique_names = request.form.get("unique_names", "").splitlines()
    if not unique_names:
        return redirect(url_for("index"))

    # Create an in-memory file
    proxy = io.StringIO()
    for name in unique_names:
        proxy.write(name + "\n")

    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode("utf-8"))
    mem.seek(0)
    proxy.close()

    return send_file(
        mem, as_attachment=True, download_name="unique_names.txt", mimetype="text/plain"
    )


if __name__ == "__main__":
    import webbrowser
    from threading import Timer

    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/")

    Timer(1, open_browser).start()
    app.run(debug=True)
