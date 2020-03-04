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
          <li class="breadcrumb-item active">Carátula 1</li>
          <li class="breadcrumb-item"><a href="index2.html">Carátula 2</a></li>
          <li class="breadcrumb-item"><a href="index3.html">Carátula 3</a></li>
        </ol>
    </nav>


 <?php
 echo '<center><h1>DATOS EN TIEMPO REAL</h1></center>';
 echo '<center><h1>********SCAIZEN**********</h1></center>';

 $comando = escapeshellcmd('python3 dict2json.py');
 $salida = shell_exec($comando);
 $arreglov = json_decode($salida,true);
 //$i=0;
 //echo $arreglov;
 //echo $salida;
 //echo gettype($arreglov);
 /*foreach ($arreglov as $item) {
    if (gettype($item)=='array') {
        //echo 'a';
        foreach ($item as $data) {    	
            //echo '<p>'.$data.'</p>';
            if (gettype($data)=='array') {
                //echo 'a';
                foreach ($data as $info) {    	
                    echo '<p>'.$info.'</p>';
                }
            }else{
                //echo 'b';
                echo '<p>'.$data.'</p>';
            }
        }
    }else{
        //echo 'b';
        echo '<p>'.$item.'</p>';
    }
 }*/
 //echo $arreglov['timestamp'];
 //$obj1 = $arreglov['ucl'];
 //$obj2 = $obj1['data_orden'];
 //echo $obj2['cantidad_programada'];
 ?>    

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
                            <td class="tg-dvid" colspan="4">PRODUCTO: RGL-201---------------

<?php
 echo $arreglov['timestamp'];
?>
---------------------ESTADO: DISPONIBLE</td>
                          </tr>
                          <tr>
                            <td class="tg-dvid"></td>
                            <td class="tg-k3k5">OBJETIVO</td>
                            <td class="tg-k3k5">REPARTIÓ</td>
                            <td class="tg-k3k5">MEDIDOR</td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">IV:</td>

<?php
 $obj1 = $arreglov['ucl'];
 $obj2 = $obj1['data_orden'];
?>
                            <td class="tg-yz93" rowspan="3"><?php echo $obj2['cantidad_programada']; ?></td>
                            <td class="tg-dvpl"><?php echo round($obj2['cantidad_componente']*.97); ?></td>
                            <td class="tg-dvpl"><?php echo round($obj2['cantidad_componente']*.97); ?></td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">GOV:</td>
                            <td class="tg-dvpl"><?php echo $obj2['cantidad_cargada']; ?></td>
                            <td class="tg-dvpl"><?php echo $obj2['cantidad_cargada']; ?></td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">GSV:</td>
                            <td class="tg-dvpl"><?php echo $obj2['cantidad_gsv']; ?></td>
                            <td class="tg-dvpl"><?php echo $obj2['cantidad_gsv']; ?></td>
                          </tr>
<?php
 $obj1 = $arreglov['caudalimetro'];
 $obj2 = $obj1['data'];
?>
                          <tr>
                            <td class="tg-6e8n" colspan="2">MASA:</td>
                            <td class="tg-dvpl"><?php echo $obj2['masaTR']; ?></td>
                            <td class="tg-dvpl"><?php echo $obj2['masaTR']; ?></td>
                          </tr>
<?php
 $obj1 = $arreglov['rtd'];
 $obj2 = $obj1['data'];
?>
                          <tr>
                            <td class="tg-6e8n" colspan="2">AVG. TEMP (C):</td>
                            <td class="tg-dvpl"><?php echo $obj2['temperaturaAvg']/100; ?></td>
                            <td class="tg-dvpl"><?php echo $obj2['temperaturaTR']/100; ?></td>
                          </tr>
<?php
 $obj1 = $arreglov['baumanometro'];
 $obj2 = $obj1['data'];
?>
                          <tr>
                            <td class="tg-6e8n" colspan="2">AVG. PRESIÓN:</td>
                            <td class="tg-dvpl"><?php echo $obj2['presionPreset']/100; ?></td>
                            <td class="tg-dvpl"><?php echo $obj2['presionTR']/100; ?></td>
                          </tr>
<?php
 $obj1 = $arreglov['densimetro'];
 $obj2 = $obj1['data'];
?>
                          <tr>
                            <td class="tg-6e8n" colspan="2">AVG. DENSIDAD:</td>
                            <td class="tg-dvpl"><?php echo $obj2['densidadComponent']/10; ?></td>
                            <td class="tg-dvpl"><?php echo $obj2['densidadTR']/10; ?></td>
                          </tr>
<?php
 $obj1 = $arreglov['mdp'];
 $obj2 = $obj1['data'];
?>
                          <tr>
                            <td class="tg-6e8n">CTPL(TAB54B)</td>
                            <td class="tg-dvpl">0.9958</td>
                            <td class="tg-pvvw">FLUJO:</td>
                            <td class="tg-dvpl"><?php echo $obj2['flujoTR']; ?></td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">CTL:</td>
                            <td class="tg-dvpl">0.9958</td>
<?php
 $obj1 = $arreglov['kFactor'];
 $obj2 = $obj1['data'];
?>
                            <td class="tg-pvvw">K-FACTOR:</td>
                            <td class="tg-dvpl"><?php echo $obj2['kFactor']; ?></td>
                          </tr>
                          <tr>
                            <td class="tg-6e8n">CPL:</td>
                            <td class="tg-dvpl">1.0000</td>
                            <td class="tg-pvvw">METER FAC:</td>
                            <td class="tg-dvpl">1.0000</td>
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
