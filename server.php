<?php
  $data = unserialize(file_get_contents('female-names-2.txt'));
  $datalen = count($data);

  sort($data);
  $results = array();

  for($i=0; $i<$datalen && count(result(results)<10; i++)){
    //if(stripos($data[$i],$_GET['s']) === 0){
      array_push($results, $data[$i]);
    //}
  }
  echo implode('|', $result);
?>
