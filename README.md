# CV110 hw2 D0748284
###### tags: `CV`
---

# 1. 黑白影像直方圖
* 程式碼
    ``` python
    def get_pdf_cdf(data):
        PDF = np.zeros(256 , dtype=int)
        CDF = np.zeros(256 , dtype=float)
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                PDF[data[i,j]] += 1
        CDF[0] = PDF[0]
        for i in range(1,CDF.shape[0]):
            CDF[i] = CDF[i-1] + PDF[i]
        return PDF,CDF
    img = cv2.imread("img/img1.jpg" , 0 )
    img_PDF,img_CDF = get_pdf_cdf(img) 
    CDF_01= img_CDF/img_PDF.sum() # 改成機率分佈函數
    plt.bar(range(256),img_PDF/(img_PDF.sum()) , color ='r') # 繪製直方圖
    plt.plot(img_CDF/img_PDF.sum()) # 分佈圖
    plt.show()
    ```
* 結果 

|               縮放PDF                |                 原始                 |
|:------------------------------------:|:------------------------------------:|
| ![](https://i.imgur.com/m0izMCl.png) | ![](https://i.imgur.com/1UcUDOw.png) |

    
# 2. 黑白影像直方圖均化
* 程式碼
    ``` python
    img = cv2.imread("img/img1.jpg"   ,   0   )
    new_img = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # new_img[i,j] = X[img[i,j]]
            new_img[i,j] = int(np.round(CDF_01[img[i,j]] * 255)) # 重新取樣
    ```
* 結果 
    * Hawkes Bay
        ![](https://i.imgur.com/jmWLOXR.png)
    * lena
        ![](https://i.imgur.com/GUwHOPe.png)

# 彩色影像直方圖(三張)

* 程式碼
    ``` python
    for i in range(img_color.shape[-1]):
        img_PDF,img_CDF = get_pdf_cdf(img_color[:,:,i])
        plt.subplot(2, 4, 1+i)
        plt.bar(range(256),img_PDF/img_PDF.sum() , color = color_lable[i])
        plt.title(color_lable[i])
    ```
* 結果 
    * fruit
        ![](https://i.imgur.com/xWJkrWC.png)
    * lena
        ![](https://i.imgur.com/9fPXtdb.png)




# 彩色影像直方圖分別均化並合併出結果 20%

* 程式碼
    ``` python
    for color in range(img_color.shape[-1]):
        for i in range(img_color.shape[0]):
            for j in range(img_color.shape[1]):
                # new_img[i,j] = X[img[i,j]]
                new_img[i,j,color] =    int(np.round(CDF_01[img_color[i,j,color]] * 255))
    ```
* 結果 
    * fruit
        ![](https://i.imgur.com/04LwT0m.jpg)
    * lena
        ![](https://i.imgur.com/eQLwUv4.jpg)
        
        
# 心得
這次作業基本上用一個公式(圖一)就可以全部處理好了，算是比較簡單的一次作業，
希望下次摳手手的作業也那麼簡單。


* 圖一
![](https://i.imgur.com/3SAsq8d.png)
