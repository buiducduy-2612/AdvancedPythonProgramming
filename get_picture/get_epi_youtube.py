API_KEY  = '' (yêu cầu nhập mật khẩu )
video_id = [ '7cmvABXyUC0' ]
url  =  "https://www.googleapis.com/youtube/v3/video?id=" + video_id + "& part = Statistics & key =" + API_KEY
đáp ứng  =  yêu cầu . lấy ( url ). json ()
in ( phản hồi )
