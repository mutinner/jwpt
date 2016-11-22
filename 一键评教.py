import requests
import re
from bs4 import BeautifulSoup
import time
import random

s = requests.session()
pgyj = [
    "老师对待教学认真负责，语言生动，条理清晰",
    "对待学生严格要求，能够鼓励学生踊跃发言，课堂气氛比较积极热烈。",
    "课堂内容充实，简单明了，使学生能够轻轻松松掌握知识。",
    "教学过程思路清晰，始终围绕教学目标。"
    "把握重点，突出难点,能够引导学生开展观察操作比较猜想推理交流等多种形式的活动",
    "课堂教学效果好，语言清晰，能注重学法指导，培养学生的创新能力",
    "教学重难点突出，教学步骤设计合理，由浅入深，循序渐进。",
    "知识点明确，条理清晰，教师注意归纳总结",
    "教学有个性，有自己的特点与风格。在教学设计上有新的突破，课堂给人耳目一新的感觉。",
    "教学设计思路清晰，知识由浅入深,谆谆诱导，创设情景,引发学生思维",
    "教师能以饱满的精神为学生讲每一堂课。在授课过程中，教师所讲的内容能够吸引学生的注意力",
    "课堂氛围轻松活跃，积极调动了学生的兴趣"
]


def login():
    html = s.get("http://jwpt.tjpu.edu.cn/validateCodeAction.do?")
    with open('code.jpg', 'wb') as f:
        f.write(html.content)
    zjh = input("请输入用户名:")
    mm = input("请输入密码:")
    yzm = input("请输入验证码:")
    info = {'zjh': zjh, 'mm': mm, 'v_yzm': yzm}
    return s.post('http://jwpt.tjpu.edu.cn/loginAction.do', data=info);


def start():
    s.get('http://jwpt.tjpu.edu.cn/jxpgXsAction.do?oper=listWj')
    html = s.get('http://jwpt.tjpu.edu.cn/jxpgXsAction.do?pageSize=300')
    soup = BeautifulSoup(html.text, "html.parser")
    img = soup.find_all('img', title='评估')
    para = ['wjbm', 'bpr', 'bprm', 'wjmc', 'pgnrm', 'pgnr']
    info = {
        'oper': 'wjShow',
        'wjbz': 'null',
    }
    for x in img:
        value = list(re.findall('(.*?)#@(.*?)#@(.*?)#@(.*?)#@(.*?)#@(.*)', x.attrs['name'])[0])
        info.update(dict(zip(para, value)))
        html = s.post('http://jwpt.tjpu.edu.cn/jxpgXsAction.do', data=info)
        soup = BeautifulSoup(html.text, "html.parser")
        choice = soup.find_all('input', value='10_1')
        choice_data = {}
        choice_data['pgnr'] = info['pgnr']
        choice_data['wjbm'] = info['wjbm']
        choice_data['bpr'] = info['bpr']
        choice_data['xumanyzg'] = 'zg'
        choice_data['wjbz'] = ''
        for i in choice:
            choice_data[i.attrs['name']] = '10_1'
        j = random.randint(0, 11)
        choice_data['zgpj'] = pgyj[j].encode('gbk')
        html = s.post('http://jwpt.tjpu.edu.cn/jxpgXsAction.do?oper=wjpg', data=choice_data)
        result = re.findall('alert\("(.*?)"\)', html.text)[0]
        print(info['pgnrm'] + ' ' + info['bprm'] + " " + result)
        time.sleep(1)


if __name__ == '__main__':
    print("#-----------------------------------------------")
    print("#  程序:一键评教")
    print("#  版本:1.0")
    print("#  日期:2016-11-22")
    print("#  作者:Parallelc")
    print("#  操作:输入用户名,密码,验证码")
    print("#  备注:验证码在当前程序的路径内,名为code.jpg")
    print("#-----------------------------------------------")
    print("")
    flag = 0
    while flag == 0:
        try:
            html = login()
        except requests.exceptions.ConnectionError as e:
            print("连接失败!请检查网络")
            break
        except Exception as e:
            print("发生错误!")
            print(e)
            break
        else:
            soup = BeautifulSoup(html.text, "html.parser")
            error = soup.find_all('td', {'class': "errorTop"})
            if error:
                print(error[0].get_text())
            else:
                print("登录成功!")
                flag = 1
    if flag == 1:
        try:
            start()
        except requests.exceptions.ConnectionError as e:
            print("连接失败!请检查网络")
        except Exception as e:
            print("发生错误!")
            print(e)
        else:
            print("评估完成!")
print("程序将在60s后关闭...")
time.sleep(60)
