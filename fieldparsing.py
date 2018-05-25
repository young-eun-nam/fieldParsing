#string사이에 있는 것을 뽑아내줌


def find_between( s, first, last ):
    try:
        print(s, first, last)
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def parseFieldFile(fieldFilePath, parsedFieldFilePath):

    outputList = []

    with open(fieldFilePath, 'r', encoding='UTF8') as f:
        allLines = f.readlines()
        index = 0
        # 8줄마다 같은 형식으로 들어옴
        while (index + 8 <= len(allLines)):
            fieldIndex  = str(allLines[index]).rstrip().replace(",", "").split(":")[1]
            name = str(allLines[index+1]).rstrip().replace(",", "").split(":")[1]
            longitudeA, latitudeA = find_between(str(allLines[index + 3]), "{", "}").replace(" ", "").split(",")
            longitudeB, latitudeB = find_between(str(allLines[index + 4]), "{", "}").replace(" ", "").split(",")
            longitudeC, latitudeC = find_between(str(allLines[index + 5]), "{", "}").replace(" ", "").split(",")
            longitudeD, latitudeD = find_between(str(allLines[index + 6]), "{", "}").replace(" ", "").split(",")
            element = fieldIndex + "," + name + "," + longitudeA + "," + latitudeA+ "," + longitudeB + "," + latitudeB + "," + longitudeC + "," + latitudeC + "," + longitudeD + "," + latitudeD +"\n"
            outputList.append(element)
            index += 8

    with open(parsedFieldFilePath, "w+", encoding = "UTF8") as f:
        f.write("fieldIndex, name, longitudeA, latitudeA, longitudeB, latitudeB ,longitudeC, latitudeC ,longitudeD, latitudeD\n")
        f.writelines(outputList)

if __name__ == "__main__":
    fieldFilePath = input("파싱할 필드 파일 경로를 입력하시오: ").replace("\\", "/")
    #parsedFieldFilePath = input("출력할 필드 파일 경로를 입력하시오: ").replace("\\", "/")
    #fieldFilePath = "C:/Users/fitogether/Documents/AuFe/SW개발 할것/field.txt"
    #parsedFieldFilePath ="C:/Users/fitogether/Documents/AuFe/temp/output.csv"

    parsedFieldFilePath = "output.csv"
    parseFieldFile(fieldFilePath, parsedFieldFilePath)

'''
    Field : 1
    name : 동탄 방교리 축구장
05-13 16:30:31.624 18055-18055/com.fitogether.ohcoach I/Database: corners : 
    	{37.17358197789903, 127.08645592695822},
    	{37.17450663274697, 127.08665928423129},
    	{37.17460599283836, 127.08594343402139},
    	{37.17369034288183, 127.08573778314579}
    (width,height) : (10419, 6452)
    Field : 2
    name : 수원월드컵경기장 연습경기장
    corners : 
    	{37.288707695272855, 127.04017872875254},
    	{37.28941848894748, 127.04100361434641},
    	{37.28984889197794, 127.04041998459265},
    	{37.28914891072942, 127.03959503396908}
    (width,height) : (10757, 7042)
    ------------------------> parsing
     동탄 방교리 축구장,37.17358197789903,127.08645592695822,37.17450663274697,127.08665928423129,37.17460599283836,127.08594343402139,37.17369034288183,127.08573778314579
    수원월드컵경기장 연습경기장,37.288707695272855,127.04017872875254,37.28941848894748,127.04100361434641,37.28984889197794,127.04041998459265,37.28914891072942,127.03959503396908
'''

