from PIL import Image
import os

failList = []

def pic_webp(picpath):
	picpathTmp = picpath.split(".")
	orgExt = picpathTmp.pop()
	imagePath = "".join(picpathTmp)
	outputPath = imagePath + ".webp"
	print(picpath + ' is change')
	try:
		im = Image.open(picpath)
		im.save(outputPath) 
		#os.remove(picpath)
		print(outputPath + ' is ok')
	except:
		failList.append(picpath + ' is fail')
		print(picpath + ' is fail')
	

for (dirpath,dirname,dirfile) in os.walk("/var/img_path"):
    for (item) in dirfile:
		if item.split(".")[-1] in ["png","jpeg","jpg"] :
			pic_webp(dirpath+"/"+item)

print('all is ok done')
print('-------fail list-------')
for failStr in failList:
	print(failStr)
print('-------fail list done-------')