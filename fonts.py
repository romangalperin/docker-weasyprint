from weasyprint import CSS
from weasyprint.fonts import FontConfiguration

def css_for_extra_fonts():
    font_config = FontConfiguration()
    return CSS(string='''
        @font-face {
            font-family: 'BC Sans Regular';
            src: local('BCSans-Regular');
        }
        @font-face {
            font-family: 'BC Sans Bold';
            src: local('BCSans-Bold');
        }
        @font-face {
            font-family: 'BC Sans Bold Italic';
            src: local('BCSans-BoldItalic');
        }
        @font-face {
            font-family: 'BC Sans Italic';
            src: local('BCSans-Italic');
        }
        @font-face {
            font-family: 'Noto Sans Light';
            src: local('NotoSans-Light');
        }
        @font-face {
            font-family: 'Noto Sans Light Italic';
            src: local('NotoSans-LightItalic');
        }
        @font-face {
            font-family: 'Montserrat';
            src: local('Montserrat-Regular');
        }
        @font-face {
            font-family: 'Montserrat Light';
            src: local('Montserrat-Light');
        }
        @font-face {
  font-family: Fira Sans;
  font-weight: 400;
  src: url(firasans-regular.otf);
}

@page {
  @top-left {
    background: #fbc847;
    content: counter(page);
    height: 1cm;
    text-align: center;
    width: 1cm;
  }
  @top-center {
    background: #fbc847;
    content: '';
    display: block;
    height: .05cm;
    opacity: .5;
    width: 100%;
  }
  @top-right {
    content: string(heading);
    font-size: 9pt;
    height: 1cm;
    vertical-align: middle;
    width: 100%;
  }
}

html {
  color: #393939;
  font-family: 'Montserrat Bold'';
  font-size: 36pt;
  font-weight: 300;
  line-height: 1.5;
  background: #fbc847;
}

body {
    font-family: 'Montserrat';font-size: 22px;
    background: #fbc847;
}

#cover {
  align-content: space-between;
  display: flex;
  flex-wrap: wrap;
  height: 297mm;
}
#cover address {
  background: #fbc847;
  flex: 1 50%;
  margin: 0 -2cm;
  padding: 1cm 0;
  white-space: pre-wrap;
  font-family: 'Montserrat Bold';font-size: 22px;
}
#cover address:first-of-type {
  padding-left: 3cm;
}

        ''', font_config=font_config), font_config
