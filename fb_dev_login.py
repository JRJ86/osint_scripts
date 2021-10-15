import facebook

access_token = 'EAAMi1YIWPXMBACZBm3RS7f6ZC69QpTSZAp0eedIAr8xn4l8n4k8AXYFZBizqQYX45YspmV33AkFpbXYKwfByC1' \
               'h56RxiTVCWz7YpEovkr0ZCZBHb4RSNZBnYsZAyxPySnbsZAxrXEu6piHmk3uBRwRTuCCCwEp5ZBsmsKm8WKleCG' \
               'F4ImZBTnEo6V1QZBT06505DZBDgk4etEIGeZAZAWBhIfuWxuhCZB4j3KNNPvWy7RBVdnjVfi76XC0vThB4rvMQRSCOZCAz4ZD'

fb = facebook.GraphAPI(access_token=access_token)
fb.put_object()
