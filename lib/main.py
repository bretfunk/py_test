from gtts import gTTS
import boto3


#already working, DONT DELETE
tts = gTTS(text='Hello', lang='en')
tts.save("./temp/hello.mp3")

bucket = 'elasticbeanstalk-us-west-2-747213477632'
s3_client = boto3.client('s3')

# Upload the file to S3
s3_client.upload_file('./temp/hello.mp3', bucket, 'hello-remote.mp3')
