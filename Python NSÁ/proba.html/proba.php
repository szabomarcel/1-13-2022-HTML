<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    <title>hajduszoboszlo</title>
</head>
<style>
    .body{
        border-radius: 5px;
        background-color: black;
        border-style: groove;
        padding: 5px;
        border: solid; ;
    }
</style>
<body>
<?php
echo "My first PHP script!";
?>
<!-- A grey horizontal navbar that becomes vertical on small screens -->
<nav class="navbar navbar-expand-sm bg-light">
    <a class="navbar-brand" href="#">Hajduszoboszlo</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" dattarget="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>   
    </button>
    <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <!--Links-->
        <ul class="navbar-nav">
            <dd><li class="nav-item"><a href="https://nlc.p3k.hu/uploads/2020/08/napi-horoszkop-hetfo-alt.jpg">Hétfő </a></li></dd>
            <br>
            <dd><li class="nav-item"><a href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJsTT3C4358lmNPQhxx7Tlz2gWNVJyFeTA_A&usqp=CAU">Kedd </a></li></dd>
            <br>
            <dd><li class="nav-item"><a href="https://tanarnocafe.hu/wp-content/uploads/2015/12/SZERDA.jpg">Szerda </a></li></dd>
            <br>
            <dd><li class="nav-item"><a href="https://cdn.agrarszektor.hu/images/articles/daily/4_md.jpg">Csütörtök </a></li></dd>
            <br>
            <dd><li class="nav-item"><a href="http://www.diszpolgar.hu/sites/default/files/styles/big_800x600_/public/kultura/pentek.jpg?itok=FpitynLo">Péntek </a></li></dd>
            <br>
            <dd><li class="nav-item"><a href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXucPXt4V0q_W6-12pcdv83kf7whQVD-xY7g&usqp=CAU">Szombat</a></li></dd>
            <br>
            <dd><li class="nav-item"><a href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9uBxskX0kLnFH2AxJLoeqQEitLitrcyNh3w&usqp=CAU">Vasárnap </a></li></dd>
        </ul>
    </div>
    </nav>
    <div class="container mt-3">
        <h2>További elérhetőségünk</h2>
        <p>Kattintson a gombra a tartalom megjelenítése és elrejtése közötti váltáshoz.</p>
        <button type="button" class="btn btn-primary" data-bs-toggle="collapse" data-bs-target="#demo">Egyszerű összecsukható részletek rálatintás</button>
        <div id="demo" class="collapse">
            <p>További alkalmaink</p>
            <a href=""><p>Szombaton ifinap</p></a>
            <a href=""><p>Vasárnap istentisztelet</p></a>
        </div>
    <a href="https://www.google.com">
        <button onclick="doSomething()" style="background-color: #333333;color:#00FF00;border-radius: 5px;">Click me</button>
    </a>
    <p>A szöveg megfelelője gyakorlatilag az összes európai nyelvben "Text" (különböző írásképekkel a nemzeti helyesírás miatt), ami a latin "textum" szóból ered, amely szó eredeti jelentése: szövet, szöveg. A magyarban a nyelvújítás idején a jelentést magyar szóval jelöltük. A szöveg egy összefüggő és a környezetétől jól elhatárolt vagy elhatárolható megnyilvánulás, kijelentés írott vagy tágabb értelemben nem írott de (le)írható nyelven. A nem feltétlenül írott, de leírható szövegre példa a dalszöveg, egy film szövege vagy improvizált színházi szöveg.

        Egy szöveg ábrázolásához szükség van írásra is, amely eszköztárával (pl. betűkkel) fonémákat, szótagokat, ill. szavakat és fogalmakat kódol. Különböző kultúrák és korok erre a célra különböző jelrendszert használnak. A szöveg egyik legfontosabb és megkerülhetetlen (immanens) tulajdonsága, amelyet mind az író mind az olvasó kénytelen követni (ha a szöveget olvasni akarja) a linearitás.
        
        Az írott szöveg az emberiség történelmében hatalmas előrelépés, hiszen így a történelme folyamán egyedüli módon lehetővé vált az információ személytől térben és időben független tárolása szemben a szájhagyománnyal, amely mind térben mind időben adott személyhez vagy személyekhez kötött. A történelemről ránk maradt információk legnagyobb része a XX. századig írásos szövegemlékekből áll. Azok a szövegek, amelyek olyan kultúráktól származnak, ahol az írásos információrögzítés létezik, a szövegek felépítése alapvetően különbözik az olyan kultúrák szövegeitől, ahol információk csak szájhagyomány útján maradtak fenn. A társadalomtudományokban a szöveges hagyomány nélküli kultúrákat nagyrészt az ókori ill. történelme előtti kultúrákhoz sorolják. Így a társadalomtudományban létezik a kultúrának egy olyan fontos meghatározása, amelynek alapjául közvetetten bár de a szöveg szolgál.</p>
        <div class="container mt-3">
            <h2>Elhérhetőségünk</h2>
            <p>HSZBgy menu:</p>
            <ul class="nav">
              <li class="nav-item">
                <a class="nav-link" href="https://www.google.com/maps/@47.4435665,21.3867505,3a,75y,225.51h,89.74t/data=!3m6!1e1!3m4!1sEN4bJBealhD7EE8X5odrjg!2e0!7i16384!8i8192?hl=hu">Térkép</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="https://www.facebook.com/profile.php?id=100008371812916">Facebook oldalunk</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="http://www.hajduszoboszlo.baptist.hu/">Másik oldalnk</a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" href="#">Szerettettel várunk</a>
              </li>
            </ul>
          </div>
    </body>
</html>