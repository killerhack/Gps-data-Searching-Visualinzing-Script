#coding=utf-8
import folium,os
import MySQLdb
# f=open('location.txt','r')
# kerwin=folium.Map(location=[39.771409,116.370133],zoom_start=13)
# for line in f.readlines():
#     strl=line.strip()
#     strc='kerwin.simple_marker(['+strl+'])'
#     eval(strc)
# kerwin.simple_marker([39.771409,116.370133],popup=u"杀人案件")
# kerwin.create_map(path='kerwin.html')
# os.system('kerwin.html')
"""
kerwin=folium.Map(location=[39.771409,116.370133],zoom_start=13)
kerwin.simple_marker([39.771409,116.370133],popup=u"杀人案件")
kerwin.create_map(path='kerwin.html')
os.system('kerwin.html')
"""
conn = MySQLdb.connect(host="localhost",user="root",passwd="*******",db="data",charset="utf8")
cursor = conn.cursor()
print "Please input your Sql command,the system will automatically show the Locus Map for you"
sql = raw_input("PGIS-Locus-System>")
cursor.execute(sql)
f = open('location.txt','w')
for i in cursor.fetchall():
	lat,lon = i
	f.write(lat.to_eng_string()+','+lon.to_eng_string()+'\n')

f.close()

f=open('location.txt','r')
kerwin=folium.Map(location=[39.771409,116.370133],zoom_start=13)
for line in f.readlines():
    strl=line.strip()
    strc='kerwin.simple_marker(['+strl+'])'
    eval(strc)
# kerwin.simple_marker([39.771409,116.370133],popup=u"杀人案件")
kerwin.create_map(path='kerwin.html')
os.system('kerwin.html')