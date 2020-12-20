function blindStateChange() {
  //if blind state is open, then close blinds
  //if blind state is closed, then open blinds
  if (blindState.innerHTML=="open") {
    //setup gcp headers and body to change close blinds
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    let raw = JSON.stringify({"new_state":"close"});
    let requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    //perform gcp request to close blinds and then change state of app
    fetch("https://blind-control-299118.ue.r.appspot.com/flip", requestOptions)
      .then(response => response.text())
      .then(result =>
        //change blind state if successful
        blindState.innerHTML='close',
        document.getElementById('blindsAdjust').innerHTML = blindState.innerHTML,
        document.getElementById('blindsCurrent').innerHTML = 'Blinds are Closed'
      )
      .catch(error => console.log('error', error));


  }
  else if (blindState.innerHTML=="close") {
    //setup gcp headers and body to change close blinds
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    let raw = JSON.stringify({"new_state":"open"});
    let requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    //perform request to gcp and change state of blinds
    fetch("https://blind-control-299118.ue.r.appspot.com/flip", requestOptions)
      .then(response => response.text())
      .then(result =>
        //change blind state if successful
        blindState.innerHTML="open",
        document.getElementById('blindsAdjust').innerHTML = blindState.innerHTML,
        document.getElementById('blindsCurrent').innerHTML = 'Blinds are Open'
      )
      .catch(error => console.log('error', error));
  }
}
//Switch between manual control of blinds and automatic control with photoresistors
function changeMode() {
    //if current mode is manual, change to automatic
    //if current mode is automatic, change to manual
    if (blindsMode == "manual") {
      //setup gcp request to change mode to automatic
      let myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      let raw = JSON.stringify({"mode":"automatic"});
      let requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
      };

      let windowState = document.getElementById('options');
      let modeSwitch = document.getElementById('modeSwitch');

      //perform gcp request to change mode to automatic
      fetch("https://blind-control-299118.ue.r.appspot.com/change-mode\n", requestOptions)
        .then(response => response.text())
        .then(result =>
          //change blinds mode if successful
          blindsMode="automatic",
          windowState.innerHTML = '',
          modeSwitch.innerHTML = "switch to manual"
        )
        .catch(error => console.log('error', error));
    }
    else if (blindsMode == "automatic") {
      //setup gcp request to change mode to manual
      let myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      let raw = JSON.stringify({"mode":"manual"});
      let requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
      };
      let modeSwitch = document.getElementById('modeSwitch');
      let items = document.getElementById('options');
      let blindsAdjust = document.createElement("button");
      //perform gcp request to change mode to manual
      fetch("https://blind-control-299118.ue.r.appspot.com/change-mode\n", requestOptions)
        .then(response => response.text())
        .then(result =>
          //change blind mode if successful
          modeSwitch.innerHTML = "switch to magic mode",
          blindsMode = "manual",
          //render manual mode UI
          blindsAdjust.id = "blindsAdjust",
          blindsAdjust.innerHTML = blindState.innerHTML,
          items.appendChild(blindsAdjust),
          blindsAdjust.onclick = function() {blindStateChange()}
        )
        .catch(error => console.log('error', error));
    }
}

async function getWindowState() {
  blindsMode = "automatic";
  //get current blinds state using gcp cloud function
  blindState=document.createElement('p');
  let myHeaders = new Headers();
  myHeaders.append("x-rapidapi-key", "de103cb136msh54049396c04d9aap1b6bffjsnbab7cfaebe8f");
  myHeaders.append("x-rapidapi-host", "bing-image-search1.p.rapidapi.com");
  myHeaders.append("Authorization", "\"o=\"");
  let requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
  };
  //setup ui based on gcp
  let stateRequest;
  let blindImage = document.createElement('p');
  //get blind status using gcp
  await fetch("https://blind-control-299118.ue.r.appspot.com/get-state", requestOptions)
    .then(response => response.json())
    .then(result => stateRequest=result.state)
  //if blinds are open, set ui to open blinds
  //if blinds are closed, set ui to closed blinds
  if (stateRequest=='open') {
    blindState.innerHTML = 'close';
    blindImage.innerHTML='Blinds are Open';
  }
  else if (stateRequest=='closed') {
    blindState.innerHTML = 'open';
    blindImage.innerHTML = 'Blinds are Closed';
  }
  blindImage.id = 'blindsCurrent';
  document.getElementById('windowState').appendChild(blindImage);
  //setup mode switch
  let modeSwitch = document.createElement("button");
  modeSwitch.id = "modeSwitch";
  modeSwitch.onclick = function() {changeMode()}
  document.getElementById('windowState').appendChild(modeSwitch);
  if (blindsMode=="manual") {
    //render manual view by adding UI to switch state of blinds
    let items = document.getElementById('options');
    modeSwitch.innerHTML = "switch to magic mode";
    let blindsAdjust = document.createElement("button");
    blindsAdjust.id = "blindsAdjust";
    blindsAdjust.innerHTML = blindState.innerHTML;
    items.appendChild(blindsAdjust);
    blindsAdjust.onclick = function() {blindStateChange()};
  }
  else {
    //render automatic mode
    modeSwitch.innerHTML = "switch to manual mode";
  }

}
let blindState;
let blindsMode;


window.onload = function(){
  getWindowState();
}
