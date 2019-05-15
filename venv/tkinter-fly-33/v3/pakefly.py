import configparser
#第一步生成相应ConfigParser的实例
cfg  = configparser.ConfigParser()

# 生成实例后需要读入相应的配置文件,某些該死相容性的問題導致需要聲明encoding
cfg.read("pakefly.cfg",encoding = 'utf-8-sig')
#提取對象值
sp_name = cfg.get("SmallPlane", "name")
print(sp_name)
#獲取int整數型的
sp_width = cfg.getint("SmallPlane", "width")
print(sp_width)
