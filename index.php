<?php
error_reporting(0);
header("Content-Type: application/json");

$soat = date('H:i', strtotime("2 hour"));
$sana2 = date("d.m.Y");


if (isset($_GET['city'])) {

    $text = $_GET['city'];
    $u = ucfirst($text);

    if ($text == "toshkent") {
        $r = "tashkent";
    } elseif ($text == "andijon") {
        $r = "andijan";
    } elseif ($text == "buxoro") {
        $r = "bukhara";
    } elseif ($text == "guliston") {
        $r = "gulistan";
    } elseif ($text == "jizzax") {
        $r = "jizzakh";
    } elseif ($text == "zarafshon") {
        $r = "zarafshan";
    } elseif ($text == "qarshi") {
        $r = "karshi";
    } elseif ($text == "navoiy") {
        $r = "navoi";
    } elseif ($text == "namangan") {
        $r = "namangan";
    } elseif ($text == "nukus") {
        $r = "nukus";
    } elseif ($text == "samarqand") {
        $r = "samarkand";
    } elseif ($text == "termiz") {
        $r = "termez";
    } elseif ($text == "urganch") {
        $r = "urgench";
    } elseif ($text == "fargona") {
        $r = "ferghana";
    } elseif ($text == "xiva") {
        $r = "khiva";
    }else{
        echo json_encode([
            [
                'ok' => false,
                'parameter' => "city",
                'shaharlar' => [
                    'toshkent',
                    'andijon',
                    'buxoro',
                    'guliston',
                    'jizzax',
                    'zarafshon',
                    'qarshi',
                    'navoiy',
                    'namangan',
                    'nukus',
                    'samarqand',
                    'termiz',
                    'urganch',
                    'fargona',
                    'xiva'
                ],
                'programer (t.me)' => "@visualcoderuz",
            ]
        ], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);

        exit();
    }

    $urganch = file_get_contents("https://obhavo.uz/$r");

    // bugungi

    $a = explode('<strong>', $urganch);
    $a1 = explode('</strong>', $a[1]);
    $a2 = $a1[0];
    $harorat = trim("$a2");

    $aa = explode('<div class="current-forecast-desc">', $urganch);
    $aa1 = explode('</div>', $aa[1]);
    $aa2 = $aa1[0];
    $tavsif = trim("$aa2");

    $b = explode('<div class="current-day">', $urganch);
    $b1 = explode('</div>', $b[1]);
    $b2 = $b1[0];
    $sana = trim("$b2");

    $c = explode('<p class="forecast">', $urganch);
    $c1 = explode('</p>', $c[1]);
    $c2 = $c1[0];
    $tong = trim("$c2");

    $d = explode('<p class="forecast">', $urganch);
    $d1 = explode('</p>', $d[2]);
    $d2 = $d1[0];
    $kun = trim("$d2");

    $e = explode('<p class="forecast">', $urganch);
    $e1 = explode('</p>', $e[3]);
    $e2 = $e1[0];
    $oqshom = trim("$e2");

    $f = explode('<p>', $urganch);
    $f1 = explode('</p>', $f[1]);
    $f2 = $f1[0];
    $namlik = trim("$f2");

    $g = explode('<p>', $urganch);
    $g1 = explode('</p>', $g[2]);
    $g2 = $g1[0];
    $shamol = trim("$g2");

    $h = explode('<p>', $urganch);
    $g1 = explode('</p>', $g[3]);
    $g2 = $g1[0];
    $bosim = trim("$g2");

    $i = explode('<p>', $urganch);
    $i1 = explode('</p>', $i[4]);
    $i2 = $i1[0];
    $oy = trim("$i2");

    $j = explode('<p>', $urganch);
    $j1 = explode('</p>', $j[5]);
    $j2 = $j1[0];
    $quyosh_chiqishi = trim("$j2");

    $k = explode('<p>', $urganch);
    $k1 = explode('</p>', $k[6]);
    $k2 = $k1[0];
    $quyosh_botishi = trim("$k2");

    // haftalik 

    // 1

    $l = explode('<strong>', $urganch);
    $l1 = explode('</strong>', $l[2]);
    $l2 = $l1[0];
    $hafta1_kun = trim("$l2");

    $m = explode('<div>', $urganch);
    $m1 = explode('</div>', $m[1]);
    $m2 = $m1[0];
    $hafta1_sana = trim("$m2");

    $n = explode('<span class="forecast-day">', $urganch);
    $n1 = explode('</span>', $n[1]);
    $n2 = $n1[0];
    $hafta1_harorat = trim("$n2");

    $o = explode('<td class="weather-row-desc">', $urganch);
    $o1 = explode('</td>', $o[1]);
    $o2 = $o1[0];
    $hafta1_tavsif = trim("$o2");

    // 2

    $p = explode('<strong>', $urganch);
    $p1 = explode('</strong>', $p[4]);
    $p2 = $p1[0];
    $hafta2_kun = trim("$p2");

    $q = explode('<div>', $urganch);
    $q1 = explode('</div>', $q[3]);
    $q2 = $q1[0];
    $hafta2_sana = trim("$q2");

    $r = explode('<span class="forecast-day">', $urganch);
    $r1 = explode('</span>', $r[2]);
    $r2 = $r1[0];
    $hafta2_harorat = trim("$r2");

    $s = explode('<td class="weather-row-desc">', $urganch);
    $s1 = explode('</td>', $s[2]);
    $s2 = $s1[0];
    $hafta2_tavsif = trim("$s2");

    // 3

    $p = explode('<strong>', $urganch);
    $p1 = explode('</strong>', $p[6]);
    $p2 = $p1[0];
    $hafta3_kun = trim("$p2");

    $q = explode('<div>', $urganch);
    $q1 = explode('</div>', $q[5]);
    $q2 = $q1[0];
    $hafta3_sana = trim("$q2");

    $r = explode('<span class="forecast-day">', $urganch);
    $r1 = explode('</span>', $r[3]);
    $r2 = $r1[0];
    $hafta3_harorat = trim("$r2");

    $s = explode('<td class="weather-row-desc">', $urganch);
    $s1 = explode('</td>', $s[3]);
    $s2 = $s1[0];
    $hafta3_tavsif = trim("$s2");

    // 4

    $p = explode('<strong>', $urganch);
    $p1 = explode('</strong>', $p[8]);
    $p2 = $p1[0];
    $hafta4_kun = trim("$p2");

    $q = explode('<div>', $urganch);
    $q1 = explode('</div>', $q[7]);
    $q2 = $q1[0];
    $hafta4_sana = trim("$q2");

    $r = explode('<span class="forecast-day">', $urganch);
    $r1 = explode('</span>', $r[4]);
    $r2 = $r1[0];
    $hafta4_harorat = trim("$r2");

    $s = explode('<td class="weather-row-desc">', $urganch);
    $s1 = explode('</td>', $s[4]);
    $s2 = $s1[0];
    $hafta4_tavsif = trim("$s2");

    // 5

    $p = explode('<strong>', $urganch);
    $p1 = explode('</strong>', $p[10]);
    $p2 = $p1[0];
    $hafta5_kun = trim("$p2");

    $q = explode('<div>', $urganch);
    $q1 = explode('</div>', $q[9]);
    $q2 = $q1[0];
    $hafta5_sana = trim("$q2");

    $r = explode('<span class="forecast-day">', $urganch);
    $r1 = explode('</span>', $r[5]);
    $r2 = $r1[0];
    $hafta5_harorat = trim("$r2");

    $s = explode('<td class="weather-row-desc">', $urganch);
    $s1 = explode('</td>', $s[5]);
    $s2 = $s1[0];
    $hafta5_tavsif = trim("$s2");

    // 6

    $p = explode('<strong>', $urganch);
    $p1 = explode('</strong>', $p[12]);
    $p2 = $p1[0];
    $hafta6_kun = trim("$p2");

    $q = explode('<div>', $urganch);
    $q1 = explode('</div>', $q[11]);
    $q2 = $q1[0];
    $hafta6_sana = trim("$q2");

    $r = explode('<span class="forecast-day">', $urganch);
    $r1 = explode('</span>', $r[6]);
    $r2 = $r1[0];
    $hafta6_harorat = trim("$r2");

    $s = explode('<td class="weather-row-desc">', $urganch);
    $s1 = explode('</td>', $s[6]);
    $s2 = $s1[0];
    $hafta6_tavsif = trim("$s2");

    // 7

    $p = explode('<strong>', $urganch);
    $p1 = explode('</strong>', $p[14]);
    $p2 = $p1[0];
    $hafta7_kun = trim("$p2");

    $q = explode('<div>', $urganch);
    $q1 = explode('</div>', $q[13]);
    $q2 = $q1[0];
    $hafta7_sana = trim("$q2");

    $r = explode('<span class="forecast-day">', $urganch);
    $r1 = explode('</span>', $r[7]);
    $r2 = $r1[0];
    $hafta7_harorat = trim("$r2");

    $s = explode('<td class="weather-row-desc">', $urganch);
    $s1 = explode('</td>', $s[7]);
    $s2 = $s1[0];
    $hafta7_tavsif = trim("$s2");

    $result = [
        'ok' => true,
        'bugun' => [
            'shahar' => "$u",
            'bugun' => "$sana",
            'tavsif' => "$tavsif",
            'harorat' => "$harorat",
            'tong' => "$tong",
            'kun' => "$kun",
            'oqshom' => "$oqshom",
            'namlik' => "$namlik",
            'shamol' => "$shamol",
            'bosim' => "$bosim",
            'oy' => "$oy",
            'quyosh_chiqishi' => "$quyosh_chiqishi",
            'quyosh_botishi' => "$quyosh_botishi",
            'soat' => "$soat",
            'sana' => "$sana2",
        ],
        'haftalik' => [
            "ertaga" => [
                'kun' => "$hafta1_kun",
                'sana' => "$hafta1_sana",
                'harorat' => "$hafta1_harorat",
                'tavsif' => "$hafta1_tavsif",
            ],
            "kun2" => [
                'kun' => "$hafta2_kun",
                'sana' => "$hafta2_sana",
                'harorat' => "$hafta2_harorat",
                'tavsif' => "$hafta2_tavsif",
            ],
            "kun3" => [
                'kun' => "$hafta3_kun",
                'sana' => "$hafta3_sana",
                'harorat' => "$hafta3_harorat",
                'tavsif' => "$hafta3_tavsif",
            ],
            "kun4" => [
                'kun' => "$hafta4_kun",
                'sana' => "$hafta4_sana",
                'harorat' => "$hafta4_harorat",
                'tavsif' => "$hafta4_tavsif",
            ],
            "kun5" => [
                'kun' => "$hafta5_kun",
                'sana' => "$hafta5_sana",
                'harorat' => "$hafta5_harorat",
                'tavsif' => "$hafta5_tavsif",
            ],
            "kun6" => [
                'kun' => "$hafta6_kun",
                'sana' => "$hafta6_sana",
                'harorat' => "$hafta6_harorat",
                'tavsif' => "$hafta6_tavsif",
            ],
            "kun7" => [
                'kun' => "$hafta7_kun",
                'sana' => "$hafta7_sana",
                'harorat' => "$hafta7_harorat",
                'tavsif' => "$hafta7_tavsif",
            ],
        ]
    ];

    echo json_encode([
        $result
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
} else {
    echo json_encode([
        [
            'ok' => false,
            'parameter' => "city",
            'shaharlar' => [
                'toshkent',
                'andijon',
                'buxoro',
                'guliston',
                'jizzax',
                'zarafshon',
                'qarshi',
                'navoiy',
                'namangan',
                'nukus',
                'samarqand',
                'termiz',
                'urganch',
                'fargona',
                'xiva'
            ],
            'programer (t.me)' => "@visualcoderuz",
        ]
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
}