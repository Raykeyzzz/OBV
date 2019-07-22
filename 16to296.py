import numpy
def obv_or_and(path,matrix):
    """
    :param path: 数据源（16位的obv）
    :return: list（16*16的obv列表）
    """
    list_obvs = []
    with open(path,"r") as f:
        lines = f.readlines()
    for i in lines:
        list_obv = []
        i = i.replace("\n","")
        num = i.split(" ")
        for j in num:
            list_obv.append(int(j))
        matrix_new = obv16to296(list_obv,matrix)
        list_obvs.append(matrix_new)
    return list_obvs


def obv16to296(list_obv,matrix):
    """

    :param list_obv: 16位obv向量的列表形式
    :param matrix: 16*16的零矩阵
    :return: 16*16的与或矩阵
    """
    matrix = matrix.copy()  # 必须拷贝副本，不然后面的操作会影响到原数组
    for i in range(len(list_obv)):
       for j in range(len(list_obv)):
           if i > j:  # 代表在matrix矩阵的左下半部分，左下半部分用于存储“与”数据
               if list_obv[i] == list_obv[j] == 1:
                   matrix[i][j] = 1
               else:
                   matrix[i][j] = 0
           elif i < j:  # 代表在matrix矩阵的y右上半部分，右上半部分用于存储“或”数据
               if list_obv[i] == 1 or list_obv[j] == 1:
                   matrix[i][j] = 1
               else:
                   matrix[i][j] = 0
           else:
               matrix[i][j] = list_obv[i]
    return matrix

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

if __name__ =="__main__":
    path = r"C:\Users\ywx639648\Desktop\\testobv"
    target_path = r"C:\Users\ywx639648\Desktop\\output296colum"
    matrix = numpy.zeros([16,16], dtype=int, order='C') #建一个16*16得矩阵
    list_matrix = obv_or_and(path,matrix)
    output296_obv(list_matrix,target_path)