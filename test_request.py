import requests
from concurrent.futures import ThreadPoolExecutor
import time
# 定义发送请求的函数
def test_base_api():
    response = requests.get('http://localhost:8000/')
    return response.text

def test_kenlm_api():
    random_chinese="时任中影公司华东部副经理，现任太合环球影业的总经理韩小凌如今这样对南都记者回忆道，而这部电影，就是《泰坦尼克号》。3.6亿，这个数字占据了内地最高票房电影冠军宝座长达11年之久，一直到2009年才被《变形金刚2》打破。“就算到现在，《泰坦尼克号》的资源投入和效果产出比也是别的影片没法比的。它加上原版拷贝也就300个左右，《夜宴》都有400多个拷贝呢。”\n14年过去，赶在泰坦尼克号沉没100周年的纪念日，这艘无坚不摧的大船套上3D的铠甲，再度起航。记者也趁此时机，采访了当年陪不同女孩看过几遍的观 众、每天捧着两箱钱去入账的影院经理、需要武警保护才能运送拷贝的发行人员，在这些记忆碎片拼接的过程中，或许当年排长龙买过票的、哭红过眼的、一遍遍跟 着主题曲哼唱的、正在看报纸的你，也能在其中找到当年的自己。\n南都记者简芳 实习生李倩 冼志荣\nPart1\n起航\n买票的队伍从永汉电影院排到禺山路\n在他排队的一个小时里，不断看见有眼睛哭红的人从影院里走出来！男男女女，一律如此！\n现在人们谈起一部电影如何火爆，可能都会举出《阿凡达》的例子，不过相比当年《泰坦尼克号》上映时的“全民围观”，《阿凡达》简直是“弱爆了”！\n阿昌（化名）当年15岁，在广州执信中学读初三。和很多当时的“广州仔”一样，他热爱T V B，不过当T V B在介绍《泰坦尼克号》如何引起全港轰动，他并没有太放在心上，直到……\n“电影上映的第二天，课间操做完，周围的同学推推搡搡，三五成群，我一个人慢慢往回走的时候，看到比自己低两届的学妹正站在教学楼下。对方一句话也没说， 羞答答地把一张字条塞进我手头，转身跑了”。字条上，娟秀的字迹写着：我们去看《泰坦尼克号》吧。“14年前没有手机啊，后两节课一直很激动，但只能忍 着。”一直到中午放学后，回到家里，阿昌才给女孩打了电话，约好周末下午两点去北京路的永汉电影院看这部电影。\n那个周六，为了可以抢到看电影的“皇帝座”（中间位置），阿昌起得很早到电影院买票。但等他赶到影院的时候，永汉电影院门口排队买票的人龙已经排到了禺山 路口。阿昌赶紧加入到百米的排队人龙中，生怕再犹豫一会儿，就买不到票了。但是让阿昌印象深刻的不是排队的人龙，而是在他排队的一个小时里，不断看见有眼 睛哭红的人从影院里走出来！男男女女，一律如此！\n50块的票炒到200块\n当时广州各大影院几乎每天都像评书里说的那样，高挂免战牌———“票已售罄”，这种情形维持了整个四月，有观众提出买站票。\n排队一小时到买两张票，阿昌已经算幸运的了。当时最壮观的队伍在市一宫榕泉电影院的门口，每天7点开始，从售票口排到金德大厦，影院甚至特意加了保安和铁 栏杆维持秩序，提前一个小时买票、票价高达50块（当时其他电影的票价在5-20块之间）都不一定买得到。影院门口的黄牛开价就是200块，还是不愁销 路。\n上一篇：刘嘉玲回应被绑架事件：梁朝伟像座山给我依靠\n下一篇：2018年第55届金马奖颁奖典礼主持人是谁 陶晶莹个\n表情:\n风电版“速度与激情”！典型300M\n风电版“速度与激情”！典型300MW海上风电项目建设进程跟踪,...\n《極限挑戰》古畫保護游戲燒腦\n東方衛視星素互動勵志體驗節目《極限挑戰》第四季正在火熱播...\n特朗普玩《权力的游戏》“凛冬将\n当地时间11月2日，美国政府这头刚宣布将在本月5日重启对伊朗制...\n父亲是华尔街之狼 他却靠打扑克赚\n所以我们就看到丹和姑娘们的各种疯狂照片，无论是海边度假、...\n青山夹绿水，廊桥遗梦 浙江泰顺自\n青山夹绿水，廊桥遗梦" 
    # 准备要发送的 JSON 数据
    data = {
        "lang": "zh",
        "text": random_chinese,
    }

    # 发送 POST 请求
    response = requests.post('http://localhost:8000/kenlm_api', json=data)

    # 输出响应内容
    # print(response.text)

if __name__=="__main__":
    # 创建线程池
    s=time.time()
    num_task=100000
    with ThreadPoolExecutor(max_workers=64) as executor:
        # 向线程池提交任务
        futures = [executor.submit(test_kenlm_api) for _ in range(num_task)]
        
        # 获取任务的结果
        # for future in futures:
            # print(future.result())
    e=time.time()
    print(f"call {num_task}s, time consume:{e-s}s")