import pandas as pd
from datetime import datetime, timedelta

# 建立基本的結構
start_date = datetime(2025, 4, 29)  # 假設從4/29開始
days = 56  # 8周 = 56天

subjects = []
chapters = []
tasks = []
estimated_hours = []
dates = []
emojis = []

# 微積分與演算法章節大致分配
calculus_chapters = [
    "第1-2章 函數、極限、導數概念",
    "第3章 導數運算與應用",
    "第3章 圖形分析",
    "第4-5章 積分基本定理與技巧",
    "第6章 積分應用（體積、弧長）",
    "第8章 無窮級數",
    "第8,10章 泰勒展開與參數曲線",
    "全書複習與錯題整理"
]

algo_chapters = [
    "第1-3章 導論、數學背景、遞迴",
    "第4,6,7章 分治法、堆積、快速排序",
    "第8-10章 線性排序、中位數選擇、排序下界",
    "第11-13章 雜湊與樹結構",
    "第15-16章 動態規劃、貪心演算法",
    "第17,22章 最短路徑、DFS與BFS",
    "綜合小專案與LeetCode挑戰",
    "模擬考與總整理"
]

# 生成每日任務
for i in range(days):
    current_date = start_date + timedelta(days=i)
    dates.append(current_date.strftime("%Y-%m-%d"))
    
    if i % 2 == 0:  # 偶數天：演算法
        subject = "資料結構與演算法 🟢"
        week = i // 7
        if week > 7: week = 7
        chapter = algo_chapters[week]
        if current_date.weekday() >= 5:  # 週末
            task = f"深度閱讀 {chapter}，大量實作練習"
            hours = "6-8小時"
        else:
            task = f"閱讀 {chapter} 指定小節並完成一個小實作"
            hours = "1-2小時"
    else:  # 奇數天：微積分
        subject = "微積分 🔵"
        week = i // 7
        if week > 7: week = 7
        chapter = calculus_chapters[week]
        if current_date.weekday() >= 5:
            task = f"深度練習 {chapter}，大量題目練習"
            hours = "6-8小時"
        else:
            task = f"閱讀 {chapter} 指定小節並完成5題練習題"
            hours = "1-2小時"
    
    subjects.append(subject)
    chapters.append(chapter)
    tasks.append(task)
    estimated_hours.append(hours)
    emojis.append("")  # 預留心情/心得欄位

# 建立DataFrame
df = pd.DataFrame({
    "日期": dates,
    "科目": subjects,
    "主題章節": chapters,
    "任務描述": tasks,
    "預計時數": estimated_hours,
    "完成✅": "",
    "心情/心得": emojis,
    "備註": ""
})

# 存成CSV檔
csv_path = './study_plan_notion.csv'
df.to_csv(csv_path, index=False)
csv_path