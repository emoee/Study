import csv
import matplotlib.pyplot as plt

def jeju_show():
    with open("./jeju_worktogether/combined_data") as f:
        data = csv.reader(f)
        next(data)
        result = {}
        for row in data:
            category = row[4]
            result[category] = result.get(category, 0) + 1

    categories = list(result.keys())
    counts = list(result.values())
    
    plt.style.use('seaborn-pastel')
    plt.rc('font', family='AppleGothic') # Mac 사용시 맑은 고딕은 한글깨짐 오류가 발생함.
    plt.bar(categories, counts)
    plt.ylabel('Count')
    plt.title('Cultural Heritage Categories')
    plt.xticks(rotation=90)
    #plt.show()
    plt.savefig('./cha_openAPI/Cultural Heritage Categories.png') # 이미지파일 저장

def main():
    jeju_show()
    
if __name__ == '__main__':
    main()