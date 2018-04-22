from PIL import Image

img = Image.new('RGB',(352,288),'white')

def imgRead(loc):
    in_file = open(loc, "rb") # opening for [r]eading as [b]inary
    # print(loc)
    data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
    # print(data.__len__())
    global img
    # img.show()
    pixels = img.load()
    # pixels[351,100]=(1,177,177)
    # img.show()
    lim =data.__len__()
    # print(data)
    ba = []
    pos = 0
    while(pos<lim):
        in_file.seek(pos)
        ba.append(int.from_bytes(in_file.read(1), byteorder='big'))
        # print(ba[pos])
        pos+=1
    ind =0
    for y in range(0,288):
        for x in range(0,352):
            pixels[x, y] = (ba[ind],ba[ind+(288*352)],ba[ind+(288*352*2)])
            ind+=1
    # print(pos)
    # print(ind)
    # for y in range(0,288):
    #     for x in range(0,352):
    #         print("%s %s"%(pixels[x,y],(y+1)))
    #         ind+1
    in_file.close()
    return img
    # img.show()

#remove the lines below after you have integrated the function above with the class you want
# send_address_here="first003.rgb"
# imgRead(send_address_here)
# img.save('takealook.png')

# out_file = open("out-file", "wb") # open for [w]riting as [b]inary
# out_file.write(data)
# out_file.close()

# imgRead("first001.rgb")
