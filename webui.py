from flask import Flask, render_template, request, redirect, url_for, flash, Response, g
from arxiv_translate import arxiv_translate
# 引入队列
from queue import Queue
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

progress_info = Queue()
def progress_callback(message):
    global progress_info
    print(message)  # 打印到控制台
    progress_info.put(f"data: {message}\n\n")

def stream_generator():
    while True:
        if not progress_info.empty():
            msg = progress_info.get()
            if msg == "data: Completed.\n\n":
                yield msg
                break
            yield msg
        else:
            time.sleep(5)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        arxiv_id = request.form.get('arxiv_id')
        assert arxiv_id, 'arXiv ID is required.'
        api_key = request.form.get('api_key')
        split_level = request.form.get('split_level', 'section')

        if not api_key:
            flash('API key is required.')
            return redirect(url_for('index'))

        progress_callback("Starting translation...")

        try:
            result = arxiv_translate(arxiv_id, api_key, split_level, progress_callback)
            progress_callback("Completed.")
            flash(result)
        except Exception as e:
            flash(f'An error occurred: {str(e)}')

        return render_template('index.html')

    return render_template('index.html')

@app.route('/stream')
def stream():

    return Response(stream_generator(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)