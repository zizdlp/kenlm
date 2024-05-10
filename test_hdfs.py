from hdfs import InsecureClient
def list_hdfs_files(hdfs_client, hdfs_path):
    # List the contents of the directory
    try:
        files = hdfs_client.list(path)
        print("Files in directory:")
        for file in files:
            print(file)
    except Exception as e:
        print("Failed to list directory:", e)
def check_hdfs_path_exists(hdfs_client, hdfs_path):
    try:
        hdfs_client.status(hdfs_path)
        return True
    except:
        return False
if __name__ =="__main__":
    import pyarrow.fs
    fs = pyarrow.fs.HadoopFileSystem('node0', 9898)


    # hdfs_client = InsecureClient(f"hdfs://node0:9898/")
    # root_status = hdfs_client.status('/')
# if __name__=="__main__":
#     namenode="node0"
#     port=9898
#     # hdfs_client = InsecureClient(f"hdfs://node0:9898/")
#     url='http://node0:9870'
#     hdfs_client = InsecureClient("http://node0:9870")
#     root_status = hdfs_client.status('/data0')
#     # Try to list the root directory to check if the client is established successfully
#     try:
#         root_status = hdfs_client.status('/')
#         print("Client connected successfully to HDFS.")
#     except Exception as e:
#         print("Failed to connect to HDFS:", e)
#     path="/data0/k8s/node0_data/ccnet_spark/cached_data/"
#     # path="/data0/k8s/node0_data/ccnet_spark/cached_data/"
#     res=check_hdfs_path_exists(hdfs_client,path)
#     list_hdfs_files(hdfs_client,path)
#     print(f"check is:{res}")
# def save_partition(spark_df, use_hdfs: bool, output_dir: str, dump: str = "2019-09", isSample: bool = False, sampleRate: float = 0.1, min_len: int = 300):
#     if use_hdfs:
#         hdfs_client = InsecureClient("<namenode>:<port>")
#         saved_sdf_name = "_sampleRate_" + str(int(sampleRate * 100 if isSample else 100)) + "_min_len_" + str(min_len) + ".parquet"
#         saved_sdf_path = os.path.join(output_dir, "result_sdf_parquet", dump, saved_sdf_name)
#         saved_sdf_path = convert_to_absolute_path(saved_sdf_path)
#         if not check_hdfs_path_exists(hdfs_client, saved_sdf_path):
#             hdfs_client.makedirs(saved_sdf_path, permission=777, recreate=False)
#             spark_df.write.mode("overwrite").partitionBy("lang", "bucket").parquet(f"{saved_sdf_path}")
#     else:
#         saved_sdf_name = "_sampleRate_" + str(int(sampleRate * 100 if isSample else 100)) + "_min_len_" + str(min_len) + ".parquet"
#         saved_sdf_path = os.path.join(output_dir, "result_sdf_parquet", dump, saved_sdf_name)
#         saved_sdf_path = convert_to_absolute_path(saved_sdf_path)
#         if not os.path.exists(saved_sdf_path):
#             os.makedirs("/".join(saved_sdf_path.split("/")[:-1]), exist_ok=True)
#             spark_df.write.mode("overwrite").partitionBy("lang", "bucket").parquet(f"{saved_sdf_path}")
