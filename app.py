from flask import Flask, render_template ,request ,session, url_for
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)

app.config['SECRET_KEY'] = 'InCumaContohDoangBang2002'


@app.route("/", methods = ["GET", "POST"])
def home():
	if request.method == 'POST':
		session['link'] = request.form.get('url')
		try:
			url =  YouTube(session['link'])
			url.check_availability()
		except:
			return "Err!!!"
		return render_template('download.html', url=url)
	return render_template('index.html')

@app.route("/download", methods = ["GET", "POST"])
def downloadbang():
	if request.method == 'POST':
		buffer = BytesIO()
		url = YouTube(session['link'])
		itag = request.form.get('lols')
		video = url.streams.get_by_itag(22)
		video.download()
		video.stream_to_buffer(buffer)
		buffer.seek(0)
		return send_file(buffer, as_atatchment=True, download_name='bahagia-selalu.mp4', mimetype="video/mp4")
	return redirect(url_for('home'))
if __name__ == "__main__":

    app.run(debug=1)