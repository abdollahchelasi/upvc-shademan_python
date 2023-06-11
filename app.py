import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu

st.set_page_config(page_title="دکوراسیـون شادمان - رمکان", page_icon="icon.png")

st.title("دکوراسیـون شادمان  - رمکان")




con=sqlite3.connect('sql/db.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS pics(id TEXT, img BLOB, note TEXT)')




selected = option_menu (
    menu_title=None,
    options=["تماس با مدیریت","ورود ادمین","صفحه اصلی"],
    icons=["envelope","book","house" ],
    menu_icon="cast",
    default_index=2,
    orientation="horizontal",
    styles={

        
        "nav-link":{
            'font-family': 'Courier New' 'Courier' 'monospace'
        },
        
    }
)






col1,col2=st.columns(2)

with col1: 
    st.write("""
* تولیدی درب و پنجره UPVC نوین ترک
 * فروش و نصب PVC
 * طراحی و ساخت و اجرای انواع سایبان PVC
""")
    st.subheader("فروش بصورت نقد و اقساط فقط با چک")
        

with col2:
    st.video("upvc.mp4")
    
    
    

      
 
 
 


with open('c.css') as f:
    st.markdown(f'<style>{f.read()}</style>' ,unsafe_allow_html=True)










if selected == "ورود ادمین":
    
    

	username = st.text_input(label="نام کاربری",placeholder="Username")
	password = st.text_input(label="پسورد",placeholder="password",type="password")
	btnLogin = st.button("ورود")

	if username == "ahmad" and password == "shademan":
        
		st.success("خوش آمدی احمد شادمان")
        
		selected = option_menu(options=["پست های ادمین"],
        menu_title=""

        
        
        )
		
	elif username or password == "admin":
		st.error("لطفا درست وارد کنید")



 
 
  
 


 

if selected == "پست های ادمین":

    st.success("توجه : لطفا با اضافه کردن محصول محصولات خود رو کامل پر کنید (عکس محصول , کد محصول , نام محصول) این ها نباید خالی باشد")
    st.error("هشدار : کد و نام محصولات شما نباید مثل محصولات دیگه ای که اضافه میکنید باشد. کد محصولات رو با اعداد انگلیسی و از شماره بالا به پایین شروع کنید . مانند : ( از 999 شروع کنید به پایین) ")
    
    if st.button('اضافه کردن محصول'):
        cur.execute('INSERT INTO pics(id, img, note) VALUES(?,?,?)', ('', '', ''))
        con.commit()
     
    
   

    st.write('---')

    for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
        with st.form(f'ID-{row[0]}',clear_on_submit=True):
            imgcol, notecol = st.columns([3, 2])
            id=notecol.text_input('کد محصول', row[1])
            note=notecol.text_area('نام محصول', row[3])
            if row[2]:
                img=row[2] 
                imgcol.image(row[2]) 
            file=imgcol.file_uploader('تصاویر', ['png', 'jpg', 'gif','jpeg', 'bmp'])
            if file:  
                img=file.read()
            if notecol.form_submit_button('ذخیره محصول'):
                
                cur.execute(
                    'UPDATE pics SET id=?, img=?, note=? WHERE id=?;', 
                    (id, img, note, str(row[1]))
                    )
            
                con.commit()
                st.experimental_rerun()
             
            
                
            if notecol.form_submit_button("حذف محصول"):
                cur.execute(f'''DELETE FROM pics WHERE rowid="{row[0]}";''')
                con.commit()
                st.experimental_rerun()

        


if selected == "صفحه اصلی":



     


     

     

     for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
        # with st.form(f'ID-{row[0]}', clear_on_submit=True):
        st.write("---")
        imgcol, notecol = st.columns([3, 2])
        # id=notecol.text_input('id', row[1])
        id=notecol.text_input('کد محصول', row[1])
        note=notecol.text_area('اسم محصول', row[3])
        if row[2]:
            img=row[2]
            imgcol.image(row[2])

            

        
            
            
if selected == "تماس با مدیریت":
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image("ahmad.jpg")
        st.write(" احمد شادمان")
    with col2:
        
        st.error("شماره تماس:09173630491")
        st.success("شماره واتساپ:09353630491")
        st.warning("شماره تماس دفتر : 09175768357")
        
            
    with col3:
        st.write(""" آدرس : جزیــره ي قشم،روستاي باغبالـا_فروشگاه PVC و سایبان شادمان """)
        st.write("شعبه دوم : جزیره قشم - شهر رمکان جنب بانک ملت , تولیدی درب و پنجره UPVC نوین ترک ")
        st.write( "ساعت کاری و پاسخ دهی : صبح ساعت 9 الی 12:30 و عصر ساعت 16 الی 21:00 ")

st.write("---")

st.markdown("[طراح و برنامه نویس : عبداالله چلاسی](https://abdollahchelasi.iran.liara.run)")
            
    

st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)