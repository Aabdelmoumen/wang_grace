# colors_map = {"1": "#3790ca", "2": "#fec10c", "3": "#50b054"}
# main_color = "#3790ca"
# hover_color = "#3790ca"


pages_theme = """



QWidget{

background-color : #2c313c;
font: 14px "Poppins";
color : white ; 

}

QProgressBar {
    border: none;
    border-radius: 1px;
	background : rgba(120, 123, 128, 1)
}

QProgressBar::chunk {
    background-color: main_color;
}


QPushButton{ 
background-color: main_color ;
border-radius: 5px;
color : white ;
border: none;
font: 14px "Poppins";
padding-top : 7px ;
padding-bottom : 7px ;
padding-right : 27px ;
padding-left : 27px ;
 }
QPushButton:hover{
background-color: hover_color ;
border: 1px solid white;
padding : 4px ;
}



QLineEdit {
background-color: #1b1e23 ;
border-radius: 5px;
color : #858585 ;
border: 1px solid #858585;
padding-left: 12px;

}
QLineEdit:hover {
	border: 2px solid main_color ;
}
QLineEdit:focus {
	border: 2px solid  main_color;
	color :  #363636 ;
}



QComboBox {
border-radius: 0px;
color :white  ;
border: 1px solid main_color;
padding-left: 12px;
padding-right: 12px;
padding-top : 7px ;
padding-bottom : 7px ;

}



QComboBox:!editable, QComboBox::drop-down:editable {
    background-color : #1b1e23  ;
}


QComboBox::drop-down {
  	subcontrol-origin: padding;
    subcontrol-position: top left;
    border-left-width: 0px;
    border-left-style: solid; /* just a single line */
    
}

QComboBox::down-arrow {

    image: url(:/image/DownArrow_white.png);
 	width: 16px; 
 	height: 16px;
	padding-left : 10px;
}

"""
vertical_panel_theme = """
QWidget{
    background-color : #1b1e23 ;
}

QRadioButton{ 
    background-color :  transparent;
    border : none ;
    Text-align:left;
    padding-left : 15px;
    color : #858585;
    font: 14px "Poppins";

}

QRadioButton:hover{
    background-color: rgba(55,144,202 , 30);

}

QRadioButton:checked{
    color : white ; 
    background-color: rgba(55,144,202 , 30);
    border-bottom: 0px;
    border-top: 0px;
    border-right: 0px;
    border-left: 3px  solid main_color; 
    padding-left: 12px;
    Text-align:left;
}

QRadioButton::indicator {
    width:0px;
    height : 0px;
    border-radius:0px;
}

"""
