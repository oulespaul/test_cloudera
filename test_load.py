from pywebhdfs.webhdfs import PyWebHdfsClient

hdfs = PyWebHdfsClient(host='10.121.101.130',port='50070', user_name='hdfs')  # your Namenode IP & username here
my_file = '/raw/index_dashboard/File_Upload/GCR_2017-19_20Dataset.xlsx'

data = hdfs.read_file(my_file)
with open('out_load.xlsx', 'wb') as file:
    file.write(data)
    file.close()
