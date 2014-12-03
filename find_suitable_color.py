"""
 Skin color level 1 to 6
"""
"""
    Loreal Version 1
"""
# skinMap = [[69, 53, 30], [70, 52, 32], [72, 51, 34], [75, 49, 36], [76, 48, 37], [78, 47, 42],
#            [88, 69, 37], [92, 66, 41], [93, 65, 43], [97, 64, 45], [100, 62, 49], [101, 61, 53],
#            [109, 85, 51], [113, 82, 53], [116, 80, 54], [117, 79, 56], [120, 77, 61], [123, 75, 65],
#            [128, 100, 61], [131, 98, 65], [135, 96, 67], [139, 95, 70], [141, 92, 75], [144, 92, 79],
#            [146, 117, 77], [149, 115, 78], [154, 113, 83], [157, 111, 85], [161, 110, 91], [163, 106, 95],
"""
    Loreal Version 2
"""
# skinMap = [[234, 216, 196], [237, 216, 197], [238, 215, 199], [240, 214, 201], [245, 214, 203], [245, 212, 205],
#            [224, 200, 174], [225, 199, 174], [229, 198, 177], [230, 197, 178], [233, 195, 182], [234, 194, 186],
#            [210, 184, 151], [213, 182, 153], [217, 181, 155], [220, 179, 159], [221, 178, 161], [224, 176, 166],
#            [196, 166, 130], [200, 165, 133], [203, 164, 135], [207, 162, 139], [209, 160, 143], [212, 160, 147],
#            [180, 151, 111], [184, 148, 112], [189, 145, 116], [191, 143, 122], [195, 143, 122], [198, 141, 130],
#            [165, 133, 94], [167, 131, 95], [172, 128, 99], [175, 128, 102], [178, 126, 105], [182, 124, 112]
#            ]
"""
    Yerago Version
    0-3 : spring
    4-7 : summer
    8-11: autumn
    12-15:winter
"""
skinMap = [[243, 221, 161], [216, 181, 122], [222, 163, 107], [177, 132, 50],
           [213, 186, 152], [192, 160, 135], [166, 111, 81], [136, 92, 36],
           [246, 218, 164], [234, 162, 122], [193, 137, 88], [126, 87, 53],
           [242, 219, 177], [205, 171, 116], [192, 113, 59], [115, 59, 28]
           ]

def color_detector(inputBGR):
    color = [0, 0, 0]
    score = 1000

    # if color does not in range BGR
    if inputBGR[2] < 101 or inputBGR[2] > 245:
        return -1
    if inputBGR[1] < 61 or inputBGR[1] > 216:
        return -1
    if inputBGR[0] < 53 or inputBGR[0] > 205:
        return -1

    # else find best skin color
    for i in range(len(skinMap)):
        Rscore = abs(skinMap[i][0] - inputBGR[2])
        Gscore = abs(skinMap[i][1] - inputBGR[1])
        Bscore = abs(skinMap[i][2] - inputBGR[0])
        tempScore = Rscore + Gscore + Bscore
        # smaller is better suitable for skin
        if tempScore < score:
            score = tempScore
            color = i
    # when color mapper found best skin color then,
    return color

def find_suitable_weather(inputRange):
    weather_score = [0, 0, 0, 0]
    for i in range(8):
        if inputRange[i][0] <= 3:
            weather_score[0] += inputRange[i][1]
        elif inputRange[i][0] <= 7:
            weather_score[1] += inputRange[i][1]
        elif inputRange[i][0] <= 11:
            weather_score[2] += inputRange[i][1]
        elif inputRange[i][0] <= 15:
            weather_score[3] += inputRange[i][1]
        else:
            print 'something is wrong please contact to manager'
    print weather_score, 'Sp, Su, Au, Wt'