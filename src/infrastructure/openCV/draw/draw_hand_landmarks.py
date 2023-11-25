import cv2 as cv


def draw_landmarks(image: cv.typing.MatLike, landmark_point):
    if len(landmark_point) > 0:
        draw_thumb(image, landmark_point)
        draw_index(image, landmark_point)
        draw_middle_finger(image, landmark_point)
        draw_ring_finger(image, landmark_point)
        draw_little_finger(image, landmark_point)
        draw_palm(image, landmark_point)

    draw_hand_keypoints(image, landmark_point)

    return image


def draw_hand_keypoints(image, landmark_point):
    for index, landmark in enumerate(landmark_point):
        if index == 0:  # 手首1
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 1:  # 手首2
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 2:  # 親指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 3:  # 親指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 4:  # 親指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
        if index == 5:  # 人差指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 6:  # 人差指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 7:  # 人差指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 8:  # 人差指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
        if index == 9:  # 中指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 10:  # 中指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 11:  # 中指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 12:  # 中指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
        if index == 13:  # 薬指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 14:  # 薬指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 15:  # 薬指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 16:  # 薬指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
        if index == 17:  # 小指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 18:  # 小指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 19:  # 小指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 20:  # 小指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)


def draw_palm(image, landmark_point):
    cv.line(image, tuple(landmark_point[0]), tuple(landmark_point[1]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[0]), tuple(landmark_point[1]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[1]), tuple(landmark_point[2]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[1]), tuple(landmark_point[2]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[5]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[5]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[9]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[9]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[13]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[13]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[17]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[17]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[0]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[0]),
            (255, 255, 255), 2)


def draw_little_finger(image, landmark_point):
    cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[18]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[18]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[18]), tuple(landmark_point[19]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[18]), tuple(landmark_point[19]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[19]), tuple(landmark_point[20]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[19]), tuple(landmark_point[20]),
            (255, 255, 255), 2)


def draw_ring_finger(image, landmark_point):
    cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[14]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[14]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[14]), tuple(landmark_point[15]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[14]), tuple(landmark_point[15]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[15]), tuple(landmark_point[16]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[15]), tuple(landmark_point[16]),
            (255, 255, 255), 2)


def draw_middle_finger(image, landmark_point):
    cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[10]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[10]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[10]), tuple(landmark_point[11]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[10]), tuple(landmark_point[11]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[11]), tuple(landmark_point[12]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[11]), tuple(landmark_point[12]),
            (255, 255, 255), 2)


def draw_index(image, landmark_point):
    cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[6]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[6]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[6]), tuple(landmark_point[7]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[6]), tuple(landmark_point[7]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[7]), tuple(landmark_point[8]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[7]), tuple(landmark_point[8]),
            (255, 255, 255), 2)


def draw_thumb(image, landmark_point):
    cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[3]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[3]),
            (255, 255, 255), 2)
    cv.line(image, tuple(landmark_point[3]), tuple(landmark_point[4]),
            (0, 0, 0), 6)
    cv.line(image, tuple(landmark_point[3]), tuple(landmark_point[4]),
            (255, 255, 255), 2)