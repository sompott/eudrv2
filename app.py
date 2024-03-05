from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os
from html import escape
import uuid
from PIL import Image
import tempfile
import base64
app = Flask(__name__)

# Path to the font file
FONT_PATH = "fonts/THSarabun Bold.ttf"
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# def add_signature(pdf, signature_data):
#     signature_filename = str(uuid.uuid4()) + '.png'
#     signature_path = os.path.join(UPLOAD_FOLDER, signature_filename)
#     signature_image_data = base64.b64decode(signature_data.split(',')[1])
#     with open(signature_path, 'wb') as f:
#         f.write(signature_image_data)
#     pdf.add_page()
#     pdf.image(signature_path, x=10, y=10, w=100)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def draw_checkbox(pdf, x, y, size=5, checked=False):
    pdf.rect(x, y, size, size)
    if checked:
        pdf.set_fill_color(0, 0, 0)  # Set fill color to black
        pdf.rect(x + 1, y + 1, size - 2, size - 2, 'F')
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        # signature_data = request.form['signature']
        full_name = escape(request.form['full-name'])
        full_name2 = escape(request.form['full-name2'])
        full_name3 = escape(request.form['full-name3'])
        full_name4 = escape(request.form['full-name4'])
        full_name21 = escape(request.form['full-name21'])
        full_name31 = escape(request.form['full-name31'])
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')
        option4 = request.form.get('option4')
        option41 = request.form.get('full-name41')
        option5 = request.form.get('option5')
        option51 = request.form.get('full-name51')
        option6 = request.form.get('option6')
        option61 = request.form.get('full-name61')
        option7 = request.form.get('option7')
        option71 = request.form.get('full-name71')
        option8 = request.form.get('option8')
        option81 = request.form.get('full-name81')
        name111 = request.form.get('full-name111')
        option9 = request.form.get('option9')
        option10 = request.form.get('option10')
        option11 = request.form.get('option11')
        option12 = request.form.get('option12')
        option13 = request.form.get('option13')
        option14 = request.form.get('option14')
        option15 = request.form.get('option15')
        option16 = request.form.get('option16')
        option17 = request.form.get('option17')
        option18 = request.form.get('option18')
        option19 = request.form.get('option19')
        option20 = request.form.get('option20')
        option21 = request.form.get('option21')
        option22 = request.form.get('option22')
        name199 = request.form.get('full-name199')
        comment = request.form.get('comment')
        photo = request.files['photo']

        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        if photo and allowed_file(photo.filename):
            filename = str(uuid.uuid4()) + '.' + photo.filename.rsplit('.', 1)[1].lower()
            photo_path = os.path.join(UPLOAD_FOLDER, filename)
            photo.save(photo_path)
    
        pdf_file_name = f"{full_name}_{full_name2}.pdf"

        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("THSarabun-Bold", "B", FONT_PATH, uni=True)
        pdf.set_font("THSarabun-Bold", style="B" , size=16)
        pdf.set_font_size(25)
        pdf.cell(200, 10, txt="           แบบสำรวจความถูกต้องตามกฎหมายของ EUDR – ระดับแปลง", ln=True, align='L')
        pdf.cell(200, 10, txt="EUDR Legality Survey - Plot Level", ln=True, align='C')
        pdf.set_font_size(16)
        pdf.cell(200, 12, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="Q.1     ชื่อและนามสกุลหรือบริษัท Name of Farmer / Company: ", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          _________{full_name}_________", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Q.2     เลขรหัสแปลง Plot No__{full_name2}___    ที่อยู่ Address__{full_name21}___", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.3     การใช้ที่ดินในการผลิตยางพารา (ต้นโต) คิดเป็นเปอร์เซ็นต์__{full_name3}__%   อายุต้นยาง__{full_name31}__ปี", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          what percentage of this land used for rubber production (mature trees)?/Age of trees ", ln=True, align='L')
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"Q.4     ปริมาณการผลิตน้ำยางเฉลี่ยต่อเดือนจากแปลงที่ดินนี้ (กก.) คือเท่าใด?", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          What is the monthly average wet production volume from this plot of land (kg)?  ", ln=True, align='L')
        pdf.cell(200, 5, txt=f"          _______{full_name4}____กก./เดือน (kg/month) ", ln=True, align='L')
        # Checkboxes Q5
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="Q.5     เอกสารสิทธิ์ในการใช้ที่ดิน (ประเภทการอนุญาตให้ใช้ที่ดิน)Land rights (Type of permission to use the land)", ln=True)
        if option1:
            pdf.cell(200, 5, txt="          [X] เอกสารสิทธิ์ที่ดิน (ไปที่ข้อ 6) Land documents (Go to Q.6)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] เอกสารสิทธิ์ที่ดิน (ไปที่ข้อ 6) Land documents (Go to Q.6)", ln=True)
        if option2:
            pdf.cell(200, 5, txt="          [X] การใช้ที่ดินได้รับการยอมรับโดยไม่มีเอกสาร (ไปที่ข้อ 7)  Use is recognized without document (Go to Q.7)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] การใช้ที่ดินได้รับการยอมรับโดยไม่มีเอกสาร (ไปที่ข้อ 7)  Use is recognized without document (Go to Q.7)", ln=True)
        if option3:
            pdf.cell(200, 5, txt="          [X] การใช้ที่ดินโดยไม่ได้รับอนุญาต (ไปที่ข้อ 8) Unauthorized use of the land (Go to Q.8)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] การใช้ที่ดินโดยไม่ได้รับอนุญาต (ไปที่ข้อ 8) Unauthorized use of the land (Go to Q.8)", ln=True)
        # Checkboxes Q6
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="Q.6     ประเภทของเอกสารสิทธิ์ type of documentation", ln=True)
        if option4:
            pdf.cell(200, 5, txt=f"          [X] น.ส.4 โฉนด (Nor Sor 4 – Land Deed) เลขที่เอกสาร Doc No__{option41}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] น.ส.4 โฉนด (Nor Sor 4 – Land Deed) เลขที่เอกสาร Doc No", ln=True)
        if option5:
            pdf.cell(200, 5, txt=f"          [X] น.ส.3/น.ส.3 ก. (Nor Sor 3/Nor Sor 3 Gor) เลขที่เอกสาร Doc No___{option51}___", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] น.ส.3/น.ส.3 ก. (Nor Sor 3/Nor Sor 3 Gor) เลขที่เอกสาร Doc No", ln=True)
        if option6:
            pdf.cell(200, 5, txt=f"          [X] ส.ป.ก. (Sor Por Kor) เลขที่เอกสาร Doc No__{option61}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ส.ป.ก. (Sor Por Kor) เลขที่เอกสาร Doc No", ln=True)
        if option7:
            pdf.cell(200, 5, txt=f"          [X] ท.บ.5 (Tor Bor 5) เลขที่เอกสาร Doc No__{option71}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ท.บ.5 (Tor Bor 5) เลขที่เอกสาร Doc No", ln=True)
        if option8:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ Other__{option81}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อื่นๆ Other", ln=True)
        # Checkboxes Q7
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="Q.7     ขอบนิติกรรมการครอบครองที่ดินได้อย่างไร  How is land ownership legally recognized?", ln=True)
        if option9:
            pdf.cell(200, 5, txt="          [X] มีการตีระเบียบหรือทำเค้าโครงสร้างกำหนดเขตแบบดั้งเดิม (เช่น หิน/เสา/ต้นไม้)", ln=True)
            pdf.cell(200, 5, txt="             Physical customary demarcation (e.g. stone/pillar/tree)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] มีการตีระเบียบหรือทำเค้าโครงสร้างกำหนดเขตแบบดั้งเดิม (เช่น หิน/เสา/ต้นไม้)", ln=True)
            pdf.cell(200, 5, txt="          Physical customary demarcation (e.g. stone/pillar/tree)", ln=True)
        if option10:
            pdf.cell(200, 5, txt="          [X] ครอบครองท่านอยู่บนที่ดินมานานนับเป็นเวลากี่ปี(Number of years of long-term occupation)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ครอบครองท่านอยู่บนที่ดินมานานนับเป็นเวลากี่ปี(Number of years of long-term occupation)", ln=True)
        if option11:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ Others:__{name111}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อื่นๆ Others:", ln=True)
        # Checkboxes Q8
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="Q.8     มีพืชชนิดใดบ้างที่ปลูกบนพื้นที่ Are any crops planted on peat?", ln=True)
        if option12:
            pdf.cell(200, 5, txt="          [X] ใช่ Yes", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ใช่ Yes", ln=True)
        if option13:
            pdf.cell(200, 5, txt="          [X] ไม่มี No", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไม่มี No", ln=True)
        pdf.set_font_size(14)
        pdf.cell(200, 25, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="   ติดต่อสอบถาม บริษัทในเครือ บจก.ทองไทยรับเบอร์ ได้ที่อีเมล์ หรือ eudr@tongthai.co.th หรือ (02) 390-2051", ln=True)
        # Checkboxes Q9
        pdf.add_page()
        pdf.set_font_size(16)
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="Q.9     สารเคมีใดต่อไปนี้ถูกนำมาใช้บนที่ดิน? (สามารถเลือกได้มากกว่าหนึ่งตัวเลือก)", ln=True)
        pdf.cell(200, 5, txt="          Which of the following chemicals are used on the land? (multiple options allowed)", ln=True)
        pdf.cell(200, 5, txt=f"", ln=True, align='L')
        if option14:
            pdf.cell(200, 5, txt="          [X] พาราควอต (Paraquat)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] พาราควอต (Paraquat)", ln=True)
        if option15:
            pdf.cell(200, 5, txt="          [X] ไกลโฟเสต/ราวด์อัพ (Glyphosate/Roundup)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไกลโฟเสต/ราวด์อัพ (Glyphosate/Roundup)", ln=True)
        if option16:
            pdf.cell(200, 5, txt="          [X] 2-4D", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] 2-4D", ln=True)           
        if option17:
            pdf.cell(200, 5, txt="          [X] TMTD/ZnO (TZ)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] TMTD/ZnO (TZ)", ln=True)
        if option18:
            pdf.cell(200, 5, txt="          [X] คลอร์พรีฟอส (Chlorpyrifos)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] คลอร์พรีฟอส (Chlorpyrifos)", ln=True)
        if option19:
            pdf.cell(200, 5, txt=f"          [X] อื่นๆ (โปรดระบุ)__{name199}_", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] อื่นๆ (โปรดระบุ)", ln=True)
        if option20:
            pdf.cell(200, 5, txt="          [X] ไม่มีการใช้สารเคมีใดๆ ข้างต้น (Do not use any of the above chemicals)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไม่มีการใช้สารเคมีใดๆ ข้างต้น (Do not use any of the above chemicals)", ln=True)
# Checkboxes Q10
        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="Q.10    ขณะนี้มีข้อพิพาทเรื่องที่ดินกับชนพื้นเมืองหรือกลุ่มพื้นเมืองที่ยังไม่ได้รับการแก้ไขหรือไม่?", ln=True)
        pdf.cell(200, 5, txt="          Are there currently any unresolved land disputes with indigenous or native groups?", ln=True)
        pdf.cell(200, 5, txt=f"", ln=True, align='L')
        if option14:
            pdf.cell(200, 5, txt="          [X] ใช่ (ไปที่ข้อ 10.1) Yes (Go to Q.10.1)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ใช่ (ไปที่ข้อ 10.1) Yes (Go to Q.10.1)", ln=True)
        if option15:
            pdf.cell(200, 5, txt="          [X] ไม่มี No (สิ้นสุดการสำรวจ) No (End of Survey)", ln=True)
        else:
            pdf.cell(200, 5, txt="          [ ] ไม่มี No (สิ้นสุดการสำรวจ) No (End of Survey)", ln=True)

        pdf.cell(200, 7, txt=f"", ln=True, align='L')
        pdf.cell(200, 10, txt="10.1     โปรดอธิบายรายละเอียดเกี่ยวกับข้อพิพาทเรื่องที่ดิน Please elaborate on the land dispute", ln=True)
        pdf.cell(200, 10, txt=f"{comment}", ln=True, align='L')

        pdf.cell(200, 15, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="      วัตถุประสงค์ของการสำรวจนี้คือเพื่อเข้าใจโซลูชันการผลิตยางธรรมชาติและความยั่งยืนของการเกษตรยางพารา ", ln=True)
        pdf.cell(200, 5, txt="การเข้าร่วมในการสำรวจนี้เป็นอิสระ คุณสามารถถอนตัวออกจากการสำรวจได้ตลอดเวลาโดยการติดต่อที่ eudr@tongthai.co.th", ln=True)
        pdf.cell(200, 5, txt="หรือ (02) 390-2051 โดยเราไม่มีความจำเป็นที่จะขายข้อมูลส่วนบุคคลเกี่ยวกับคุณที่เก็บรวบรวมในการสำรวจนี้หรือในทางอื่น", ln=True)
        pdf.cell(200, 5, txt="      The purpose of this survey is to understand the natural rubber supply chain and its ", ln=True)
        pdf.cell(200, 5, txt="sustainability.Your participation in this survey is voluntary.You may withdraw from this survey at", ln=True)
        pdf.cell(200, 5, txt="any time by contacting eudr@tongthai.co.th or (02) 390-2051. We do not sell the Personal Information ", ln=True)
        pdf.cell(200, 5, txt="about you which is collected in connection with this survey or otherwise.", ln=True)
        pdf.cell(200, 10, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="      ข้าพเจ้าได้ให้ข้อมูลทั้งหมดแล้ว และยินยอมให้ใช้และเปิดเผยข้อมูลในการสำรวจนี้ เป็นไปตามกฎหมาย", ln=True)
        pdf.cell(200, 5, txt="คุ้มครองข้อมูลส่วนบุคคล (PDPA)", ln=True)
        pdf.cell(200, 5, txt="      This is to certify that the information I have provided above is to the best of my knowledge ", ln=True)
        pdf.cell(200, 5, txt="and belief.  I have consent to the collection, use and disclosure of this survey based on the Personal", ln=True) 
        pdf.cell(200, 5, txt="Data Protection Act (PDPA). ", ln=True)
        pdf.cell(200, 35, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt=f"____________________", ln=True, align='L')
        pdf.cell(200, 5, txt=f"ลายเซ็น Signature", ln=True, align='L')
        pdf.cell(200, 5, txt=f"วันที่ Date ", ln=True, align='L')
        pdf.set_font_size(14)
        pdf.cell(200, 10, txt=f"", ln=True, align='L')
        pdf.cell(200, 5, txt="   ติดต่อสอบถาม บริษัทในเครือ บจก.ทองไทยรับเบอร์ ได้ที่อีเมล์ หรือ eudr@tongthai.co.th หรือ (02) 390-2051", ln=True)
         
        # if signature_data:
        #     add_signature(pdf, signature_data)

        if photo and allowed_file(photo.filename):
            pdf.add_page()
            pdf.image(photo_path, x=10, y=10, w=190)

        pdf_file_path = os.path.join("pdfs", pdf_file_name)
        pdf.output(pdf_file_path)

        return send_file(pdf_file_path, as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='192.168.0.251', port=5000)
