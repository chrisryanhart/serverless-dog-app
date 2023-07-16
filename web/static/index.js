
async function clickHandler(e){

  const lambdaUrl = 'https://cvu6ay74cjrcdotmcrddruzaea0jygfa.lambda-url.eu-north-1.on.aws/';
  let res = await axios.get(lambdaUrl);

  addDogElement(res.data);
};

// take result and add dom element
function addDogElement(data){
  const newDiv = document.createElement('div');
  const newP = document.createElement('p');
  const dogContainerDiv = document.getElementById('dog-container');

  newP.innerText = `Name: ${data.name}`;
  newP.style.padding = '5px';


  newDiv.style.border = '3px solid black';
  newDiv.style.margin = '10px';
  newDiv.style.width = '400px';

  newDiv.appendChild(newP);
  dogContainerDiv.appendChild(newDiv);

}

  

const newDogButton = document.getElementById('new-dog-button');

newDogButton.addEventListener('click', clickHandler);
