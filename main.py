import numpy as np

#array1 = np.array([1, 2, 3])
#array2 = np.array([4, 3, 2])
#new_array = array1 + array2
#print(new_array)

#test = np.savetxt('output.csv', dataT, delimiter=',', fmt='%f')


# load array
#data = np.genfromtxt('output.csv', delimiter=',')
# print the array
#print(data)

 
# Slice elements from index 0 to index 3
#emp = np.array([1, 2, 3, 4, 5, 6, 7])
#lastElementIndex = len(arr)-1
# Removing the last element using slicing 
#arr = arr[:lastElementIndex]
#print(arr[0:3])
#print(len(arr))
#print(temp[2] + temp[3])


#nd1 = np.array([[1,2,3],[4,5,6]])
#nd2 = np.array([[7,8,9]])

#print(nd1)
#print(nd2)
#print(np.append(nd1,nd2,0))
#test = np.array([1, 2, 3, 4, 5, 4, 4])

#result = np.where(test == 4)

#print(result)
#np.savetxt('outfile.txt',test)
#disp = np.loadtxt('output.csv')
#print(disp)
#Give an array any dimension you want
#new_array=np.array(11, ndmin=4)
#print(new_array)


#num = np.array([[1, 2, 3],
              #[4, 5, 6],
              #[7, 8, 9]])
#print(num[0])
#print(num.ndim)
#print(num[0:2, 1:3])
#print(num[1:,0:2])
#x = np.array([[23,34,45], [24, 45, 78]])

#y = x.copy()
#x[0,0]=10
#print(y)
#print(x)

array1 = np.array([11,11,11,12,12.12,13,13,13])
array2 = np.array([40,36,20,60,75,65,89,96,56])
score_split=array2.reshape(3,3)
print(score_split)

a =np.arange(0,5)
print(a)



