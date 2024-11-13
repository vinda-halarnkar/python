import django.core.files.storage
from PIL import Image
from django.conf import settings
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .forms import DocumentForm
import boto3
import io
from django.core.files.storage import default_storage
# Create your views here.


def upload_document(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']

        try:
            image = Image.open(file)

            # Optional: Resize the image (e.g., to 800x800)
            image.thumbnail((800, 800))

            # Save the resized image to an in-memory file
            in_mem_file = io.BytesIO()
            image_format = image.format if image.format else 'JPEG'
            image.save(in_mem_file, format=image_format)
            in_mem_file.seek(0)

        except Exception as e:
            return render(request, 'upload.html', {'error': str(e)})

        # Save the file to S3 using Django's storage system
        file_name = file.name
        file_content = ContentFile(in_mem_file.read(), name=file_name)
        file_path = default_storage.save(file_name, file_content)
        # Construct the file URL
        file_url = default_storage.url(file_path)

        # Upload the file to S3
        # s3_client = boto3.client(
        #     's3',
        #     aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
        #     aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY,
        #     region_name=settings.AWS_S3_REGION_NAME
        # )
        #
        # s3_client.upload_fileobj(
        #     in_mem_file,
        #     settings.AWS_STORAGE_BUCKET_NAME,
        #     file.name
        # )

        # file_url_formulated = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/{file.name}"
        # file_url = s3_client.generate_presigned_url(
        #     'get_object',
        #     Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': file.name},
        #     ExpiresIn=3600  # 1 hour expiration
        # )

        return render(request, 'upload.html', {'file_url': file_url})
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})