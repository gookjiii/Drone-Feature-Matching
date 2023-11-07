import requests
#Add base map
service_url = "mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
service_uri = "type=xyz&zmin=0&zmax=21&url=https://"+requests.utils.quote(service_url)
tms_layer = iface.addRasterLayer(service_uri, "Google Sat", "wms")
canvas = iface.mapCanvas()

#Add data to set_up
f = open('D:/CyberIntellect/FeatureMatching/set_up.txt')
x = float(f.readline())
y = float(f.readline())
Scale = int(f.readline())
resolution_x = int(f.readline())
resolution_y = int(f.readline())

#Set up
canvas.setCenter(QgsPointXY(x, y))
canvas.zoomScale(Scale)
img = QImage(QSize(resolution_x, resolution_y), QImage.Format_ARGB32_Premultiplied)
img.setDotsPerMeterX(1)
img.setDotsPerMeterY(1)

ms = QgsMapSettings()

p = QPainter()
p.begin(img)
p.setRenderHint(QPainter.Antialiasing)

layers = list(reversed([lyr for lyr in QgsProject.instance().mapLayers().values()]))
ms.setLayers(layers)

rect = iface.mapCanvas().extent()
rect.scale(1.1)
ms.setExtent(rect)

ms.setOutputSize(img.size())

render = QgsMapRendererCustomPainterJob(ms, p)
render.start()
render.waitForFinished()
p.end()

#Save
img.save('D:/CyberIntellect/FeatureMatching/images/img4.png')
