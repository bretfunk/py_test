from gtts import gTTS
import boto3

phrase = "test phrase"
language = "en"
file_name = "test_filename"


#create file
tts = gTTS(text=phrase, lang=language)
tts.save("./temp/{}/{}.mp3".format(language, file_name))

bucket = 'elasticbeanstalk-us-west-2-747213477632'
s3_client = boto3.client('s3')

# Upload the file to S3
s3_client.upload_file("./temp/{}/{}.mp3".format(language, file_name), bucket, "{}/{}.mp3".format(language, file_name))
