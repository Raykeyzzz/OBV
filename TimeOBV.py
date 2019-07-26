"""
说明：生成时间序列的obv 16*16位
数据集：cuckoo数据集

obv = [0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,0]
list_obv = [13,12,6,4,14,1,1,12,4,1,1,1]
"""
import numpy


def time_obv(list_obv, obv):
    """
    :param list_obv: 基本元素0~16，代表16种行为，按照时间顺序存储在列表中
    :param obv: 16中行为，1代表有，0代表无，索引代表行为
    :return: 关于时间的16*16向量
    """
    matrix_zeros = numpy.zeros([16, 16])
    for i in range(len(obv)):
        if obv[i] == 1:
            if list_obv.index(i) != len(list_obv) - 1:
                for j in range(list_obv.index(i) + 1, len(list_obv)):
                    matrix_zeros[i][list_obv[j]] = 1
    return matrix_zeros

if __name__ == "__main__":
    obv = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0]
    list_obv = [13, 12, 6, 4, 14, 1, 1, 12, 4, 1, 1, 1]
    print(time_obv(list_obv, obv))
