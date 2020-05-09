def getPItems():
    return [{
        "id": 0,
        "title": "Blur the image",
        "path": "gaussian.jpg"
    },
        {
        "id": 1,
        "title": "Convert to gray scale image"
    },
        {
        "id": 2,
        "title": "Convert to binary image"
    },
        {
        "id": 3,
        "title": "Convert canny"
    },
    ]


def getBItems():
    return [
        {
            "id": 0,
            "title": "Averaging",
            "path": "averaging.jpg",
            "explanation": "This is done by convolving the image with a normalized box filter. It simply takes the average of all the pixels under kernel area and replaces the central element with this average. This is done by the function cv2.blur() or cv2.boxFilter(). "
        },
        {
            "id": 1,
            "title": "Gaussian blur",
            "path": "gaussian.jpg",
            "explanation": "In this approach, instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used. It is done with the function, cv2.GaussianBlur(). We should specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as equal to sigmaX. If both are given as zeros, they are calculated from the kernel size. Gaussian filtering is highly effective in removing Gaussian noise from the image."
        },
        {
            "id": 2,
            "title": "Median Filtering",
            "path": "median.jpg",
            "explanation": "Here, the function cv2.medianBlur() computes the median of all the pixels under the kernel window and the central pixel is replaced with this median value. This is highly effective in removing salt-and-pepper noise. One interesting thing to note is that, in the Gaussian and box filters, the filtered value for the central element can be a value which may not exist in the original image. However this is not the case in median filtering, since the central element is always replaced by some pixel value in the image. This reduces the noise effectively. The kernel size must be a positive odd integer."
        },
        {
            "id": 3,
            "title": "Bilateral Filtering",
            "path": "bilateral.jpg",
            "explanation": "As we noted, the filters we presented earlier tend to blur edges. This is not the case for the bilateral filter, cv2.bilateralFilter(), which was defined for, and is highly effective at noise removal while preserving edges. But the operation is slower compared to other filters. We already saw that a Gaussian filter takes the a neighborhood around the pixel and finds its Gaussian weighted average. This Gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It does not consider whether pixels have almost the same intensity value and does not consider whether the pixel lies on an edge or not. The resulting effect is that Gaussian filters tend to blur edges, which is undesirable. The bilateral filter also uses a Gaussian filter in the space domain, but it also uses one more (multiplicative) Gaussian filter component which is a function of pixel intensity differences. The Gaussian function of space makes sure that only pixels are ‘spatial neighbors’ are considered for filtering, while the Gaussian component applied in the intensity domain (a Gaussian function of intensity differences) ensures that only those pixels with intensities similar to that of the central pixel (‘intensity neighbors’) are included to compute the blurred intensity value. As a result, this method preserves edges, since for pixels lying near edges, neighboring pixels placed on the other side of the edge, and therefore exhibiting large intensity variations when compared to the central pixel, will not be included for blurring."
        },
    ]


def getRItems():
    return [
        {
            "id": 0,
            "title": "Averaging"
        },
        {
            "id": 1,
            "title": "Gaussian blur",
            "path": "gaussian.jpg",
            "explanation": "In this approach, instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used. It is done with the function, cv2.GaussianBlur(). We should specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as equal to sigmaX. If both are given as zeros, they are calculated from the kernel size. Gaussian filtering is highly effective in removing Gaussian noise from the image."
        },
        {
            "id": 2,
            "title": "Median Filtering"
        },
        {
            "id": 3,
            "title": "Bilateral Filtering"
        },
    ]


def getCItems():
    return [
        {
            "id": 0,
            "title": "To Gray"
        },
        {
            "id": 1,
            "title": "To HLS"
        },
        {
            "id": 2,
            "title": "To HSV"
        },
        {
            "id": 3,
            "title": "To LAB"
        },
        {
            "id": 4,
            "title": "To LUV"
        },
        {
            "id": 5,
            "title": "To XYZ"
        },
    ]


def getTutorialItems():
    return [
        {
            "id": 0,
            "title": "First chunk of code",
            "explanation": """
            <span class="code">tf.get_default_graph()</span> 
            Returns the default graph for the current thread.</br>
            <span class="code">with</span> means you need to first set this graph as default and then perform loading the model from the given location
            """,
            "code": """<pre>
graph = tf.get_default_graph()
with graph.as_default():
    # load model at very first
    model = load_model("./static/" + 'model_design.h5')
</pre>
"""
        },
        {
            "id": 1,
            "title": "Second chunk of code",
            "explanation": """
            Let's look at  <span class="code">getResult</span> function, which serves as a place. where you compute the prediction for future use. But be patient. I will explain you how it works line by line 
            <br/>
            So, first of all we load the image from <span class="code">imagePath</span> on your computer by using <span class="code">tf.keras.preprocessing.image.load_img(path, grayscale=False, color_mode='rgb', target_size=None, interpolation='nearest')</span></br> function and we also give it the size
            <br/>
            After that we expand dimensions at specified axis position <span class="code">np.expand_dims(data, axis=0)</span> </br>
            <span class="code">with</span> means you need to first set this graph as default and then perform prediction based on model when we give it our image preprocessed for this model to work
            """,

            "code": """<pre>
def getResult(imagePath):
    data = image.load_img(imagePath, target_size=(150, 150, 3))
    data = np.expand_dims(data, axis=0)
    data = data * 1.0 / 255

    with graph.as_default():
        predicted = model.predict(data)
        return predicted
</pre>
"""
        },
        {
            "id": 2,
            "title": "Finally, Classification",
            "explanation": """
           Now we came to the final part of this tutorial. We get the image, we make a list of possible labels. 
           <span class="code">getResult</span> is the function we saw before. It returns the prediction based on our image, which was
           applied to the model
            <br/>
           <span class="code">np.argmax</span> returns the indices of the maximum values along an axis and
           <span class="code">np.asscalar</span> converts an array of size 1 to its scalar equivalent.
Then we calculate the accuracy in percentage and get resulted label.
            <br/>
            And we are done!
            """,
            "code": """<pre>
def classification(img):
    indices = {0: 'Cat', 1: 'Dog', 2: 'Not normal', 3: 'Normal'}
    result = getResult(img)
    predicted_class = np.asscalar(np.argmax(result, axis=1))
    accuracy = round(result[0][predicted_class] * 100, 2)
    label = indices[predicted_class]
    results = {
        "label": label,
        "accuracy": accuracy
    }
    return results
</pre>
"""
        },
    ]


# graph = tf.get_default_graph()
# with graph.as_default():
#     # load model at very first
#     model = load_model("./static/" + 'model_design.h5')


# def classification(img):
#     indices = {0: 'Cat', 1: 'Dog', 2: 'Not normal', 3: 'Normal'}
#     data = image.load_img(imagePath, target_size=(150, 150, 3))
#     data = np.expand_dims(data, axis=0)
#     data = data * 1.0 / 255
#     result = None
#     with graph.as_default():
#         predicted = model.predict(data)
#         result = predicted
#     predicted_class = np.asscalar(np.argmax(result, axis=1))
#     accuracy = round(result[0][predicted_class] * 100, 2)
#     label = indices[predicted_class]
#     results = {
#         "label": label,
#         "accuracy": accuracy
#     }
#     return results


# def getResult(imagePath):
