from botocore.model import NOT_SET
import uploadFile as up

res = up.upload_file('test.py', 's3bucket-dk', None)

print(res)