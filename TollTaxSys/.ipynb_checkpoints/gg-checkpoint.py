{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "504db7c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running locally at: http://127.0.0.1:7863/\n",
      "To create a public link, set `share=True` in `launch()`.\n",
      "Interface loading below...\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"900\"\n",
       "            height=\"500\"\n",
       "            src=\"http://127.0.0.1:7863/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x17658043c40>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(<Flask 'gradio.networking'>, 'http://127.0.0.1:7863/', None)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import gradio as gr\n",
    "\n",
    "def greet(name):\n",
    "    return \"Hello \" + name + \" !.\"\n",
    "iface=gr.Interface(fn=greet,inputs=\"text\",outputs=\"text\")\n",
    "iface.launch()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8176196e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b31cdff2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: gradio in c:\\users\\hp\\anaconda3\\lib\\site-packages (2.3.4)\n",
      "Requirement already satisfied: ffmpy in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (0.3.0)\n",
      "Requirement already satisfied: flask-cachebuster in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (1.0.0)\n",
      "Requirement already satisfied: Flask>=1.1.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (1.1.2)\n",
      "Requirement already satisfied: numpy in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (1.20.1)\n",
      "Requirement already satisfied: Flask-Login in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (0.5.0)\n",
      "Requirement already satisfied: pycryptodome in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (3.10.1)\n",
      "Requirement already satisfied: paramiko in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (2.7.2)\n",
      "Requirement already satisfied: scipy in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (1.6.2)\n",
      "Requirement already satisfied: analytics-python in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (1.4.0)\n",
      "Requirement already satisfied: Flask-Cors>=3.0.8 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (3.0.10)\n",
      "Requirement already satisfied: markdown2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (2.4.1)\n",
      "Requirement already satisfied: matplotlib in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (3.3.4)\n",
      "Requirement already satisfied: pillow in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (8.2.0)\n",
      "Requirement already satisfied: requests in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (2.25.1)\n",
      "Requirement already satisfied: pandas in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gradio) (1.2.4)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask>=1.1.1->gradio) (1.1.0)\n",
      "Requirement already satisfied: click>=5.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask>=1.1.1->gradio) (7.1.2)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask>=1.1.1->gradio) (1.0.1)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask>=1.1.1->gradio) (2.11.3)\n",
      "Requirement already satisfied: Six in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Flask-Cors>=3.0.8->gradio) (1.15.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from Jinja2>=2.10.1->Flask>=1.1.1->gradio) (1.1.1)\n",
      "Requirement already satisfied: monotonic>=1.5 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from analytics-python->gradio) (1.6)\n",
      "Requirement already satisfied: backoff==1.10.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from analytics-python->gradio) (1.10.0)\n",
      "Requirement already satisfied: python-dateutil>2.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from analytics-python->gradio) (2.8.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests->gradio) (2020.12.5)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests->gradio) (4.0.0)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests->gradio) (1.26.4)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests->gradio) (2.10)\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->gradio) (1.3.1)\n",
      "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->gradio) (2.4.7)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->gradio) (0.10.0)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pandas->gradio) (2021.1)\n",
      "Requirement already satisfied: bcrypt>=3.1.3 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from paramiko->gradio) (3.2.0)\n",
      "Requirement already satisfied: pynacl>=1.0.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from paramiko->gradio) (1.4.0)\n",
      "Requirement already satisfied: cryptography>=2.5 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from paramiko->gradio) (3.4.7)\n",
      "Requirement already satisfied: cffi>=1.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from bcrypt>=3.1.3->paramiko->gradio) (1.14.5)\n",
      "Requirement already satisfied: pycparser in c:\\users\\hp\\anaconda3\\lib\\site-packages (from cffi>=1.1->bcrypt>=3.1.3->paramiko->gradio) (2.20)\n"
     ]
    }
   ],
   "source": [
    "! pip install gradio\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5932c99a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running locally at: http://127.0.0.1:7865/\n",
      "To create a public link, set `share=True` in `launch()`.\n",
      "Interface loading below...\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"900\"\n",
       "            height=\"500\"\n",
       "            src=\"http://127.0.0.1:7865/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1765ce80640>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(<Flask 'gradio.networking'>, 'http://127.0.0.1:7865/', None)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import gradio as gr\n",
    "\n",
    "def greet(name):\n",
    "    return \"Hello \" + name + \" !.\"\n",
    "iface=gr.Interface(fn=greet,inputs=gr.inputs.Textbox(lines=2,label=\"Name\", placeholder=\"Enter your name ....\"),outputs=\"text\")\n",
    "iface.launch()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "28c41e31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running locally at: http://127.0.0.1:7869/\n",
      "To create a public link, set `share=True` in `launch()`.\n",
      "Interface loading below...\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"900\"\n",
       "            height=\"500\"\n",
       "            src=\"http://127.0.0.1:7869/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1765cb3bb20>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(<Flask 'gradio.networking'>, 'http://127.0.0.1:7869/', None)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 3 inputs and 2 outputs\n",
    "import gradio as gr\n",
    "def greet(name,is_morning,temperature):\n",
    "    if is_morning:\n",
    "        salutation=\"Good morning\"\n",
    "    else:\n",
    "        salutation=\"Good evening\"\n",
    "    outputs=\"%s %s.It is %s degrees today\" %(salutation,name,temperature)\n",
    "    celsius = (temperature - 32) * 5 / 9\n",
    "    return outputs,round(celsius,2)\n",
    "iface=gr.Interface(fn=greet,inputs=[\"text\",\"checkbox\",gr.inputs.Slider(0,100)],outputs=[\"text\",\"number\"]) #inputs ke type,nd here we determine how many inputs\n",
    "#how many outputs,passed as list and separarted by commas,the paramteres of func act as label to text fields\n",
    "iface.launch()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "927b415d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running locally at: http://127.0.0.1:7886/\n",
      "To create a public link, set `share=True` in `launch()`.\n",
      "Interface loading below...\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"900\"\n",
       "            height=\"500\"\n",
       "            src=\"http://127.0.0.1:7886/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1765eb96e20>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(<Flask 'gradio.networking'>, 'http://127.0.0.1:7886/', None)"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Working with images\n",
    "import gradio as gr\n",
    "import numpy as np\n",
    "def images(img):\n",
    "    filter=np.array([[.255,.255,.255],[.255,.255,.255],[.255,.255,.255]]) #numpy array of b/w image\n",
    "    new_img=img.dot(filter.T)\n",
    "    new_img/=new_img.max()\n",
    "    return new_img\n",
    "iface=gr.Interface(images,gr.inputs.Image(shape=(200,200)),\"image\")\n",
    "iface.launch()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "2fb2d229",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running locally at: http://127.0.0.1:7888/\n",
      "To create a public link, set `share=True` in `launch()`.\n",
      "Interface loading below...\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"900\"\n",
       "            height=\"500\"\n",
       "            src=\"http://127.0.0.1:7888/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1766259c940>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(<Flask 'gradio.networking'>, 'http://127.0.0.1:7888/', None)"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[2021-09-20 20:40:42,063] ERROR in app: Exception on /api/predict/ [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\flask_cors\\extension.py\", line 165, in wrapped_function\n",
      "    return cors_after_request(app.make_response(f(*args, **kwargs)))\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\gradio\\networking.py\", line 92, in wrapper\n",
      "    return func(*args, **kwargs)\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\gradio\\networking.py\", line 180, in predict\n",
      "    prediction, durations = app.interface.process(raw_input)\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\gradio\\interface.py\", line 334, in process\n",
      "    predictions, durations = self.run_prediction(processed_input, return_duration=True)\n",
      "  File \"C:\\Users\\HP\\anaconda3\\lib\\site-packages\\gradio\\interface.py\", line 307, in run_prediction\n",
      "    prediction = predict_fn(*processed_input)\n",
      "  File \"<ipython-input-58-d21fc3b0e137>\", line 15, in detection\n",
      "    image = cv2.imread(image)\n",
      "TypeError: Can't convert object of type 'Tensor' to 'str' for 'filename'\n"
     ]
    }
   ],
   "source": [
    "import gradio as gr\n",
    "import pytesseract as pyt\n",
    "import numpy as np\n",
    "import cv2\n",
    "import torch\n",
    "import torchvision.models as models\n",
    "from torchvision import transforms\n",
    "import requests\n",
    "from PIL import Image\n",
    "\n",
    "def detection(img):\n",
    "                \n",
    "                \n",
    "                image = cv2.imread('C:/Users/HP/Documents/Python/TollTaxSys/test_noplates/c9.jpeg')\n",
    "                image=cv2.resize(image,(700,480))\n",
    "                pyt.pytesseract.tesseract_cmd = r'C:\\Users\\HP\\Downloads\\Tesseract-OCR\\tesseract.exe'\n",
    "\n",
    "                plateCascade = cv2.CascadeClassifier('')\n",
    "               \n",
    "\n",
    "                getCoordinates = plateCascade.detectMultiScale(image=image, scaleFactor=1.1,\n",
    "                                                            minNeighbors=4)  # returns 4 args-x,y,w,h\n",
    "\n",
    "                for (x, y, w, h) in getCoordinates:\n",
    "                    a, b = (int(0.02 * image.shape[0]), int(0.025 * image.shape[1]))\n",
    "                    plate = image[y:y + h, x:x + w]\n",
    "\n",
    "                    # image processing\n",
    "                    kernal = np.ones((1, 1), np.uint8)  # 1*1 matrix\n",
    "                    plate = cv2.dilate(src=plate, kernel=kernal, iterations=1)\n",
    "                    plate = cv2.erode(src=plate, kernel=kernal, iterations=1)\n",
    "                    # resize_test_license_plate = cv2.resize(plate, None, fx = 2.1, fy = 2.1,  interpolation = cv2.INTER_CUBIC)\n",
    "                    plateGray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)  # convert image to b/w\n",
    "                    # gray = cv2.bilateralFilter(plate, 11, 24, 26)\n",
    "                    #\n",
    "                    (thresh, plate) = cv2.threshold(plateGray, 127, 255,\n",
    "                                                    cv2.THRESH_BINARY_INV)  # image se numbers alg kro,threshold image\n",
    "                    # noise_removal=cv2.medianBlur(plate,5)\n",
    "\n",
    "                    # gaussian_blur_license_plate = cv2.GaussianBlur(plate, (5, 5), 0)\n",
    "                    text = pyt.image_to_string(plate)\n",
    "                    print(text)\n",
    "                    print(plate)\n",
    "                    text = ''.join(e for e in text if e.isalnum())  # remove blank spaces\n",
    "                    state = text[0:2]\n",
    "                    # print(states[state])\n",
    "                    \n",
    "                    # cv2.imwrite(filename='newPlate.png',img=plate)\n",
    "                cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(51, 51, 255), thickness=2)\n",
    "                cv2.rectangle(image,(x,y-40),(x+w,y),(51,51,255),-1)\n",
    "                cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)\n",
    "                return image\n",
    "iface=gr.Interface(detection,gr.inputs.Image(),\"image\")\n",
    "iface.launch()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "b96e7463",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pytesseract in c:\\users\\hp\\anaconda3\\lib\\site-packages (0.3.8)\n",
      "Requirement already satisfied: Pillow in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pytesseract) (8.2.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pytesseract\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5daa8cb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting opencv-python\n",
      "  Downloading opencv_python-4.5.3.56-cp38-cp38-win_amd64.whl (34.9 MB)\n",
      "Requirement already satisfied: numpy>=1.17.3 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from opencv-python) (1.20.1)\n",
      "Installing collected packages: opencv-python\n",
      "Successfully installed opencv-python-4.5.3.56\n"
     ]
    }
   ],
   "source": [
    "!pip install opencv-python\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "cb2bcc2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting torch\n",
      "  Downloading torch-1.9.0-cp38-cp38-win_amd64.whl (222.0 MB)\n",
      "Requirement already satisfied: typing-extensions in c:\\users\\hp\\anaconda3\\lib\\site-packages (from torch) (3.7.4.3)\n",
      "Installing collected packages: torch\n",
      "Successfully installed torch-1.9.0\n"
     ]
    }
   ],
   "source": [
    "!pip install torch\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "384658e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pillow in c:\\users\\hp\\anaconda3\\lib\\site-packages (8.2.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pillow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b76f4f37",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
