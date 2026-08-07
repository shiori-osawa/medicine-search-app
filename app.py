from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
import markdown
load_dotenv()

app = Flask(__name__)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #POSTの処理（検索ボタンを押したときだけ実行）
        medicine=request.form["medicine"].strip()
        condition=request.form.getlist("condition")
        current_medicine=request.form.get("current_medicine").strip()

        if medicine == "":
            return render_template(
                "index.html",
                message="薬名を入力してください。",
                medicine=medicine,
                condition=condition,
                current_medicine=current_medicine
            )
        elif len(medicine) > 30:
            return render_template(
                "index.html",
                message="薬名は30文字以内で入力してください。",
                medicine=medicine,
                condition=condition,
                current_medicine=current_medicine
            )
        
        prompt=f"""
        薬名は{medicine}です。
        """
        if condition:
            prompt+=f"""
            \n患者情報は{','.join(condition)}です。
            """

        if current_medicine != "":
            prompt += f"""
            現在服薬している薬は{current_medicine}です。
        """
        prompt+=f"""
        患者情報を考慮して、{medicine}の代替薬を探し、
        以下の項目ごとにわかりやすく説明してください。
        ・代替薬がある場合はその候補
        ・当該薬と代替薬の相違点
        ・代替薬の適応症
        ・代替薬の主な副作用、禁忌薬、禁忌病態
        ・患者情報を考慮した注意点
        
        
        """
        

        response = client.responses.create(
        model="gpt-5.5",
        input=prompt,
        max_output_tokens=1200
        )
        answer= markdown.markdown(response.output_text)

        return render_template(
            "index.html.",
            answer=answer,
            medicine=medicine,
            condition=condition,
            current_medicine=current_medicine
        )

    return render_template("index.html")#GETの場合は画面が表示(最初http://127.0.0.1:5000/に入ったとき)
    
    
if __name__ == "__main__":#pythonファイルがたくさんあってapp.py以外のファイルを読み込む必要がある場合に書く必要がある
   # app.run(debug=True)
   app.run(host="0.0.0.0", port=5000, debug=True)