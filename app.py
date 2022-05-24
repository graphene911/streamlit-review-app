from ast import Pass
from prompt_toolkit import PromptSession
import streamlit as st
from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
my_stopwords = stopwords.words('english')


def message_cleaning(sentence) :
  # 1. 구두점 제거
  Test_punc_removed = [char for char in sentence if char not in string.punctuation ]
  # 2. 각 글자들을 하나의 문자열로 합친다.
  Test_punc_removed_join = ''.join(Test_punc_removed)
  # 3. 문자열에 불용어가 포함되어있는지 확인해서, 불용어 제거한다.
  Test_punc_removed_join_clean = [word for word in Test_punc_removed_join.split() if word.lower() not in my_stopwords ]
  # 4. 결과로 남은 단어들만 리턴한다.
  return Test_punc_removed_join_clean





def main() :
    st.title('리뷰 긍정 부정 예측 앱')

    menu = ['Home', 'EDA', 'ML']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()






if __name__ == '__main__' :
    main()