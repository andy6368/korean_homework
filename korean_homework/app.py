#app.py

from flask import Flask, render_template, request

ONSET_START_LETTER = 4352
NUCLEUS_START_LETTER = 4449
CODA_START_LETTER = 4520

JAMO_START_LETTER = 44032
JAMO_END_LETTER = 55203
JAMO_CYCLE = 588



def isHangul(ch): #한글인지 아닌지
    JAMO_START_LETTER = 44032
    JAMO_END_LETTER = 55203
    return ord(ch) >= JAMO_START_LETTER and ord(ch) <= JAMO_END_LETTER

def getOnset(ch): #초성 추출
    return chr(int(((ord(ch) - JAMO_START_LETTER) / 28) / 21 + ONSET_START_LETTER))

def getNucleus(ch): #중성 추출
    return chr(int(((ord(ch) - JAMO_START_LETTER) / 28) % 21 + NUCLEUS_START_LETTER))

def getCoda(ch): #종성 추출
    return chr(int((ord(ch) - JAMO_START_LETTER) % 28 + CODA_START_LETTER -1))

def wtr_BD(a):
    result = ""
    if len(a) > 1:
        for i in range(0, len(a)-1):
            byeondong_batcim = ""
            byeondong_cho = ""
            yeoneum = 0
            
            if ord(getOnset(a[i+1])) == 4363:       #연음
                if ord(getCoda(a[i])) == 4522:
                    byeondong_batcim = "ㄱ"
                    byeondong_cho = "ㅅ"
                elif ord(getCoda(a[i])) == 4524:
                    byeondong_batcim = "ㄴ"
                    byeondong_cho = "ㅈ"
                elif ord(getCoda(a[i])) == 4525:
                    byeondong_batcim = "ㄴ"
                elif ord(getCoda(a[i])) == 4528:
                    byeondong_batcim = "ㄹ"
                    byeondong_cho = "ㄱ"
                elif ord(getCoda(a[i])) == 4529:
                    byeondong_batcim = "ㄹ"
                    byeondong_cho = "ㅁ"
                elif ord(getCoda(a[i])) == 4530:
                    byeondong_batcim = "ㄹ"
                    byeondong_cho = "ㅂ"
                elif ord(getCoda(a[i])) == 4531:
                    byeondong_batcim = "ㄹ"
                    byeondong_cho = "ㅅ"
                elif ord(getCoda(a[i])) == 4532:
                    byeondong_batcim = "ㄹ"
                    byeondong_cho = "ㅌ"
                elif ord(getCoda(a[i])) == 4533:
                    byeondong_batcim = "ㄹ"
                    byeondong_cho = "ㅍ"
                elif ord(getCoda(a[i])) == 4534:
                    byeondong_batcim = "ㄹ"
                elif ord(getCoda(a[i])) == 4537:
                    byeondong_batcim = "ㅂ"
                    byeondong_cho = "ㅅ"
                yeoneum = 1
            else:
                if ord(getCoda(a[i])) == 4522:         #자음군 단순화
                    byeondong_batcim = "ㄱ"
                    result = result + '자음군 단순화로 {}이 ㄱ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4524:
                    byeondong_batcim = "ㄴ"
                    result = result + '자음군 단순화로 {}이 ㄴ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4525:
                    byeondong_batcim = "ㄴ"
                    result = result + '자음군 단순화로 {}이 ㄴ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4528:
                    if ord(getOnset(a[i+1])) == 4355:
                        byeondong_batcim = "ㄱ"
                        result = result + '자음군 단순화로 {}이 ㄱ으로 발음\n'.format(getCoda(a[i]))
                    else:
                        byeondong_batcim = "ㄹ"
                        result = result + '자음군 단순화로 {}이 ㄹ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4529:
                    byeondong_batcim = "ㅁ"
                    result = result + '자음군 단순화로 {}이 ㅁ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4530:
                    if a[i] == "밟":
                        byeondong_batcim = "ㅂ"
                        result = result + '자음군 단순화로 {}이 ㅂ으로 발음\n'.format(getCoda(a[i]))
                    elif a[i] == "넓":
                        if a[i+1] == "죽":
                            byeondong_batcim = "ㅂ"
                            result = result + '자음군 단순화로 {}이 ㅂ으로 발음\n'.format(getCoda(a[i]))
                        elif a[i+1] == "둥":
                            byeondong_batcim = "ㅂ"
                            result = result + '자음군 단순화로 {}이 ㅂ으로 발음\n'.format(getCoda(a[i]))
                        elif a[i+1] == "데":
                            byeondong_batcim = "ㅂ"
                            result = result + '자음군 단순화로 {}이 ㅂ으로 발음\n'.format(getCoda(a[i]))
                        else:
                            byeondong_batcim = "ㄹ"
                            result = result + '자음군 단순화로 {}이 ㄹ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4531:
                    byeondong_batcim = "ㄹ"
                    result = result + '자음군 단순화로 {}이 ㄹ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4532:
                    byeondong_batcim = "ㄹ"
                    result = result + '자음군 단순화로 {}이 ㄹ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4533:
                    byeondong_batcim = "ㅂ"
                    result = result + '자음군 단순화로 {}이 ㅂ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4534:
                    byeondong_batcim = "ㄹ"
                    result = result + '자음군 단순화로 {}이 ㄹ으로 발음\n'.format(getCoda(a[i]))
                if ord(getCoda(a[i])) == 4537:
                    byeondong_batcim = "ㅂ"
                    result = result + '자음군 단순화로 {}이 ㅂ으로 발음\n'.format(getCoda(a[i]))
                
            if ord(getOnset(a[i+1])) == 4370 and ord(getCoda(a[i])) == 4541:
                result = result + getCoda(a[i])+"과 "+getOnset(a[i+1])+"에서 "+"자음 축약 현상 일어남\n"
            if ord(getCoda(a[i])) == 4520:
                byeondong_batcim = 'ㄱ'
            elif ord(getCoda(a[i])) == 4521:
                byeondong_batcim = 'ㄱ'
                result = result + '음절의 끝소리 규칙으로 {}이 ㄱ으로 발음\n'.format(getCoda(a[i]))
            elif ord(getCoda(a[i])) == 4543:
                byeondong_batcim = 'ㄱ'
                result = result + '음절의 끝소리 규칙으로 {}이 ㄱ으로 발음\n'.format(getCoda(a[i]))
            elif ord(getCoda(a[i])) == 4523:
                byeondong_batcim = 'ㄴ'
            elif ord(getCoda(a[i])) == 4526:
                byeondong_batcim = 'ㄷ'
            elif ord(getCoda(a[i])) == 4538:
                byeondong_batcim = 'ㄷ'
                result = result + '음절의 끝소리 규칙으로 {}이 ㄷ으로 발음\n'.format(getCoda(a[i]))
            elif ord(getCoda(a[i])) == 4539:
                byeondong_batcim = 'ㄷ'
                result = result + '음절의 끝소리 규칙으로 {}이 ㄷ으로 발음\n'.format(getCoda(a[i]))
            elif ord(getCoda(a[i])) == 4541:
                byeondong_batcim = 'ㄷ'
                result = result + '음절의 끝소리 규칙으로 {}이 ㄷ으로 발음\n'.format(getCoda(a[i]))
            elif ord(getCoda(a[i])) == 4542:
                byeondong_batcim = 'ㄷ'
                result = result + '음절의 끝소리 규칙으로 {}이 ㄷ으로 발음\n'.format(getCoda(a[i]))
            elif ord(getCoda(a[i])) == 4544:
                byeondong_batcim = 'ㄷ'
                result = result + '음절의 끝소리 규칙으로 {}이 ㄷ으로 발음\n'.format(getCoda(a[i]))
            elif ord(getCoda(a[i])) == 4527:
                byeondong_batcim = 'ㄹ'
            elif ord(getCoda(a[i])) == 4535:
                byeondong_batcim = 'ㅁ'
            elif ord(getCoda(a[i])) == 4536:
                byeondong_batcim = 'ㅂ'
            elif ord(getCoda(a[i])) == 4545:
                byeondong_batcim = 'ㅂ'
                result = result + '음절의 끝소리 규칙으로 {}이 ㅂ으로 발음\n'.format(getCoda(a[i]))
            elif ord(getCoda(a[i])) == 4540:
                byeondong_batcim = 'ㅇ'
            elif ord(getCoda(a[i])) == 4546:
                byeondong_batcim = 'ㄷ'
                result = result + '음절의 끝소리 규칙으로 {}이 ㄷ으로 발음\n'.format(getCoda(a[i]))
        
        
        
        
            if byeondong_batcim == 'ㄹ' and ord(getOnset(a[i+1])) == 4354:            #부터 유음화
                result = result + byeondong_batcim+"과 "+getOnset(a[i+1])+"에서 "+"유음화 현상 일어남\n"
            elif byeondong_batcim == 'ㄴ' and ord(getOnset(a[i+1])) == 4357:
                result = result + byeondong_batcim+"과 "+getOnset(a[i+1])+"에서 "+"유음화 현상 일어남\n"



            if byeondong_batcim == 'ㄱ' and ord(getOnset(a[i+1])) == 4354:            #부터 비음화
                result = result + byeondong_batcim+"과 "+getOnset(a[i+1])+"에서 "+"비음화 현상 일어남\n"
            elif byeondong_batcim == 'ㄱ' and ord(getOnset(a[i+1])) == 4358:            
                result = result + byeondong_batcim+"과 "+getOnset(a[i+1])+"에서 "+"비음화 현상 일어남\n"
            elif byeondong_batcim == 'ㄷ' and ord(getOnset(a[i+1])) == 4354:            
                result = result + byeondong_batcim+"과 "+getOnset(a[i+1])+"에서 "+"비음화 현상 일어남\n"
            elif byeondong_batcim == 'ㄷ' and ord(getOnset(a[i+1])) == 4358:            
                result = result + byeondong_batcim+"과 "+getOnset(a[i+1])+"에서 "+"비음화 현상 일어남\n"
            elif byeondong_batcim == 'ㅂ' and ord(getOnset(a[i+1])) == 4354:            
                result = result + byeondong_batcim+"과 "+getOnset(a[i+1])+"에서 "+"비음화 현상 일어남\n"
            elif byeondong_batcim == 'ㅂ' and ord(getOnset(a[i+1])) == 4358:            
                result = result + byeondong_batcim+"과 "+getOnset(a[i+1])+"에서 "+"비음화 현상 일어남\n"
            

            
            if ord(getCoda(a[i])) == 4546 and ord(getOnset(a[i+1])) == 4352:
                byeondong_cho = "ㅋ"
                result = result + getCoda(a[i])+"과 ",getOnset(a[i+1])+"에서 "+"자음 축약 현상 일어남\n"
            elif ord(getCoda(a[i])) == 4546 and ord(getOnset(a[i+1])) == 4355:
                byeondong_cho = "ㅌ"
                result = result + getCoda(a[i])+"과 "+getOnset(a[i+1])+"에서 "+"자음 축약 현상 일어남\n"
            elif ord(getCoda(a[i])) == 4546 and ord(getOnset(a[i+1])) == 4359:
                byeondong_cho = "ㅍ"
                result = result + getCoda(a[i])+"과 "+getOnset(a[i+1])+"에서 "+"자음 축약 현상 일어남\n"
            elif ord(getCoda(a[i])) == 4546 and ord(getOnset(a[i+1])) == 4364:
                byeondong_cho = "ㅊ"
                result = result + getCoda(a[i])+"과 "+getOnset(a[i+1])+"에서 "+"자음 축약 현상 일어남\n" #까지 ㅎ이 종성
            elif ord(getOnset(a[i+1])) == 4370 and byeondong_batcim == 'ㅂ':
                byeondong_cho = "ㅍ"
                result = result + getCoda(a[i])+"과 "+getOnset(a[i+1])+"에서 "+"자음 축약 현상 일어남\n"
            if ord(getCoda(a[i])) != 4541:
                if ord(getOnset(a[i+1])) == 4370 and byeondong_batcim == 'ㄷ':
                    if ord(getOnset(a[i+1])) == 4363:
                        byeondong_cho = "ㅌ"
                    result = result + getCoda(a[i])+"과 "+getOnset(a[i+1])+"에서 "+"자음 축약 현상 일어남\n"
            elif ord(getOnset(a[i+1])) == 4370 and byeondong_batcim == 'ㄱ':
                byeondong_cho = "ㅋ"
                result = result + getCoda(a[i])+"과 "+getOnset(a[i+1])+"에서 "+"자음 축약 현상 일어남\n"


            if a[i] != " ":         #구개음화
                if byeondong_cho == "ㄷ":
                    if ord(getNucleus(a[i+1])) == 4469 or ord(getNucleus(a[i+1])) == 4451:
                        result = result + '구개음화로 {}이 ㅈ으로 발음\n'.format(byeondong_cho)
                    elif ord(getNucleus(a[i+1])) == 4455 or ord(getNucleus(a[i+1])) == 4461:
                        result = result + '구개음화로 {}이 ㅈ으로 발음\n'.format(byeondong_cho)
                    elif ord(getNucleus(a[i+1])) == 4466 or ord(getNucleus(a[i+1])) == 4456:
                        result = result + '구개음화로 {}이 ㅈ으로 발음\n'.format(byeondong_cho)
                    elif ord(getNucleus(a[i+1])) == 4452:
                        result = result + '구개음화로 {}이 ㅈ으로 발음\n'.format(byeondong_cho)
                if byeondong_cho == "ㅌ":
                    if ord(getNucleus(a[i+1])) == 4469 or ord(getNucleus(a[i+1])) == 4451:
                        result = result + '구개음화로 {}이 ㅊ으로 발음\n'.format(byeondong_cho)
                    elif ord(getNucleus(a[i+1])) == 4455 or ord(getNucleus(a[i+1])) == 4461:
                        result = result + '구개음화로 {}이 ㅊ으로 발음\n'.format(byeondong_cho)
                    elif ord(getNucleus(a[i+1])) == 4466 or ord(getNucleus(a[i+1])) == 4456:
                        result = result + '구개음화로 {}이 ㅊ으로 발음\n'.format(byeondong_cho)
                    elif ord(getNucleus(a[i+1])) == 4452:
                        result = result + '구개음화로 {}이 ㅊ으로 발음\n'.format(byeondong_cho)
                        
            if ord(getCoda(a[i])) == 4521 or 4526 or 4536 or byeondong_batchim == "ㄱ" or "ㄷ" or "ㅂ":    #된소리되기
                    if ord(getOnset(a[i+1])) == 4352 or byeondong_cho == "ㄱ":
                        result = result + '된소리되기로 ㄱ이 ㄲ으로 발음\n'
                    elif ord(getOnset(a[i+1])) == 4355 or byeondong_cho == "ㄷ":
                        result = result + '된소리되기로 ㄷ이 ㄸ으로 발음\n'
                    elif ord(getOnset(a[i+1])) == 4359 or byeondong_cho == "ㅂ":
                        result = result + '된소리되기로 ㅂ이 ㅃ으로 발음\n'
                    elif ord(getOnset(a[i+1])) == 4361 or byeondong_cho == "ㅅ":
                        result = result + '된소리되기로 ㅅ이 ㅆ으로 발음\n'
                    elif ord(getOnset(a[i+1])) == 4364 or byeondong_cho == "ㅈ":
                        result = result + '된소리되기로 ㅈ이 ㅉ으로 발음\n'


    return result
                
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    
    if request.method == 'POST':
        a = str(request.form['textbox'])
        d = wtr_BD(a)
        e = d.replace("\n", ", ")
        

        return render_template('result.html', f = a, d = e)
if __name__=="__main__":
    app.run(debug=True)
