yêu cầu nhập mật khẩu
from  bs4  import  BeautifulSoup
nhập khẩu  os

# Khai báo url
url  =  'https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages'
# nô lệ r = request.get
r  =  yêu cầu . get ( url )
# satanh suop = BeautifulSuop (is 1 Package python to parship the HTML Synthetic)
suop  =  BeautifulSoup ( r . text , 'html.parser' )
# ánh xạ hình ảnh bằng suop.find_all để tìm tất cả các tệp img
hình ảnh  =  suop . find_all ( 'img' )

cho  hình ảnh  trong  hình ảnh :
    name =  images [ 'alt' ]
    link = ( 'https://developer.mozilla.org' + hình ảnh [ 'src' ])
    print ( tên , liên kết )
    với  open ( name . Replace ( '' , '-' ). Replace ( '/' , '' ) + '.jpg' , 'wb' ) là  f :
        im  =  yêu cầu . get ( liên kết )
        f . write ( im . nội dung )