# -*- coding:utf-8 -*-from qiniu import Auth, put_file, etag, urlsafe_base64_encodeimport qiniu.configfrom pictureShare import appfrom qiniu import Auth,put_stream,put_dataaccess_key = app.config['QINIU_ACCESS_KEY']secret_key = app.config['QINIU_SECRET_KEY']bucket_name = app.config['QINIU_BUCKET_NAME']domain_host = app.config['QINIU_DOMAIN']q = Auth (access_key, secret_key)# 对接配置成功# 要上传的空间# 资源文件和保存的文件名def qiniu_upload_file(source_file, save_file_name):    # 生成上传 Token，可以指定过期时间等    token = q.upload_token(bucket_name, save_file_name)    ret, info = put_data(token, save_file_name, source_file.stream)    print type(info.status_code), info    if info.status_code == 200:        return domain_host + save_file_name    return None