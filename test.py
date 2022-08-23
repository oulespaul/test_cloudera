from pywebhdfs.webhdfs import PyWebHdfsClient
from pprint import pprint

hdfs = PyWebHdfsClient(host='10.121.101.130',port='50070', user_name='cloudera')  # your Namenode IP & username here
my_dir = '/user/cloudera/test_cloudera'
hdfs.make_dir(my_dir)
hdfs.make_dir(my_dir, permission=755)

#my_data = '01010101010101010101010101010101'
#my_file = my_dir+'/test2.txt'
#hdfs.create_file(my_file, my_data, overwrite=True)

with open('/home/mastermakerdev/test_cloudera/test.txt') as file_data:
    my_data = file_data.read()
    hdfs.create_file(my_dir+'/text.txt', my_data, overwrite=True)

pprint(hdfs.list_dir(my_dir))
