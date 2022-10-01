
def check_digital_downloads(request):
    digital_download_enabled = False

    if request.GET:
        if 'format' in request.GET:
            format = request.GET['format']
            if format == 'digital_download':
                digital_download_enabled = True

    context = {
        'digital_download_enabled': digital_download_enabled
    }

    return context

