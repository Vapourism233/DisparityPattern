import os
import datetime
import numpy as np
import cv2
import urllib.request
import requests
import multiprocessing


inputlist = [
    "10.1.31.4"
    # "10.0.31.101",
    # "10.0.31.102",
    # "10.0.31.103",
    # "10.0.31.104",
    # "10.0.31.105",
    # "10.0.31.106",
    # "10.0.31.107",
    # "10.0.31.108",
    # "10.0.31.109",
    # "10.0.31.110",
    # "10.0.31.111",
    # "10.0.31.112",
    # "10.0.31.113",
    # "10.0.31.114",
    # "10.0.31.115",
    # "10.0.31.116",
    # "10.0.31.117",
    # "10.0.31.118",
    # "10.0.31.119",
    # "10.0.31.120",
    # "10.0.31.121",
    # "10.0.31.139",
    # "10.0.31.140",
    # "10.0.31.141",
    # "10.0.31.142",
    # "10.0.31.143",
]

__use_password = False
__user = "user"
__password = "OALOBQhMhNY.qfuWhwgyp7Cm"

def main():
    folderpath = create_folder()
    for cam_ip in inputlist:
        save_necessary_images(cam_ip, folderpath)
    

    #cv2.destroyAllWindows()

def save_necessary_images(cam_ip, folderpath):
    baseurl = "http://" + cam_ip
    baseurl8081 = "http://" + cam_ip + ":8081"
    if __use_password:
        set_user_and_pass(baseurl)
        set_user_and_pass(baseurl8081)

    for i in range(3):
        #get_and_save_localgrid(cam_ip, folderpath)
        #get_and_save_disparity(cam_ip, folderpath)
        get_and_save_rawimg(cam_ip, folderpath)
        #get_and_save_tiff(cam_ip, folderpath)

def create_folder()-> str:
    path = os.path.dirname(__file__)
    now = datetime.datetime.now()
    foldername = now.strftime('%Y%m%d')
    folder_path = os.path.join(path, foldername)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def get_and_save_disparity(ip, folderpath):
    urlAdress = "http://" + ip  + ":8081/disparityImage"
    req = urllib.request.urlopen(urlAdress)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    imgGrayscale = cv2.imdecode(arr, -1)
    #cv2.imshow("disparity", imgGrayscale)
    #cv2.waitKey(0)
    save_img(ip, folderpath, imgGrayscale)
    print("disparity of {} has been saved.".format(ip))

def get_and_save_localgrid(ip, folderpath):
    # TODO need to check URL for local grid
    urlAdress = "http://" + ip  + ":8081/grid"
    if __use_password:
        req = requests.get(urlAdress, auth=requests.auth.HTTPBasicAuth(__user, __password))
    else:
        req = requests.get(urlAdress)
    arr = np.asarray(bytearray(req.content), dtype=np.uint32)
    #img = cv2.imdecode(arr, -1)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    save_img(ip, folderpath, img)
    print("localgrid of {} has been saved.".format(ip))

def get_and_save_rawimg(ip, folderpath):
        url = "rtsp://{user}:{passwd}@{ip}".format(user=__user, passwd=__password, ip=ip)
        cap = cv2.VideoCapture(url)
        if cap.isOpened():
            ret, frame = cap.read()
            #cv2.imshow("streaming", frame)
            #cv2.waitKey(0)
            save_img(ip, folderpath, frame, "raw")
            cap.release()
            print("raw image of {} has been saved.".format(ip))

def get_and_save_tiff(ip, folderpath):
    url = "http://" + ip  + "/snap.tif?Cam=2&rectify=1&monochrome=1&prefetch=1&width=1920&height=1080"
    subfolder_name = get_subfolder_name(ip)
    now = datetime.datetime.now()
    filename = "tiff_" + now.strftime("%H%M%S_" + subfolder_name + ".tiff")
    fullpath = os.path.join(folderpath, subfolder_name, filename)
    #urllib.request.urlretrieve(url, fullpath)
    # with urllib.request.urlopen(url) as infile, open(fullpath, 'wb') as outfile:
    #     copyfileobj(infile, outfile)
    #     print("tiff file of {} has been saved.".format(ip))
    resut = requests.get(url, auth=requests.auth.HTTPBasicAuth(__user, __password))
    pass




def save_img(ip, folderpath, img, prefix="disparity"):
    subfolder_name = get_subfolder_name(ip)
    fullpath = os.path.join(folderpath, subfolder_name)
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)
    
    now = datetime.datetime.now()
    filename = prefix + "_" + now.strftime("%H%M%S_" + subfolder_name + ".png")
    return cv2.imwrite(os.path.join(fullpath, filename), img)

def get_subfolder_name(ip):
    end_ip = ip.split('.')[3]
    return "{num: 04d}".format(num=int(end_ip))

def set_user_and_pass(baseurl):
    pass_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pass_mgr.add_password(
        realm=None,
        uri=baseurl,
        user=__user,
        passwd=__password
    )
    ah = urllib.request.HTTPBasicAuthHandler(pass_mgr)
    opener = urllib.request.build_opener(ah)
    urllib.request.install_opener(opener)
    return urllib.request

if "__main__" == __name__:
    main()
