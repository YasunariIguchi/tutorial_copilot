def get_rectangle_area(width, height):
    """四角形の面積を求める
    Args:
        width (float): 幅
        height (float): 高さ
    Returns:
        float: 面積
    Raises:
        ValueError: width, heightが負の値の場合
    """
    if width < 0 or height < 0:
        raise ValueError('width and height must be positive values.')
    return width * height


def get_bbox_area(bbox):
    """バウンディングボックスの面積を求める
    Args:
        bbox (list): [xmin, ymin, xmax, ymax]
    Returns:
        float: 面積
    Raises:
        ValueError: bboxの長さが4でない場合
    """
    if len(bbox) != 4:
        raise ValueError('bbox must be a list of length 4.')
    return get_rectangle_area(bbox[2] - bbox[0], bbox[3] - bbox[1])
