from exercises.normalize import normalize
import numpy as np

def test_normalize():
    # 测试样例1：常规数据标准化
    input1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    expected1 = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    result1 = normalize(input1)
    print("测试样例1 (常规数据):", 
          "yes" if np.allclose(result1, expected1) else "no")

    # 测试样例2：所有值相同
    input2 = np.array([3.0, 3.0, 3.0])
    expected2 = np.array([0.5, 0.5, 0.5])  # (0+1)/2=0.5
    result2 = normalize(input2)
    print("测试样例2 (所有值相同):", 
          "yes" if np.allclose(result2, expected2) else "no")

    # 测试样例3：自定义范围
    input3 = np.array([10, 20, 30])
    expected3 = np.array([-1.0, 0.0, 1.0])  # 缩放到[-1,1]
    result3 = normalize(input3, min_val=-1.0, max_val=1.0)
    print("测试样例3 (自定义范围):", 
          "yes" if np.allclose(result3, expected3) else "no")

if __name__ == "__main__":
    test_normalize()
