from gtts import gTTS
import boto as boto
import boto3
import soundfile as sf


tts = gTTS(text='Hello', lang='en')
tts.save("./temp/hello.mp3")

# s3 = boto3.client('s3')
# with open('./temp/hello.mp3', 'rb') as data:
        # s3.upload_fileobj(data, 'elasticbeanstalk-us-west-2-747213477632', 'AKIAJM3MQIWK3A64BR6A')

s3_connection = boto.connect_s3()
bucket = s3_connection.get_bucket('elasticbeanstalk-us-west-2-747213477632')
key = boto.s3.key.Key(bucket, 'AKIAJM3MQIWK3A64BR6A')
key.send_file('./temp/hello.mp3')
# with open('./temp/hello.mp3') as f:
        # key.send_file(f)
