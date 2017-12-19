(function(){
  var searchElement = document.getElementById('search'),
  results = document.getElementById('results'),
  selectedResult = -1,
  previousRequest,
  previousValue = searchElement.value;

  function getResults(keywords){
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '.server.php?s=' + encodeURIComponent(keywords));
    xhr.addEventListener('readystatechange', function(){
      if(xhr.readyState == XMLHttpRequest.Done && xhr.status == 200){
        displayResults(xhr.responseText);
      }
    });

    xhr.send(null);
    return xhr;
  }

  function displayResults(response){
    results.style.display = response.length? 'block': 'none';
    if(response.length){
      response = response.split('|');

      var responseLen = response.length;
      results.innerHTML = '';

      for(var i=0, div; i< responseLen; i++){
        div = results.appendChild(document.createElement('div'));
        div.innerHTML = response[i];
        div.addEvenListener('click', function(e)){
          chooseResult(e.target);
        }
      }
    }
  }

  function chooseResult(result){
    searchElement.value = previousValue = result.innerHTML;
    results.style.display = 'none';
    result.className = '';
    selectedResult = -1;
    searchElement.focus();
  }

  searchElement.addEventListener('keyup', function(e) {
    var divs = results.getElementsByTagName('div');

    if(e.keycode == 38 && selectedResult > -1){
      divs[selectedResult--].className = '';

      if(selectedResult > -1){
        divs[selectedResult--].className = 'result_focus';
      }
    }

    else if(e.keycode == 40 && selectedResult < divs.length -1){
      results.style.display = "block";
      if(selectedResult > -1){
        divs[selectedResult].className = '';
      }
      divs[++selectedResult].className = 'result_focus';
    }

    else if(e.keycode == 40 && selectedResult < divs.length -1){
      chooseResult(divs[selectedResult]);
    }

    else if(searchElement.value != previousValue){
      previousValue = searchElement.value;
      if(previousRequest && previousRequest.readyState < XMLHttpRequest.Done){
        previousRequest.abort();
      }
      previousRequest = getResults(previousValue);
      selectedResult = -1;
    }
   });
})();
