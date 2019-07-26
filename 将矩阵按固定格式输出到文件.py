"""
说明：将16*16的矩阵输出到文件每行296个数字，由空格隔开
"""
import numpy
def output296_obv(list_matrix,target_path):
    """
    :param list_matrix: 16*16矩阵的列表
    :return: （无）将296维的向量输出到output296colum
    """
    with open(target_path,"w") as f:
        for i in list_matrix:
            for x in numpy.nditer(i):
                f.write(str(x)+ ' ')
            f.write("\n")
if __name__ == "__main__":
    target_path = ""
    list_matrix = numpy.zeros([16*16])
    output296_obv(list_matrix, target_path)
    

