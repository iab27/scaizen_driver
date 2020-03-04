<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SCAIZEN - Tiempo real</title>
<link rel="stylesheet" href="css/font-awesome.min.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<link rel="stylesheet" href="css/styles.css">
<script src="https://code.jquery.com/jquery-3.2.1.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:10px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:10px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-78na{background-color:#fe0000;color:#ffffff;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-pvvw{font-weight:bold;background-color:#c0c0c0;border-color:inherit;text-align:right;vertical-align:top}
.tg .tg-dvid{font-weight:bold;background-color:#efefef;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-1ke3{font-weight:bold;font-size:11px;font-family:"Arial Black", Gadget, sans-serif !important;;background-color:#fffc9e;color:#333333;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-k3k5{font-weight:bold;background-color:#999903;color:#ffffff;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-6e8n{font-weight:bold;background-color:#c0c0c0;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-yz93{border-color:inherit;text-align:right;vertical-align:middle}
.tg .tg-7719{background-color:#efefef;color:#333333;border-color:inherit;text-align:right;vertical-align:top}
.tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-zlqz{font-weight:bold;background-color:#c0c0c0;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-kftd{background-color:#efefef;text-align:left;vertical-align:top}
.tg .tg-fckf{background-color:#efefef;border-color:inherit;text-align:right;vertical-align:top}
.tg .tg-dvpl{border-color:inherit;text-align:right;vertical-align:top}
</style>
<script>

var current = 0;
var imagenes = new Array();

$(document).ready(function() {
    var numImages = 6;
    if (numImages <= 3) {
        $('.right-arrow').css('display', 'none');
        $('.left-arrow').css('display', 'none');
    }
	 
    $('.left-arrow').on('click',function() {
        if (current > 0) {
            current = current - 1;
        } else {
            current = numImages - 3;
        }
        
        $(".carrusel").animate({"left": -($('#product_'+current).position().left)}, 600);
        
        return false;
    });

    $('.left-arrow').on('hover', function() {
        $(this).css('opacity','0.5');
    }, function() {
        $(this).css('opacity','1');
    });

    $('.right-arrow').on('hover', function() {
        $(this).css('opacity','0.5');
    }, function() {
        $(this).css('opacity','1');
    });

    $('.right-arrow').on('click', function() {
        if (numImages > current + 3) {
            current = current+1;
        } else {
            current = 0;
        }
        
        $(".carrusel").animate({"left": -($('#product_'+current).position().left)}, 600);
        
        return false;
    }); 
 });
</script>
</head>

<body>
<nav class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark">
    <a class="navbar-brand" href="https://www.jose-aguilar.com/">
        <img src="https://www.jose-aguilar.com/blog/wp-content/themes/jaconsulting/images/jose-aguilar.png" width="30" height="30" alt="Jose Aguilar">
      </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
            <a class="nav-item nav-link active" href="https://www.jose-aguilar.com/scripts/jquery/carrousel-html/">Scaizen - Tiempo Real <span class="sr-only">(current)</span></a>
            <a class="nav-item nav-link" href="https://www.alba-dti.com/">&copy; INCOMEX, Puebla</a>
        </div>
    </div>
</nav>
<div class="container">
    <h1>Información en tiempo real</h1>
    
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
          <li class="breadcrumb-item"><a href="index.html">Carátula 1</a></li>
          <li class="breadcrumb-item active">Carpatula 2</li>
          <li class="breadcrumb-item"><a href="index3.html">Carátula 3</a></li>
        </ol>
    </nav>
    
    <div class="row">
        <div id="content" class="col-lg-12">
            
                        <table class="tg" style="undefined;table-layout: fixed; width: 462px">
                        <colgroup>
                        <col style="width: 126px">
                        <col style="width: 106px">
                        <col style="width: 118px">
                        <col style="width: 112px">
                        </colgroup>
                          <tr>
                            <th class="tg-1ke3" colspan="4">01 BRAZO 01 COMPONENTE ESTADO</th>
                          </tr>
                          <tr>
                            <td class="tg-dvid" colspan="4">PRODUCTO: Combustible Regular-----------------------------------------------ESTADO: Completa</td>
                          </tr>
                          <tr>
                            <td class="tg-dvid"></td>
                            <td class="tg-k3k5">SOLICITÓ</td>
                            <td class="tg-k3k5">FALTANTE</td>
                            <td class="tg-k3k5">REPARTIÓ</td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">IV:</td>
                            <td class="tg-yz93" rowspan="3">15000</td>
                            <td class="tg-yz93" rowspan="3">2</td>
                            <td class="tg-dvpl">14939.79</td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">GOV:</td>
                            <td class="tg-dvpl">14998.42</td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">GSV:</td>
                            <td class="tg-dvpl">14935.43</td>
                          </tr>
                          <tr>
                            <td class="tg-dvid" colspan="2"></td>
                            <td class="tg-hvgs">TOTAL</td>
                            <td class="tg-dvpl">14998.42</td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">Temp. LIVE</td>
                            <td class="tg-dvpl">0.00</td>
                            <td class="tg-6e8n">Temp AVG</td>
                            <td class="tg-dvpl">20.00</td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">Presión LIVE</td>
                            <td class="tg-dvpl">0.00</td>
                            <td class="tg-6e8n">Presión AVG</td>
                            <td class="tg-dvpl">0.00</td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">Densidad LIVE</td>
                            <td class="tg-dvpl">0.00</td>
                            <td class="tg-6e8n">Densidad AVG</td>
                            <td class="tg-dvpl">840.0</td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">BSW LIVE</td>
                            <td class="tg-dvpl">0.00%</td>
                            <td class="tg-6e8n">BSW AVG</td>
                            <td class="tg-p8y5">0.00%</td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">Flujo</td>
                            <td class="tg-dvpl">0</td>
                            <td class="tg-wrrr" colspan="2" rowspan="2"></td>
                          </tr>
                          <tr>
                            <td class="tg-dvid" colspan="2"></td>
                          </tr>
                          <tr>
                            <td class="tg-78na" colspan="4">Next     Prev    Exit</td>
                          </tr>
                        </table>
        </div>
    </div>
    
    <div class="row">
        <div class="col-lg-12">
            <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
            <!-- Bloque de anuncios adaptable -->
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-client="ca-pub-6676636635558550"
                 data-ad-slot="8523024962"
                 data-ad-format="auto"
                 data-full-width-responsive="true"></ins>
            <script>
            (adsbygoogle = window.adsbygoogle || []).push({});
            </script>
        </div>
    </div>
    
    
</div>
<footer class="footer bg-dark">
    <div class="container">
        <span class="text-muted"><a href="https://www.alba-dti.com/">&copy; ALBA-DTI, S. de R.L. de C.V.</a></span>
    </div>
</footer>
</body>
</html>
