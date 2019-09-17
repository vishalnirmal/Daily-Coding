##############################################
# Merge Sort                                 #
# by Vishal Nirmal                           #
##############################################




def sort(arr, reverse=False):

    if len(arr)>1:

        mid = len(arr)//2



        L = arr[:mid]

        R = arr[mid:]



        sort(L)

        sort(R)



        i = j = k = 0



        while i < len(L) and j < len(R):

            if reverse:

                if L[i] > R[j]:

                    arr[k] = L[i]

                    i+=1

                else:

                    arr[k] = R[j]

                    j+=1

            else:

                if L[i] > R[j]:

                    arr[k] = R[j]

                    j+=1

                else:

                    arr[k] = L[i]

                    i+=1

            k+=1

        

        while i < len(L):

            arr[k] = L[i]

            i+=1

            k+=1

        

        while j < len(R):

            arr[k] = R[j]

            j+=1

            k+=1