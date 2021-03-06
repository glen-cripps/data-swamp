import arrow
today_dt = arrow.now().format('YYYYMMDD')

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import StringType, StructType, StructField
from pyspark.sql.functions import col



sc = SparkContext()


#df = sqlc.read.parquet(f_full_path)

#df.show()
#df.printSchema()

#df2.show()
#df2.printSchema()


URI           = sc._gateway.jvm.java.net.URI
Path          = sc._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem    = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
Configuration = sc._gateway.jvm.org.apache.hadoop.conf.Configuration


fs = FileSystem.get(URI("hdfs://localhost:54310"), Configuration())

status = fs.listStatus(Path('/bigdata/rdl/'))

print(dir(fs))
print(dir(status))
for fileStatus in status:
    print fileStatus.getPath()
    print(dir(fileStatus))
    mod_time = fileStatus.getModificationTime.ToString()
    print(mod_time)
    print(mod_time)
    print(dir(mod_time))
    print (fileStatus.getOwner)
    print (fileStatus.getGroup)
#    print(dir(status))
#    print(dir(fs))
